function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a}
function norm([a,b]){let d=gcd(a,b);a/=d;b/=d;return [a,b]}
function key([a,b]){return a+','+b}
function kids([u,v]){if(((u-v)%3n+3n)%3n===0n)return [];return [norm([-3n*v,u-v]),norm([u-v,-3n*v])].map(x=>x)}
let level=new Map([[key([-1n,1n]),[-1n,1n,'']]]);
for(let d=1;d<=30;d++){
 let next=new Map();
 for(let [k,[u,v,w]] of level){for(let [j,x] of kids([u,v]).entries()){let kk=key(x);if(!next.has(kk))next.set(kk,[x[0],x[1],w+(j?'B':'A')]);}}
 level=next;
 let best; for(let [k,[u,v,w]] of level){let n=(u<0n?-u:u)+(v<0n?-v:v);if(!best||n<best.n)best={n,u,v,w}}
 console.log(d,level.size,best.n.toString(),best.u.toString(),best.v.toString(),best.w);
}
