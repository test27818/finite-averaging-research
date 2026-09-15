#!/usr/bin/env python3
"""Production admissible bound: opposite-pair counting + optional connectivity DP.

The old kappa/depth experimental implementation is preserved as research_lower.py,
but is NOT trusted by the default optimality-certification path. In particular its
per-position depth saturation needs a separate proof/review. Empirical agreement on
a finite dataset alone does not prove an algorithm's bound is admissible.
"""
from functools import lru_cache
import time
from mix_engine import deviations, reduce_prim, h_pairs
# Keep the research APIs importable explicitly, without using them for certification.
from research_lower import (kappa_of_value, kappas_of_deviation, bound_kappa,
                            depth_process_distance, partition_lb)


def simple_lb(x):
    return h_pairs(x)


def connectivity_bound(vals, max_n=14, deadline=None):
    """m - maximum number of disjoint zero-sum support blocks.

    Every connected component of a solution graph must have zero total deviation.
    Each component with s nonzero vertices needs at least s-1 operations, even when
    zero vertices are borrowed. This is a relaxation; no subset solvability assumed.
    Returns None on budget exhaustion, never a partial/enlarged lower bound.
    """
    vals = tuple(x for x in vals if x)
    n = len(vals)
    if n > max_n:
        return None
    if not n:
        return 0
    if sum(vals):
        return None
    zs = [[] for _ in vals]
    sums = [0]*(1 << n)
    for mask in range(1, len(sums)):
        if mask % 512 == 0 and deadline is not None and time.time() >= deadline:
            return None
        bit = mask & -mask
        sums[mask] = sums[mask ^ bit]+vals[bit.bit_length()-1]
        if not sums[mask]:
            for i in range(n):
                if mask >> i & 1:
                    zs[i].append(mask)

    @lru_cache(None)
    def blocks(mask):
        if deadline is not None and time.time() >= deadline:
            raise TimeoutError
        if not mask:
            return 0
        b = (mask & -mask).bit_length()-1
        return max(1+blocks(mask ^ part) for part in zs[b] if part & mask == part)
    try:
        return n-blocks(len(sums)-1)
    except TimeoutError:
        return None


def lower_bound(a, max_h=8, use_partition=True, detail=False):
    x = reduce_prim(deviations(a))
    h = h_pairs(x)
    c = connectivity_bound(x, deadline=time.time()+0.05) if use_partition else None
    bound = max(h, c or 0)
    info = dict(pairs=h, simple=h, partition=c, kappa=None, D_kappa=None)
    return (bound, info) if detail else bound


if __name__ == '__main__':
    for a in [[0,0,0,1], [0,0,0,1,9], [1,3,5,7,9]]:
        print(a, lower_bound(a, detail=True))
