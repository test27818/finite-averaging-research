from math import gcd


def norm(u, v):
    d = gcd(abs(u), abs(v))
    u //= d; v //= d
    return (u, v) if (u > 0 or (u == 0 and v >= 0)) else (-u, -v)


def children(u, v):
    return [('A', norm(-3*v, u-v)), ('B', norm(u-v, -3*v))]


level = {norm(-1, 1): ("", 2)}
for d in range(1, 26):
    nxt = {}
    for (u, v), (word, _) in level.items():
        for op, child in children(u, v):
            nxt.setdefault(child, (word + op, 0))
    level = nxt
    best = min(level, key=lambda z: abs(z[0]) + abs(z[1]))
    word = level[best][0]
    print(d, best, abs(best[0])+abs(best[1]), word)
