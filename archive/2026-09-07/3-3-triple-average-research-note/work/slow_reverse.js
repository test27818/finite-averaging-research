function abs(x){return x<0n?-x:x}
function step(u,v){let a=abs(u),b=abs(v); if(a<b)[a,b]=[b,a]; let d=a-b; let x=3n*b,y=d; if(x<y)[x,y]=[y,x]; return [x,y]}
let u=1n,v=-1n;
for(let k=0;k<50;k++){let a=abs(u),b=abs(v);if(a<b)[a,b]=[b,a];let r=b?Number(a)/Number(b):Infinity;console.log(k,a.toString(),b.toString(),r.toFixed(3));[u,v]=step(u,v)}
