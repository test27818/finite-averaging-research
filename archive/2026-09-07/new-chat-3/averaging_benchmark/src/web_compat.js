function bigCmp(a, b) { return a < b ? -1 : (a > b ? 1 : 0); }

function gcdBig(a, b) {
  a = a < 0n ? -a : a; b = b < 0n ? -b : b;
  while (b) { [a, b] = [b, a % b]; }
  return a;
}

// ---- Dyadic rational helpers: value = n / 2^e, kept reduced ----
function dyReduce(n, e) {
  while (n !== 0n && e > 0 && n % 2n === 0n) { n /= 2n; e--; }
  if (n === 0n) e = 0;
  return { n, e };
}
function dyAvg(a, b) {
  const em = Math.max(a.e, b.e);
  const an = a.n << BigInt(em - a.e);
  const bn = b.n << BigInt(em - b.e);
  return dyReduce(an + bn, em + 1);
}
function dyCmp(a, b) {
  const em = Math.max(a.e, b.e);
  const an = a.n << BigInt(em - a.e);
  const bn = b.n << BigInt(em - b.e);
  return an === bn ? 0 : (an < bn ? -1 : 1);
}
function dyEqToRatio(d, S, n) {
  // true iff d.n / 2^d.e == S / n
  return d.n * BigInt(n) === S * (1n << BigInt(d.e));
}


// Compatibility facade: old exports keep 1-based index pairs and never report an
// unproved minSteps. The historical bfsSolve/greedySolve names now delegate to v3.
function judge(arr){return possible(stateOf(arr.map(x=>BigInt(x))));}
function solve(arr,opts={}){
  const r=solveOne(arr.map(x=>typeof x==='bigint'?String(x):x),{
    hardMs:opts.hardMs??10000,optMs:opts.optMs??350
  });
  return {ok:r.classification==='solvable',steps:r.status==='solved'?r.operations:null,
    minSteps:r.optimal?r.steps:null,method:r.algorithm||r.status,
    certified:r.optimal,verified:r.verified===true,lb:r.lowerBound,ub:r.steps,
    status:r.status,metrics:r.metrics};
}
function bfsSolve(arr,budget=200000){
  const st=stateOf(arr.map(BigInt));
  if(!possible(st))return null;
  const c=construct(st,{deadline:performance.now()+10000});
  if(!c.moves)return null;
  const r=ida(st,c.moves,{deadline:performance.now()+10000,nodeLimit:budget});
  if(!r.optimal)return null;
  const steps=mapMoves(arr.map(BigInt),r.moves).map(([i,j])=>[i+1,j+1]);
  if(!independentVerify(arr.map(String),steps).ok)throw Error('verification failed');
  return {steps,minSteps:steps.length};
}
function power2Tree(n){
  if(!Number.isInteger(n)||n<1||(n&(n-1)))return null;
  const steps=[];
  for(let d=1;d<n;d*=2)for(let p=0;p<n;p++)if((p&d)===0)steps.push([p+1,p+d+1]);
  return steps;
}
function greedySolve(arr,restarts=80,maxSteps=19000){
  const r=solve(arr,{optMs:0});
  return r.steps!==null&&r.steps.length<=maxSteps?{steps:r.steps,minSteps:r.minSteps}:null;
}
if(typeof module!=='undefined')Object.assign(module.exports,{
  judge,solve,bfsSolve,greedySolve,power2Tree,dyAvg,dyCmp,dyReduce,dyEqToRatio,
  stateOf,possible,construct,ida,lowerBound,independentVerify,solveOne,analyzeInput,
  sampleCase,mapMoves,gen,bestTail,parseVerificationText,builtinCases
});
