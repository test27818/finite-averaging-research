function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b) [a, b] = [b, a % b];
  return a;
}

function norm(u, v) {
  const d = gcd(u, v);
  return [u / d, v / d];
}

// One deterministic predecessor step in the backward tree of the terminal ray.
function peel(u, v) {
  if (u % 3n === 0n && v % 3n !== 0n) return norm(u / 3n - v, u / 3n);
  if (v % 3n === 0n && u % 3n !== 0n) return norm(v / 3n, v / 3n - u);
  return null;
}

const stats = { success: 0, dead: 0, cycle: 0, limit: 0 };
const hardest = [];
const cycles = [];
let maxSteps = 0;
const longRuns = [];

for (let U = -150; U <= 150; U++) {
  for (let V = -150; V <= 150; V++) {
    let u = BigInt(U);
    let v = BigInt(V);
    if ((!u && !v) || gcd(u, v) !== 1n) continue;

    const seen = new Map();
    let steps = 0;
    let why;
    while (steps < 10000) {
      if (u + v === 0n) {
        why = "success";
        break;
      }
      const key = `${u},${v}`;
      if (seen.has(key)) {
        why = "cycle";
        cycles.push([U, V, steps - seen.get(key), steps, key]);
        break;
      }
      seen.set(key, steps);
      const next = peel(u, v);
      if (!next) {
        why = "dead";
        break;
      }
      [u, v] = next;
      steps++;
    }
    if (!why) why = "limit";
    stats[why]++;
    if (steps > maxSteps) maxSteps = steps;
    if (steps > 10) longRuns.push([steps, U, V, why, `${u}`, `${v}`]);
  }
}

hardest.sort((a, b) => b[0] - a[0]);
longRuns.sort((a, b) => b[0] - a[0]);
console.log(stats);
console.log({ maxSteps, longRuns: longRuns.slice(0, 30) });
console.log({ nonAxisCycles: cycles.filter(([, , , , key]) => !/[01-],0|0,[01-]/.test(key)).slice(0, 30) });
