"""Exact ternary-averaging BFS modulo coordinate permutation and nonzero scale.

This is conjecture-screening code, not an impossibility oracle when a depth or
state cap is hit.  Quotienting is sound because every 3-subset is available.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement
from math import gcd
from time import perf_counter


def canonical(values: tuple[int, ...]) -> tuple[int, ...]:
    divisor = 0
    for value in values:
        divisor = gcd(divisor, abs(value))
    if divisor == 0:
        return values
    values = tuple(sorted(value // divisor for value in values))
    reflected = tuple(sorted(-value for value in values))
    return min(values, reflected)


def successors(state: tuple[int, ...]):
    n = len(state)
    for selected in combinations(range(n), 3):
        selected_set = set(selected)
        total = sum(state[index] for index in selected)
        yield canonical(tuple(total if index in selected_set else 3 * value for index, value in enumerate(state)))


def gcd_difference(state: tuple[int, ...]) -> int:
    result = 0
    for value in state[1:]:
        result = gcd(result, abs(value - state[0]))
    return result


def ternary_condition(state: tuple[int, ...]) -> bool:
    value = gcd_difference(state)
    while value and value % 3 == 0:
        value //= 3
    return value == 1


def search(initial: tuple[int, ...], max_depth: int, max_states: int):
    initial = canonical(initial)
    zero = (0,) * len(initial)
    frontier = {initial}
    seen = {initial}
    for depth in range(max_depth + 1):
        if zero in frontier:
            return depth, len(seen), False
        if depth == max_depth:
            return None, len(seen), False
        next_frontier = set()
        for state in frontier:
            for child in successors(state):
                if child not in seen:
                    seen.add(child)
                    next_frontier.add(child)
                    if len(seen) > max_states:
                        return None, len(seen), True
        frontier = next_frontier
    raise AssertionError("unreachable")


def inputs(n: int, bound: int):
    for prefix in combinations_with_replacement(range(-bound, bound + 1), n - 1):
        last = -sum(prefix)
        if last < prefix[-1] or last > bound:
            continue
        state = canonical(prefix + (last,))
        if state != (0,) * n:
            yield state


def main() -> None:
    n, bound, depth, cap = 5, 3, 10, 1_000_000
    started = perf_counter()
    results = []
    for state in inputs(n, bound):
        if not ternary_condition(state):
            continue
        distance, states, hit_cap = search(state, depth, cap)
        results.append((state, distance, states, hit_cap))
        print(f"state={state} depth={distance} visited={states} cap={hit_cap}", flush=True)
    solved = [item for item in results if item[1] is not None]
    unresolved = [item for item in results if item[1] is None]
    print(
        f"SUMMARY candidates={len(results)} solved={len(solved)} unresolved={len(unresolved)} "
        f"seconds={perf_counter() - started:.3f}"
    )
    print("HARDEST=" + repr(sorted(solved, key=lambda item: item[1], reverse=True)[:10]))


if __name__ == "__main__":
    main()
