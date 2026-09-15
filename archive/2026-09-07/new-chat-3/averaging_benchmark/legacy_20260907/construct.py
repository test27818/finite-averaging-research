#!/usr/bin/env python3
"""General construction for Task 2 (a verified mixing sequence), replacing the
"power2_tree only when n = 2^k / BFS only when n <= 6" situation of solver.py.

Ingredients
-----------
(A) SAME-PARITY GREEDY (paper Lemma 6, made algorithmic).  Put the instance in primitive
    integer deviation form x (sum 0, so mean 0 is an integer).  If a set of positions has
    size 2^t and sum 0, then repeatedly mixing two *distinct same-parity* values inside it
    strictly decreases  Psi = sum x_i^2  (by (x-y)^2/2 >= 2 whenever x != y, x = y mod 2)
    and preserves "integral, mean 0, size 2^t"; the only configurations with no legal move
    have <= 2 distinct values, and for size 2^t & mean 0 & integral that forces both values
    to be even => a legal move exists unless everything is already 0.  Hence the greedy
    TERMINATES AT THE GOAL - a complete, polynomial, precision-0 construction for every
    block of power-of-two size (in particular for every instance with n = 2^t, no matter
    what the values are).  This replaces solver.power2_tree_sequence, which always spends
    (n/2) log2 n mixers and is far from minimal (e.g. 4 mixers for n=4, where 3 suffice).

(B) NEAR-FINAL PARTITION.  If the positions split into blocks of power-of-two size with
    zero deviation-sum each, (A) is applied block by block.  Blocks are found by a subset
    DP for n <= 22 (exact), greedily/randomised otherwise.

(C) SMALL BLOCKS BY EXACT SEARCH: blocks with <= 8 positions are solved optimally by the
    A* of solver_v2 (fewer mixers than (A)).

(D) FALLBACK: run (A) on the whole instance anyway and *verify*; many non-near-final
    instances still succeed.  Sequences are always checked by exact simulation, so nothing
    wrong is ever claimed: failures are reported as failures.

Complexity: each greedy step costs O(n) and reduces Psi by >= 2, so O(n * Psi_0) worst
case (pseudo-polynomial, as in the paper); empirically a handful of steps per droplet.
"""
from __future__ import annotations

import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from solver import judge, verify_sequence, power2_tree_sequence  # noqa: E402
import solver_v2 as v2  # noqa: E402


def primitive_deviations(a):
    return list(v2.reduce_prim(v2.deviations(a)))


# --------------------------------------------------------------- (A) same-parity greedy
def greedy_same_parity(x, positions, max_steps=200_000, deadline=None):
    """Mix distinct same-parity values inside `positions` until all are zero.

    Returns (steps, ok) where steps are 1-based index pairs into the WHOLE vector x.
    """
    x = list(x)
    pos = list(positions)
    steps = []
    while max_steps:
        max_steps -= 1
        if deadline is not None and len(steps) % 512 == 0 and time.time() > deadline:
            return steps, False
        best = None
        for par in (0, 1):
            cand = [i for i in pos if x[i] % 2 == par]
            if len(cand) < 2:
                continue
            lo = min(cand, key=lambda i: x[i])
            hi = max(cand, key=lambda i: x[i])
            d = x[hi] - x[lo]
            if d > 0 and (best is None or d > best[0]):
                best = (d, lo, hi)
        if best is None:
            return steps, (all(x[i] == 0 for i in pos))
        _, lo, hi = best
        m = (x[lo] + x[hi]) // 2
        x[lo] = x[hi] = m
        steps.append((lo + 1, hi + 1))
        if all(x[i] == 0 for i in pos):
            return steps, True
    return steps, False


