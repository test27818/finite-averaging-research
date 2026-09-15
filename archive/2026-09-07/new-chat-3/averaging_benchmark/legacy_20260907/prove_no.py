#!/usr/bin/env python3
"""Memory-BOUNDED decision search: prove "no solution with <= K moves".

Why this file exists
--------------------
`solver_v2.astar` is best-first: it keeps `state`/`parent`/`best` for every generated node
(~1 KB each).  Certifying the lower bound of a hard n=10 instance needs 10^7-10^8 nodes,
and the A* then gets OOM-killed (it happened: 25M nodes, 14 GB).  So the certificate is
produced here by depth-first branch-and-bound (IDA* style) with an explicitly bounded
transposition table: memory is O(cap), not O(nodes).

Speed ingredients
-----------------
* the same admissible heuristics as solver_v2 (non-zero count / no opposite pair /
  distinct magnitudes) prune on `heuristic(state) > remaining budget`;
* children are de-duplicated by the *value pair* they act on (positions holding equal
  values are interchangeable) - the single biggest branching reduction here;
* the transposition table maps a canonical state to the largest remaining budget that has
  already been proved to fail, so it prunes (not just dedupes).

Usage
-----
    python3 src/prove_no.py  K  a1 a2 ... an        # certificate: min > K
    python3 src/prove_no.py --batch                 # the two case_study.md n=10 instances
    python3 src/prove_no.py --find  K a1 ... an     # search for a <=K solution instead
"""
from __future__ import annotations

import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from solver import judge, verify_sequence  # noqa: E402
from solver_v2 import deviations, reduce_prim, key_of, heuristic, gcd_all  # noqa: E402


