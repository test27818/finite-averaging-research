from __future__ import annotations

from math import gcd


def norm(u: int, v: int) -> tuple[int, int]:
    d = gcd(abs(u), abs(v))
    u //= d
    v //= d
    return (u, v) if (u > 0 or (u == 0 and v >= 0)) else (-u, -v)


def children(u: int, v: int):
    # Inverses of the two unnormalised A/B maps.
    for a, b in ((-3 * v, u - v), (u - v, -3 * v)):
        yield norm(a, b)


def forward(u: int, v: int):
    if u + v == 0:
        return None
    if u % 3 == 0 and u != 0 and v % 3:
        return norm(v - u // 3, -u // 3)
    if v % 3 == 0 and v != 0 and u % 3:
        return norm(u - v // 3, -v // 3)
    return None


level = {norm(-1, 1)}
seen = set(level)
for d in range(1, 31):
    nxt = set()
    for state in level:
        for child in children(*state):
            if forward(*child) == state:
                nxt.add(child)
    level = nxt
    fresh = level - seen
    seen |= level
    if not level:
        break
    mins = min(max(abs(u), abs(v)) for u, v in level)
    minfresh = min((max(abs(u), abs(v)) for u, v in fresh), default=None)
    print(d, len(level), len(fresh), mins, minfresh)
