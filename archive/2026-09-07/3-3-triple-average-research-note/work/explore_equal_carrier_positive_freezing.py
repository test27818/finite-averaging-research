"""Batched bounded test of positive equal-carrier freezing.

If W is a positive word in the equal-carrier exchanges, a zero leaf at the
end means that one row of W annihilates the initial leaf vector.  This script
enumerates the projective row covectors once and tests them against every
small primitive input in NumPy batches.  It is a finite diagnostic only.
"""

from argparse import ArgumentParser
from math import gcd

import numpy as np


def canonical(vector):
    divisor = gcd(*(abs(value) for value in vector))
    vector = tuple(value // divisor for value in vector)
    if next(value for value in vector if value) < 0:
        vector = tuple(-value for value in vector)
    return vector


def covector_step(vector, index):
    pivot = vector[index]
    output = [3 * (value - pivot) for value in vector]
    output[index] = -2 * pivot
    return canonical(output)


def initial_inputs(height, rank, dimension_prime):
    if rank != 3:
        raise ValueError("complete box generation is currently optimized for rank3")
    values = []
    for first in range(-height, height + 1):
        for second in range(-height, height + 1):
            for third in range(-height, height + 1):
                vector = (first, second, third)
                if not all(vector) or gcd(*(abs(value) for value in vector)) != 1:
                    continue
                if next(value for value in vector if value) < 0:
                    continue
                total = sum(vector)
                carrier = (-3 * total * pow(2, -1, dimension_prime)) % dimension_prime
                if all(value % dimension_prime == carrier for value in vector):
                    continue
                values.append(vector)
    return np.asarray(values, dtype=np.int64)


def covered_by(frontier, inputs, covector_batch):
    if not len(frontier) or not len(inputs):
        return np.zeros(len(inputs), dtype=bool)
    covectors = np.asarray(tuple(frontier), dtype=np.int64)
    covered = np.zeros(len(inputs), dtype=bool)
    # Keep the temporary dot-product array below roughly128 MiB.
    memory_batch = max(1, (128 * 1024 * 1024) // (8 * len(inputs)))
    batch_size = min(covector_batch, memory_batch)
    for start in range(0, len(covectors), batch_size):
        batch = covectors[start:start + batch_size]
        covered |= np.any(inputs @ batch.T == 0, axis=1)
        if covered.all():
            break
    return covered


def explore(height=24, depth=10, covector_batch=4096):
    rank = 3
    dimension_prime = 3 * rank + 2
    inputs = initial_inputs(height, rank, dimension_prime)
    uncovered = inputs
    seen = {tuple(int(row == column) for column in range(rank))
            for row in range(rank)}
    frontier = set(seen)
    print("positive equal-carrier inputs", len(inputs), "height", height,
          "depth", depth, flush=True)
    for level in range(depth + 1):
        hit = covered_by(frontier, uncovered, covector_batch)
        uncovered = uncovered[~hit]
        largest = max(max(abs(value) for value in vector)
                      for vector in frontier)
        print("level", level, "new covectors", len(frontier),
              "all covectors", len(seen), "uncovered", len(uncovered),
              "largest", largest, flush=True)
        if not len(uncovered):
            break
        following = {covector_step(vector, index)
                     for vector in frontier for index in range(rank)}
        following.difference_update(seen)
        seen.update(following)
        frontier = following
    examples = [tuple(map(int, row)) for row in uncovered[:20]]
    print("positive equal-carrier bounded coverage:",
          "PASS" if not len(uncovered) else "OPEN",
          len(inputs) - len(uncovered), len(inputs), examples)


def primitive_rows(rows):
    divisors = np.gcd.reduce(np.abs(rows), axis=1)
    rows //= divisors[:, None]
    pivots = np.argmax(rows != 0, axis=1)
    signs = rows[np.arange(len(rows)), pivots] < 0
    rows[signs] *= -1
    return np.unique(rows, axis=0)


def targeted(depth=16):
    targets = np.asarray((
        (2, -23, -23), (4, 23, 23), (10, 23, 23),
        (23, -2, 23), (23, 4, 23), (23, 10, 23),
        (23, 23, -2), (23, 23, 4), (23, 23, 10),
    ), dtype=np.int64)
    first_hits = [-1] * len(targets)
    witnesses = [None] * len(targets)
    frontier = np.eye(3, dtype=np.int64)
    for level in range(depth + 1):
        products = frontier @ targets.T
        for index in range(len(targets)):
            if first_hits[index] < 0:
                hits = np.flatnonzero(products[:, index] == 0)
                if len(hits):
                    first_hits[index] = level
                    witnesses[index] = tuple(map(int, frontier[hits[0]]))
        print("target level", level, "covectors", len(frontier),
              "hits", first_hits, "largest", int(np.abs(frontier).max()),
              flush=True)
        if all(level >= 0 for level in first_hits):
            break
        following = []
        for index in range(3):
            pivot = frontier[:, index:index + 1]
            output = 3 * (frontier - pivot)
            output[:, index] = -2 * frontier[:, index]
            following.append(output)
        frontier = primitive_rows(np.concatenate(following, axis=0))
    print("positive equal-carrier targeted coverage:",
          "PASS" if all(level >= 0 for level in first_hits) else "OPEN",
          first_hits, witnesses)


def main():
    parser = ArgumentParser()
    parser.add_argument("--height", type=int, default=24)
    parser.add_argument("--depth", type=int, default=10)
    parser.add_argument("--covector-batch", type=int, default=4096)
    parser.add_argument("--targeted", action="store_true")
    args = parser.parse_args()
    if args.targeted:
        targeted(args.depth)
    else:
        explore(args.height, args.depth, args.covector_batch)


if __name__ == "__main__":
    main()
