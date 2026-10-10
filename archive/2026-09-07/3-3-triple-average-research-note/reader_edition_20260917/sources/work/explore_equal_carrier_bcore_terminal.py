"""Search the actual B_p-derived equal-carrier family for a zero leaf.

States are symbolic coefficient pairs in the two input parameters.  Equal
leaf types are compressed, so branching is by value type rather than by the
number of physical blocks.  This is a bounded discovery search.
"""

from argparse import ArgumentParser
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from math import gcd
import os


DEFAULT_PRIMES = (17, 23, 29, 41, 47, 53, 59, 71)


def normalize(leaves, carrier):
    divisor = gcd(*(abs(value) for pair in (*leaves, carrier)
                    for value in pair))
    leaves = tuple((left // divisor, right // divisor)
                   for left, right in leaves)
    carrier = tuple(value // divisor for value in carrier)
    positive = tuple(sorted(leaves)), carrier
    negative = (tuple(sorted((-left, -right) for left, right in leaves)),
                tuple(-value for value in carrier))
    return min(positive, negative)


def initial(prime):
    rank = (prime - 2) // 3
    # A common factor3 clears c=-(p-6)u/3-v.
    background = (3, 0)
    exceptional = (0, 3)
    last = (-(prime - 6), -3)
    leaves = (background,) * (rank - 2) + (exceptional, last)
    return normalize(leaves, background)


def successors(state):
    leaves, carrier = state
    counts = Counter(leaves)
    for selected in counts:
        output_leaf = (selected[0] + 2 * carrier[0],
                       selected[1] + 2 * carrier[1])
        output_carrier = (3 * selected[0], 3 * selected[1])
        output = [(3 * left, 3 * right) for left, right in leaves]
        output.remove((3 * selected[0], 3 * selected[1]))
        output.append(output_leaf)
        yield normalize(tuple(output), output_carrier), selected


def terminal(state):
    return (0, 0) in state[0]


def inspect(case):
    prime, depth = case
    start = initial(prime)
    seen = {start: None}
    frontier = {start: ()}
    levels = []
    for level in range(depth + 1):
        levels.append((level, len(frontier), len(seen),
                       max(len(set(state[0])) for state in frontier)))
        for state, word in frontier.items():
            if terminal(state):
                return {
                    "prime": prime,
                    "hit": True,
                    "level": level,
                    "word": word,
                    "levels": levels,
                    "terminal": state,
                }
        if level == depth:
            break
        following = {}
        for state, word in frontier.items():
            for output, selected in successors(state):
                if output not in seen and output not in following:
                    following[output] = word + (selected,)
        seen.update({state: None for state in following})
        frontier = following
    return {
        "prime": prime,
        "hit": False,
        "level": depth,
        "frontier": len(frontier),
        "seen": len(seen),
        "levels": levels,
    }


def legal_parameter(prime, value):
    rank = (prime - 2) // 3
    scaled = [3] * (rank - 2) + [3 * value,
              -(prime - 6) - 3 * value, 3]
    anchor = scaled[0]
    divisor = gcd(*(abs(entry - anchor) for entry in scaled))
    while divisor and divisor % 3 == 0:
        divisor //= 3
    return divisor == 1


def roots_for_prime(case):
    prime, depth, lower, upper = case
    start = initial(prime)
    seen = {start}
    frontier = {start}
    roots = {}
    levels = []
    for level in range(depth + 1):
        new_roots = 0
        for state in frontier:
            for left, right in state[0]:
                if right and (-left) % right == 0:
                    value = (-left) // right
                    if lower <= value <= upper and value not in roots:
                        roots[value] = level
                        new_roots += 1
        levels.append((level, len(frontier), len(seen), new_roots,
                       len(roots)))
        following = set()
        for state in frontier:
            for output, _ in successors(state):
                if output not in seen:
                    following.add(output)
        seen.update(following)
        frontier = following
    legal = [value for value in range(lower, upper + 1)
             if legal_parameter(prime, value)]
    uncovered = [value for value in legal if value not in roots]
    return {
        "prime": prime,
        "legal": len(legal),
        "covered": len(legal) - len(uncovered),
        "uncovered": uncovered,
        "levels": levels,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--prime", action="append", type=int)
    parser.add_argument("--depth", type=int, default=8)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    parser.add_argument("--symbolic-roots", action="store_true")
    parser.add_argument("--lower", type=int, default=-100)
    parser.add_argument("--upper", type=int, default=101)
    args = parser.parse_args()
    primes = tuple(args.prime or DEFAULT_PRIMES)
    if args.symbolic_roots:
        cases = tuple((prime, args.depth, args.lower, args.upper)
                      for prime in primes)
        workers = min(args.jobs, len(cases))
        print("B-core symbolic root cases", len(cases), "workers", workers,
              "depth", args.depth, flush=True)
        with ProcessPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(roots_for_prime, case): case
                       for case in cases}
            for future in as_completed(futures):
                print(future.result(), flush=True)
        return
    cases = tuple((prime, args.depth) for prime in primes)
    workers = min(args.jobs, len(cases))
    print("B-core equal-carrier symbolic cases", len(cases),
          "workers", workers, "depth", args.depth, flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(inspect, case): case for case in cases}
        for future in as_completed(futures):
            print(future.result(), flush=True)


if __name__ == "__main__":
    main()
