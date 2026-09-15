const absBI = x => x < 0n ? -x : x;
function gcdBI(a, b){ a = absBI(a); b = absBI(b); while(b){ const t = a % b; a = b; b = t; } return a; }
class Fr{
  constructor(n, d = 1n){
    if(d < 0n){ n = -n; d = -d; }
    const g = gcdBI(n, d) || 1n;
    this.n = n / g; this.d = d / g;
  }
  static of(x){ return x instanceof Fr ? x : new Fr(BigInt(x)); }
  add(o){ o = Fr.of(o); return new Fr(this.n*o.d + o.n*this.d, this.d*o.d); }
  sub(o){ o = Fr.of(o); return new Fr(this.n*o.d - o.n*this.d, this.d*o.d); }
  neg(){ return new Fr(-this.n, this.d); }
  abs(){ return this.n < 0n ? new Fr(-this.n, this.d) : this; }
  isZero(){ return this.n === 0n; }
  cmp(o){ o = Fr.of(o); const L = this.n*o.d, R = o.n*this.d; return L < R ? -1 : (L > R ? 1 : 0); }
  key(){ return this.d === 1n ? this.n.toString() : this.n + '/' + this.d; }
  toString(){ return this.key(); }
  num(){ return Number(this.n) / Number(this.d); }
}
const avg3 = (a,b,c) => { const s = a.add(b).add(c); return new Fr(s.n, s.d * 3n); };
const log3 = (G) => { let k = 0; while(G % 3n === 0n){ G /= 3n; k++; } return G === 1n ? k : -1; };
function smallestNonThreeFactor(G){
  G = absBI(G);
  while(G % 3n === 0n) G /= 3n;
  if(G === 1n) return null;
  for(let p = 2n; p*p <= G && p < 1000000n; p++) if(G % p === 0n) return p;
  return G;
}

/* ============================================================
   判定
============================================================ */
function analyze(arr){
  const n = arr.length;
  const S = arr.reduce((s,x) => s + x, 0n);
  const A = new Fr(S, BigInt(n));
  const allEqual = arr.every(x => x === arr[0]);
  const info = { n, S, A, allEqual, supported:true, feasible:null, trivial:false, reason:'', e:null, g:null, G:null, k:null };
  if(allEqual){ info.feasible = true; info.trivial = true; info.reason = '所有数已经相等，0 步即可。'; return info; }
  if(n === 2){ info.feasible = false; info.reason = 'n = 2：仅当两数原本相等时可行。'; return info; }
  if(n === 3){ info.feasible = true; info.reason = 'n = 3：恒可，一次平均即可。'; return info; }
  if(n >= 4 && n <= 6){ info.supported = false; info.reason = 'n = 4, 5, 6 暂不支持（G 判据仅适用于 n ≥ 7）。'; return info; }
  if(n >= 7){
    const d = arr.map(x => BigInt(n)*x - S);
    let g = 0n; for(const x of d) g = gcdBI(g, x);
    const e = d.map(x => x / g);
    let G = 0n; for(let i = 1; i < n; i++) G = gcdBI(G, absBI(e[i] - e[0]));
    const k = log3(G);
    info.e = e; info.g = g; info.G = G; info.k = k;
    info.feasible = (k >= 0);
    info.reason = info.feasible
      ? ('G = ' + G.toString() + ' = 3^' + k + '，满足判据。')
      : ('G = ' + G.toString() + '，含非 3 素因子 ' + smallestNonThreeFactor(G) + '，不是 3 的幂。');
  }
  return info;
}

