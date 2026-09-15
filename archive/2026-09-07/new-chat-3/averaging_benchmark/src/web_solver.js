'use strict';
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
const cmp=(a,b)=>a<b?-1:a>b?1:0;
function normalize(a,sort=true){let g=0n;for(const x of a){g=gcd(g,x);if(g===1n)break;}let b=g>1n?a.map(x=>x/g):a.slice();return sort?b.sort(cmp):b;}
function stateOf(a){const n=BigInt(a.length),s=a.reduce((s,x)=>s+x,0n);return normalize(a.map(x=>n*x-s));}
function possible(a){if(!a.some(x=>x!==0n))return true;if(a.length<=2)return true;if(a.length===3)return a.includes(0n);let G=0n;for(let i=1;i<a.length;i++){G=gcd(G,a[i]-a[0]);if(G===1n)return true;}return G>0n&&(G&(G-1n))===0n;}
const keyOf=a=>a.join(',');
const energy=a=>a.reduce((s,x)=>s+x*x,0n);
const active=a=>a.reduce((s,x)=>s+(x!==0n),0);
const floorPow=n=>2**Math.floor(Math.log2(n));
function op(a,x,y,sort=true){const i=a.indexOf(x);let j=a.indexOf(y);if(j===i)j=a.indexOf(y,i+1);if(i<0||j<0)throw Error('Bad value move');const b=a.map(v=>v*2n);b[i]=b[j]=x+y;return normalize(b,sort);}
function gen(a){const res=[];for(let i=0;i<a.length;i++){if(i&&a[i]===a[i-1])continue;for(let j=i+1;j<a.length;j++){if(a[j]===a[i]||(j>i+1&&a[j]===a[j-1]))continue;const b=op(a,a[i],a[j]);if(possible(b))res.push({a:b,move:[a[i],a[j]],en:energy(b),m:active(b)});}}return res;}
class Heap {constructor(cmp){this.a=[];this.cmp=cmp;}push(x){const a=this.a;let i=a.length;a.push(x);while(i){let p=(i-1)>>1;if(this.cmp(a[p],x)<=0)break;a[i]=a[p];i=p;}a[i]=x;}pop(){const a=this.a,r=a[0],x=a.pop();if(a.length){let i=0;while(i*2+1<a.length){let c=i*2+1;if(c+1<a.length&&this.cmp(a[c+1],a[c])<0)c++;if(this.cmp(x,a[c])<=0)break;a[i]=a[c];i=c;}a[i]=x;}return r;}get length(){return this.a.length;}}
function reconstruct(node){let out=[];while(node.parent){out.push(node.move);node=node.parent;}return out.reverse();}
function escape(a,{limit=20000,deadline=Infinity,stateCap=100000}={}){const E=energy(a),M=active(a),P=floorPow(a.length);let count=0;const score=(a,d)=>BigInt((energy(a).toString(2).length+active(a)*2+d*2));const root={a,d:0,parent:null};root.score=score(a,0);const q=new Heap((u,v)=>cmp(u.score,v.score)||u.d-v.d);q.push(root);const seen=new Map([[keyOf(a),0]]);
 while(q.length&&count++<limit&&performance.now()<deadline){const cur=q.pop();for(const c of gen(cur.a)){let d=cur.d+1,k=keyOf(c.a);if((seen.get(k)??Infinity)<=d)continue;if(!seen.has(k)&&seen.size>=stateCap)return {moves:null,count};seen.set(k,d);const node={...c,parent:cur,d,score:score(c.a,d)};if(c.m<=P||c.en<E)return {moves:reconstruct(node),count};q.push(node);}}
 return{moves:null,count};}
function mapMoves(input,moves){let a=stateOf(input); // label state separately
 const n=BigInt(input.length),s=input.reduce((t,x)=>t+x,0n);a=normalize(input.map(x=>n*x-s),false);const ops=[];
 for(const [x,y]of moves){let i=a.indexOf(x),j=a.indexOf(y);if(i===j)j=a.indexOf(y,i+1);if(i<0||j<0)throw Error('map move missing');ops.push([i,j]);const b=a.map(v=>v*2n);b[i]=b[j]=x+y;a=normalize(b,false);}if(active(a))throw Error('not solved');return ops;}
