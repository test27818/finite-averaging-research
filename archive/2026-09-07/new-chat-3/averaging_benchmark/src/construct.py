#!/usr/bin/env python3
"""Fast verified construction, replacing the old near-final-DP/greedy default.

Keeps construct(a, exact_block, deadline_s, verbose, max_steps_mult) and its result
schema. exact_block is retained for compatibility; default construction does NOT run
an exact search before finding a witness. For optimization use optimize_ms or v2.solve.
"""
from __future__ import annotations
import json
import sys
from solver_v2 import solve
from mix_engine import deviations, reduce_prim


def primitive_deviations(a):
    return list(reduce_prim(deviations(a)))


def construct(a, exact_block=8, deadline_s=20.0, verbose=False, max_steps_mult=80,
              *, optimize_ms=0, max_steps=None):
    r = solve(a, deadline_s=deadline_s, optimize_ms=optimize_ms,
              max_steps=max_steps if max_steps is not None else max_steps_mult*len(a))
    result = dict(steps=r['sequence'], verified=r.get('verified', False),
                  method=r['method'], n_steps=r['ub'], time=r['time'],
                  status=r['status'], certified=r['certified'], lb=r['lb'], ub=r['ub'])
    if verbose:
        print(json.dumps(result))
    return result


if __name__ == '__main__':
    cases = [json.loads(arg) for arg in sys.argv[1:]] or [[0,0,0,1], [0,0,0,1,9]]
    for a in cases:
        print(json.dumps(dict(a=a, **construct(a)), ensure_ascii=False))