/* ============================================================
   求解器内部工具（在偏差坐标系 v[i] = a[i] − A，目标全零）
============================================================ */
function viewOf(v){
  const nums = v.map(f => f.num());
  const nz = [], zl = [];
  for(let i = 0; i < v.length; i++) (v[i].isZero() ? zl : nz).push(i);
  const sorted = nums.map((x,i) => ({x, i})).sort((p,q) => p.x - q.x);
  return { v, nums, nz, zl, sorted };
}
function applyOpArr(v, i, j, l){
  const m = avg3(v[i], v[j], v[l]);
  const w = v.slice(); w[i] = m; w[j] = m; w[l] = m; return w;
}
// 在排序数组中找值最接近 t 的下标（排除 exc）
function nearestIdx(view, t, exc){
  const s = view.sorted; let lo = 0, hi = s.length - 1, best = null, bd = Infinity;
  while(lo <= hi){ const mid = (lo + hi) >> 1; if(s[mid].x < t) lo = mid + 1; else hi = mid - 1; }
  for(const c of [lo-1, lo, lo+1]){
    if(c < 0 || c >= s.length) continue;
    const idx = s[c].i; if(exc && exc.has(idx)) continue;
    const d = Math.abs(s[c].x - t); if(d < bd){ bd = d; best = idx; }
  }
  return best;
}
// 零和三元组（含借助零位置的 (u,-u,0) 与 (u,u,-2u)）：精确判定，Number 预筛
function findKill(view){
  const { v, nums, nz, sorted } = view;
  const P = nz.length;
  if(P < 2) return null;
  let best = null, bestScore = -1;
  for(let a = 0; a < P; a++){
    for(let b = a + 1; b < P; b++){
      const i = nz[a], j = nz[b];
      const t = -(nums[i] + nums[j]);
      const tol = 1e-9 * (1 + Math.abs(nums[i]) + Math.abs(nums[j]));
      // 二分定位窗口左端，再扫描整个窗口
      let lo = 0, hi = sorted.length - 1;
      while(lo <= hi){ const mid = (lo + hi) >> 1; if(sorted[mid].x < t - tol) lo = mid + 1; else hi = mid - 1; }
      for(let c = Math.max(0, lo - 1); c < sorted.length && sorted[c].x <= t + tol; c++){
        const l = sorted[c].i;
        if(l === i || l === j) continue;
        if(!v[i].add(v[j]).add(v[l]).isZero()) continue;
        const killNz = v[l].isZero() ? 2 : 3;
        const mag = Math.abs(nums[i]) + Math.abs(nums[j]) + Math.abs(nums[l]);
        const score = killNz * 1e15 + mag;
        if(score > bestScore){ bestScore = score; best = [i, j, l]; }
      }
    }
  }
  return best;
}
// 中间相遇：单趟查找大小 ∈ sizes（按优先序）的精确零和子集
function mitmZeroSubset(v, idxList, sizes){
  const half = idxList.length >> 1;
  const A = idxList.slice(0, half), B = idxList.slice(half);
  const maxSize = Math.max(...sizes);
  const mapA = new Map(); // "sz|key" -> mask
  const nA = A.length;
  const total = 1 << nA;
  const szOf = new Uint8Array(total); const sumOf = new Array(total);
  sumOf[0] = new Fr(0n);
  mapA.set('0|0', 0); // 空子集：允许纯 B 侧命中
  for(let m = 1; m < total; m++){
    const lb = m & (-m); const bit = 31 - Math.clz32(lb);
    const pm = m ^ lb;
    szOf[m] = szOf[pm] + 1;
    sumOf[m] = sumOf[pm].add(v[A[bit]]);
    if(szOf[m] <= maxSize){
      const k = szOf[m] + '|' + sumOf[m].key();
      if(!mapA.has(k)) mapA.set(k, m);
    }
  }
  const nB = B.length; const totalB = 1 << nB;
  const szB = new Uint8Array(totalB); const sumB = new Array(totalB);
  sumB[0] = new Fr(0n);
  for(let m = 0; m < totalB; m++){
    if(m > 0){
      const lb = m & (-m); const bit = 31 - Math.clz32(lb); const pm = m ^ lb;
      szB[m] = szB[pm] + 1; sumB[m] = sumB[pm].add(v[B[bit]]);
    }
    if(szB[m] > maxSize) continue;
    const negKey = sumB[m].neg().key();
    for(const size of sizes){
      const needSz = size - szB[m];
      if(needSz < 0 || needSz > nA) continue;
      const am = mapA.get(needSz + '|' + negKey);
      if(am !== undefined){
        const out = [];
        for(let b = 0; b < nA; b++) if(am & (1 << b)) out.push(A[b]);
        for(let b = 0; b < nB; b++) if(m & (1 << b)) out.push(B[b]);
        if(out.length === size) return { size, indices: out };
      }
    }
  }
  return null;
}
// 宏构造：输入位置数组 P（其值精确和为 0）与零位置列表 zl
function buildMacro(size, P, zl){
  const [p1,p2,p3,p4,p5,p6,p7,p8,p9] = P;
  if(size === 4){ const [z1,z2,z3] = zl; return [[p1,p2,z1],[p3,p4,z2],[p1,p3,z3],[p2,p4,p1],[z1,z2,p3]]; }
  if(size === 5){ const [z1,z2] = zl; return [[p1,p2,p3],[p4,p5,z1],[p1,p4,z2],[p2,p5,p1],[p3,z1,p2]]; }
  if(size === 6){ const [z1] = zl; return [[p1,p2,p3],[p4,p5,p6],[p1,p4,z1],[p2,p5,p1],[p3,p6,p2]]; }
  if(size === 7){ const [z1,z2] = zl; return [[p1,p2,p3],[p4,p5,z1],[p6,p7,z2],[p1,p4,p6],[p2,p5,p7],[p3,z1,z2]]; }
  if(size === 8){ const [z1] = zl; return [[p1,p2,p3],[p4,p5,p6],[p7,p8,z1],[p1,p4,p7],[p2,p5,p8],[p3,p6,z1]]; }
  if(size === 9){ return [[p1,p2,p3],[p4,p5,p6],[p7,p8,p9],[p1,p4,p7],[p2,p5,p8],[p3,p6,p9]]; }
  return null;
}
const MACRO_ORDER = [[9,0],[8,1],[7,2],[6,1],[5,2],[4,3]];
function findMacro(view){
  const p = view.nz.length;
  if(p < 4 || p > 24) return null;
  const sizes = MACRO_ORDER.filter(([size, needZ]) => p >= size && view.zl.length >= needZ).map(x => x[0]);
  if(!sizes.length) return null;
  const hit = mitmZeroSubset(view.v, view.nz, sizes);
  if(hit) return buildMacro(hit.size, hit.indices, view.zl);
  return null;
}
// 一步构造：尝试一个操作使下一步可以立即消元
function findFab(view){
  const { v, nums, nz, zl } = view;
  const p = nz.length;
  const pool = nz.slice().sort((a,b) => Math.abs(nums[b]) - Math.abs(nums[a])).slice(0, 12);
  let best = null, bestNnz = p, bestAbs = Infinity;
  const curAbs = nz.reduce((s,i) => s + Math.abs(nums[i]), 0);
  for(let a = 0; a < pool.length; a++){
    for(let b = a + 1; b < pool.length; b++){
      const i = pool[a], j = pool[b];
      const s = nums[i] + nums[j];
      const cand = [];
      const ln = nearestIdx(view, -s, new Set([i, j]));
      if(ln !== null && ln !== undefined) cand.push(ln);
      if(zl.length) cand.push(zl[0]);
      for(const l of cand){
        if(l === i || l === j) continue;
        const v2 = applyOpArr(v, i, j, l);
        const vw2 = viewOf(v2);
        const kt = findKill(vw2);
        if(!kt) continue;
        const nnz2 = vw2.nz.length - (v2[kt[2]].isZero() ? 2 : 3);
        const abs2 = vw2.nz.reduce((s2,i2) => s2 + Math.abs(vw2.nums[i2]), 0);
        if(nnz2 < bestNnz || (nnz2 === bestNnz && abs2 < bestAbs - 1e-9)){
          bestNnz = nnz2; bestAbs = abs2; best = [[i, j, l], kt];
        }
      }
    }
  }
  if(best && bestNnz < p) return best;
  return null;
}
/* ---------------- 集束搜索 ---------------- */
function sigOf(v){ return v.map(f => f.key()).sort().join('|'); }
function scoreOf(view){
  let sa = 0; for(const i of view.nz) sa += Math.abs(view.nums[i]);
  const distinct = new Set(view.nz.map(i => view.v[i].key())).size;
  return view.nz.length * 1e12 + distinct * 1e6 + sa;
}
function genMoves(view, cap){
  const { v, nums, nz, zl } = view;
  const moves = []; const seen = new Set();
  const push = (i,j,l) => {
    if(i === j || i === l || j === l) return;
    const key = [i,j,l].sort((x,y) => x - y).join(',');
    if(seen.has(key)) return; seen.add(key); moves.push([i,j,l]);
  };
  // 1) 精确消元
  const P = nz.length;
  const sortedPool = nz.slice().sort((a,b) => Math.abs(nums[b]) - Math.abs(nums[a]));
  outer:
  for(let a = 0; a < P; a++) for(let b = a + 1; b < P; b++){
    const i = nz[a], j = nz[b];
    const t = -(nums[i] + nums[j]);
    const l = nearestIdx(view, t, new Set([i, j]));
    if(l === null || l === undefined) continue;
    if(Math.abs(nums[l] - t) <= 1e-9 * (1 + Math.abs(nums[i]) + Math.abs(nums[j]))){
      if(v[i].add(v[j]).add(v[l]).isZero()){ push(i, j, l); if(moves.length >= 14) break outer; }
    }
  }
  // 2) 构造候选：大幅值/异号配对 + 最近伙伴 + 零伙伴
  const pairs = [];
  const top = sortedPool.slice(0, 14);
  for(let a = 0; a < top.length; a++) for(let b = a + 1; b < top.length; b++){
    const i = top[a], j = top[b];
    const mixed = (nums[i] > 0) !== (nums[j] > 0);
    pairs.push({ i, j, w: (mixed ? 1e15 : 0) + Math.abs(nums[i] + nums[j]) * -1 });
  }
  pairs.sort((p,q) => q.w - p.w);
  for(const pr of pairs.slice(0, 22)){
    const s = nums[pr.i] + nums[pr.j];
    const l1 = nearestIdx(view, -s, new Set([pr.i, pr.j]));
    if(l1 !== null && l1 !== undefined) push(pr.i, pr.j, l1);
    if(zl.length) push(pr.i, pr.j, zl[0]);
    if(moves.length >= cap) break;
  }
  // 2b) 制造等值：op 后 m 恰好等于某个现有值（为 (u,u,-2u)/三消铺路）
  let dupCount = 0;
  const uniqIdx = nz.slice(0, 24);
  for(const pr of pairs.slice(0, 10)){
    const s = nums[pr.i] + nums[pr.j];
    for(const t of uniqIdx){
      const target = 3 * nums[t] - s; // 需要 v_l = 3v_t − (v_i+v_j)
      const l = nearestIdx(view, target, new Set([pr.i, pr.j, t]));
      if(l === null || l === undefined) continue;
      if(Math.abs(nums[l] - target) > 1e-9 * (1 + Math.abs(target))) continue;
      const mVal = avg3(v[pr.i], v[pr.j], v[l]);
      if(mVal.cmp(v[t]) !== 0) continue;
      push(pr.i, pr.j, l);
      if(++dupCount >= 16) break;
    }
    if(dupCount >= 16 || moves.length >= cap) break;
  }
  // 3) 分散操作以制造副本
  if(zl.length >= 2 && sortedPool.length) push(sortedPool[0], zl[0], zl[1]);
  return moves.slice(0, cap);
}
async function beamSearch(v0, budget, shouldCancel){
  const t0 = performance.now();
  const W = budget.width, D = budget.depth, cap = budget.moveCap;
  const visited = new Set([sigOf(v0)]);
  let beam = [{ v: v0, parent: null, op: null, h: scoreOf(viewOf(v0)) }];
  let nodes = 1;
  for(let depth = 0; depth < D; depth++){
    let cand = [];
    for(const node of beam){
      const view = viewOf(node.v);
      const moves = genMoves(view, cap);
      for(const m of moves){
        const v2 = applyOpArr(node.v, m[0], m[1], m[2]);
        const s = sigOf(v2);
        if(visited.has(s)) continue;
        visited.add(s);
        const vw2 = viewOf(v2);
        const nn = { v: v2, parent: node, op: m, h: scoreOf(vw2) };
        nodes++;
        if(vw2.nz.length === 0){
          const ops = []; let cur = nn;
          while(cur && cur.op){ ops.push(cur.op); cur = cur.parent; }
          return ops.reverse();
        }
        cand.push(nn);
      }
      if((nodes & 511) === 0){
        if(shouldCancel && shouldCancel()) return null;
        if(performance.now() - t0 > budget.timeMs) return null;
        if(nodes > budget.maxNodes) return null;
        await new Promise(r => setTimeout(r, 0));
      }
    }
    if(!cand.length) return null;
    cand.sort((x, y) => x.h - y.h);
    beam = cand.slice(0, W);
    cand = null;
  }
  return null;
}

