"""Search raw triple averages for a nonstandard B_p Hecke wall.

States keep primitive integer coefficient pairs and multiplicities.  The
number of physical positions never enters the stored representation.  Triple
index patterns are cached by multiplicity signature, and primes run in
separate worker processes.
"""

from argparse import ArgumentParser
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
from itertools import combinations_with_replacement
from math import gcd, isqrt
from os import cpu_count


def prime(value):
    return value >= 2 and all(value % divisor
                              for divisor in range(2, isqrt(value) + 1))


def normalize(counter):
    counter = Counter({pair: count for pair, count in counter.items() if count})
    divisor = gcd(*(abs(value) for pair in counter for value in pair))
    positive = tuple(sorted((left // divisor, right // divisor, count)
                            for (left, right), count in counter.items()))
    negative = tuple(sorted((-left // divisor, -right // divisor, count)
                            for (left, right), count in counter.items()))
    return min(positive, negative)


def source(p):
    m = p - 4
    return normalize(Counter({(1, 0): m, (0, 1): 3, (-m, -3): 1}))


@lru_cache(maxsize=None)
def choices(capacities):
    result = []
    for selected in combinations_with_replacement(range(len(capacities)), 3):
        demand = Counter(selected)
        if len(demand) > 1 and all(demand[index] <= capacities[index]
                                   for index in demand):
            result.append(selected)
    return tuple(result)


def successors(state):
    values = tuple((left, right) for left, right, _ in state)
    capacities = tuple(count for _, _, count in state)
    for selected in choices(capacities):
        output = Counter({(3 * left, 3 * right): count
                          for left, right, count in state})
        total_left = total_right = 0
        for index in selected:
            left, right = values[index]
            output[(3 * left, 3 * right)] -= 1
            total_left += left
            total_right += right
        output[(total_left, total_right)] += 3
        yield normalize(output)


def bcore_matrix(p, state):
    m = p - 4
    by_count = {}
    for left, right, count in state:
        by_count.setdefault(count, []).append((left, right))
    if set(by_count) != {1, 3, m}:
        return None
    if any(len(by_count[count]) != 1 for count in (1, 3, m)):
        return None
    u = by_count[m][0]
    v = by_count[3][0]
    w = by_count[1][0]
    if w != (-m * u[0] - 3 * v[0], -m * u[1] - 3 * v[1]):
        return None
    return u + v


def hecke_reflection(matrix):
    a, b, c, d = matrix
    determinant = a * d - b * c
    return determinant and 3 * (a + d) ** 2 + 4 * determinant == 0


def proportional(left, right):
    return all(left[i] * right[j] == left[j] * right[i]
               for i in range(4) for j in range(i))


def inspect(case):
    p, depth, state_limit = case
    standard = (-3, 0, p - 4, 1)
    start = source(p)
    seen = {start}
    frontier = {start}
    levels = []
    hits = set()
    stopped = False
    for level in range(depth + 1):
        new_hits = set()
        for state in frontier:
            matrix = bcore_matrix(p, state)
            if (matrix is not None and hecke_reflection(matrix)
                    and not proportional(matrix, standard)):
                new_hits.add(matrix)
        hits.update(new_hits)
        levels.append((level, len(frontier), len(seen), len(new_hits)))
        if level == depth or hits:
            break
        following = set()
        for state in frontier:
            for output in successors(state):
                if output not in seen:
                    following.add(output)
                    if len(seen) + len(following) >= state_limit:
                        stopped = True
                        break
            if stopped:
                break
        seen.update(following)
        frontier = following
        if stopped:
            break
    return {
        "prime": p,
        "hits": tuple(sorted(hits)),
        "levels": levels,
        "stopped": stopped,
        "choice_cache": choices.cache_info()._asdict(),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--limit", type=int, default=71)
    parser.add_argument("--depth", type=int, default=5)
    parser.add_argument("--state-limit", type=int, default=2_000_000)
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    args = parser.parse_args()
    primes = tuple(p for p in range(11, args.limit + 1)
                   if p % 3 == 2 and prime(p))
    cases = tuple((p, args.depth, args.state_limit) for p in primes)
    workers = min(args.jobs, len(cases))
    print("atomic B_p Hecke wall cases", len(cases), "workers", workers,
          "depth", args.depth, "state-limit", args.state_limit, flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = sorted(executor.map(inspect, cases),
                         key=lambda result: result["prime"])
    for result in results:
        print(result, flush=True)
    print("atomic B_p nonstandard Hecke wall survey: PASS",
          sum(bool(result["hits"]) for result in results), len(results),
          sum(result["stopped"] for result in results), flush=True)


if __name__ == "__main__":
    main()
