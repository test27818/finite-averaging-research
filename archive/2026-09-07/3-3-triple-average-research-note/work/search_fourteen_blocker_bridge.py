"""Finite mod-8/mod-7 bridge search for two disjoint dangerous pairs.

The mod-7 main value is translated to 0 and its two exceptions scaled to
+/-1. Mod-8 values are unscaled. This preserves exactly the tests used by
the local twelve-point call and the output B14 legality.
"""

from collections import Counter, deque
from itertools import product, combinations_with_replacement
from time import perf_counter
import argparse
import json
from pathlib import Path


MODULUS = 56
INV3 = 19


def crt(res8, res7):
    return (res8+8*((res7-res8) % 7)) % 56


def initial_patterns():
    patterns = []
    for u in range(8):
        opposite = [x for x in range(8) if x % 2 != u % 2]
        same = [x for x in range(8) if x % 2 == u % 2]
        for b, bp, c, cp in product(opposite, opposite, same, same):
            if (10*u+b+bp+c+cp) % 8:
                continue
            patterns.append((u, b, bp, c, cp))
    return patterns


def initial_state(pattern):
    u, b, bp, c, cp = pattern
    values = [crt(u, 0)]*10+[crt(b, 0), crt(bp, 0), crt(c, 1), crt(cp, -1)]
    return tuple(sorted(Counter(values).items()))


def choices(state):
    for indices in combinations_with_replacement(range(len(state)), 3):
        i, j, k = indices
        if i == k or (i == j and state[i][1] < 2) or (j == k and state[j][1] < 2):
            continue
        yield tuple(state[index][0] for index in indices)


def step(state, triple):
    following = dict(state)
    for value in triple:
        if following.get(value, 0) < 1:
            raise ValueError("not enough residue representatives")
        following[value] -= 1
        if following[value] == 0:
            del following[value]
    mean = sum(triple)*INV3 % MODULUS
    following[mean] = following.get(mean, 0)+3
    return tuple(sorted(following.items()))


def terminal_pair(state):
    parity = [sum(count for x, count in state if x % 2 == bit) for bit in (0, 1)]
    for i, (x, cx) in enumerate(state):
        for y, cy in state[i:]:
            if (x-y) % 7 == 0 or (5*x+y) % 8 != 4:
                continue
            left = list(parity)
            left[x % 2] -= 1
            left[y % 2] -= 1
            if min(left) >= 1:
                return x, y
    return None


def search_state(start, depth):
    queue = deque([(start, ())])
    seen = {start}
    while queue:
        state, path = queue.popleft()
        pair = terminal_pair(state)
        if pair is not None:
            return path, pair, len(seen)
        if len(path) >= depth:
            continue
        for triple in choices(state):
            following = step(state, triple)
            if following not in seen:
                seen.add(following)
                queue.append((following, path+(triple,)))
    return None, None, len(seen)


def examine(depth):
    started = perf_counter()
    cache = {}
    result, missing = [], []
    histogram = Counter()
    for pattern in initial_patterns():
        start = initial_state(pattern)
        if start not in cache:
            cache[start] = search_state(start, depth)
        path, pair, count = cache[start]
        if path is None:
            missing.append(pattern)
        else:
            histogram[len(path)] += 1
            result.append({"pattern": pattern, "path": path, "omitted": pair})
    print("patterns", len(initial_patterns()), "unique starts", len(cache),
          "covered", len(result), "missing", len(missing),
          "histogram", dict(sorted(histogram.items())), flush=True)
    print("missing sample", missing[:12], "seconds", round(perf_counter()-started, 3))
    return {"depth": depth, "certificates": result, "missing": missing}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=2)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = examine(args.depth)
    if args.output:
        args.output.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