/* ============================================================
   主求解入口
============================================================ */
async function solveFeasible(arr, info, budget, shouldCancel){
  const n = arr.length;
  const t0 = performance.now();
  if(info.trivial) return { ops: [], method: '已全等（0 步）', timeMs: 0 };
  if(n === 3) return { ops: [[0,1,2]], method: 'n=3 一次平均', timeMs: performance.now() - t0 };
  let v = arr.map(x => new Fr(x).sub(info.A));
  const ops = [];
  const notes = new Set();
  const doOp = (i, j, l) => { const m = avg3(v[i], v[j], v[l]); v[i] = m; v[j] = m; v[l] = m; ops.push([i, j, l]); };
  let guard = 3000;
  while(guard-- > 0){
    const view = viewOf(v);
    const p = view.nz.length;
    if(p === 0) break;
    if(p === 2){
      if(view.zl.length){ doOp(view.nz[0], view.nz[1], view.zl[0]); notes.add('正负对消元'); continue; }
      break;
    }
    if(p === 3){ doOp(view.nz[0], view.nz[1], view.nz[2]); notes.add('零和三元组'); continue; }
    const kt = findKill(view);
    if(kt){ doOp(kt[0], kt[1], kt[2]); notes.add('零和三元组/对消'); continue; }
    const mc = findMacro(view);
    if(mc){ for(const o of mc) doOp(o[0], o[1], o[2]); notes.add('零和子集宏(' + mc.length + '步)'); continue; }
    const fb = findFab(view);
    if(fb){ doOp(fb[0][0], fb[0][1], fb[0][2]); doOp(fb[1][0], fb[1][1], fb[1][2]); notes.add('一步构造+消元'); continue; }
    break;
  }
  if(!v.every(x => x.isZero())){
    notes.add('集束搜索');
    const rest = await beamSearch(v, budget, shouldCancel);
    if(!rest) return { ops: null, notFound: true, partialOps: ops.length, timeMs: performance.now() - t0, method: [...notes].join(' → ') };
    for(const o of rest) doOp(o[0], o[1], o[2]);
  }
  let finalOps = ops;
  if(finalOps.length <= 60){ // 冗余步删除优化
    let i = 0, trimmed = 0;
    while(i < finalOps.length){
      const cand = finalOps.slice(0, i).concat(finalOps.slice(i + 1));
      const r = verify(arr, cand, false);
      if(r.ok){ finalOps = cand; trimmed++; } else i++;
    }
    if(trimmed) notes.add('删除冗余 ' + trimmed + ' 步');
  }
  return { ops: finalOps, method: [...notes].join(' → '), timeMs: performance.now() - t0 };
}

