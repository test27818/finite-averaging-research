#!/usr/bin/env python3
"""Exact min-steps solver v2: projective integer states + admissible heuristics
+ zero-sum-partition branch & bound.

RECIPE (why each ingredient matters)
------------------------------------
1.  Deviation space, integer only.  x_i = n*a_i - S (integers, sum 0), goal = zero
    vector, a move is (x_i,x_j) -> (x_i+x_j)/2.  Global rescaling by a non-zero rational
    commutes with every move and preserves "all zero" => it is a symmetry, so after each
    move multiply by 2 and divide by the gcd:

        x_i, x_j <- x_i + x_j,   x_k <- 2 x_k,   then / gcd     (all integers!)

    => primitive integer states, bounded bit size, and NO denominator cutoff.  The old
    Fraction BFS needed max_den_exp and silently became incomplete without it.
2.  Canonical key = sorted + primitive + sign-canonical (x ~ -x is free as well):
    permutations, scalings and sign flips collapse to one node.
3.  A* with admissible+consistent heuristics (non-zero count, "no opposite pair => a
    setup move is needed", distinct magnitudes), and a `limit` mode that *certifies*
    "no solution with <= limit moves" when the frontier is exhausted.
4.  Partition theorem: min(support) = min over zero-sum partitions of sum of the block
    minima.  So enumerate zero-sum subsets (2^z), solve each block exactly (memoised by
    canonical key), DP over partitions => an exact UB; the same DP with the admissible
    block bounds => LB.  UB == LB certifies the answer; otherwise a limit-mode decision
    search on the whole instance closes the gap (this is what turns the hand-written
    "no 9-step solution" proof of case_study.md into 20 seconds of machine search).

API: solve(a) -> dict(min_steps, sequence, lb, ub, certified, method, states, time, blocks)
     exact_block_map(a), partition_lb(...), astar(...)
"""
from __future__ import annotations

import heapq
import json
import os
import sys
import time
from functools import lru_cache
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from solver import judge, verify_sequence  # noqa: E402

_USE_KAPPA = os.environ.get("AVG_NO_KAPPA") is None     # kappa bound is a bit costly


# ------------------------------------------------------------------ state utilities
def gcd_all(vec):
    g = 0
    for v in vec:
        g = gcd(g, v)
    return g


