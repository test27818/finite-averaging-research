#!/usr/bin/env python3
"""Exact reference solver for the "averaging-to-equalize" / perfect-mixability problem.

Zero dependencies (Python standard library only). Uses arbitrary-precision integers
(Python `int`) so the criterion is correct on inputs of any size.

Contents
--------
judge(a)                    -> bool    : decide mixability (the G-criterion + special cases)
min_steps_sequence(a, ...)  -> (int|None, list|None) : certified IDA* minimum + verified sequence
verify_sequence(a, steps)   -> (bool, values, reason) : exact simulation of an operation seq.
"""
from __future__ import annotations

from math import gcd
from fractions import Fraction
from collections import deque


def judge(a) -> bool:
    """Return True iff multiset `a` can be averaged to all-equal in finitely many steps."""
    n = len(a)
    if n == 0:
        return True
    S = sum(a)
    if n <= 2:
        return True
    if n == 3:
        # Three numbers are mixable iff they form an arithmetic progression.
        b = sorted(a)
        return 2 * b[1] == b[0] + b[2]

    # n >= 4 : G-criterion (Coviello Gonzalez & Chrobak, arXiv:1806.08875).
    # Normalized deviations e_i = (n*a_i - S) / g, with g = gcd(...) so gcd(e) = 1.
    dev = [n * x - S for x in a]
    g = 0
    for d in dev:
        g = gcd(g, d)
    if g == 0:                      # all elements are equal -> already at the mean
        return True
    e = [d // g for d in dev]

    # G = gcd of all pairwise differences = gcd(e_i - e_0).
    G = 0
    e0 = e[0]
    for i in range(1, n):
        G = gcd(G, e[i] - e0)

    # Mixable  <=>  G is a power of two (1,2,4,8,...).
    return G > 0 and (G & (G - 1)) == 0


def _canonical(state) -> tuple:
    return tuple(sorted(state))


def min_steps_sequence(a, max_depth=80, max_den_exp=None, budget_states=400_000,
                       deadline_s=20.0):
    """Certified minimum and 1-based sequence via the current IDA* engine.

    max_den_exp is accepted for source compatibility but ignored: no denominator
    truncation is performed. (None, None) means impossible OR resource-limited;
    use solver_v2.solve() when the distinction or a nonoptimal incumbent matters.
    Independent old BFS is available explicitly in legacy_bfs.py.
    """
    from solver_v2 import solve
    r = solve(a, max_depth=max_depth, node_budget=budget_states,
              deadline_s=deadline_s, max_exact_n=max(14, len(a)))
    if r.get('certified'):
        return r['min_steps'], r['sequence']
    return None, None


def power2_tree_sequence(a):
    """A correct (not necessarily minimal) construction for n = 2^k multisets.

    Any 2^k numbers can be equalized to their mean by recursively equalizing each half
    to its own mean and then pair-averaging across the two halves. This is valid for
    EVERY multiset of power-of-two size (n=2,4,8,16,...), independent of the values.
    Returns a list of 1-based index pairs, or None if n is not a power of two.
    """
    n = len(a)
    if n == 0:
        return []
    if n & (n - 1):
        return None

    def rec(lo, hi, out):
        if hi - lo == 1:
            return
        if hi - lo == 2:
            out.append((lo + 1, hi))          # average the two (1-based)
            return
        mid = (lo + hi) // 2
        rec(lo, mid, out)
        rec(mid, hi, out)
        for k in range(mid - lo):             # pair-average across the two halves
            out.append((lo + k + 1, mid + k + 1))

    steps = []
    rec(0, n, steps)
    return steps


def verify_sequence(a, steps):
    """Exact simulation of an operation sequence.

    Returns (ok, final_values, reason) where reason is "" when ok.
    """
    n = len(a)
    if n == 0:
        return (not steps), [], ("" if not steps else "bad_index")
    S = sum(a)
    A = Fraction(S, n)
    v = [Fraction(x) for x in a]
    for s in steps:
        if not (isinstance(s, (list, tuple)) and len(s) == 2):
            return False, v, "bad_step_format"
        i, j = s
        if not (type(i) is int and type(j) is int):
            return False, v, "bad_index_type"
        if not (1 <= i <= n and 1 <= j <= n and i != j):
            return False, v, "bad_index"
        avg = (v[i - 1] + v[j - 1]) / 2
        v[i - 1] = avg
        v[j - 1] = avg
    ok = all(x == A for x in v)
    return ok, v, ("" if ok else "not_all_equal_to_mean")


if __name__ == "__main__":
    # Quick self-test against the documented examples.
    import sys

    cases = [
        ([0, 1], True), ([0, 1, 2], True), ([0, 1, 5], False), ([0, 2, 4], True),
        ([0, 0, 0, 1], True), ([0, 0, 0, 0, 5], False), ([0, 0, 0, 1, 9], True),
        ([1, 3, 5, 7, 9], True), ([0, 0, 0, 5, 5], False), ([1, 1, 4], False),
    ]
    bad = 0
    for a, want in cases:
        got = judge(a)
        mark = "ok" if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"{mark}  judge({a}) = {got}  (want {want})")
    if bad:
        sys.exit(1)
    for a in ([0, 0, 0, 1, 9], [0, 0, 0, 1], [0, 1, 2], [0, 0, 0, 0, 0]):
        ms, seq = min_steps_sequence(a)
        print(f"min_steps({a}) = {ms}, seq = {seq}")