# ------------------------------------------------------------- (B) near-final partition
def near_final_dp(x, cap_n=22):
    """Exact partition of the non-zero support into power-of-two-size zero-sum blocks."""
    supp = [i for i, v in enumerate(x) if v]
    z = len(supp)
    if z == 0:
        return []
    if z > cap_n:
        return None
    vals = [x[i] for i in supp]
    sums = [0] * (1 << z)
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        sums[mask] = sums[mask ^ (1 << b)] + vals[b]
    full = (1 << z) - 1
    if sums[full] != 0:
        return None
    ok_mask = [False] * (1 << z)
    for mask in range(1, 1 << z):
        if sums[mask] == 0 and (mask.bit_count() & (mask.bit_count() - 1)) == 0:
            ok_mask[mask] = True
    if not ok_mask[full] and not any(ok_mask):
        return None
    INF = float("inf")
    dp = [INF] * (1 << z)
    ch = [0] * (1 << z)
    dp[0] = 0
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << b)
        sub = rest
        while True:
            part = sub | (1 << b)
            if ok_mask[part] and dp[mask ^ part] + 1 < dp[mask]:
                dp[mask] = dp[mask ^ part] + 1
                ch[mask] = part
            if sub == 0:
                break
            sub = (sub - 1) & rest
    if dp[full] == INF:
        return None
    out, m = [], full
    while m:
        p = ch[m]
        out.append([supp[k] for k in range(z) if p >> k & 1])
        m ^= p
    return out


def near_final_greedy(x, tries=40, seed=12345):
    """Randomised packing for large n: repeatedly pull out a small zero-sum block whose
    size is a power of two (2,4,8,16) via random sampling + pair matching."""
    rng = random.Random(seed)
    supp = [i for i, v in enumerate(x) if v]
    best = None
    for attempt in range(tries):
        left = list(supp)
        rng.shuffle(left)
        blocks = []
        ok = True
        while left:
            got = None
            for size in (1, 2, 4, 8):
                if size == 1:
                    cand = [i for i in left if x[i] == 0]
                    if cand:
                        got = [cand[0]]
                    break
                # sample subsets of `size` from left with sum 0 (random tries + pair/triple hunt)
                for _ in range(3000):
                    s = rng.sample(left, min(size, len(left)))
                    if len(s) == size and sum(x[i] for i in s) == 0:
                        got = s
                        break
                if got:
                    break
            if got is None:
                # give up on packing: leave the rest as one block
                if len(left) and (len(left) & (len(left) - 1)) == 0:
                    blocks.append(left)
                    ok = True
                    left = []
                    break
                blocks.append(left)
                ok = False
                break
            blocks.append(got)
            left = [i for i in left if i not in set(got)]
        if ok:
            return blocks
        if best is None or len(blocks) > len(best):
            best = blocks if ok else None
    return best


def zero_sum_partition(x, cap_n=22):
    """Partition the non-zero support into as many zero-sum blocks as possible
    (any sizes).  By the component/zero-sum theorem each block can then be mixed
    independently, which is what makes big instances tractable."""
    supp = [i for i, v in enumerate(x) if v]
    z = len(supp)
    if z == 0:
        return []
    if z > cap_n:
        return None
    vals = [x[i] for i in supp]
    sums = [0] * (1 << z)
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        sums[mask] = sums[mask ^ (1 << b)] + vals[b]
    full = (1 << z) - 1
    if sums[full] != 0:
        return None
    INF = float("inf")
    big = z + 1                      # penalise large blocks: minimise (size-1) total
    dp = [INF] * (1 << z)
    ch = [0] * (1 << z)
    dp[0] = 0
    for mask in range(1, 1 << z):
        b = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << b)
        sub = rest
        while True:
            part = sub | (1 << b)
            if sums[part] == 0 and dp[mask ^ part] < INF:
                c = dp[mask ^ part] + (part.bit_count() - 1)
                if c < dp[mask]:
                    dp[mask], ch[mask] = c, part
            if sub == 0:
                break
            sub = (sub - 1) & rest
    if dp[full] == INF:
        return None
    out, m = [], full
    while m:
        p = ch[m]
        out.append([supp[k] for k in range(z) if p >> k & 1])
        m ^= p
    return out


