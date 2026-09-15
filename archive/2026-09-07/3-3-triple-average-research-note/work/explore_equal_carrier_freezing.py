"""Finite-field obstruction test for freezing an equal-carrier leaf.

On the weighted zero-sum kernel

    (u_1^3, ..., u_r^3, a^2),   3 sum(u_i) + 2a = 0,

an equal-carrier exchange replaces one leaf by (u_i + 2a)/3 and makes
the two unused copies of u_i the new carriers.  After eliminating a, its
action on leaf coordinates is

    (S_i u)_i = u_i/3 - sum(u_j),   (S_i u)_j = u_j  (j != i).

A rational zero leaf must be zero in every finite-field reduction.  Hence
an orbit of <S_i> avoiding all coordinate hyperplanes is a rigorous
obstruction to a freezing proof that uses only these exchanges.

The search works projectively and traverses each orbit once.  Independent
(r, q) cases run in separate processes.
"""

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import product
import os


DEFAULT_CASES = (
    (3, 5), (3, 7), (3, 11), (3, 13), (3, 17),
    (5, 5), (5, 7), (5, 11), (5, 13), (5, 17),
    (7, 5), (7, 7), (7, 11),
    (9, 5),
)


def canonical(vector, modulus):
    for value in vector:
        if value:
            scale = pow(value, -1, modulus)
            return tuple((scale * entry) % modulus for entry in vector)
    raise ValueError("the zero vector has no projective representative")


def exchange(vector, index, modulus):
    output = list(vector)
    output[index] = (pow(3, -1, modulus) * vector[index]
                     - sum(vector)) % modulus
    return canonical(output, modulus)


def inverse_exchange(vector, index, modulus):
    output = list(vector)
    output[index] = (-3 * pow(2, -1, modulus) * sum(vector)) % modulus
    return canonical(output, modulus)


def projective_points(rank, modulus):
    for pivot in range(rank):
        prefix = (0,) * pivot + (1,)
        for tail in product(range(modulus), repeat=rank - pivot - 1):
            yield prefix + tail


def orbit(seed, rank, modulus, seen):
    reached = {seed}
    frontier = [seed]
    hits_terminal = any(value == 0 for value in seed)
    while frontier:
        vector = frontier.pop()
        for index in range(rank):
            for action in (exchange, inverse_exchange):
                output = action(vector, index, modulus)
                if output in reached:
                    continue
                reached.add(output)
                frontier.append(output)
                hits_terminal |= any(value == 0 for value in output)
    seen.update(reached)
    return reached, hits_terminal


def inspect_case(case):
    rank, modulus = case
    expected = (modulus ** rank - 1) // (modulus - 1)
    seen = set()
    orbit_count = 0
    avoiding = []
    terminal_orbit_sizes = []
    for point in projective_points(rank, modulus):
        if point in seen:
            continue
        reached, hits_terminal = orbit(point, rank, modulus, seen)
        orbit_count += 1
        if hits_terminal:
            terminal_orbit_sizes.append(len(reached))
        else:
            avoiding.append((point, len(reached)))
    assert len(seen) == expected

    prime_dimension = modulus == 3 * rank + 2
    constant = (1,) * rank
    illegal_constant_orbit = None
    if prime_dimension:
        for representative, size in avoiding:
            if constant in orbit(representative, rank, modulus, set())[0]:
                illegal_constant_orbit = (representative, size)
                break
    relevant = [item for item in avoiding if item != illegal_constant_orbit]
    return {
        "rank": rank,
        "modulus": modulus,
        "points": expected,
        "orbits": orbit_count,
        "terminal_orbits": len(terminal_orbit_sizes),
        "avoiding_orbits": len(avoiding),
        "relevant_avoiding_orbits": len(relevant),
        "example": relevant[0] if relevant else None,
        "constant_only": bool(avoiding) and not relevant,
        "largest_terminal_orbit": max(terminal_orbit_sizes, default=0),
    }


def parse_cases(values):
    if not values:
        return DEFAULT_CASES
    cases = []
    for value in values:
        rank, modulus = map(int, value.split(","))
        if modulus in (2, 3):
            raise ValueError("the eliminated equal-carrier model needs q != 2,3")
        cases.append((rank, modulus))
    return tuple(cases)


def main():
    parser = ArgumentParser()
    parser.add_argument("--case", action="append",
                        help="rank,prime-modulus; may be repeated")
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    args = parser.parse_args()
    cases = parse_cases(args.case)
    workers = min(args.jobs, len(cases))
    print("equal-carrier projective orbit cases", len(cases),
          "workers", workers, flush=True)
    results = []
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(inspect_case, case): case for case in cases}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(result, flush=True)
    total_points = sum(result["points"] for result in results)
    relevant = sum(result["relevant_avoiding_orbits"] for result in results)
    print("equal-carrier freezing finite-field audit: PASS",
          len(results), total_points, relevant)


if __name__ == "__main__":
    main()
