"""Search a reproducible sample for short, nontrivial ternary-average paths."""

from __future__ import annotations

import random
from itertools import combinations

from triple_bfs_scan import find_path, gcd_difference, is_power_of_three, primitive


def main() -> None:
    random.seed(20260907)
    found = 0
    attempts = 0
    while attempts < 80 and found < 5:
        prefix = tuple(random.randint(-5, 5) for _ in range(4))
        state = primitive(prefix + (-sum(prefix),))
        attempts += 1
        if max(map(abs, state)) > 7:
            continue
        if not is_power_of_three(gcd_difference(state)):
            continue
        if any(sum(state[index] for index in triple) == 0 for triple in combinations(range(5), 3)):
            continue
        path = find_path(state, max_depth=5, max_states=200_000)
        if path:
            print(f"FOUND state={state} path={path}")
            found += 1
    print(f"attempts={attempts} found={found}")


if __name__ == "__main__":
    main()
