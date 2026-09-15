"""Mine existing return libraries for two-factor mixed trace-zero returns.

The two defining conditions are homogeneous linear forms in the product.
Candidates are first bucketed by the projective pair of row sums required by
the mixed-singleton condition, then checked with one integer trace form.  No
template grammar or word depth is expanded.
"""

import argparse
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from math import gcd
from os import cpu_count

from compile_bn_integer_templates import compile_returns


def direction(a, b):
    if not a and not b:
        return (0, 0)
    divisor = gcd(a, b)
    a, b = a // divisor, b // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return a, b


def multiply(a, b):
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def mixed_parameter(p, matrix):
    a, b, c, d = matrix
    m = p - 4
    scale = a + b
    singleton_v = -m * b - 3 * d
    if not scale:
        return None
    beta = F(singleton_v, scale)
    t = F(b, scale)
    assert t == F(9 + beta, 2 * p + 1)
    return beta


def inspect(p):
    rows, stats = compile_returns(
        p, include_six=True, current_library=True, expanded_first=True
    )
    matrices = tuple(rows)
    buckets = defaultdict(list)
    zero_sums = []
    for matrix in matrices:
        key = direction(matrix[0] + matrix[1], matrix[2] + matrix[3])
        buckets[key].append(matrix)
        if key == (0, 0):
            zero_sums.append(matrix)

    hits = []
    tested = 0
    for left in matrices:
        a, b, c, d = left
        first = (p - 3) * a + 3 * c
        second = (p - 3) * b + 3 * d
        candidates = list(buckets.get(direction(second, -first), ()))
        candidates.extend(zero_sums)
        if not first and not second:
            candidates = matrices
        for right in candidates:
            e, f, g, h = right
            tested += 1
            trace_numerator = (
                3 * a * e + (-(p - 4) * a - c) * f
                + 3 * b * g + (-(p - 4) * b - d) * h
            )
            if trace_numerator:
                continue
            product = multiply(left, right)
            if product[0] * product[3] == product[1] * product[2]:
                continue
            hits.append((mixed_parameter(p, product), left, right))

    beta_counts = defaultdict(int)
    for beta, _, _ in hits:
        beta_counts[beta] += 1
    examples = sorted((beta, count) for beta, count in beta_counts.items())[:20]
    return {
        "p": p,
        "returns": len(matrices),
        "all_pairs": len(matrices) ** 2,
        "tested": tested,
        "hits": len(hits),
        "betas": len(beta_counts),
        "examples": examples,
        "stats": (stats["prefixes"], stats["middle_tests"], stats["final_tests"]),
    }


def parse_primes(value):
    return tuple(int(item) for item in value.split(",") if item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", type=parse_primes,
                        default=(17, 23, 29, 41, 47, 53, 59, 71, 83))
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    args = parser.parse_args()
    with ProcessPoolExecutor(max_workers=min(args.jobs, len(args.primes))) as pool:
        for result in sorted(pool.map(inspect, args.primes), key=lambda row: row["p"]):
            print(result)
