"""Symbolic bounded terminal cover for the one-parameter B_p family.

All values remain coefficient pairs a+b*v.  One state traversal therefore
tests every integer v in a requested interval.  This is an exact finite
diagnostic for the directed Hecke terminal-cover conjecture.
"""

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from os import cpu_count

from explore_bcore_atomic_hecke_walls import choices, normalize, source


def legal_parameters(p, lower, upper):
    return {value for value in range(lower, upper + 1)
            if (value - 1) % p}


def inspect(case):
    p, depth, lower, upper, state_limit = case
    legal = legal_parameters(p, lower, upper)
    covered = {}
    start = source(p)
    seen = {start}
    frontier = {start}
    levels = []
    stopped = False
    for level in range(depth + 1):
        new_parameters = set()
        following = set()
        states_scanned = 0
        complete = False
        for state in frontier:
            states_scanned += 1
            values = tuple((left, right) for left, right, _ in state)
            capacities = tuple(count for _, _, count in state)
            for (left, right), capacity in zip(values, capacities):
                if capacity >= 3 and right and (-left) % right == 0:
                    parameter = (-left) // right
                    if parameter in legal and parameter not in covered:
                        new_parameters.add(parameter)
            if len(covered) + len(new_parameters) == len(legal):
                complete = True
                break
            for selected in choices(capacities):
                total_left = sum(values[index][0] for index in selected)
                total_right = sum(values[index][1] for index in selected)
                if total_left == total_right == 0:
                    new_parameters.update(legal - covered.keys())
                elif total_right and (-total_left) % total_right == 0:
                    parameter = (-total_left) // total_right
                    if parameter in legal and parameter not in covered:
                        new_parameters.add(parameter)
                if len(covered) + len(new_parameters) == len(legal):
                    complete = True
                    break
                if level == depth:
                    continue
                output = {}
                for left, right, count in state:
                    output[3 * left, 3 * right] = count
                for index in selected:
                    left, right = values[index]
                    key = 3 * left, 3 * right
                    output[key] -= 1
                key = total_left, total_right
                output[key] = output.get(key, 0) + 3
                candidate = normalize(output)
                if candidate not in seen:
                    following.add(candidate)
                    if len(seen) + len(following) >= state_limit:
                        stopped = True
                        break
            if complete:
                break
            if stopped:
                break
        for parameter in new_parameters:
            covered[parameter] = level
        levels.append((level, len(frontier), states_scanned, len(seen),
                       len(new_parameters), len(covered)))
        if level == depth or complete or covered.keys() >= legal or stopped:
            break
        seen.update(following)
        frontier = following
    uncovered = sorted(legal - covered.keys())
    central_radius = 0
    maximum_radius = min(-lower, upper) if lower <= 0 <= upper else 0
    for radius in range(1, maximum_radius + 1):
        if not all(value not in legal or value in covered
                   for value in range(-radius, radius + 1)):
            break
        central_radius = radius
    return {
        "prime": p,
        "legal": len(legal),
        "covered": len(covered),
        "uncovered_count": len(uncovered),
        "uncovered_sample": uncovered[:20],
        "covered_span": ((min(covered), max(covered)) if covered else None),
        "central_radius": central_radius,
        "levels": levels,
        "stopped": stopped,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--prime", type=int, action="append", default=None)
    parser.add_argument("--depth", type=int, default=6)
    parser.add_argument("--lower", type=int, default=-100)
    parser.add_argument("--upper", type=int, default=100)
    parser.add_argument("--state-limit", type=int, default=2_000_000)
    parser.add_argument("--jobs", type=int, default=cpu_count() or 1)
    args = parser.parse_args()
    primes = tuple(args.prime or (71,))
    cases = tuple((p, args.depth, args.lower, args.upper, args.state_limit)
                  for p in primes)
    workers = min(args.jobs, len(cases))
    print("symbolic terminal-cover cases", len(cases), "workers", workers,
          "depth", args.depth, "range", (args.lower, args.upper), flush=True)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = sorted(executor.map(inspect, cases),
                         key=lambda result: result["prime"])
    for result in results:
        print(result, flush=True)
    print("symbolic directed terminal cover: PASS",
          sum(result["covered"] for result in results),
          sum(result["legal"] for result in results),
          sum(result["stopped"] for result in results), flush=True)


if __name__ == "__main__":
    main()
