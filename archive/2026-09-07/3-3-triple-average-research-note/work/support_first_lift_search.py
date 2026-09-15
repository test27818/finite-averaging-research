from __future__ import annotations

from collections import deque
from itertools import combinations, product
from math import gcd


def primitive(state: tuple[int, ...]) -> tuple[int, ...]:
    d = 0
    for x in state:
        d = gcd(d, abs(x))
    if d:
        state = tuple(x // d for x in state)
    neg = tuple(-x for x in state)
    return min(state, neg)


def step(state: tuple[int, ...], chosen: tuple[int, ...]):
    s = sum(state[i] for i in chosen)
    chosen_set = set(chosen)
    raw = tuple(s if i in chosen_set else 3 * state[i] for i in range(len(state)))
    return primitive(raw), (s % 3 == 0)


def support(state: tuple[int, ...]) -> frozenset[int]:
    return frozenset(i for i, x in enumerate(state) if x % 3)


def shortest_paths(start: tuple[int, ...], max_depth: int, restrict_first_lift: bool = False):
    n = len(start)
    choices = list(combinations(range(n), 3))
    start = primitive(start)
    initial = support(start)
    queue = deque([(start, 0)])
    parent = {(start, 0): None}
    parent_choice = {}
    depth = {(start, 0): 0}
    while queue:
        state, phase = queue.popleft()
        d = depth[(state, phase)]
        if not any(state):
            path = []
            key = (state, phase)
            while parent[key] is not None:
                path.append(parent_choice[key])
                key = parent[key]
            return d, list(reversed(path))
        if d >= max_depth:
            continue
        for chosen in choices:
            nxt, lift = step(state, chosen)
            if restrict_first_lift and phase == 0 and lift:
                chosen_set = set(chosen)
                if chosen_set != set(initial) and chosen_set & set(initial):
                    continue
            next_phase = phase or lift
            key = (nxt, int(next_phase))
            if key not in parent:
                parent[key] = (state, phase)
                parent_choice[key] = chosen
                depth[key] = d + 1
                queue.append(key)
    return None


def enumerate_states(n: int, bound: int):
    for values in product(range(-bound, bound + 1), repeat=n - 1):
        last = -sum(values)
        if abs(last) > bound:
            continue
        state = tuple(values) + (last,)
        if primitive(state) != state:
            continue
        if support(state) and len(support(state)) == 3:
            yield state


def inspect_path(start, path):
    current = start
    initial = support(start)
    for k, chosen in enumerate(path, 1):
        nxt, lift = step(current, chosen)
        if lift:
            kind = "T" if set(chosen) == set(initial) else "disjoint" if not (set(chosen) & set(initial)) else "mixed"
            return k, chosen, kind, current, nxt
        current = nxt
    return None


def run(n: int, bound: int, max_depth: int):
    total = 0
    successes = 0
    mixed_shortest = []
    for start in enumerate_states(n, bound):
        total += 1
        result = shortest_paths(start, max_depth)
        if result is None:
            continue
        successes += 1
        restricted = shortest_paths(start, max_depth, restrict_first_lift=True)
        if restricted is None or restricted[0] > result[0]:
            mixed_shortest.append((start, result, restricted))
            print("COUNTEREXAMPLE", mixed_shortest[-1], flush=True)
            break
    print({"n": n, "bound": bound, "total": total, "successes": successes, "mixed": len(mixed_shortest)})


if __name__ == "__main__":
    run(6, 2, 8)
