"""Exact colored braid and longest-word operators for weighted blocks."""

from fractions import Fraction as F
from math import gcd


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def crossing(colors, values, index):
    a, b = colors[index:index + 2]
    x, y = values[index:index + 2]
    if a >= b:
        output = x, add(scale(F(a - b, a), x), scale(F(b, a), y))
    else:
        output = add(scale(F(b - a, b), y), scale(F(a, b), x)), y
    colors = list(colors)
    values = list(values)
    colors[index:index + 2] = b, a
    values[index:index + 2] = output
    return tuple(colors), tuple(values)


def longest_word(size):
    return tuple(index for stop in range(size - 1, 0, -1)
                 for index in range(stop))


def operator(colors, word):
    size = len(colors)
    values = tuple(tuple(F(i == j) for j in range(size)) for i in range(size))
    output_colors = tuple(colors)
    for index in word:
        output_colors, values = crossing(output_colors, values, index)
    # Return rows to the original color order.  Equal colors retain stable order.
    slots = {}
    for index, color in enumerate(output_colors):
        slots.setdefault(color, []).append(index)
    ordered = []
    used = {color: 0 for color in slots}
    for color in colors:
        index = slots[color][used[color]]
        used[color] += 1
        ordered.append(values[index])
    return tuple(ordered)


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(a)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def power(a, exponent):
    result = tuple(tuple(F(i == j) for j in range(len(a))) for i in range(len(a)))
    while exponent:
        if exponent & 1:
            result = multiply(a, result)
        a = multiply(a, a)
        exponent //= 2
    return result


def centered_scalar(matrix, colors):
    size = len(colors)
    basis = []
    for index in range(size - 1):
        vector = [F(0)] * size
        vector[index] = 1
        vector[-1] = -F(colors[index], colors[-1])
        basis.append(tuple(vector))
    ratio = None
    for vector in basis:
        image = tuple(sum(matrix[i][j] * vector[j] for j in range(size))
                      for i in range(size))
        for x, y in zip(vector, image):
            if x:
                candidate = y / x
                if ratio is None:
                    ratio = candidate
                elif candidate != ratio:
                    return None
            elif y:
                return None
    return ratio


def inspect(colors):
    word = longest_word(len(colors))
    matrix = operator(colors, word)
    hits = []
    for exponent in range(1, 2 * len(colors) + 1):
        scalar = centered_scalar(power(matrix, exponent), colors)
        if scalar is not None:
            hits.append((exponent, scalar))
            break
    return colors, word, matrix, hits


if __name__ == "__main__":
    for colors in (
        (9, 3, 1), (27, 3, 1), (27, 9, 1), (81, 9, 3),
        (27, 9, 3, 1), (81, 27, 3, 1), (81, 9, 3, 1),
        (81, 27, 9, 3, 1), (243, 81, 9, 3, 1),
    ):
        print(inspect(colors))