def reduce_prim(vec):
    g = gcd_all(vec)
    return tuple(vec) if g == 0 else tuple(x // g for x in vec)


def key_of(vec):
    """Projective canonical key: primitive + sorted + sign canonical."""
    g = gcd_all(vec)
    if g == 0:
        return tuple([0] * len(vec))
    pos = tuple(sorted(x // g for x in vec))
    neg = tuple(sorted(-x // g for x in vec))
    return pos if pos <= neg else neg


def deviations(a):
    n, S = len(a), sum(a)
    return [n * x - S for x in a]


# ----------------------------------------------------------------------- heuristics
def h_cancel(vec):
    return (sum(1 for v in vec if v) + 1) // 2


def h_setup(vec):
    z = sum(1 for v in vec if v)
    if z < 2:
        return z
    s = {v for v in vec if v}
    if any(-v in s for v in s):
        return (z + 1) // 2
    return (z + 1) // 2 + 1


def h_distinct(vec):
    return (len({abs(v) for v in vec if v}) + 1) // 2


def heuristic(vec):
    return max(h_cancel(vec), h_setup(vec), h_distinct(vec))


# --------------------------------------------------------------------------- A*
_Memo: dict = {}          # LABELED start tuple -> (min_steps, seq)   (order matters!
                        #            a sequence is only valid for the order it was found in)


def astar(vec, node_budget=1_000_000, deadline=None, limit=None, memo=True):
    """Optimal search on primitive-integer deviation states.

    Returns (steps|None, sequence|None, pops, status) with status in
      'solved'  optimal count found (a solution with <= limit moves, in limit mode)
      'proved'  exhausted: no solution with <= limit moves exists (a certificate)
      'budget'  gave up on node budget / wall clock
    """
    n = len(vec)
    start = reduce_prim(vec)
    if not any(start):
        return 0, [], 0, "solved"
    ck = key_of(start)
    if memo and limit is None and start in _Memo:
        st, sq = _Memo[start]
        return st, sq, 0, "solved"
    h0 = heuristic(start)
    if limit is not None and h0 > limit:
        return None, None, 0, "proved"
    k0 = ck
    heap = [(h0, 0, k0)]
    best = {k0: 0}
    state = {k0: start}
    parent = {k0: None}
    pops = 0
    while heap:
        f, cst, key = heapq.heappop(heap)
        if best.get(key, 1 << 60) != cst:
            continue
        if limit is not None and f > limit:
            return None, None, pops, "proved"
        pops += 1
        if pops > node_budget:
            return None, None, pops, "budget"
        if deadline is not None and pops % 8192 == 0 and time.time() > deadline:
            return None, None, pops, "budget"
        st = state[key]
        if not any(st):                      # goal on POP => optimal
            seq = []
            cur = key
            while parent[cur] is not None:
                pk, mv = parent[cur]
                seq.append((mv[0] + 1, mv[1] + 1))
                cur = pk
            seq.reverse()
            if memo and limit is None:
                _Memo[start] = (cst, seq)
            return cst, seq, pops, "solved"
        g2 = cst + 1
        for i in range(n):
            si = st[i]
            for j in range(i + 1, n):
                if si == st[j]:
                    continue                 # averaging equal values = no-op
                s = si + st[j]
                ns = [s if k in (i, j) else 2 * x for k, x in enumerate(st)]
                nk = key_of(ns)
                if best.get(nk, 1 << 60) <= g2:
                    continue
                nsl = reduce_prim(ns)
                hh = heuristic(nsl)
                if limit is not None and g2 + hh > limit:
                    continue
                best[nk] = g2
                state[nk] = nsl
                parent[nk] = (key, (i, j))
                heapq.heappush(heap, (g2 + hh, g2, nk))
    return None, None, pops, ("proved" if not heap else "budget")


# ------------------------------------------------- zero-sum subsets & partition DP
def zero_sum_masks(vals):
    """masks (over the support) whose value-sum is 0, as dict mask -> True."""
    z = len(vals)
    sums = [0] * (1 << z)
    out = []
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        sums[mask] = sums[mask ^ (1 << b)] + vals[b]
        if sums[0 + mask] == 0:
            out.append(mask)
    return sums, out


def block_lb(block):
    """Admissible cost of one zero-sum block: connectivity + counting + kappa bound."""
    m = sum(1 for v in block if v)
    if m <= 0:
        return 0
    lb = max(m - 1, heuristic(block))
    if _USE_KAPPA:
        try:
            from lower import bound_kappa
            d, _kap = bound_kappa(list(reduce_prim(block)))
            if d:
                lb = max(lb, d)
        except Exception:
            pass
    return lb


def partition_dp(vals, cost, cost_lb):
    """DP over set partitions into zero-sum parts.

    cost(mask)     -> an achievable block cost (None if unknown)      => UB
    cost_lb(mask)  -> admissible block lower bound
    Returns (ub, ub_parts, lb, lb_parts) with None where not derivable.
    """
    z = len(vals)
    sums, zs = zero_sum_masks(vals)
    full = (1 << z) - 1
    if z == 0:
        return 0, [], 0, []
    if sums[full] != 0:
        return None, None, None, None
    INF = float("inf")
    dpU, chU = [INF] * (1 << z), [0] * (1 << z)
    dpL, chL = [INF] * (1 << z), [0] * (1 << z)
    dpU[0] = dpL[0] = 0
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << b)
        sub = rest
        while True:
            part = sub | (1 << b)
            if sums[part] == 0 and mask ^ part < mask:
                c = cost(part)
                if c is not None and dpU[mask ^ part] < INF:
                    cand = dpU[mask ^ part] + c
                    if cand < dpU[mask]:
                        dpU[mask], chU[mask] = cand, part
                cand = dpL[mask ^ part] + cost_lb(part)
                if cand < dpL[mask]:
                    dpL[mask], chL[mask] = cand, part
            if sub == 0:
                break
            sub = (sub - 1) & rest
    def unpack(ch):
        parts, m = [], full
        while m:
            p = ch[m]
            parts.append(p)
            m ^= p
        return parts
    ub = None if dpU[full] == INF else dpU[full]
    lb = None if dpL[full] == INF else dpL[full]
    return ub, (unpack(chU) if ub is not None else None), lb, (unpack(chL) if lb is not None else None)


def bits(mask):
    return [k for k in range(mask.bit_length()) if mask >> k & 1]


# --------------------------------------------------------------------- top level solve
def solve(a, deadline_s=60.0, node_budget=1_000_000, max_support=22,
          max_exact_block=7):
    t0 = time.time()
    dl = t0 + deadline_s
    if not judge(a):
        return {"ok": False, "reason": "not mixable"}
    base = list(reduce_prim(deviations(a)))
    if not any(base):
        return {"ok": True, "min_steps": 0, "sequence": [], "certified": True,
                "method": "trivial", "lb": 0, "ub": 0, "states": 0, "time": 0.0}
    supp = [i for i, v in enumerate(base) if v]
    z = len(supp)
    nodes = 0
    vals = [base[i] for i in supp]

    if z <= max_support:
        exact: dict = {}

        def cost(mask):
            """Exact block cost, only for blocks small enough to solve exhaustively."""
            if len(bits(mask)) > max_exact_block:
                return None
            if mask not in exact:
                sub = [vals[k] for k in bits(mask)]
                ms, sq, p, _ = astar(sub, node_budget=node_budget, deadline=dl)
                nodes_holder[0] += p
                exact[mask] = (ms, sq)
            return exact[mask][0]

        nodes_holder = [0]

        def clb(mask):
            return block_lb([vals[k] for k in bits(mask)])

        ub, pU, lb, pL = partition_dp(vals, cost, clb)
        nodes += nodes_holder[0]
        if ub is not None:
            # rebuild the absolute-index sequence for the chosen partition
            seq, ok = [], True
            for pmask in pU:
                sub = [vals[k] for k in bits(pmask)]
                if pmask not in exact or exact[pmask][0] is None:
                    ok = False
                    break
                blk = [supp[k] for k in bits(pmask)]
                seq += [(blk[i - 1] + 1, blk[j - 1] + 1) for i, j in exact[pmask][1]]
            if ok:
                if lb is not None and lb == ub:
                    return {"ok": True, "min_steps": ub, "sequence": seq,
                            "certified": True, "method": "partition DP (LB==UB)",
                            "lb": lb, "ub": ub, "states": nodes,
                            "blocks": [[supp[k] for k in bits(p)] for p in pU],
                            "time": time.time() - t0}
                # gap: certify with a decision search on the whole instance.
                # Prefer the memory-BOUNDED DFS certificate (best-first A* keeps ~1 KB per
                # node and gets OOM-killed on n>=10 / K>=10 proofs; see prove_no.py).
                ms, sq, p, status = None, None, 0, "budget"
                try:
                    from prove_no import decision as _dfs
                    proved, p, memo, reason, seq2 = _dfs(base, ub - 1,
                                                         memo_cap=4_000_000, deadline=dl)
                    if reason == "found" and seq2:
                        ms, sq, status = ub - 1, seq2, "solved"
                    elif reason == "proved":
                        status = "proved"
                except ImportError:
                    ms, sq, p, status = astar(base, node_budget=node_budget, deadline=dl,
                                              limit=ub - 1, memo=False)
                nodes += p
                if status == "proved":
                    return {"ok": True, "min_steps": ub, "sequence": seq,
                            "certified": True, "method": "partition DP + proved minimal",
                            "lb": ub, "ub": ub, "states": nodes, "time": time.time() - t0}
                if ms is not None:
                    return {"ok": True, "min_steps": ms, "sequence": sq,
                            "certified": True, "method": "A* connected", "lb": ms,
                            "ub": ms, "states": nodes, "time": time.time() - t0}
                return {"ok": True, "min_steps": None, "sequence": seq,
                        "certified": False, "method": "gap (decision search incomplete)",
                        "lb": lb, "ub": ub, "states": nodes, "time": time.time() - t0}

    # monolithic fallback: A* first, then the memory-bounded certificate ladder
    ms, sq, p, status = astar(base, node_budget=node_budget, deadline=dl)
    nodes += p
    if ms is None:
        try:
            from prove_no import exact_min
            m2, info = exact_min(a, lo=max(heuristic(base), 0), hi=None, deadline=dl)
            nodes += sum(n for (_K, _r, n, _m, _s) in info.get("notes", []))
            if m2 is not None and info.get("sequence"):
                return {"ok": True, "min_steps": m2, "sequence": info["sequence"],
                        "certified": True, "method": "DFS certificate ladder",
                        "lb": m2, "ub": m2, "states": nodes, "time": time.time() - t0}
        except ImportError:
            pass
    if ms is not None:
        return {"ok": True, "min_steps": ms, "sequence": sq, "certified": True,
                "method": "A*", "lb": ms, "ub": ms, "states": nodes,
                "time": time.time() - t0}
    return {"ok": True, "min_steps": None, "sequence": None, "certified": False,
            "method": "timeout", "lb": max(heuristic(base), (z - 1) if z else 0),
            "ub": None, "states": nodes, "time": time.time() - t0}


def min_steps(a, **kw):
    return solve(a, **kw).get("min_steps")


def prove_min(a, K, node_budget=1_000_000, deadline_s=300.0):
    """Certificate 'min_steps(a) > K'.  Returns (proved, states, secs)."""
    base = list(reduce_prim(deviations(a)))
    t0 = time.time()
    ms, _, p, status = astar(base, node_budget=node_budget,
                             deadline=t0 + deadline_s, limit=K, memo=False)
    return (ms is None and status == "proved"), p, time.time() - t0


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        inst = json.loads(arg)
        r = solve(inst)
        if not r.get("ok"):
            print(f"{inst}\n   -> NOT MIXABLE ({r.get('reason')})")
            continue
        v = verify_sequence(inst, r["sequence"])[0] if r.get("sequence") else None
        print(f"{inst}\n   -> {r.get('method')} min={r.get('min_steps')} lb={r.get('lb')} "
              f"ub={r.get('ub')} certified={r.get('certified')} states={r.get('states')} "
              f"t={r.get('time', 0):.2f}s verify={v}")
