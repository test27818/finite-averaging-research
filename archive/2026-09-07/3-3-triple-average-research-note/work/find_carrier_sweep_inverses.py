"""Meet-in-the-middle positive inverse certificates for rank-three sweeps."""

from fractions import Fraction as F
from itertools import permutations, product as words

from explore_carrier_sweep_relations import normalized, product


def inverse(matrix):
    size = len(matrix)
    work = [list(map(F, row)) + [F(i == j) for j in range(size)]
            for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(row for row in range(column, size)
                     if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(size):
            if row == column:
                continue
            value = work[row][column]
            work[row] = [x - value * y
                         for x, y in zip(work[row], work[column])]
    result = tuple(tuple(entry for entry in row[size:]) for row in work)
    assert all(entry.denominator == 1 for row in result for entry in row)
    return tuple(tuple(int(entry) for entry in row) for row in result)


def evaluate(generators, word):
    size = len(generators[0])
    result = tuple(tuple(int(i == j) for j in range(size))
                   for i in range(size))
    for letter in word:
        result = product(generators[letter], result)
    return result


def products_exact(generators, length):
    result = {}
    for word in words(range(len(generators)), repeat=length):
        result.setdefault(evaluate(generators, word), word)
    return result


def find_inverse_words(half_depth=4):
    orders = tuple(permutations(range(3)))
    generators = tuple(normalized(3, order) for order in orders)
    inverses = tuple(inverse(generator) for generator in generators)
    forward = products_exact(generators, half_depth)
    certificates = []
    for index, target in enumerate(inverses):
        found = None
        # evaluate(prefix + suffix) is R A because each new letter acts on
        # the left.  Thus R A=target exactly when A=R^{-1} target.
        for suffix in words(range(len(generators)), repeat=half_depth):
            suffix_matrix = evaluate(generators, suffix)
            required = product(inverse(suffix_matrix), target)
            prefix = forward.get(required)
            if prefix is not None:
                candidate = prefix + suffix
                assert evaluate(generators, candidate) == target
                found = candidate
                break
        certificates.append((index, orders[index], found))
    return generators, certificates


if __name__ == "__main__":
    generators, certificates = find_inverse_words()
    for row in certificates:
        print(row)
    assert all(word is not None for _, _, word in certificates)
    print("rank-three carrier-sweep positive inverses: PASS", len(certificates))
