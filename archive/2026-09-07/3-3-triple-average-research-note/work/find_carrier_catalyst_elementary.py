"""Meet-in-the-middle standard elementary roots in the catalyst group."""

from itertools import product as words

from verify_carrier_sweep_catalyst import I3, evaluate, round_determinant
from explore_carrier_sweep_relations import product, unipotent_rank_one


def inverse_integer(matrix):
    assert round_determinant(matrix) == 1
    a, b, c = matrix
    return (
        (b[1] * c[2] - b[2] * c[1],
         a[2] * c[1] - a[1] * c[2],
         a[1] * b[2] - a[2] * b[1]),
        (b[2] * c[0] - b[0] * c[2],
         a[0] * c[2] - a[2] * c[0],
         a[2] * b[0] - a[0] * b[2]),
        (b[0] * c[1] - b[1] * c[0],
         a[1] * c[0] - a[0] * c[1],
         a[0] * b[1] - a[1] * b[0]),
    )


def generators():
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    result = []
    certificates = []
    for matrix, certificate in roots.items():
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            result.append(matrix)
            certificates.append(certificate)
    assert len(result) == 12
    return tuple(result), tuple(certificates)


def products_exact(generators_, length):
    result = {}
    for word in words(range(len(generators_)), repeat=length):
        matrix = I3
        for letter in word:
            matrix = product(generators_[letter], matrix)
        result.setdefault(matrix, word)
    return result


def find(half_depth=4):
    generators_, certificates = generators()
    forward = products_exact(generators_, half_depth)
    suffixes = []
    for suffix in words(range(len(generators_)), repeat=half_depth):
        matrix = I3
        for letter in suffix:
            matrix = product(generators_[letter], matrix)
        suffixes.append((suffix, inverse_integer(matrix)))
    found = {}
    for row in range(3):
        for column in range(3):
            if row == column:
                continue
            for level in (10, 20, 40, 80, 160):
                target = [list(values) for values in I3]
                target[row][column] = level
                target = tuple(map(tuple, target))
                for suffix, suffix_inverse in suffixes:
                    required = product(suffix_inverse, target)
                    prefix = forward.get(required)
                    if prefix is not None:
                        candidate = prefix + suffix
                        matrix = I3
                        for letter in candidate:
                            matrix = product(generators_[letter], matrix)
                        assert matrix == target
                        found[(row, column, level)] = candidate
                        break
    for target, word in sorted(found.items()):
        print(target, word, tuple(certificates[index] for index in word))
    print("standard elementary targets", len(found), "/ 30")


if __name__ == "__main__":
    find()
