from math import gcd


def inverse_cascade(k, u, v):
    """Inverse of a length-k cascade whose next state is (u, v)."""
    a = (-1) ** k * 3**k
    gamma = (a - 1) // 4
    return a * v, u + gamma * v


def step(u, v):
    if u and u % 3 == 0 and v % 3:
        q = u // 3
        return v - q, -q
    if v and v % 3 == 0 and u % 3:
        q = v // 3
        return u - q, -q
    return None


def cascade(u, v):
    result = step(u, v)
    if result is None:
        return None
    u, v = result
    length = 1
    while v and v % 3 == 0:
        u, v = step(u, v)
        length += 1
    return u, v, length


def trace(u, v):
    lengths = []
    while u + v:
        result = cascade(u, v)
        if result is None:
            return None
        u, v, length = result
        lengths.append(length)
    return lengths


levels = [{(1, -1): ()}]
for cost in range(1, 19):
    level = {}
    for k in range(1, cost + 1):
        for state, tail in levels[cost - k].items():
            start = inverse_cascade(k, *state)
            level[start] = (k,) + tail
    levels.append(level)

    for start, word in level.items():
        assert gcd(abs(start[0]), abs(start[1])) == 1
        assert trace(*start) == list(word)

    best = min(level, key=lambda pair: max(abs(pair[0]), abs(pair[1])))
    print(cost, len(level), max(abs(best[0]), abs(best[1])), level[best])