/* ============================================================
   独立验证器：从原始输入精确重放
============================================================ */
function verify(arr, ops, wantTrace = true){
  const n = arr.length;
  const S = arr.reduce((s,x) => s + x, 0n);
  const A = new Fr(S, BigInt(n));
  let v = arr.map(x => new Fr(x));
  const trace = wantTrace ? [v] : null;
  for(let t = 0; t < ops.length; t++){
    const [i, j, l] = ops[t];
    const bad = [i, j, l].some(x => !Number.isInteger(x) || x < 0 || x >= n);
    if(bad || i === j || i === l || j === l) return { ok: false, failAt: t + 1, msg: '第 ' + (t+1) + ' 步位置不合法（越界或重复）' };
    const m = avg3(v[i], v[j], v[l]);
    v = v.slice(); v[i] = m; v[j] = m; v[l] = m;
    if(wantTrace) trace.push(v);
  }
  const ok = v.every(x => x.cmp(A) === 0);
  return ok
    ? { ok: true, trace, msg: '重放 ' + ops.length + ' 步，终态全部精确等于均值 A = ' + A.toString() }
    : { ok: false, trace, msg: '终态未全部等于均值' };
}

/* ============================================================
   随机实例：真随机抽样 + 判据筛选（拒绝采样）
============================================================ */
function randInt(V){ return Math.floor(Math.random() * (2 * V + 1)) - V; }
function genSolvable(n, V){
  const t0 = performance.now();
  let attempts = 0, arr = null, info = null;
  while(attempts < 400000){
    attempts++;
    const a = Array.from({length: n}, () => BigInt(randInt(V)));
    const inf = analyze(a);
    if(!inf.supported || !inf.feasible) continue;
    if(inf.trivial) continue; // 跳过太平凡的全等
    arr = a; info = inf; break;
  }
  return { arr, info, attempts, ms: performance.now() - t0 };
}

/* ============================================================
   UI 状态
============================================================ */
