function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a}
function norm([a,b]){let d=gcd(a,b);return[a/d,b/d]}
function kids([u,v]){return[norm([-3n*v,u-v]),norm([u-v,-3n*v])]}
let L=[[-1n,1n]];
for(let d=0;d<=7;d++){ console.log(d,L.map(([u,v])=>Number(u)/Number(v)).sort((a,b)=>a-b).join(" "));let N=[];for(let q of L)N.push(...kids(q));L=N}
