#!/usr/bin/env python3
"""HISTORICAL/EXPERIMENTAL kappa-depth lower-bound implementation.

Not used by production certification. The per-position depth saturation requires
separate soundness review; the historical claims below are not current guarantees.

These turn "prove that no k-move solution exists" from a hand-written case analysis
(see case_study.md section 2.8) into a millisecond computation.

============================================== BOUND B1: the kappa / depth bound
Work in deviation space: integers x_1..x_n, sum 0; a move replaces x_i,x_j by
(x_i+x_j)/2; the goal is the zero vector.  Track ancestry weights: w_i starts at e_i and
a move on {i,j} sets both to (w_i+w_j)/2.  Induction: the final value of position i is

      value_i = ( sum_j m_ij x_j ) / 2^{h_i}

with m_ij non-negative integers, sum_j m_ij = 2^{h_i}, m_ii >= 1, where h_i is the depth
of position i's ancestry DAG.  h starts at 0 and a move on {i,j} sets both h's to
max(h_i,h_j)+1.  value_i = 0 therefore requires a non-negative integer RELATION of exact
weight 2^{h_i} that involves position i.  Define

      kappa_i = min{ h : exists m >= 0, sum_j m_j = 2^h, m_i >= 1, sum_j m_j x_j = 0 }

(kappa is invariant under scaling x by a non-zero rational; kappa_i = 0 if x_i = 0).
Any solution must realise the depth profile kappa through the process above, hence

      T >= D(kappa) := min #moves of  h=(0,..,0);  move: h_i,h_j <- max(h_i,h_j)+1
                                 to reach h_i >= kappa_i for every i.

D(kappa) is computed by BFS over count-vectors of the small type set {(kappa_i, h_i)}.
Note that the tempting bound "T >= (sum_i kappa_i)/2" is FALSE: when the two chosen
positions have different depths, one move raises the total depth by more than 2
(e.g. [0,0,0,1]: kappa=(2,2,2,2), D=3=min, sum/2=4 would be unsound).

============================================== BOUND B2: zero-sum block partition
The components of a solution's move-graph are zero-sum subsets of the support, so
T >= min over zero-sum partitions P of sum_{B in P} lb(B), for any admissible lb.  Feeding
lb(B) = max(|B|-1, D(kappa(B))) into a subset DP gives a bound that is usually stronger
than either piece alone.

API: lower_bound(a) -> int (admissible), kappas(a), bound_kappa(x), depth_process_distance.
"""
from __future__ import annotations

from collections import deque
from math import gcd


# --------------------------------------------------------------- basic normalisation
def gcd_all(vec):
    g = 0
    for v in vec:
        g = gcd(g, v)
    return g


