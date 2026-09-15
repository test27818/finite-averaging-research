// Node regression: no external modules. The source bundle is identical to HTML scripts.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname,'..');
const S = require('../src/solver_core.js');
let cases=0;
function test(name,f){f();cases++;console.log('PASS',name);}
function load(p){return fs.readFileSync(path.join(root,p),'utf8');}

test('all 1636 labels and 538 constructive witnesses',()=>{
  let all=0,yes=0;
  for(const sp of ['small','dev','test','hard']){
    for(const line of load('data/'+sp+'.jsonl').trim().split('\n')){
      const r=JSON.parse(line), a=r.a.map(BigInt);all++;
      assert.equal(S.judge(a),r.label==='YES');
      if(r.label==='YES'){
        const v=S.solve(a,{hardMs:10000,optMs:0});yes++;
        assert(v.verified,r.id);
        assert(S.independentVerify(a.map(String),v.steps).ok,r.id);
      }
    }
  }
  assert.equal(all,1636);assert.equal(yes,538);
});
test('78 frozen original minima',()=>{
  for(const line of load('tests/fixtures/original_small.jsonl').trim().split('\n')){
    const r=JSON.parse(line);if(r.min_steps===null)continue;
    const out=S.solve(r.a,{optMs:1000});assert(out.certified);assert.equal(out.minSteps,r.min_steps);
  }
});
test('two case studies and truthful limit status',()=>{
  const cases=[[[38,-23,-14,16,-11,4,63,80,14,38],10],
    [[-81,-60,-95,-95,-20,-13,-87,-80,42,54],11]];
  for(const [a,m]of cases){
    const out=S.solve(a,{hardMs:10000,optMs:3000});assert(out.certified);assert.equal(out.minSteps,m);
    const fast=S.solve(a,{optMs:0});assert(!fast.certified);assert.equal(fast.minSteps,null);
    const state=S.stateOf(a.map(BigInt)),seed=S.construct(state).moves;
    const r=S.ida(state,seed,{deadline:performance.now()-1});assert(!r.optimal);
    const c=S.ida(state,seed,{nodeLimit:0,deadline:Infinity});assert(!c.optimal);assert.equal(c.expanded,0);
    const cap=S.ida(state,seed,{memoCap:0,deadline:Infinity});assert(!cap.optimal);
  }
});
test('big integers, n=3 precision, zero steps and n>=13 optimal shortcut',()=>{
  assert(!S.judge([9000000000000000n,9000000000000002n,9000000000000005n]));
  const a=[10n**255n+7n,-(10n**255n)+4n,12n,3n];assert(S.solve(a).verified);
  for(const a of [[5],[5,5],[5,5,5]])assert.equal(S.solve(a).minSteps,0);
  assert.equal(S.solve(Array.from({length:14},(_,i)=>i)).minSteps,7);
  assert(!S.independentVerify([9007199254740993,0],[]).ok);
});
test('step cap, invalid operation indices, independent TXT/JSON import',()=>{
  const st=S.stateOf([0n,0n,0n,1n]);assert.equal(S.construct(st,{maxSteps:2}).moves,null);
  const a=[0,0,0,1,9],r=S.solve(a);
  const record={input:a.map(String),operations:r.steps};
  const parsed=S.parseVerificationText(JSON.stringify(record))[0];assert(S.independentVerify(parsed.input,parsed.operations).ok);
  const txt='题面：\n'+a.join(', ')+'\n操作序列（1 基）：\n'+r.steps.map(p=>p.join(', ')).join('\n')+'\n结束操作';
  const p=S.parseVerificationText(txt)[0];assert(S.independentVerify(p.input,p.operations).ok);
  for(const bad of [[[1,1]],[[1,3]],[[true,2]],[]])assert(!S.independentVerify(['0','2'],bad).ok);
});
test('actual concatenated Worker scripts: builtin tests and messages',()=>{
  const html=load('solver.html');
  const blocks=['solver-source','verifier-source','runner-source'].map(id=>{
    const match=html.match(new RegExp('<script id="'+id+'"[^>]*>([\\s\\S]*?)</script>'));
    assert(match);return match[1];
  });
  const messages=[];
  const context={performance,crypto:require('node:crypto').webcrypto,postMessage:m=>messages.push(m),console};
  vm.createContext(context);vm.runInContext(blocks.join('\n'),context);
  context.onmessage({data:{type:'selftest'}});
  assert(!messages.some(m=>m.type==='error'),JSON.stringify(messages));
  const results=messages.find(m=>m.type==='selftested');assert(results);assert(results.data.every(r=>r.ok));
  messages.length=0;
  context.onmessage({data:{type:'batch',count:3,n:7,lo:'-10',hi:'10',options:{hardMs:2000,optMs:0}}});
  const batch=messages.filter(m=>m.type==='batchResult');assert.equal(batch.length,3);
  assert(batch.every(m=>m.data.verified));assert(messages.some(m=>m.type==='done'));
});
console.log('All',cases,'groups passed. Browser DOM/visual layout is not tested by this Node suite.');
