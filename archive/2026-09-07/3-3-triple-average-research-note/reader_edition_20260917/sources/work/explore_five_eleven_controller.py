"""Small exact controller experiment on explicit two-atom return formulas.

This explores a fixed ten-letter alphabet, not arbitrary averaging words.
"""

from collections import Counter
from itertools import product
from math import gcd


def mul(a, b):
    x, y, z, t = a
    u, v, w, h = b
    return x * u + y * w, x * v + y * h, z * u + t * w, z * v + t * h


def primitive(matrix):
    g = gcd(*matrix)
    result = tuple(x // g for x in matrix)
    first = next(x for x in result if x)
    return tuple(-x for x in result) if first < 0 else result


def determinant(matrix):
    a, b, c, d = matrix
    return a * d - b * c


def period(matrix):
    a, b, c, d = matrix
    if b == c == 0 and a == d:
        return 1
    trace = a + d
    det = determinant(matrix)
    if trace == 0:
        return 2
    if det > 0:
        return {det: 3, 2 * det: 4, 3 * det: 6}.get(trace * trace)
    return None


SWAP = (0, 1, 1, 0)
LETTERS = {}
for j in range(1, 6):
    matrix = (j - 6, -j, 5 - j, j)
    LETTERS[str(j)] = primitive(matrix)
    LETTERS[str(j) + 's'] = primitive(mul(SWAP, matrix))


def main():
    cycles = []
    current = {(1, 0, 0, 1): ()}
    seen = dict(current)
    for length in range(1, 5):
        following = {}
        for matrix, word in current.items():
            for label, letter in LETTERS.items():
                after = primitive(mul(letter, matrix))
                if after in seen or after in following:
                    continue
                extended = word + (label,)
                following[after] = extended
                order = period(after)
                if order:
                    cycles.append((extended, order, after))
        seen.update(following)
        current = following
        print('length', length, 'new', len(following), 'cycles', len(cycles), flush=True)
    for item in cycles[:45]:
        print('finite-order', item)
    # Rotating a positive scalar cycle gives a positive inverse for every
    # letter appearing in it, without a prior inverse for the other letters.
    unlocked = {x.replace('s', '') for word, _, _ in cycles for x in word}
    print('invertible letters from cycles:', sorted(unlocked))


if __name__ == '__main__':
    main()