def reduce_prim(vec):
    g = gcd_all(vec)
    return tuple(vec) if g == 0 else tuple(x // g for x in vec)


def deviations(a):
    n, S = len(a), sum(a)
    return [n * t - S for t in a]


# ------------------------------------------------------------------- kappa_i by DP
def kappa_of_value(xs, val, max_h=8):
    """min h such that SOME non-negative relation m using `val` has sum(m) <= 2^h.

    Sound version: for a position whose ancestry DAG has depth h, the leaf multiplicities
    m satisfy sum(m) <= 2^h  (induction: mixing DAGs of depth h1,h2 gives depth max+1 and
    leaf count L1+L2 <= 2^h1 + 2^h2 <= 2^(max+1)).  So the least admissible h for position
    i is the smallest h with a relation of leaf-count <= 2^h, NOT requiring = 2^h.
    """
    mx = max(abs(v) for v in xs)
    if mx == 0:
        return 0
    # the DP window holds every reachable sum of up to 2^max_h terms, so its size is
    # mx * 2^max_h bits: shrink max_h so the bound stays cheap, give up if it cannot.
    while max_h > 1 and mx * (1 << max_h) > 3_000_000:
        max_h -= 1
    if mx * (1 << max_h) > 3_000_000:
        return None
    terms = 1 << max_h
    window = mx * terms
    mask = (1 << (2 * window + 1)) - 1
    off = window
    others = sorted({v for v in xs if v != val})
    allv = sorted(set(others) | {val})

    def shl(bits, v):
        if v > 0:
            return (bits << v) & mask
        if v < 0:
            return (bits >> (-v)) & mask
        return bits & mask

    g_bits = 1 << off           # reachable sums with exactly t terms, `val` unused
    f_bits = 0                  # reachable sums with exactly t terms, `val` used
    for t in range(1, terms + 1):
        gn = 0
        for v in others:
            gn |= shl(g_bits, v)
        fn = 0
        for v in allv:
            fn |= shl(f_bits, v)
        fn |= shl(g_bits, val)
        g_bits, f_bits = gn & mask, fn & mask
        if (f_bits >> off) & 1:              # a t-term relation using `val` exists
            return (t - 1).bit_length()      # ceil(log2 t)  = smallest h with t <= 2^h
        if not g_bits and not f_bits:
            break
    return None


def kappas_of_deviation(x, max_h=8):
    """[kappa_i] for primitive deviation vector x; None if some kappa is unreachable."""
    x = list(reduce_prim(x))
    if not any(x):
        return [0] * len(x)
    if sum(x) != 0:
        return None
    cache, out = {}, []
    for v in x:
        if v == 0:
            k = 0
        else:
            if v not in cache:
                cache[v] = kappa_of_value(x, v, max_h=max_h)
            k = cache[v]
        if k is None:
            return None
        out.append(k)
    return out


# ------------------------------------------- depth-process distance D(kappa) via BFS
def depth_process_distance(kap, state_cap=300_000):
    """min moves of 'h_i,h_j <- max(h_i,h_j)+1' to get h_i >= kappa_i for all i."""
    req = [k for k in kap if k > 0]
    if not req:
        return 0
    ks = sorted(set(req))
    K = max(ks)
    types = [(k, h) for k in ks for h in range(k + 1)]
    tix = {t: i for i, t in enumerate(types)}
    start = [0] * len(types)
    for k in req:
        start[tix[(k, 0)]] += 1
    start = tuple(start)
    total = len(req)

    def at_goal(cnt):
        return sum(cnt[tix[(k, k)]] for k in ks) == total

    if at_goal(start):
        return 0
    seen = {start}
    q = deque([(start, 0)])
    while q:
        cnt, d = q.popleft()
        present = [(tix[t], t, c) for t, c in zip(types, cnt) if c > 0]
        for ai in range(len(present)):
            ia, ta, ca = present[ai]
            for bi in range(ai, len(present)):
                ib, tb, cb = present[bi]
                if ai == bi and ca < 2:
                    continue
                ka, ha = ta
                kb, hb = tb
                nh = max(ha, hb) + 1
                na, nb = min(nh, ka), min(nh, kb)
                if (ka, na) == ta and (kb, nb) == tb:
                    continue
                new = list(cnt)
                new[ia] -= 1
                new[ib] -= 1
                if new[ia] < 0 or new[ib] < 0:
                    continue
                new[tix[(ka, na)]] += 1
                new[tix[(kb, nb)]] += 1
                nt = tuple(new)
                if nt in seen:
                    continue
                if at_goal(nt):
                    return d + 1
                seen.add(nt)
                if len(seen) > state_cap:
                    return None
                q.append((nt, d + 1))
    return None


def bound_kappa(x, max_h=8):
    kap = kappas_of_deviation(x, max_h=max_h)
    if kap is None:
        return None, None
    return depth_process_distance(kap), kap


# ------------------------------------------------------- block partition DP (B2)
def _block_bound_cache():
    return {}


def partition_lb(vals, cost_lb, cap=1 << 20):
    """min over zero-sum partitions of sum cost_lb(block); None if impossible/large."""
    z = len(vals)
    if z == 0:
        return 0
    if z > 20:
        return None
    sums = [0] * (1 << z)
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        sums[mask] = sums[mask ^ (1 << b)] + vals[b]
    full = (1 << z) - 1
    if sums[full] != 0:
        return None
    INF = float("inf")
    dp = [INF] * (1 << z)
    dp[0] = 0
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << b)
        sub = rest
        while True:
            part = sub | (1 << b)
            if sums[part] == 0 and dp[mask ^ part] < INF:
                c = cost_lb(tuple(vals[k] for k in range(z) if part >> k & 1))
                if c is not None and dp[mask ^ part] + c < dp[mask]:
                    dp[mask] = dp[mask ^ part] + c
            if sub == 0:
                break
            sub = (sub - 1) & rest
    return None if dp[full] == INF else dp[full]


def simple_lb(x):
    """Non-zero count / 2 and distinct-magnitude / 2 (both moves touch 2 positions).

    NOTE: a global "z-1" connectivity bound would be UNSOUND (it ignores that the
    solution may split into several zero-sum components); connectivity only enters
    legitimately through the per-block |B|-1 term of the partition DP below.
    """
    nz = [v for v in x if v]
    z = len(nz)
    if z == 0:
        return 0
    return max((z + 1) // 2, (len({abs(v) for v in nz}) + 1) // 2)


def lower_bound(a, max_h=8, use_partition=True, detail=False):
    x = list(reduce_prim(deviations(a)))
    if not any(x):
        return (0, {}) if detail else 0
    lb_k, kap = bound_kappa(x, max_h=max_h)
    best = max(lb_k or 0, simple_lb(x))
    info = {"kappa": kap, "D_kappa": lb_k, "simple": simple_lb(x)}
    if use_partition:
        nz_idx = [i for i, v in enumerate(x) if v]
        vals = [x[i] for i in nz_idx]

        def blk_lb(block):
            b = list(block)
            k2 = kappas_of_deviation(b)
            d2 = depth_process_distance(k2) if k2 else None
            # |B|-1 is sound here: a block of the partition is one connected component
            return max(len(b) - 1, simple_lb(b), d2 or 0)

        p = partition_lb(vals, blk_lb)
        info["partition"] = p
        if p is not None:
            best = max(best, p)
    return (best, info) if detail else best


if __name__ == "__main__":
    import time
    tests = [
        ([0, 0, 0, 1], 3),
        ([0, 0, 0, 1, 9], 9),
        ([1, 3, 5, 7, 9], None),
        ([0, 2, 4, 6, 8], None),
        ([38, -23, -14, 16, -11, 4, 63, 80, 14, 38], 10),
        ([-81, -60, -95, -95, -20, -13, -87, -80, 42, 54], 11),
    ]
    for a, truth in tests:
        t0 = time.time()
        lb, info = lower_bound(a, detail=True)
        flag = "" if truth is None else ("  ok" if lb <= truth else "  UNSOUND!!")
        print(f"{str(a):>46} true={truth}  LB={lb}  kappa={info['kappa']} "
              f"D={info['D_kappa']} part={info['partition']} ({time.time()-t0:.3f}s){flag}")
