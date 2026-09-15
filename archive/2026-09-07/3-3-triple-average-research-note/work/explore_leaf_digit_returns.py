"""Search a uniform original-position leaf-digit/carrier syntax.

For p=3r+2 and gcd(r,3)=1, D is one full leaf-digit cycle, T exchanges the
exceptional triple block with the active singleton carrier, and S swaps the
two singleton labels.  All are positive words or free relabelings on the
original p positions.  Matrices are primitive integers and independent
prefix trees are distributed across processes.
"""

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from itertools import product as words
from math import gcd
from os import cpu_count


SAMPLES = (5, 7, 13, 17, 19, 23, 35, 37, 43, 49)


def order_three(r):
    value = 3 % r
    exponent = 1
    while value != 1:
        value = value * 3 % r
        exponent += 1
    return exponent


def generators(r):
    q = 3 ** order_three(r)
    digital = (
        (q * (r - 1) + 1, q - 1, 0),
        ((r - 1) * (q - 1), q + r - 1, 0),
        (0, 0, r * q),
    )
    exchange = ((3, 0, 0), (0, 2, 1), (0, 3, 0))
    swap = ((1, 0, 0), (0, 1, 0), (-3 * (r - 1), -3, -1))
    return digital, exchange, swap


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def primitive(matrix):
    divisor = gcd(*(entry for row in matrix for entry in row))
    matrix = tuple(tuple(entry // divisor for entry in row) for row in matrix)
    first = next(entry for row in matrix for entry in row if entry)
    if first < 0:
        matrix = tuple(tuple(-entry for entry in row) for row in matrix)
    return matrix


def append(matrix, generator):
    return primitive(multiply(generator, matrix))


def evaluate(word, r):
    generators_ = dict(zip("DTS", generators(r)))
    matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for letter in word:
        matrix = append(matrix, generators_[letter])
    return matrix


def induced_return(matrix, r):
    # Input B-plane: (U,V,A)=(u,v,u).  A return requires A'=U'.
    rows = tuple((row[0] + row[2], row[1]) for row in matrix)
    if rows[2] != rows[0]:
        return None
    result = rows[:2]
    if result[0][0] * result[1][1] == result[0][1] * result[1][0]:
        return None
    return result


def classify(matrix, r):
    result = induced_return(matrix, r)
    if result is None:
        return None
    p, m = 3 * r + 2, 3 * r - 2
    (a, b), (c, d) = result
    trace_zero = 3 * a - m * b - d == 0
    mixed = trace_zero and (m + 1) * (a + b) + 3 * (c + d) == 0
    return trace_zero, mixed, result


def universal_classification(word):
    classes = []
    for r in SAMPLES:
        classification = classify(evaluate(word, r), r)
        if classification is None:
            return None
        classes.append(classification)
    return classes


def worker(task):
    prefix, maximum, alphabet = task
    base_r = SAMPLES[0]
    digital, exchange, swap = generators(base_r)
    generators_ = {"D": digital, "T": exchange, "S": swap}
    matrix = evaluate(prefix, base_r)
    stack = [(prefix, matrix)]
    counts = Counter()
    counts[('all', 'checked')] = 0
    common = []
    while stack:
        word, matrix = stack.pop()
        counts[('all', 'checked')] += 1
        classification = classify(matrix, base_r)
        if classification is not None:
            counts[(len(word), "base_return")] += 1
            universal = universal_classification(word)
            if universal is not None:
                counts[(len(word), "common_return")] += 1
                if all(row[0] for row in universal):
                    counts[(len(word), "common_trace_zero")] += 1
                if all(row[1] for row in universal):
                    counts[(len(word), "common_mixed")] += 1
                if len(common) < 20:
                    common.append((word, tuple((row[0], row[1]) for row in universal)))
        if len(word) == maximum:
            continue
        for letter in alphabet:
            if letter == "S" and word.endswith("S"):
                continue
            stack.append((word + letter, append(matrix, generators_[letter])))
    return counts, common


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=18)
    parser.add_argument("--split-depth", type=int, default=3)
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    parser.add_argument("--alphabet", choices=("DT", "DTS"), default="DTS")
    args = parser.parse_args()
    if args.depth < args.split_depth:
        raise ValueError("depth must be at least split-depth")
    prefixes = ("".join(word) for word in words(args.alphabet, repeat=args.split_depth)
                if "SS" not in "".join(word))
    tasks = [(prefix, args.depth, args.alphabet) for prefix in prefixes]
    total = Counter()
    examples = []
    with ProcessPoolExecutor(max_workers=min(args.jobs, len(tasks))) as pool:
        for counts, common in pool.map(worker, tasks):
            total.update(counts)
            examples.extend(common)
    for key, value in sorted((item for item in total.items()
                              if item[0] != ('all', 'checked'))):
        print(key, value)
    for example in sorted(examples)[:40]:
        print("common", example)
    print("words checked", total[('all', 'checked')])
    print("Finite uniform-syntax survey; no all-r extrapolation.")
