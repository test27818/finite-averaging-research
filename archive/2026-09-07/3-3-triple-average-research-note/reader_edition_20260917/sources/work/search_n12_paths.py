"""Beam search for the first open n=12 low-support kernels."""

from collections import Counter
from fractions import Fraction as F
from heapq import nsmallest
from itertools import combinations_with_replacement
from math import gcd, log2


def primitive(counter):
    denominators = [value.denominator for value in counter]
    common = 1
    for denominator in denominators:
        common = common * denominator // gcd(common, denominator)
    integer = Counter({int(value * common): count for value, count in counter.items()})
    divisor = gcd(*(abs(value) for value in integer))
    integer = Counter({value // divisor: count for value, count in integer.items()})
    first = min(integer)
    if abs(max(integer)) < abs(first):
        integer = Counter({-value: count for value, count in integer.items()})
    return +integer


def key(counter):
    return tuple(sorted(counter.items()))


def difference_gcd(counter):
    values = list(counter)
    return gcd(*(abs(value - values[0]) for value in values[1:]))


def power3(value):
    while value and value % 3 == 0:
        value //= 3
    return value == 1


def successors(counter):
    values = sorted(counter)
    for triple in combinations_with_replacement(values, 3):
        need = Counter(triple)
        if len(need) == 1 or any(counter[value] < count
                                 for value, count in need.items()):
            continue
        following = counter.copy()
        for value in triple:
            following[value] -= 1
        following[sum(triple, F(0)) / 3] += 3
        following = primitive(+following)
        if power3(difference_gcd(following)):
            yield triple, following


def terminal(counter):
    n = sum(counter.values())
    q = 1
    while 3 * q <= n:
        q *= 3
    if counter.get(0, 0) >= n - q:
        return "zero padding"
    if len(counter) <= 2:
        return "two values"
    return None


def score(counter):
    zero = counter.get(0, 0)
    support = len(counter)
    energy = sum(value * value * count for value, count in counter.items())
    height = max(abs(value) for value in counter)
    return (-zero, support, log2(1 + energy), log2(1 + height))


def search(start, depth, width):
    start = Counter(start)
    frontier = [start]
    parents = {key(start): None}
    paths = {key(start): ()}
    for level in range(depth + 1):
        candidates = {}
        for counter in frontier:
            result = terminal(counter)
            if result:
                path = paths[key(counter)]
                print("FOUND", result, "depth", len(path), "path", path)
                print("state", counter)
                return path, counter
            for triple, following in successors(counter):
                identifier = key(following)
                if identifier not in parents:
                    parents[identifier] = key(counter)
                    paths[identifier] = paths[key(counter)] + (triple,)
                    candidates[identifier] = following
        frontier = nsmallest(width, candidates.values(), key=score)
        print("level", level + 1, "new", len(candidates), "retained", len(frontier),
              "seen", len(parents), "best", score(frontier[0]) if frontier else None,
              flush=True)
    print("NOT FOUND")
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=("12", "14"), default="12")
    arguments = parser.parse_args()
    starts = ([
        {-2: 5, 1: 4, 2: 3},
        {-2: 2, -1: 3, 1: 7},
        {-3: 4, 1: 4, 2: 4},
        {-1: 5, 0: 2, 1: 5},
    ] if arguments.case == "12" else [
        {-2: 6, 1: 4, 2: 4},
        {-3: 6, 2: 6, 3: 2},
        {-2: 3, -1: 4, 1: 4, 2: 3},
        {-1: 6, 0: 5, 2: 3},
        {-1: 5, 0: 4, 1: 5},
    ])
    for start in starts:
        print("START", start)
        search(start, 10, 50000)
