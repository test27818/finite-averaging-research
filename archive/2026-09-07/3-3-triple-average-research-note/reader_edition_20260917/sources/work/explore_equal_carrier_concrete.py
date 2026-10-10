"""Concrete bounded BFS for equal-carrier exchanges on one B_p input."""

from argparse import ArgumentParser
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from math import gcd
import os


def normalize(leaves, carrier):
    values = (*leaves, carrier)
    divisor = gcd(*(abs(value) for value in values))
    values = tuple(value // divisor for value in values)
    if next(value for value in values if value) < 0:
        values = tuple(-value for value in values)
    return tuple(sorted(values[:-1])), values[-1]


def initial(prime, u, v):
    rank = (prime - 2) // 3
    c = -(prime - 6) * u - 3 * v
    leaves = (3 * u,) * (rank - 2) + (3 * v, c)
    leaf_sum = sum(leaves)
    assert (-3 * leaf_sum) % 2 == 0
    carrier = (-3 * leaf_sum) // 2
    assert 3 * leaf_sum + 2 * carrier == 0
    return normalize(leaves, carrier)


def legal_parameter(prime, u, v):
    rank = (prime - 2) // 3
    scaled = [3 * u] * (rank - 2) + [3 * v,
             -(prime - 6) * u - 3 * v, 3 * u]
    anchor = scaled[0]
    difference_gcd = gcd(*(abs(value - anchor) for value in scaled))
    while difference_gcd and difference_gcd % 3 == 0:
        difference_gcd //= 3
    return difference_gcd == 1


def successors(state):
    leaves, carrier = state
    for selected in set(leaves):
        output = list(leaves)
        output.remove(selected)
        output = [3 * value for value in output]
        output.append(selected + 2 * carrier)
        yield normalize(tuple(output), 3 * selected), selected


def inspect(prime, depth, u, v):
    start = initial(prime, u, v)
    frontier = {start: ()}
    seen = {start}
    levels = []
    for level in range(depth + 1):
        levels.append((level, len(frontier), len(seen)))
        for state, word in frontier.items():
            if 0 in state[0]:
                return True, level, word, levels, state
        if level == depth:
            break
        following = {}
        for state, word in frontier.items():
            for output, selected in successors(state):
                if output not in seen and output not in following:
                    following[output] = word + (selected,)
        seen.update(following)
        frontier = following
    return False, depth, None, levels, None


def main():
    parser = ArgumentParser()
    parser.add_argument("--prime", type=int, action="append", default=None)
    parser.add_argument("--depth", type=int, default=9)
    parser.add_argument("--u", type=int, default=1)
    parser.add_argument("--v", type=int, action="append", default=None)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    args = parser.parse_args()
    primes = tuple(args.prime if args.prime is not None else (17, 23, 29, 41,
                                                               47, 53, 59, 71))
    values = tuple(args.v if args.v is not None else range(-8, 9))
    cases = tuple((prime, args.depth, args.u, value)
                  for prime in primes for value in values
                  if legal_parameter(prime, args.u, value))
    workers = min(args.jobs, len(cases))
    print("concrete equal-carrier cases", len(cases), "workers", workers,
          flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(inspect, *case): case for case in cases}
        for future in as_completed(futures):
            case = futures[future]
            print("case", case[0], case[2], case[3], "result",
                  future.result(), flush=True)


if __name__ == "__main__":
    main()
