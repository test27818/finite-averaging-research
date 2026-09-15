"""Exact checks for the (s^2,s,1) cyclotomic macro family."""

from fractions import Fraction as F
from math import gcd


def primitive(matrix):
    divisor = gcd(*(abs(value) for value in matrix))
    result = tuple(value // divisor for value in matrix)
    if next(value for value in result if value) < 0:
        result = tuple(-value for value in result)
    return result


def multiply(left, right):
    a, b, c, d = left
    e, f, g, h = right
    return primitive((a * e + b * g, a * f + b * h,
                      c * e + d * g, c * f + d * h))


def determinant(matrix):
    a, b, c, d = matrix
    return a * d - b * c


def inverse(matrix):
    a, b, c, d = matrix
    return primitive((d, -b, -c, a))


def core(r, s, u, v):
    return [u] * r + [v] * s + [-r * u - s * v]


def average(state, indices):
    value = sum((state[index] for index in indices), F(0)) / 3
    for index in indices:
        state[index] = value


def expand_singleton_block(state, distinguished, repeated, block_size):
    """Expand one value with two repeated values until block_size copies exist."""
    block = [distinguished]
    available = list(repeated)
    while len(block) < block_size:
        next_block = []
        for left in block:
            pair = [available.pop(), available.pop()]
            average(state, [left] + pair)
            next_block.extend([left] + pair)
        block = next_block
    assert len(block) == block_size
    assert not available
    return state[block[0]]


def check_macro(r, s):
    u, v = F(2), F(-5)
    values = core(r, s, u, v)
    # A_s: consume s-1 v's with the singleton, leave one old v.
    singleton = r + s
    v_positions = list(range(r, r + s))
    output = expand_singleton_block(values, singleton, v_positions[:-1], s)
    assert output == F(-r * u - v, s)
    assert sorted(values) == sorted(core(r, s, u, output))

    values = core(r, s, u, v)
    singleton = r + s
    u_positions = list(range(r))
    output = expand_singleton_block(values, singleton, u_positions[:-1], r)
    assert output == F(-u - s * v, r)
    assert sorted(values) == sorted(core(r, s, output, v))

    # R_{r/s}: expand each of the s v-values uniformly to r copies.
    values = core(r, s, u, v)
    u_positions = list(range(r))
    current = list(range(r, r + s))
    available = u_positions[:r - s]
    level = s
    while level < r:
        next_current = []
        for position in current:
            pair = [available.pop(), available.pop()]
            average(values, [position] + pair)
            next_current.extend([position, pair[0], pair[1]])
        current = next_current
        level = len(current)
    assert not available
    target = F((r - s) * u + s * v, r)
    assert all(values[position] == target for position in current)
    remaining = [values[index] for index in range(r + s + 1)
                 if index not in current]
    assert sorted(remaining) == sorted([u] * s + [-r * target - s * u])
    assert len(current) == r
    return (r - 1) // 2, (s - 1) // 2, (r - s) // 2


def check_group(s):
    a = (s, 0, -s * s, -1)
    r = (s - 1, 1, s, 0)
    b = (1, s, 0, -s * s)
    c = primitive((a[0] * r[0] + a[1] * r[2],
                   a[0] * r[1] + a[1] * r[3],
                   a[2] * r[0] + a[3] * r[2],
                   a[2] * r[1] + a[3] * r[3]))
    assert c == (s - 1, 1, -s * s + s - 1, -s)
    assert multiply(c, multiply(c, c)) == (1, 0, 0, 1)
    assert multiply(b, multiply(inverse(c), b)) == c
    assert determinant(c) == 1
    return a, r, b, c


if __name__ == "__main__":
    total = 0
    for k in range(1, 4):
        s = 3 ** k
        r = s * s
        counts = check_macro(r, s)
        check_group(s)
        total += 1
        print("s", s, "n", r + s + 1, "operation counts", counts,
              "group identities: PASS")
    print("cyclotomic macro family checks: PASS", total)
