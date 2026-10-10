function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a}
function norm([a,b]){const d=gcd(a,b); return [a/d,b/d]}
function children([u,v]) { return [norm([-3n*v,u-v]), norm([u-v,-3n*v])] }
function height([u,v]) { return (u<0n?-u:u)+(v<0n?-v:v) }

let states = [[[-1n,1n], ""]];
const width = 50000;
for (let depth=1; depth<=100; depth++) {
  const next = new Map;
  for (const [pair, word] of states) {
    for (const [i, child] of children(pair).entries()) {
      const key=child.join(",");
      if (!next.has(key)) next.set(key, [child, word+(i ? "B" : "A")]);
    }
  }
  states = [...next.values()];
  states.sort((x,y) => height(x[0]) < height(y[0]) ? -1 : height(x[0]) > height(y[0]) ? 1 : 0);
  const best = states[0];
  console.log(depth, best[0].join(","), height(best[0]).toString(), best[1]);
  states = states.slice(0,width);
}
