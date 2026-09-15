"""Find B_p chart returns in one or two punctured Reynolds layers.

The search works with block coefficient pairs.  A target B_p chart is
recognized by grouping equal output rows, so no p by p rational matrices or
physical p-vectors are stored.  Independent primes run in separate workers.
"""

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from math import isqrt
from os import cpu_count

from explore_nonsplit_bcore_closed_words import (
    bcore_basis,
    labels,
    transition_scaled,
)
from verify_nonsplit_projective_layers import partition


def prime(value):
    return value >= 2 and all(value % divisor
                              for divisor in range(2, isqrt(value) + 1))


def target_charts(p, target, outputs):
    pairs = tuple(zip(*outputs))
    hits = []
    for w_index, u_index in ((0, 1), (1, 0)):
        u_row = pairs[u_index]
        exceptional = [index for index in range(2, len(target))
                       if pairs[index] != u_row]
        if len(exceptional) != 1:
            continue
        v_index = exceptional[0]
        v_row = pairs[v_index]
        expected_w = tuple(-(p - 4) * u_row[column]
                           - 3 * v_row[column] for column in (0, 1))
        if pairs[w_index] != expected_w:
            continue
        matrix = u_row + v_row
        a, b, c, d = matrix
        hecke = 3 * (a + d) ** 2 + 4 * (a * d - b * c) == 0
        hits.append((w_index, v_index, matrix, hecke))
    return hits


def inspect(case):
    p, depth = case
    parts = tuple(partition(shift, p) for shift in range(p))
    block_labels = tuple(labels(part, p) for part in parts)
    basis = bcore_basis(p, parts[0])
    one_layer = []
    two_layer = []
    three_layer = []
    first_outputs = []
    for middle_index, middle in enumerate(parts):
        output = tuple(transition_scaled(vector, block_labels[0], middle)
                       for vector in basis)
        first_outputs.append(output)
        for hit in target_charts(p, middle, output):
            one_layer.append((middle_index, *hit))
    if depth >= 2:
        for middle_index, (middle, values) in enumerate(zip(parts,
                                                             first_outputs)):
            for target_index, target in enumerate(parts):
                output = tuple(transition_scaled(vector,
                                                 block_labels[middle_index],
                                                 target)
                               for vector in values)
                for hit in target_charts(p, target, output):
                    two_layer.append((middle_index, target_index, *hit))
                if depth >= 3:
                    returned = tuple(transition_scaled(
                        vector, block_labels[target_index], parts[0])
                                     for vector in output)
                    for hit in target_charts(p, parts[0], returned):
                        three_layer.append((middle_index, target_index, *hit))
    return {
        "prime": p,
        "one_charts": len(one_layer),
        "one_hecke": sum(hit[-1] for hit in one_layer),
        "two_charts": len(two_layer),
        "two_hecke": sum(hit[-1] for hit in two_layer),
        "three_charts": len(three_layer),
        "three_hecke": sum(hit[-1] for hit in three_layer),
        "one_examples": one_layer[:4],
        "two_examples": two_layer[:8],
        "three_examples": three_layer[:8],
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--limit", type=int, default=149)
    parser.add_argument("--depth", type=int, choices=(1, 2, 3), default=2)
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    args = parser.parse_args()
    primes = tuple(value for value in range(11, args.limit + 1)
                   if value % 3 == 2 and prime(value))
    cases = tuple((p, args.depth) for p in primes)
    workers = min(args.jobs, len(cases))
    print("nonsplit Hecke chart cases", len(cases), "workers", workers,
          "depth", args.depth, flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = sorted(executor.map(inspect, cases),
                         key=lambda result: result["prime"])
    for result in results:
        print(result, flush=True)
    print("nonsplit one-to-three-layer Hecke chart survey: PASS",
          sum(result["one_charts"] for result in results),
          sum(result["two_charts"] for result in results),
          sum(result["two_hecke"] for result in results),
          sum(result["three_charts"] for result in results),
          sum(result["three_hecke"] for result in results), flush=True)


if __name__ == "__main__":
    main()
