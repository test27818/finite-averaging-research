"""Enumerate every primitive successful five-state certificate below a height cap.

The reverse parents of (u, v) are (-3v, u-v) and (u-v, -3v).  They are
legal exactly when u-v is a 3-adic unit.  Their l1 height is strictly larger
than that of (u, v).  A final state of max height at most H has l1 height at
most 2H, so pruning at l1 height 2H cannot remove any such state.
"""

from __future__ import annotations

from math import gcd


def normalise(u: int, v: int) -> tuple[int, int]:
    d = gcd(abs(u), abs(v))
    u //= d
    v //= d
    return (u, v) if (u > 0 or (u == 0 and v >= 0)) else (-u, -v)


def legal_parents(u: int, v: int):
    if (u - v) % 3 == 0:
        return
    yield normalise(-3 * v, u - v)
    yield normalise(u - v, -3 * v)


def profile(cap: int) -> None:
    root = (1, -1)
    level = {root}
    seen = {root}
    depth = 0
    print("cap", cap)
    while level:
        print(depth, len(level), min(max(abs(u), abs(v)) for u, v in level))
        next_level: set[tuple[int, int]] = set()
        for state in level:
            for parent in legal_parents(*state):
                if abs(parent[0]) + abs(parent[1]) <= 2 * cap:
                    next_level.add(parent)
        next_level -= seen
        seen |= next_level
        level = next_level
        depth += 1
    accepted = [
        state for state in seen if max(abs(state[0]), abs(state[1])) <= cap
    ]
    max_accepted_depth = max(
        # l1 grows strictly, hence a simple forward walk recovers the depth.
        # This local loop avoids retaining a path word for every tree node.
        depth_of(state) for state in accepted
    )
    print(
        "max-depth-at-height", max_accepted_depth,
        "accepted-states", len(accepted),
        "tree-states", len(seen),
    )


def depth_of(u_v: tuple[int, int]) -> int:
    u, v = u_v
    depth = 0
    while u + v:
        if u and u % 3 == 0 and v % 3:
            u, v = v - u // 3, -u // 3
        elif v and v % 3 == 0 and u % 3:
            u, v = u - v // 3, -v // 3
        else:
            raise AssertionError(f"reverse tree generated an invalid state: {(u, v)}")
        depth += 1
    return depth


if __name__ == "__main__":
    for bound in (100, 1_000, 10_000, 100_000):
        profile(bound)