if(typeof module!=='undefined')module.exports={gcd,normalize,stateOf,possible,op,gen,energy,escape,mapMoves,active,Heap,reconstruct};
function lowerBound(a){let m=0,c=0;const counts=new Map();for(const x of a){if(x!==0n)m++;counts.set(x,(counts.get(x)||0)+1);}for(const [x,n]of counts)if(x>0n)c+=Math.min(n,counts.get(-x)||0);let C=Math.ceil(m/2);return C+Math.max(0,Math.ceil((C-c)/2));}
function ida(a,best,{deadline=performance.now()+500,nodeLimit=200000,maxDepth=80,memoCap=200000}={}){
  let expanded=0,lower=lowerBound(a),found=null,interrupted=false;
  function dfs(st,remain,path,failed){
    const h=lowerBound(st);
    if(h===0){found=path.slice();return true;}
    if(h>remain)return false;
    if(expanded>=nodeLimit||((expanded&127)===0&&performance.now()>=deadline)){
      interrupted=true;return false;
    }
    expanded++;
    const key=keyOf(st),prev=failed.get(key);
    if(prev!==undefined&&prev>=remain)return false;
    const cc=gen(st);
    cc.sort((u,v)=>lowerBound(u.a)-lowerBound(v.a)||cmp(u.en,v.en));
    for(const c of cc){
      path.push(c.move);
      if(dfs(c.a,remain-1,path,failed))return true;
      path.pop();
      if(interrupted)return false;
    }
    if(!failed.has(key)&&failed.size>=memoCap){interrupted=true;return false;}
    failed.set(key,remain);return false;
  }
  if(lower>best.length)throw Error('lower bound exceeds verified incumbent');
  for(;lower<best.length&&lower<=maxDepth;lower++){
    if(performance.now()>=deadline||expanded>=nodeLimit)
      return {moves:best,optimal:false,expanded,lower};
    if(dfs(a,lower,[],new Map()))return {moves:found,optimal:true,expanded,lower};
    if(interrupted)return {moves:best,optimal:false,expanded,lower};
  }
  return {moves:best,optimal:lower===best.length,expanded,lower};
}
if(typeof module!=='undefined')Object.assign(module.exports,{ida,lowerBound});
function smartTail(a,mode=0,subset=null){let b=a.slice();let ids=subset?subset.slice():b.map((v,i)=>i).filter(i=>b[i]!==0n);if(!ids.length)return[];let N=1;while(N<ids.length)N*=2;if(N>b.length)return null;for(let i=0;ids.length<N;i++)if(b[i]===0n&&!ids.includes(i))ids.push(i);if(ids.reduce((s,i)=>s+b[i],0n)!==0n)return null;
 let groups=ids.map(i=>[i]),out=[];while(groups.length>1){let unused=groups.slice(),pairs=[];while(unused.length){let found=null;if(mode<3){for(let i=0;i<unused.length&&!found;i++)for(let j=i+1;j<unused.length;j++){let x=b[unused[i][0]],y=b[unused[j][0]];if((mode===1?x===y:x+y===0n)){found=[i,j];break;}}}
 if(!found&&mode!==2){for(let i=0;i<unused.length&&!found;i++)for(let j=i+1;j<unused.length;j++)if(b[unused[i][0]]===b[unused[j][0]]){found=[i,j];break;}}
 if(!found){unused.sort((u,v)=>cmp(b[u[0]],b[v[0]]));found=mode===4?[0,1]:[0,unused.length-1];}const [i,j]=found,G=unused[i],H=unused[j];pairs.push([G,H]);unused.splice(j,1);unused.splice(i,1);}
 groups=[];for(const[G,H]of pairs){for(let k=0;k<G.length;k++){const i=G[k],j=H[k],x=b[i],y=b[j];if(x===y)continue;out.push([x,y]);const c=b.map(x=>x*2n);c[i]=c[j]=x+y;b=normalize(c,false);}groups.push(G.concat(H));}}
 if(subset?subset.some(i=>b[i]!==0n):active(b))throw Error('smart tail failure');return out;}
