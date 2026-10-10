"""Exact checks for the zero-padding ternary block theorem."""

from fractions import Fraction as F
from random import Random


def average(values, selected):
    mean = sum((values[index] for index in selected), F(0)) / 3
    result = list(values)
    for index in selected:
        result[index] = mean
    return tuple(result)


def equalize(values, indices, operations):
    if len(indices) == 1:
        return values
    third = len(indices) // 3
    chunks = [
        indices[offset * third:(offset + 1) * third]
        for offset in range(3)
    ]
    for chunk in chunks:
        values = equalize(values, chunk, operations)
    for offset in range(third):
        selected = tuple(chunk[offset] for chunk in chunks)
        values = average(values, selected)
        operations.append(selected)
    return values


def largest_power_three(n):
    q = 1
    while 3 * q <= n:
        q *= 3
    return q


def verify():
    random = Random(20260908)
    checked = 0
    for n in range(3, 100):
        q = largest_power_three(n)
        for _ in range(100):
            if q < 3:
                continue
            r = random.randrange(2, q + 1)
            nonzero = random.sample(range(n), r)
            values = [F(0)] * n
            for index in nonzero[:-1]:
                values[index] = F(random.randrange(-50, 51))
                if values[index] == 0:
                    values[index] = F(1)
            values[nonzero[-1]] = -sum(values, F(0))
            if values[nonzero[-1]] == 0:
                values[nonzero[-1]] = F(1)
                values[nonzero[0]] -= 1
            nonzero = [index for index, value in enumerate(values) if value]
            r = len(nonzero)
            assert r <= q
            block_size = 1
            while block_size < r:
                block_size *= 3
            zeros = [index for index, value in enumerate(values) if not value]
            block = nonzero + zeros[:block_size - r]
            operations = []
            result = equalize(tuple(values), block, operations)
            assert result == tuple(F(0) for _ in range(n))
            exponent = 0
            layer = block_size
            while layer > 1:
                layer //= 3
                exponent += 1
            assert len(operations) == exponent * block_size // 3
            checked += 1
    return checked


if __name__ == "__main__":
    print("zero-padding theorem checks: PASS", verify())