def children(state):
    """Successors of a primitive-integer state, one per unordered *value* pair."""
    cnt = Counter(state)
    vals = sorted(cnt)
    out = []
    for ai in range(len(vals)):
        u = vals[ai]
        for bj in range(ai + 1, len(vals)):
            v = vals[bj]
            if u == v:
                continue
            new = Counter()
            new[u + v] += 2                       # the two positions that were mixed
            for w in vals:                        # every untouched position doubles
                rem = cnt[w] - (1 if w == u else 0) - (1 if w == v else 0)
                if rem > 0:
                    new[2 * w] += rem
            vec = []
            for w, c in new.items():
                if c > 0:
                    vec.extend([w] * c)
            g = gcd_all(vec)
            vec = sorted(x // g for x in vec) if g else vec
            out.append((tuple(vec), (u, v)))
    return out


def replay_value_pairs(vec, moves):
    """Value-pair schedule -> position schedule on the original labelling (1-based)."""
    cur = list(reduce_prim(vec))
    seq = []
    for (u, v) in moves:
        i = next(k for k, x in enumerate(cur) if x == u)
        j = next((k for k, x in enumerate(cur) if x == v and k != i), None)
        if j is None:
            return None
        s = cur[i] + cur[j]
        cur = [s if k in (i, j) else 2 * x for k, x in enumerate(cur)]
        g = gcd_all(cur)
        if g:
            cur = [x // g for x in cur]
        seq.append((i + 1, j + 1))
    return seq


class Verdict(Exception):
    pass


def decision(vec, K, memo_cap=2_000_000, deadline=None, report_every=1_000_000,
             want_solution=False, t_start=None):
    """DFS over the projective state space.

    Returns (proved_no_solution, nodes, memo_size, reason, sequence_or_None)
    reason in 'proved' | 'found' | 'cap' | 'time'
    """
    start = tuple(reduce_prim(vec))
    memo = {}
    st = {"nodes": 0, "found": None, "seq": None}
    T0 = t_start or time.time()

    def dfs(state, budget, path):
        if not any(state):
            st["found"] = True
            st["seq"] = list(path)
            return False                      # solution exists => not proved
        if budget == 0 or heuristic(state) > budget:
            return True                       # this branch cannot finish in budget
        k = key_of(state)
        prev = memo.get(k)
        if prev is not None and prev >= budget:
            return True
        st["nodes"] += 1
        if st["nodes"] % report_every == 0:
            print(f"      nodes={st['nodes']:,} memo={len(memo):,} depth-left={budget} "
                  f"{time.time()-T0:.0f}s", flush=True)
        if deadline is not None and st["nodes"] % 20000 == 0 and time.time() > deadline:
            raise Verdict("time")
        if len(memo) > memo_cap:
            raise Verdict("cap")
        all_fail = True
        for ns, mv in children(state):
            path.append(mv)
            ok = dfs(ns, budget - 1, path)
            if not ok:
                path.pop()
                all_fail = False
                break
            path.pop()
        if all_fail:
            memo[k] = max(prev or 0, budget)
        return all_fail

    try:
        proved = dfs(start, K, [])
    except Verdict as e:
        return False, st["nodes"], len(memo), str(e), None
    if st["found"]:
        seq = replay_value_pairs(vec, st["seq"])
        return False, st["nodes"], len(memo), "found", seq
    return proved, st["nodes"], len(memo), ("proved" if proved else "found"), None


def prove_min_greater_than(a, K, **kw):
    """Public helper: True => min_steps(a) > K (a real certificate)."""
    if not judge(a):
        raise ValueError("instance is not mixable")
    proved, nodes, memo, reason, _ = decision(list(reduce_prim(deviations(a))), K, **kw)
    return proved and reason == "proved", nodes, memo, reason


def exact_min(a, lo=None, hi=None, deadline=None, memo_cap=3_000_000, verbose=False):
    """Smallest K with a <=K solution, via memory-bounded certificates.

    lo defaults to the admissible bound max(D(kappa), simple, partition); hi must be an
    achievable move count (e.g. from construct.py).  Returns (min_steps|None, notes).
    """
    from solver import judge
    from solver_v2 import deviations, reduce_prim
    if not judge(a):
        return None, {"reason": "not mixable"}
    vec = list(reduce_prim(deviations(a)))
    if lo is None:
        try:
            import lower
            lo = lower.lower_bound(a)
        except Exception:
            lo = 0
    notes = []
    K = max(0, int(lo))
    while hi is None or K <= hi:
        t0 = time.time()
        proved, nodes, memo, reason, seq = decision(
            vec, K, memo_cap=memo_cap, deadline=deadline)
        notes.append((K, reason, nodes, memo, round(time.time() - t0, 1)))
        if verbose:
            print(f"    K={K}: {reason} nodes={nodes:,} memo={memo:,} "
                  f"({time.time()-t0:.1f}s)", flush=True)
        if reason == "found":
            return K, {"notes": notes, "sequence": seq}
        if reason in ("cap", "time"):
            return None, {"notes": notes, "incomplete": reason}
        K += 1
    return None, {"notes": notes, "incomplete": "hi exceeded"}


CASES = [([38, -23, -14, 16, -11, 4, 63, 80, 14, 38], 10, [9]),
         ([-81, -60, -95, -95, -20, -13, -87, -80, 42, 54], 11, [9, 10])]

if __name__ == "__main__":
    if sys.argv[1] == "--batch":
        for a, ub, Ks in CASES:
            print(f"\ninstance {a}\n  best verified construction = {ub} moves", flush=True)
            for K in Ks:
                t0 = time.time()
                proved, nodes, memo, reason, seq = decision(
                    list(reduce_prim(deviations(a))), K, deadline=time.time() + 1200)
                print(f"  min > {K}? proved={proved} nodes={nodes:,} memo={memo:,} "
                      f"reason={reason} ({time.time()-t0:.0f}s)", flush=True)
                if seq:
                    print("     !! a <=K solution was found:", seq,
                          "verified:", verify_sequence(a, seq)[0], flush=True)
                    break
                if proved and ub == K + 1:
                    print(f"     CERTIFICATE: min = {K+1}", flush=True)
    elif sys.argv[1] == "--find":
        K = int(sys.argv[2]); a = [int(x) for x in sys.argv[3:]]
        p, n, m, r, seq = decision(list(reduce_prim(deviations(a))), K)
        print(f"<=K solution: {'yes' if r=='found' else 'no'}  reason={r} nodes={n:,}")
        if seq:
            print("  sequence:", seq, "verified:", verify_sequence(a, seq)[0])
    else:
        K = int(sys.argv[1]); a = [int(x) for x in sys.argv[2:]]
        ok, n, m, r = prove_min_greater_than(a, K)
        print(f"min({a}) > {K}: proved={ok} nodes={n:,} memo={m:,} reason={r}")
