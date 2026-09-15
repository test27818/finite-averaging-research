"""Exact finite-field reachability tests for ternary averaging.

Failure to reach zero modulo p is a proof of non-reachability over Q for
p != 3.  Success modulo p is only a necessary-condition check.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations


def orbit_to_zero(initial: tuple[int, ...], p: int):
    n = len(initial)
    inverse_three = pow(3, -1, p)
    initial = tuple(value % p for value in initial)
    target = (0,) * n
    queue = deque([initial])
    seen = {initial}
    triples = tuple(combinations(range(n), 3))
    while queue:
        state = queue.popleft()
        if state == target:
            return True, len(seen)
        for triple in triples:
            average = sum(state[i] for i in triple) * inverse_three % p
            child = list(state)
            for i in triple:
                child[i] = average
            child = tuple(child)
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return False, len(seen)


def main() -> None:
    candidates = [
        (-3, 0, 1, 1, 1),
        (-3, -1, 0, 2, 2),
        (-2, -1, 1, 2),
        (2, 2, -1, 2, -5),
    ]
    for state in candidates:
        for p in (2, 5, 7, 11, 13, 17, 19):
            reachable, states = orbit_to_zero(state, p)
            print(f"state={state} p={p} reachable={reachable} orbit={states}")


if __name__ == "__main__":
    main()
