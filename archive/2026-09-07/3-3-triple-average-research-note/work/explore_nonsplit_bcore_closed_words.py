"""Search the first nontrivial punctured-Reynolds closed words on B_p.

The search is structural: it fixes the symbolic family of partitions P_c and
tests all length-three closed words Q_0 Q_b Q_a on the two-dimensional B_p
subspace.  It also tests the shortest positive-adjoint closure
Q_0 Q_a Q_b Q_a.  No general conclusion is inferred from finite primes.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
from math import isqrt
from os import cpu_count

from verify_nonsplit_projective_layers import partition


def labels(partition_, p):
    result = [None] * p
    for index, block in enumerate(partition_):
        for position in block:
            result[position] = index
    assert all(value is not None for value in result)
    return result


def transition_scaled(values, source_labels, target):
    """Apply one layer to integer numerators and multiply its output by 3.

    After depth d, all block values have common denominator 3**d.  A target
    singleton copies its source value and therefore gets numerator 3*x at
    depth d+1; a target triple gets the sum of its three source numerators.
    """
    return [
        3 * values[source_labels[block[0]]]
        if len(block) == 1
        else sum(values[source_labels[position]] for position in block)
        for block in target
    ]


def common_scaled_integer(inputs, outputs):
    """Return r when every output equals r times its input, else None."""
    ratio = None
    for source, target in zip(inputs, outputs):
        for x, y in zip(source, target):
            if x:
                if y % x:
                    return None
                candidate = y // x
                if ratio is None:
                    ratio = candidate
                elif candidate != ratio:
                    return None
            elif y:
                return None
    return ratio


def bcore_basis(p, base):
    m = p - 4
    # Blocks are singleton 0, singleton -1, then sorted ternary orbits.
    u = [-m, 1, 0] + [1] * (len(base) - 3)
    v = [-3, 0, 1] + [0] * (len(base) - 3)
    weights = [len(block) for block in base]
    assert sum(a * w for a, w in zip(u, weights)) == 0
    assert sum(a * w for a, w in zip(v, weights)) == 0
    return u, v


def inspect(p):
    parts = [partition(c, p) for c in range(p)]
    block_labels = [labels(part, p) for part in parts]
    basis = bcore_basis(p, parts[0])
    closed = []
    adjoint_closed = []
    for a in range(1, p):
        first = [transition_scaled(vector, block_labels[0], parts[a])
                 for vector in basis]
        for b in range(1, p):
            if b == a:
                continue
            second = [transition_scaled(vector, block_labels[a], parts[b])
                      for vector in first]
            outputs = [transition_scaled(vector, block_labels[b], parts[0])
                       for vector in second]
            scalar = common_scaled_integer(basis, outputs)
            if scalar:
                closed.append((a, b, scalar, 3 ** 3))

            third = [transition_scaled(vector, block_labels[b], parts[a])
                     for vector in second]
            outputs = [transition_scaled(vector, block_labels[a], parts[0])
                       for vector in third]
            scalar = common_scaled_integer(basis, outputs)
            if scalar:
                adjoint_closed.append((a, b, scalar, 3 ** 4))
    return p, closed, adjoint_closed


def prime(value):
    return value >= 2 and not any(value % q == 0
                                  for q in range(2, isqrt(value) + 1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=149)
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    args = parser.parse_args()
    primes = [p for p in range(11, args.limit + 1) if p % 3 == 2 and prime(p)]
    with ProcessPoolExecutor(max_workers=min(args.jobs, len(primes))) as pool:
        for p, closed, adjoint_closed in sorted(pool.map(inspect, primes)):
            print("p", p, "closed3", closed, "adjoint4", adjoint_closed)
    print("Finite structural survey; no all-prime extrapolation.")