function bestTail(a,subset=null){let best=null;for(let mode=0;mode<5;mode++){const t=smartTail(a,mode,subset);if(t!==null&&(!best||t.length<best.length))best=t;}return best;}
function opposite(a){let l=0,r=a.length-1;while(l<r){let s=a[l]+a[r];if(s===0n){if(a[l]!==0n)return[a[l],a[r]];break;}if(s<0n)l++;else r--;}return null;}
function quartet(a){const pairs=new Map();for(let i=0;i<a.length;i++){if(!a[i])continue;for(let j=i+1;j<a.length;j++){if(!a[j])continue;let s=a[i]+a[j],other=pairs.get(-s);if(other)for(const [u,v]of other)if(u!==i&&u!==j&&v!==i&&v!==j)return [u,v,i,j];let list=pairs.get(s);if(!list)pairs.set(s,list=[]);if(list.length<8)list.push([i,j]);}}return null;}
function descentChoice(a,E){
 if(a.length<=16){const cc=gen(a).filter(c=>c.en<E);cc.sort((u,v)=>cmp(u.en,v.en));return cc[0]||null;}
 const buckets=[[],[]];for(const x of a){const k=Number(abs(x)%2n),g=buckets[k];if(!g.length||g[g.length-1]!==x)g.push(x);}
 let best=null;const seen=new Set();for(const values of buckets){if(values.length<2)continue;const candidates=values.slice(0,4).concat(values.slice(-4));for(let i=0;i<candidates.length;i++)for(let j=i+1;j<candidates.length;j++){let x=candidates[i],y=candidates[j];if(x===y)continue;const k=x+','+y;if(seen.has(k))continue;seen.add(k);const b=op(a,x,y);if(!possible(b))continue;const en=energy(b);if(en<E&&(!best||en<best.en))best={a:b,move:[x,y],en,m:active(b)};}}
 if(best)return best;const cc=gen(a).filter(c=>c.en<E);cc.sort((u,v)=>cmp(u.en,v.en));return cc[0]||null;
}
function construct(a,{deadline=Infinity,escapeLimit=30000,maxSteps=8192,partition=true}={}){let moves=[],esc=0,expanded=0,rounds=0;while(moves.length<maxSteps&&performance.now()<deadline){rounds++;const opp=opposite(a);if(opp){moves.push(opp);a=op(a,...opp);continue;}if(!active(a))return{moves,esc,expanded};if(partition&&active(a)>4){const ids=quartet(a);if(ids){let t=bestTail(a,ids);if(moves.length+t.length>maxSteps)return {moves:null,esc,expanded};for(const mv of t){moves.push(mv);a=op(a,...mv);}continue;}}
 let t=bestTail(a);if(t!==null)return{moves:moves.length+t.length<=maxSteps?moves.concat(t):null,esc,expanded};const E=energy(a);const best=descentChoice(a,E);if(best){moves.push(best.move);a=best.a;}else{const r=escape(a,{limit:escapeLimit,deadline});expanded+=r.count;esc++;if(!r.moves||moves.length+r.moves.length>maxSteps)return{moves:null,esc,expanded,partial:moves,a};for(const mv of r.moves){a=op(a,...mv);moves.push(mv);}}}return{moves:null,esc,expanded,partial:moves,a};}
if(typeof module!=='undefined')Object.assign(module.exports,{construct,bestTail,smartTail,opposite,quartet});
function beamImprove(a,best,{deadline=performance.now()+200,width=24,maxStates=40000}={}){let expanded=0,seen=new Map([[keyOf(a),0]]),beam=[{a,parent:null,d:0,score:0}];let bestPath=best;for(let depth=0;beam.length&&depth<Math.min(bestPath.length-1,96);depth++){let next=[];for(const cur of beam){if(performance.now()>deadline)return{moves:bestPath,expanded};for(const c of gen(cur.a)){expanded++;let d=cur.d+1;if(d+lowerBound(c.a)>=bestPath.length)continue;let key=keyOf(c.a);if((seen.get(key)??Infinity)<=d)continue;seen.set(key,d);const node={...c,d,parent:cur,score:lowerBound(c.a)*4+c.en.toString(2).length};if(c.m===0){bestPath=reconstruct(node);continue;}next.push(node);}}
 next.sort((u,v)=>u.score-v.score||cmp(u.en,v.en));beam=next.slice(0,width);for(const cur of beam){if(performance.now()>deadline)return{moves:bestPath,expanded};if(cur.m<=floorPow(a.length)){const t=bestTail(cur.a);if(t&&cur.d+t.length<bestPath.length)bestPath=reconstruct(cur).concat(t);}}if(seen.size>maxStates)seen=new Map(beam.map(c=>[keyOf(c.a),c.d]));}
 return{moves:bestPath,expanded};}
if(typeof module!=='undefined')Object.assign(module.exports,{beamImprove});
