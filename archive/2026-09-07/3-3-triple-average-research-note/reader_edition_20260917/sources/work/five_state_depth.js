function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a}
function norm([a,b]){let d=gcd(a,b);return [a/d,b/d]}
function kids([u,v]) {
  // Projective preimages under A(u,v)=(-u+3v,-u) and B(u,v)=(3u-v,-v).
  return [norm([-3n*v,u-v]),norm([u-v,-3n*v])]
}
for(const seed of [[[-1n,1n]]]) {
 let level=seed;
 console.log("seed",seed[0].join(","));
 for(let d=1;d<=21;d++) {
   const next=new Map;
   for(const x of level) for(const y of kids(x)) next.set(y.join(","),y);
   level=[...next.values()];
   let mn=level.reduce((a,[u,v])=>{let h=(u<0n?-u:u)+(v<0n?-v:v);return h<a?h:a},10n**100n);
   console.log(d,level.length,mn.toString());
 }
}
