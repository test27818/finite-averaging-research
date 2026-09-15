#!/usr/bin/env python3
"""Backward-compatible bounded decision-search API, now using mix_engine.

'proved' is exhaustive non-reachability within K; 'time'/'cap'/'depth' are UNKNOWN.
A proved lower bound is a reproducible computation, not a portable formal proof file.
"""
from __future__ import annotations
import sys
import time
import mix_engine as E
from solver import judge, verify_sequence

children = E.children
replay_value_pairs = E.replay_value_pairs


def decision(vec, K, memo_cap=200_000, deadline=None, report_every=1_000_000,
             want_solution=False, t_start=None, node_budget=1_000_000):
    """Old tuple API: (proved_no, nodes, memo_size, reason, POSITION sequence|None)."""
    found, moves, nodes, memo, reason = E.decision(
        E.prim_sorted(vec), K, deadline=deadline, node_budget=node_budget, memo_cap=memo_cap)
    seq = E.replay_value_pairs(vec, moves) if moves is not None else None
    if found and (seq is None or not verify_sequence(vec, seq)[0]):
        raise AssertionError('decision witness failed independent verification')
    return reason == 'proved', nodes, memo, reason, seq


def prove_min_greater_than(a, K, **kw):
    if not judge(a):
        raise ValueError('instance is not mixable')
    p, nodes, memo, reason, _seq = decision(E.deviations(a), K, **kw)
    return p, nodes, memo, reason


def exact_min(a, lo=None, hi=None, deadline=None, memo_cap=200_000, verbose=False,
              node_budget=1_000_000):
    """lo must be a valid proved bound; hi is a depth cap, not a witness.

    Unlike a verified incumbent, a numeric hi alone cannot certify an optimum.
    Returns (minimum|None, notes) with POSITION sequence when a solution is found.
    """
    if not judge(a):
        return None, dict(reason='not mixable')
    state = E.state_of(a)
    r = E.ida_ladder(state, lower=lo, deadline=deadline, memo_cap=memo_cap,
                     node_budget=node_budget, max_depth=80 if hi is None else hi)
    notes = dict(notes=r['notes'], lower=r['lower'], reason=r['reason'])
    if r['certified']:
        seq = E.replay_value_pairs(E.deviations(a), r['moves'])
        if seq is None or not verify_sequence(a, seq)[0]:
            raise AssertionError('exact_min witness failed verification')
        notes['sequence'] = seq
        ans = r['steps']
    else:
        notes['incomplete'] = r['reason']
        ans = None
    if verbose:
        print(notes)
    return ans, notes


CASES = [([38,-23,-14,16,-11,4,63,80,14,38],10,[9]),
         ([-81,-60,-95,-95,-20,-13,-87,-80,42,54],11,[9,10])]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: prove_no.py --batch | [--find] K a1 a2 ...')
    if sys.argv[1] == '--batch':
        for a, ub, ks in CASES:
            for k in ks:
                t0 = time.time()
                p, n, m, reason, seq = decision(E.deviations(a), k, deadline=t0+60)
                print(f'{a}: min > {k}? {p}; reason={reason} nodes={n} memo={m} time={time.time()-t0:.3f}s')
    else:
        args = sys.argv[2:] if sys.argv[1] == '--find' else sys.argv[1:]
        k, *a = map(int, args)
        p, n, m, reason, seq = decision(E.deviations(a), k)
        print(dict(proved_no=p, reason=reason, nodes=n, memo=m, sequence=seq))
