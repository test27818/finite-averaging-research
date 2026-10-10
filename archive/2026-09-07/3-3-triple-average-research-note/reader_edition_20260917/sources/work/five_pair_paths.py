from functools import lru_cache
from math import gcd


def norm(u, v):
    d = gcd(abs(u), abs(v))
    if not d:
        return (0, 0)
    u //= d
    v //= d
    # global sign is immaterial; retain a deterministic representative
    return (u, v) if (u > 0 or (u == 0 and v >= 0)) else (-u, -v)


def transitions(u, v):
    raw = {
        "A": (-u + 3 * v, -u),
        "B": (3 * u - v, -v),
        "C": (-u - v, -u - v),
    }
    for op, pair in raw.items():
        yield op, norm(*pair)


@lru_cache(None)
def solve(u, v, depth):
    if u + v == 0:
        return ""
    if depth == 0:
        return None
    for op, (x, y) in transitions(u, v):
        if (x, y) == (u, v):
            continue
        tail = solve(x, y, depth - 1)
        if tail is not None:
            return op + tail
    return None


for B in [10, 30, 100]:
    found = []
    total = 0
    for u in range(-B, B + 1):
        for v in range(-B, B + 1):
            if (u, v) == (0, 0) or gcd(abs(u), abs(v)) != 1:
                continue
            path = solve(*norm(u, v), depth=18)
            if path is not None:
                total += 1
                if "C" in path:
                    found.append((u, v, path))
    print("B", B, "success", total, "with-C", found[:20], "count", len(found), flush=True)
