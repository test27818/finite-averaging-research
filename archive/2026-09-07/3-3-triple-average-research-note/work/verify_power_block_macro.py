"""Exact checks for the n-4=3^k return macro."""

from collections import Counter
from fractions import Fraction as F


def average(values, selected):
    mean = sum((values[index] for index in selected), F(0)) / 3
    result = list(values)
    for index in selected:
        result[index] = mean
    return tuple(result)


def macro(k):
    m = 3 ** k
    n = m + 4
    u, v = F(2), F(-1)
    w = -m * u - 3 * v
    values = [u] * m + [v] * 3 + [w]
    operations = 0
    block = [index for index in range(m, m + 3)]
    next_u = list(range(m))
    a = v
    for j in range(1, k):
        old_block = block
        new_block = []
        for _ in range(3 ** j):
            u_indices = [index for index in next_u[:2]]
            next_u = next_u[2:]
            selected = (old_block.pop(), u_indices[0], u_indices[1])
            values = average(values, selected)
            new_block.extend(selected)
            operations += 1
        block = new_block
        a = (a + 2 * u) / 3
        assert all(values[index] == a for index in block)
    assert Counter(values).most_common(1)[0][1] == m
    assert operations == (m - 3) // 2
    target = tuple(sorted([a] * m + [u] * 3 + [-m * a - 3 * u]))
    assert tuple(sorted(values)) == target
    return n, operations


if __name__ == "__main__":
    for k in range(1, 6):
        print("n", macro(k)[0], "operations", macro(k)[1])
    print("power-block macro checks: PASS")
