#!/usr/bin/env python3
"""Compatible solve() facade for the new construction + bounded IDA* engine.

Public operations are always 1-based POSITION pairs, verified with Fraction.
min_steps is non-null ONLY if certified. sequence/ub may exist without optimality.
Large n and resource limits are explicitly reported; no general polynomial-time or
fixed-n completeness claim is made. Old max_support/max_exact_block options remain
accepted, but no exponential subset DP is run ahead of the constructive incumbent.
"""
from __future__ import annotations

import json
import sys
import time
from functools import lru_cache
from solver import judge, verify_sequence
import mix_engine as E

# Preserve names used by older callers. All labelled-to-unlabelled transitions are
# explicit: only cost/reachability keys may identify states with their negatives.
gcd_all = E.gcd_all
reduce_prim = E.reduce_prim
prim_sorted = E.prim_sorted
key_of = E.key_of
deviations = E.deviations
state_of = E.state_of
energy = E.energy
heuristic = E.heuristic
h_pairs = E.h_pairs
h_cancel = E.h_cancel
h_distinct = E.h_distinct
h_setup = E.h_setup
possible = E.possible
children = E.children
replay_value_pairs = E.replay_value_pairs
decision = E.decision
ida_ladder = E.ida_ladder
construct_moves = E.construct_moves


def astar(vec, node_budget=1_000_000, deadline=None, limit=None, memo=True):
    """Old API: (minimum|None, 1-based POSITION sequence|None, pops, status)."""
    ms, moves, pops, status = E.astar(vec, node_budget, deadline, limit, memo)
    seq = E.replay_value_pairs(vec, moves) if moves is not None else None
    if moves is not None and (seq is None or not verify_sequence(vec, seq)[0]):
        raise AssertionError('A* position replay failed')
    return ms, seq, pops, status


def bits(mask):
    return [k for k in range(mask.bit_length()) if mask >> k & 1]


def zero_sum_masks(vals):
    if len(vals) > 22:
        raise ValueError('subset enumeration limited to 22 positions')
    sums = [0] * (1 << len(vals))
    out = []
    for mask in range(1, len(sums)):
        bit = mask & -mask
        sums[mask] = sums[mask ^ bit] + vals[bit.bit_length()-1]
        if not sums[mask]:
            out.append(mask)
    return sums, out


def block_lb(block):
    """Lower bound for a connected zero-sum component, not arbitrary whole input."""
    return max(max(0, len(block)-1), E.h_pairs(block))


def partition_dp(vals, cost, cost_lb):
    """Compatibility helper (opt-in, n<=14). Not on the default solve path.

    A complete partition enumeration is needed for a lower bound; selecting a single
    convenient partition yields ONLY an upper bound. The full block is included.
    """
    if len(vals) > 14:
        raise ValueError('partition_dp requires <=14 positions; use constructive tails')
    sums, zs = zero_sum_masks(vals)
    full = len(sums)-1
    if sums[full]:
        return None, None, None, None
    bybit = [[] for _ in vals]
    for mask in zs:
        for i in bits(mask):
            bybit[i].append(mask)

    @lru_cache(None)
    def dp(mask):
        if not mask:
            return 0, (), 0, ()
        ub, up, lb, lp = float('inf'), None, float('inf'), None
        b = (mask & -mask).bit_length()-1
        for part in bybit[b]:
            if part & mask != part:
                continue
            u, us, l, ls = dp(mask ^ part)
            c, cl = cost(part), cost_lb(part)
            if c is not None and u+c < ub:
                ub, up = u+c, (part,)+us
            if cl is not None and l+cl < lb:
                lb, lp = l+cl, (part,)+ls
        return ub, up, lb, lp
    u, us, l, ls = dp(full)
    return (None if us is None else u, None if us is None else list(us),
            None if ls is None else l, None if ls is None else list(ls))


