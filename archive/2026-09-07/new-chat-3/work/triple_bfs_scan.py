"""Finite-depth exact search for ternary averaging, used only for conjecture screening."""

from __future__ import annotations

from collections import deque
from itertools import combinations, product
from math import gcd
from time import perf_counter


def primitive(state: tuple[int, ...]) -> tuple[int, ...]:
    divisor = 0
    for value in state:
        divisor = gcd(divisor, abs(value))
    if divisor == 0:
        return state
    state = tuple(value // divisor for value in state)
    for value in state:
        if value:
            return state if value > 0 else tuple(-x for x in state)
    return state


def triple_step(state: tuple[int, ...], triple: tuple[int, int, int]) -> tuple[int, ...]:
    selected = set(triple)
    total = sum(state[index] for index in triple)
    return primitive(tuple(total if index in selected else 3 * value for index, value in enumerate(state)))


def gcd_difference(state: tuple[int, ...]) -> int:
    value = 0
    for item in state[1:]:
        value = gcd(value, abs(item - state[0]))
    return value


def is_power_of_three(value: int) -> bool:
    if value < 1:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def distance_to_zero(initial: tuple[int, ...], max_depth: int, max_states: int) -> tuple[int | None, int, bool]:
    n = len(initial)
    triples = tuple(combinations(range(n), 3))
    initial = primitive(initial)
    frontier = {initial}
    seen = {initial}
    for depth in range(max_depth + 1):
        if (0,) * n in frontier:
            return depth, len(seen), False
        if depth == max_depth:
            break
        next_frontier = set()
        for state in frontier:
            for triple in triples:
                child = triple_step(state, triple)
                if child not in seen:
                    seen.add(child)
                    next_frontier.add(child)
                    if len(seen) > max_states:
                        return None, len(seen), True
        frontier = next_frontier
    return None, len(seen), False


def find_path(initial: tuple[int, ...], max_depth: int, max_states: int):
    """Return one exact path, or None; this is not an impossibility oracle."""
    n = len(initial)
    zero = (0,) * n
    triples = tuple(combinations(range(n), 3))
    initial = primitive(initial)
    frontier = {initial}
    parent = {initial: None}
    for _depth in range(max_depth):
        next_frontier = set()
        for state in frontier:
            for triple in triples:
                child = triple_step(state, triple)
                if child not in parent:
                    parent[child] = (state, triple)
                    if child == zero:
                        path = []
                        while parent[child] is not None:
                            previous, operation = parent[child]
                            path.append((operation, child))
                            child = previous
                        return list(reversed(path))
                    next_frontier.add(child)
                    if len(parent) > max_states:
                        return None
        frontier = next_frontier
    return None


def enumerate_vectors(n: int, bound: int):
    seen = set()
    for prefix in product(range(-bound, bound + 1), repeat=n - 1):
        last = -sum(prefix)
        if abs(last) > bound:
            continue
        state = primitive(prefix + (last,))
        if state == (0,) * n or state in seen:
            continue
        seen.add(state)
        yield state


def main() -> None:
    n = 5
    bound = 3
    max_depth = 10
    max_states = 500_000
    tested = solved = unresolved = capped = 0
    hardest: list[tuple[tuple[int, ...], int]] = []
    started = perf_counter()
    for state in enumerate_vectors(n, bound):
        if not is_power_of_three(gcd_difference(state)):
            continue
        tested += 1
        distance, states, hit_cap = distance_to_zero(state, max_depth, max_states)
        if distance is None:
            unresolved += 1
            capped += int(hit_cap)
            print(f"UNRESOLVED state={state} explored={states} capped={hit_cap}")
        else:
            solved += 1
            hardest.append((state, distance))
    hardest.sort(key=lambda entry: entry[1], reverse=True)
    print(
        f"n={n} bound={bound} depth={max_depth} tested={tested} solved={solved} "
        f"unresolved={unresolved} capped={capped} seconds={perf_counter() - started:.3f}"
    )
    print("hardest=" + repr(hardest[:20]))


if __name__ == "__main__":
    main()
