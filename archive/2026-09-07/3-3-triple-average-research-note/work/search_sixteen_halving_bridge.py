"""Symbolic B16 bridge into duplicated legal B8-sized states.

Finite domains are projective pairs mod 16 and mod 5. Only sufficient,
lift-invariant local conditions on solved even-sized subblocks are used.
"""

from collections import deque, Counter
from itertools import combinations_with_replacement, product
from pathlib import Path
from time import perf_counter
import argparse
import json


START = tuple(sorted(((1, 0, 12), (0, 1, 3), (-12, -3, 1))))
SIZES = (8, 10, 12)


def domains():
    two = [(1, t) for t in range(0, 16, 2)]+[(t, 1) for t in range(0, 16, 2)]
    five = [(1, t) for t in range(5)]+[(0, 1)]
    return list(product(two, five))


def choices(state):
    for ids in combinations_with_replacement(range(len(state)), 3):
        i, j, k = ids
        if i == k or (i == j and state[i][2] < 2) or (j == k and state[j][2] < 2):
            continue
        yield ids


def step(state, ids):
    following = {(3*a, 3*b): c for a, b, c in state}
    mean = [0, 0]
    for i in ids:
        a, b, _ = state[i]
        mean[0] += a
        mean[1] += b
        key = 3*a, 3*b
        following[key] -= 1
        if not following[key]:
            del following[key]
    key = tuple(mean)
    following[key] = following.get(key, 0)+3
    return tuple(sorted((a, b, c) for (a, b), c in following.items()))


def block_choices(state, size):
    """Consume each odd multiplicity oddly, so all remaining counts are even."""
    for counts in product(*(range(c % 2, c+1, 2) for a, b, c in state)):
        if sum(counts) == size:
            yield counts


def qualifies(state, counts, size, domain):
    pair2, pair5 = domain
    v2 = {8:3, 10:1, 12:2}[size]
    values2 = [(a*pair2[0]+b*pair2[1]) % 16 for a, b, c in state]
    total2 = sum(x*c for x, c in zip(values2, counts))
    if total2 % (1 << v2):
        return False
    chosen = {x % 2 for x, c in zip(values2, counts) if c}
    if len(chosen) < 2:
        return False
    remaining = {x % 2 for x, (_, _, c), used in zip(values2, state, counts) if c-used}
    mean2 = (total2 >> v2) % 2
    if len(remaining | {mean2}) < 2:
        return False
    if size == 10:
        values5 = [(a*pair5[0]+b*pair5[1]) % 5 for a, b, c in state]
        if sum(x*c for x, c in zip(values5, counts)) % 5:
            return False
        if len({x for x, c in zip(values5, counts) if c}) < 2:
            return False
    return True


def search(depth):
    started = perf_counter()
    all_domains = domains()
    missing = set(range(len(all_domains)))
    records = {}
    queue = deque([(START, ())])
    seen = {START}
    inspected = 0
    while queue and missing:
        state, path = queue.popleft()
        inspected += 1
        for size in SIZES:
            for counts in block_choices(state, size):
                covered = [i for i in sorted(missing)
                           if qualifies(state, counts, size, all_domains[i])]
                for i in covered:
                    records[i] = {"domain": all_domains[i], "path": path,
                                  "size": size, "counts": counts}
                    missing.remove(i)
        if len(path) >= depth:
            continue
        for ids in choices(state):
            following = step(state, ids)
            if following not in seen:
                seen.add(following)
                queue.append((following, path+(ids,)))
    histogram = Counter(len(row["path"]) for row in records.values())
    print("B16 local bridge covered", len(records), "/", len(all_domains),
          "inspected", inspected, "generated", len(seen),
          "histogram", dict(sorted(histogram.items())), flush=True)
    print("missing", [all_domains[i] for i in sorted(missing)],
          "seconds", round(perf_counter()-started, 3))
    return {"depth": depth, "certificates": [records[i] for i in sorted(records)],
            "missing": [all_domains[i] for i in sorted(missing)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = search(args.depth)
    if args.output:
        args.output.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