def solve(a, deadline_s=60.0, node_budget=1_000_000, max_support=22,
          max_exact_block=7, ladder=True, *, max_exact_n=14, max_depth=80,
          memo_cap=200_000, optimize_ms=None, max_steps=19000):
    """Construct first, then spend the remaining budget on shortest-path search.

    deadline_s=None means no wall-clock deadline (node/memory/depth caps still apply).
    optimize_ms=None spends the remaining deadline on optimization; 0 is fast mode.
    max_exact_n can be raised explicitly. Even above it, LB==UB certifies optimality.
    No per-instance cache is shared across calls.
    """
    a = list(a)
    t0 = time.time()
    dl = None if deadline_s is None else t0 + max(0, deadline_s)
    metrics = dict(judge_s=0.0, construct_s=0.0, optimize_s=0.0, verify_s=0.0)
    if not judge(a):
        return dict(ok=False, status='impossible', reason='not mixable', min_steps=None,
                    sequence=None, certified=False, lb=None, ub=None, states=0,
                    time=time.time()-t0, method='criterion', metrics=metrics)
    base = E.reduce_prim(E.deviations(a))
    state = tuple(sorted(base))
    metrics['judge_s'] = time.time()-t0
    lb = E.heuristic(state)
    if not any(state):
        return dict(ok=True, status='solved', min_steps=0, sequence=[], certified=True,
                    lb=0, ub=0, states=0, time=time.time()-t0, method='already equal',
                    verified=True, metrics=metrics, notes=[])
    ct = time.time()
    moves = E.construct_moves(state, deadline=dl, max_steps=max_steps)
    metrics['construct_s'] = time.time()-ct
    initial_steps = len(moves) if moves is not None else None
    ot = time.time()
    opt_dl = dl
    if optimize_ms is not None:
        opt_dl = min(dl if dl is not None else float('inf'), ot+max(0, optimize_ms)/1000)
    can_opt = ladder and optimize_ms != 0
    can_opt = can_opt and (opt_dl is None or time.time() < opt_dl)
    certified, nodes, notes, method = False, 0, [], 'construction upper bound'

    # Larger beam search improves the incumbent but is never used as a proof.
    # Small exact instances go straight to IDA*, avoiding a fixed 350ms UI tax.
    if (moves is not None and len(moves) > lb and can_opt
            and max_exact_n < len(a) <= 24):
        end = time.time()+0.35
        if opt_dl is not None:
            end = min(end, opt_dl)
        moves, beam_nodes = E.beam_improve(state, moves, deadline=end)
        nodes += beam_nodes
        method += ' + beam'
    if moves is not None and len(moves) == lb:
        certified, method = True, 'counting bound meets verified upper bound'
    elif can_opt and len(a) <= max_exact_n:
        r = E.ida_ladder(state, incumbent=moves, lower=lb, deadline=opt_dl,
                         node_budget=node_budget, memo_cap=memo_cap, max_depth=max_depth)
        moves, certified, lb = r['moves'], r['certified'], r['lower']
        nodes += r['expanded']
        notes, method = r['notes'], 'IDA*: '+r['reason']
    metrics['optimize_s'] = time.time()-ot
    vt = time.time()
    sequence = E.replay_value_pairs(base, moves) if moves is not None else None
    if moves is not None:
        if sequence is None or not verify_sequence(a, sequence)[0]:
            raise AssertionError('independent position-sequence verification failed')
    metrics['verify_s'] = time.time()-vt
    ub = len(sequence) if sequence is not None else None
    if ub is not None and lb > ub:
        raise AssertionError('lower bound exceeds verified upper bound')
    if certified and ub is None:
        raise AssertionError('optimality without a witness')
    return dict(ok=True, status='solved' if ub is not None else 'limit',
                min_steps=ub if certified else None, sequence=sequence,
                verified=ub is not None, certified=certified, lb=lb, ub=ub,
                states=nodes, time=time.time()-t0, method=method,
                initial_steps=initial_steps, notes=notes, metrics=metrics)


def min_steps(a, **kw):
    return solve(a, **kw).get('min_steps')


def prove_min(a, K, node_budget=1_000_000, deadline_s=300.0):
    t0 = time.time()
    dl = None if deadline_s is None else t0+deadline_s
    found, _moves, nodes, _memo, reason = E.decision(
        E.state_of(a), K, deadline=dl, node_budget=node_budget)
    return reason == 'proved' and not found, nodes, time.time()-t0


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        a = json.loads(arg)
        r = solve(a)
        print(json.dumps(dict(a=a, **r), ensure_ascii=False))
