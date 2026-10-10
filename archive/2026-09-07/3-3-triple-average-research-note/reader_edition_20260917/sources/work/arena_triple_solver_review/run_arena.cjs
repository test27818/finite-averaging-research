'use strict';
const {Worker, isMainThread, parentPort, workerData} = require('node:worker_threads');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {performance} = require('node:perf_hooks');

if (isMainThread) {
  const readline = require('node:readline');
  const lines = readline.createInterface({input: process.stdin, crlfDelay: Infinity});
  let chain = Promise.resolve();
  lines.on('line', line => {
    chain = chain.then(() => new Promise(resolve => {
      const request = JSON.parse(line);
      const worker = new Worker(__filename, {workerData: request});
      const started = performance.now();
      let finished = false;
      const done = result => {
        if (finished) return;
        finished = true;
        clearTimeout(timer);
        process.stdout.write(JSON.stringify({...result, outer_ms: performance.now()-started},
          (_,x) => typeof x === 'bigint' ? x.toString() : x) + '\n');
        worker.terminate().then(resolve);
      };
      const timer = setTimeout(() => done({status:'hard_timeout', hard_limit_ms:request.hard_ms || 16000}), request.hard_ms || 16000);
      worker.on('message', done);
      worker.on('error', e => done({status:'error', error:String(e.stack)}));
    }));
  });
} else {
  const source = fs.readFileSync(path.join(__dirname,'arena_solver.js'),'utf8');
  const context = vm.createContext({performance, setTimeout, clearTimeout, request:workerData});
  vm.runInContext(source, context, {timeout:1000});
  const invocation = `(async () => {
    if (request.action === 'macros') {
      const results = [];
      for (const [size, zeros] of [[4,3],[5,2],[6,1],[7,2],[8,1],[9,0]]) {
        let checked = 0;
        for (let j=0;j<size-1;j++) {
          const raw = Array(size+zeros).fill(0n); raw[j]=1n; raw[size-1]=-1n;
          const word = buildMacro(size,Array.from({length:size},(_,i)=>i),Array.from({length:zeros},(_,i)=>size+i));
          if (!verify(raw,word,false).ok) throw new Error('macro failure '+size);
          checked++;
        }
        results.push({size,zeros,basis_checks:checked,operations:buildMacro(size,Array.from({length:size},(_,i)=>i),Array.from({length:zeros},(_,i)=>size+i)).map(a=>a.map(i=>i+1))});
      }
      return {status:'ok',results};
    }
    if (request.action === 'suite') {
      const budget={width:400,depth:70,maxNodes:60000,timeMs:9000,moveCap:60};
      for(let j=0;j<3;j++) { const a=request.cases[0].input.map(BigInt); await solveFeasible(a,analyze(a),budget,()=>false); }
      const cases=[];
      for(const c of request.cases) {
        const a=c.input.map(BigInt),info=analyze(a);
        const result=await solveFeasible(a,info,budget,()=>false);
        const ok=result.ops && verify(a,result.ops,false).ok;
        cases.push({id:c.id,status:ok?'solved':'not_found',steps:ok?result.ops.length:null,
          reported_solve_ms:result.timeMs,operations:ok?result.ops.map(a=>a.map(i=>i+1)):null,method:result.method});
      }
      return {status:'ok',cases};
    }
    const raw = request.input.map(BigInt);
    const begin = performance.now();
    const info = analyze(raw);
    const judge_ms = performance.now()-begin;
    if (!info.supported || !info.feasible) return {status:info.supported?'impossible':'unsupported',G:info.G,judge_ms};
    const budget = request.budget || {width:400,depth:70,maxNodes:60000,timeMs:9000,moveCap:60};
    let calls = null;
    if (request.diagnostics) {
      calls = {kill:0,macro:0,fab:0,gen:0,candidates:0,nonfinite_views:0};
      const k=findKill,m=findMacro,f=findFab,g=genMoves,v=viewOf;
      findKill = (...args) => {calls.kill++;return k(...args);};
      findMacro = (...args) => {calls.macro++;return m(...args);};
      findFab = (...args) => {calls.fab++;return f(...args);};
      genMoves = (...args) => {calls.gen++;const out=g(...args);calls.candidates+=out.length;return out;};
      viewOf = (...args) => {const out=v(...args);if(out.nums.some(x=>!Number.isFinite(x)))calls.nonfinite_views++;return out;};
    }
    if (request.action === 'inspect') {
      const v=raw.map(x=>new Fr(x).sub(info.A)), view=viewOf(v);
      const kill=findKill(view),macro=findMacro(view),moves=genMoves(view,60);
      return {status:'ok',G:info.G,kill,macro,moves,view_numbers:view.nums.map(String),calls};
    }
    const result = await solveFeasible(raw,info,budget,()=>false);
    const startVerify=performance.now();
    const verified=result.ops ? verify(raw,result.ops,false).ok : null;
    return {status:result.ops?(verified?'solved':'invalid'):'not_found',G:info.G,
      steps:result.ops?result.ops.length:null,operations:result.ops?result.ops.map(a=>a.map(i=>i+1)):null,
      method:result.method,reported_solve_ms:result.timeMs,judge_ms,verify_ms:performance.now()-startVerify,
      partial_steps:result.partialOps,budget,calls};
  })()`;
  vm.runInContext(invocation,context,{timeout:workerData.hard_ms || 16000})
    .then(result=>parentPort.postMessage(result))
    .catch(error=>parentPort.postMessage({status:'error',error:String(error.stack)}));
}
