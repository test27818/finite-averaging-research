"""Bounded count-state search for a zero-sum triple in B_p.

Each state is a sorted tuple of (integer numerator, multiplicity).  A common
power-of-three denominator is suppressed.  This avoids expanding p physical
positions and makes exact branching depend on the number of value types.
"""

from argparse import ArgumentParser
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import combinations_with_replacement
from math import ceil, gcd
import os


def normalize(counter):
    counter = Counter({value: count for value, count in counter.items() if count})
    divisor = gcd(*(abs(value) for value in counter))
    counter = Counter({value // divisor: count for value, count in counter.items()})
    positive = tuple(sorted(counter.items()))
    negative = tuple(sorted((-value, count) for value, count in counter.items()))
    # Quotient by global sign without relying on the first nonzero value.
    return min(positive, negative)


def initial(prime, u, v):
    c = -(prime - 4) * u - 3 * v
    # B_p(u,v)=(u^(p-4),v^3,c), with c the singleton after clearing
    # the common denominator implicit in this integer input.
    state = Counter()
    state[u] += prime - 4
    state[v] += 3
    state[c] += 1
    assert sum(value * count for value, count in state.items()) == 0
    return normalize(state)


def legal_case(prime, u, v):
    state = initial(prime, u, v)
    values = [value for value, _ in state]
    anchor = values[0]
    return gcd(*(abs(value - anchor) for value in values)) % prime != 0


def triples(state):
    values = tuple(value for value, _ in state)
    counts = dict(state)
    for selected in combinations_with_replacement(values, 3):
        demand = Counter(selected)
        if all(demand[value] <= counts[value] for value in demand):
            if len(demand) > 1:
                yield selected


def has_zero_sum_triple(state):
    counts = dict(state)
    values = tuple(counts)
    for left_index, left in enumerate(values):
        for middle_index in range(left_index, len(values)):
            middle = values[middle_index]
            right = -left - middle
            if right < middle or right not in counts:
                continue
            demand = Counter((left, middle, right))
            if all(demand[value] <= counts[value] for value in demand):
                return left, middle, right
    return None


def step(state, selected):
    output = Counter({3 * value: count for value, count in state})
    for value in selected:
        output[3 * value] -= 1
    output[sum(selected)] += 3
    return normalize(output)


def inspect(case):
    prime, u, v, depth = case
    start = initial(prime, u, v)
    seen = {start}
    frontier = {start: ()}
    levels = []
    for level in range(depth + 1):
        levels.append((level, len(frontier), len(seen),
                       max(len(state) for state in frontier)))
        for state, word in frontier.items():
            terminal = has_zero_sum_triple(state)
            if terminal is not None:
                return {
                    "prime": prime,
                    "u": u,
                    "v": v,
                    "hit": True,
                    "level": level,
                    "word": word,
                    "terminal": terminal,
                    "levels": levels,
                }
        if level == depth:
            break
        following = {}
        for state, word in frontier.items():
            for selected in triples(state):
                output = step(state, selected)
                if output not in seen and output not in following:
                    following[output] = word + (selected,)
        seen.update(following)
        frontier = following
    return {
        "prime": prime,
        "u": u,
        "v": v,
        "hit": False,
        "level": depth,
        "frontier": len(frontier),
        "seen": len(seen),
        "levels": levels,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--prime", type=int, action="append", default=None)
    parser.add_argument("--v", type=int, action="append", default=None)
    parser.add_argument("--v-min", type=int)
    parser.add_argument("--v-max", type=int)
    parser.add_argument("--u", type=int, default=1)
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    primes = tuple(args.prime or (17, 23, 29, 41, 47, 53, 59, 71))
    if args.v is not None:
        values = tuple(args.v)
    elif args.v_min is not None or args.v_max is not None:
        lower = args.v_min if args.v_min is not None else -8
        upper = args.v_max if args.v_max is not None else 8
        values = tuple(range(lower, upper + 1))
    else:
        values = (-8, -5, -3, -1, 0, 2, 3, 5, 8)
    cases = tuple((prime, args.u, value, args.depth)
                  for prime in primes for value in values
                  if legal_case(prime, args.u, value))
    workers = min(args.jobs, len(cases))
    print("B-core zero-triple cases", len(cases), "workers", workers,
          "depth", args.depth, flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        chunk_size = max(1, ceil(len(cases) / (4 * workers)))
        results = []
        for result in executor.map(inspect, cases, chunksize=chunk_size):
            results.append(result)
            if not args.summary:
                print(result, flush=True)
    if args.summary:
        for prime in primes:
            selected = [result for result in results if result["prime"] == prime]
            hits = [result for result in selected if result["hit"]]
            misses = sorted(result["v"] for result in selected if not result["hit"])
            maximum = max((result["level"] for result in hits), default=None)
            print("prime", prime, "covered", len(hits), "/", len(selected),
                  "max-depth", maximum, "misses", misses, flush=True)
        print("B-core zero-triple bounded summary: PASS",
              sum(result["hit"] for result in results), len(results), flush=True)


if __name__ == "__main__":
    main()
