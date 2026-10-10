function gcd(a,b){a=Math.abs(a);b=Math.abs(b);while(b)[a,b]=[b,a%b];return a}
function next(u,v){
  if(u+v===0)return null;
  if(u%3===0&&v%3!==0)return [v-u/3,-u/3];
  if(v%3===0&&u%3!==0)return [u-v/3,-v/3];
  return null;
}
for(let K=1;K<=12;K++){
 let best={ratio:-1};
 for(let u=-3000;u<=3000;u++)for(let v=-3000;v<=3000;v++){
  if(!u&&!v||gcd(u,v)!==1)continue;
  let a=u,b=v, ok=true;
  for(let i=0;i<K;i++){let z=next(a,b);if(!z){ok=false;break}[a,b]=z}
  if(ok){let r=(Math.abs(a)+Math.abs(b))/(Math.abs(u)+Math.abs(v));if(r>best.ratio)best={ratio:r,u,v,a,b}}
 }
 console.log(K,best);
}
