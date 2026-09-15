// Solver core for the averaging-to-equalize problem (shared with solver.html).
// Uses BigInt for exact arithmetic. Values are exact dyadic rationals {n, e} = n / 2^e.

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

// ---- Mixability criterion (exact, any size) ----
function judge(arr) { // arr: array of BigInt
  const n = arr.length;
  if (n <= 2) return true;
  let S = 0n; for (const x of arr) S += x;
  if (n === 3) {
    const b = arr.slice().sort(bigCmp);        // BigInt compare: Number() would lose precision
    return 2n * b[1] === b[0] + b[2];
  }
  const dev = arr.map(x => BigInt(n) * x - S);
  let g = 0n; for (const d of dev) g = gcdBig(g, d);
  if (g === 0n) return true;
  const e = dev.map(d => d / g);
  let G = 0n; for (let i = 1; i < n; i++) G = gcdBig(G, e[i] - e[0]);
  return G > 0n && (G & (G - 1n)) === 0n;
}

// ---- BFS exact min-steps (small n only) ----
function bfsSolve(arr, budget = 200000) {
  const n = arr.length;
  const S = arr.reduce((s, x) => s + x, 0n);
  const start = arr.map(x => ({ n: x, e: 0 }));
  const isTarget = (st) => {
    if (!dyEqToRatio(st[0], S, n)) return false;
    for (let i = 1; i < n; i++) if (dyCmp(st[i], st[0]) !== 0) return false;
    return true;
  };
  if (isTarget(start)) return { steps: [], minSteps: 0 };
  const key = (st) => st.map(d => d.n + '/' + d.e).sort().join(',');
  const seen = new Set([key(start)]);
  const parent = new Map(); // key(child) -> [key(parent), i, j]   (0-based i<j)
  let frontier = [start];
  let depth = 0;
  while (frontier.length) {
    depth++;
    const next = [];
    for (const st of frontier) {
      const sk = key(st);
      for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
          const avg = dyAvg(st[i], st[j]);
          const ns = st.slice();
          ns[i] = avg; ns[j] = avg;
          const k = key(ns);
          if (seen.has(k)) continue;
          seen.add(k);
          parent.set(k, [sk, i, j]);
          if (seen.size > budget) return null;
          if (isTarget(ns)) {
            const steps = [];
            let cur = k;
            while (cur !== key(start)) {
              const [pk, i, j] = parent.get(cur);
              steps.push([i + 1, j + 1]); // 1-based
              cur = pk;
            }
            steps.reverse();
            return { steps, minSteps: depth };
          }
          next.push(ns);
        }
      }
    }
    frontier = next;
  }
  return null;
}

// ---- Correct (non-minimal) construction for n = 2^k ----
function power2Tree(n) {
  if (n & (n - 1)) return null;
  const steps = [];
  (function rec(lo, hi) {
    if (hi - lo === 1) return;
    if (hi - lo === 2) { steps.push([lo + 1, hi]); return; }
    const mid = (lo + hi) >> 1;
    rec(lo, mid); rec(mid, hi);
    for (let k = 0; k < mid - lo; k++) steps.push([lo + k + 1, mid + k + 1]);
  })(0, n);
  return steps;
}

// ---- Randomized constructive search (fallback, not guaranteed) ----
function greedySolve(arr, restarts = 80, maxSteps = 100) {
  const n = arr.length;
  const S = arr.reduce((s, x) => s + x, 0n);
  const start = arr.map(x => ({ n: x, e: 0 }));
  const isDone = (st) => {
    for (let i = 1; i < n; i++) if (dyCmp(st[i], st[0]) !== 0) return false;
    return dyEqToRatio(st[0], S, n);
  };
  let seed = 987654321;
  const rnd = () => { seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5; return (seed >>> 0) / 4294967296; };
  for (let r = 0; r < restarts; r++) {
    let st = start.slice();
    const steps = [];
    for (let t = 0; t < maxSteps; t++) {
      let imin = 0, imax = 0;
      for (let k = 1; k < n; k++) {
        if (dyCmp(st[k], st[imin]) < 0) imin = k;
        if (dyCmp(st[k], st[imax]) > 0) imax = k;
      }
      let i, j;
      if (rnd() < 0.15) { i = Math.floor(rnd() * n); j = Math.floor(rnd() * n); if (i === j) j = (j + 1) % n; }
      else { i = imin; j = imax; }
      if (i > j) [i, j] = [j, i];
      const avg = dyAvg(st[i], st[j]);
      st = st.slice(); st[i] = avg; st[j] = avg;
      steps.push([i + 1, j + 1]);
      if (isDone(st)) return { steps, minSteps: null };
    }
  }
  return null;
}

// ---- Orchestrator ----
function solve(arr, opts = {}) {
  const n = arr.length;
  const big = arr.map(x => BigInt(x));
  const ok = judge(big);
  if (!ok) return { ok: false, steps: null, minSteps: null, method: 'criterion' };
  const maxAbs = Math.max(...arr.map(x => Math.abs(Number(x))));

  // fast paths
  if (n === 1) return { ok: true, steps: [], minSteps: 0, method: 'trivial' };
  if (n === 2) return { ok: true, steps: [[1, 2]], minSteps: 1, method: 'trivial' };
  if (n === 3) {
    const b = arr.map((v, i) => [BigInt(v), i]).sort((x, y) => (x[0] < y[0] ? -1 : x[0] > y[0] ? 1 : 0));
    return { ok: true, steps: [[b[0][1] + 1, b[2][1] + 1]], minSteps: 1, method: 'arithmetic-progression' };
  }

  if (n <= 7 && maxAbs <= 80) {
    const r = bfsSolve(big);
    if (r) return { ok: true, steps: r.steps, minSteps: r.minSteps, method: 'bfs-exact' };
  }
  if (power2Tree(n)) {
    return { ok: true, steps: power2Tree(n), minSteps: null, method: 'power2-tree' };
  }
  const g = greedySolve(big);
  if (g) return { ok: true, steps: g.steps, minSteps: null, method: 'greedy' };
  return { ok: true, steps: null, minSteps: null, method: 'criterion-only' };
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { judge, bfsSolve, power2Tree, greedySolve, solve, dyAvg, dyCmp, dyReduce, dyEqToRatio };
}