# --------------------------------------------------------------------- top-level construct
def construct(a, exact_block=8, deadline_s=20.0, verbose=False, max_steps_mult=80):
    """Return dict(steps, verified, method, steps_per_droplet)."""
    t0 = time.time()
    dl = t0 + deadline_s
    if not judge(a):
        return {"steps": None, "verified": False, "method": "not mixable"}
    x = primitive_deviations(a)
    n = len(x)
    if not any(x):
        return {"steps": [], "verified": True, "method": "already equal", "n_steps": 0}

    blocks = None
    if n & (n - 1) == 0:
        blocks = [list(range(n))]                      # whole instance is one 2^t block
    else:
        if n <= 22:
            blocks = near_final_dp(x)                  # prefer power-of-two blocks
            if blocks is None:
                blocks = near_final_greedy(x, tries=8 if n > 14 else 40)
        if blocks is None:
            blocks = zero_sum_partition(x)             # any zero-sum blocks

    trials = []
    # (0) the branch-and-bound solver: optimal whenever it stays in budget
    r0 = v2.solve(a, deadline_s=min(deadline_s, 20.0), node_budget=400_000)
    if r0.get("min_steps") is not None and r0.get("sequence") is not None:
        trials.append((f"v2.solve[{r0.get('method')}]", r0["sequence"]))
    if blocks:
        # exact search for small blocks (optimal), greedy for the big ones
        seq = []
        ok = True
        for blk in blocks:
            b = [i for i in blk if x[i]]
            if not b:
                continue
            sub = [x[i] for i in b]
            solved = False
            if len(b) <= exact_block:
                ms, sq, p, status = v2.astar(sub, deadline=dl, node_budget=400_000)
                if sq is not None and ms is not None:
                    seq += [(b[i - 1] + 1, b[j - 1] + 1) for i, j in sq]
                    solved = True
            if not solved and (len(b) & (len(b) - 1)) == 0:
                st, good = greedy_same_parity(x, b, max_steps=max_steps_mult*len(b), deadline=dl)     # Lemma 6: guaranteed to work
                if good:
                    seq += st
                    solved = True
            if not solved:
                st, good = greedy_same_parity(x, b, max_steps=max_steps_mult*len(b), deadline=dl)     # try anyway, verified later
                if good:
                    seq += st
                    solved = True
            if not solved:
                ok = False
                break
        if ok:
            trials.append(("blocks(near-final)+greedy", seq))
    # (D) plain greedy on everything
    if len(trials) < 3:                                # don't burn the budget on long shots
        st, good = greedy_same_parity(x, list(range(n)), max_steps=max_steps_mult*n,
                                      deadline=dl)
        if good:
            trials.append(("greedy(all)", st))
    # (E) last resort: monolithic exact search
    ms, sq, p, status = v2.astar(x, deadline=dl, node_budget=400_000)
    if sq is not None:
        trials.append(("A*", sq))
    # (F) classic butterfly for n = 2^k (always valid, many steps)
    if n & (n - 1) == 0:
        trials.append(("power2_tree", power2_tree_sequence(a)))

    best = None
    for method, seq in trials:
        if not seq and seq != []:
            continue
        good, _, _ = verify_sequence(a, seq)
        if good and (best is None or len(seq) < len(best[1])):
            best = (method, seq)
    if best is None:
        return {"steps": None, "verified": False, "method": "FAILED",
                "time": time.time() - t0}
    return {"steps": best[1], "verified": True, "method": best[0],
            "n_steps": len(best[1]), "time": time.time() - t0}


if __name__ == "__main__":
    import json
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            a = json.loads(arg)
            r = construct(a)
            print(a, "->", r["method"], r.get("n_steps"), "verified:", r["verified"])
    else:
        tests = ([0, 0, 0, 1], [0, 0, 0, 1, 9], [38, -23, -14, 16, -11, 4, 63, 80, 14, 38],
                 [-81, -60, -95, -95, -20, -13, -87, -80, 42, 54], [0, 0, 0, 0, 5])
        for a in tests:
            r = construct(a)
            print(f"{str(a):>50} -> {r['method']:>24} steps={r.get('n_steps')} "
                  f"verified={r['verified']}")
