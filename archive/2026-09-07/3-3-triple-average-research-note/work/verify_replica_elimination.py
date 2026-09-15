"""Exact checks for the synchronized part of three-copy elimination.

This file deliberately does not search for arbitrary paths.  It checks four
interfaces that are useful for the open problem:

* a clean three-orbit macro descends to one genuine ternary average;
* orbit macros with a repeated original coordinate cannot preserve copy
  symmetry, for any ordering and offsets;
* cyclic symmetrization of a 3n-dimensional doubly stochastic certificate
  has a valid n-dimensional quotient, but this is only a matrix certificate;
* low-support states and the documented 5/6-point replicated examples have
  exact ternary network ledgers.
"""

from fractions import Fraction as F
from itertools import permutations, product
from random import Random


def average(state, selected):
    selected = tuple(selected)
    assert len(selected) == 3 and len(set(selected)) == 3
    mean = sum((state[i] for i in selected), F(0)) / 3
    result = list(state)
    for index in selected:
        result[index] = mean
    return tuple(result)


def lift(values):
    return tuple(value for value in values for _ in range(3))


def index(original, colour):
    return 3 * original + (colour % 3)


def copy_symmetric(state, n):
    return all(state[index(i, 0)] == state[index(i, 1)] == state[index(i, 2)]
               for i in range(n))


def project(state, n):
    assert copy_symmetric(state, n)
    return tuple(state[index(i, 0)] for i in range(n))


def clean_orbit_step(state, n, triple, offsets):
    """Apply one disjoint orbit and return the endpoint and lifted ledger."""
    i, j, k = triple
    assert len({i, j, k}) == 3
    a, b, d = offsets
    orbit = [
        (index(i, c + a), index(j, c + b), index(k, c + d))
        for c in range(3)
    ]
    assert all(len(set(move)) == 3 for move in orbit)
    assert len(set(sum((list(move) for move in orbit), []))) == 9
    assert copy_symmetric(state, n)
    endpoint = state
    for move in orbit:
        endpoint = average(endpoint, move)
    assert copy_symmetric(endpoint, n)
    base = project(state, n)
    expected = list(base)
    mean = sum((base[q] for q in triple), F(0)) / 3
    for q in triple:
        expected[q] = mean
    assert endpoint == lift(expected)
    return endpoint, tuple(orbit)


def check_clean_orbits():
    random = Random(20260910)
    checked = 0
    for n in range(7, 18):
        for _ in range(80):
            base = [F(random.randrange(-1000, 1001)) for _ in range(n - 1)]
            base.append(-sum(base, F(0)))
            state = lift(base)
            for _ in range(8):
                triple = tuple(random.sample(range(n), 3))
                offsets = tuple(random.randrange(3) for _ in range(3))
                state, ledger = clean_orbit_step(state, n, triple, offsets)
                checked += 1
    return checked


def coeff_average(state, selected):
    return average(state, selected)


def check_repeated_coordinate_obstruction():
    """A (2,1)-projection orbit never returns to copy symmetry.

    Coefficients are two-vectors, so this is a symbolic check in independent
    variables a and b rather than a finite numerical sample.
    """
    checked = 0
    for p, q, r in product(range(3), repeat=3):
        if p == q:
            continue
        orbit = [
            (index(0, c + p), index(0, c + q), index(1, c + r))
            for c in range(3)
        ]
        for order in permutations(range(3)):
            state = [[F(1), F(0)] for _ in range(3)]
            state.extend([[F(0), F(1)] for _ in range(3)])
            for position in order:
                selected = orbit[position]
                mean = [sum((state[i][coordinate] for i in selected), F(0)) / 3
                        for coordinate in range(2)]
                for i in selected:
                    state[i] = list(mean)
            assert not (state[0] == state[1] == state[2]
                        and state[3] == state[4] == state[5])
            checked += 1
    # The pattern with one i and two j is obtained by exchanging the labels.
    return 2 * checked


def identity_matrix(size):
    return [[F(int(i == j)) for j in range(size)] for i in range(size)]


def matrix_average(matrix, selected):
    result = [row[:] for row in matrix]
    for column in range(len(matrix)):
        mean = sum((matrix[i][column] for i in selected), F(0)) / 3
        for i in selected:
            result[i][column] = mean
    return result


def conjugate_copy_shift(matrix, n):
    size = 3 * n
    result = [[F(0) for _ in range(size)] for _ in range(size)]

    def shift(position):
        original, colour = divmod(position, 3)
        return index(original, colour + 1)

    for row in range(size):
        for column in range(size):
            result[shift(row)][shift(column)] = matrix[row][column]
    return result


def add_matrices(left, right):
    return [[a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(left, right)]


def scale_matrix(matrix, scalar):
    return [[scalar * value for value in row] for row in matrix]


def check_matrix_quotient():
    """Check the cyclic quotient on a genuine replicated zeroing path."""
    n = 7
    base = (F(-1), F(-1), F(2), F(0), F(0), F(0), F(0))
    state = lift(base)
    matrix = identity_matrix(3 * n)
    state, orbit = clean_orbit_step(state, n, (0, 1, 2), (0, 1, 2))
    for move in orbit:
        matrix = matrix_average(matrix, move)
    assert all(value == 0 for value in state)

    shifted = conjugate_copy_shift(matrix, n)
    shifted_twice = conjugate_copy_shift(shifted, n)
    sym = scale_matrix(add_matrices(add_matrices(matrix, shifted), shifted_twice), F(1, 3))

    size = 3 * n
    for row in range(size):
        assert sum(sym[row], F(0)) == 1
    for column in range(size):
        assert sum((sym[row][column] for row in range(size)), F(0)) == 1
    for row in range(size):
        for column in range(size):
            assert sym[index(row // 3, row % 3)][index(column // 3, column % 3)] == \
                sym[index(row // 3, (row % 3) + 1)][index(column // 3, (column % 3) + 1)]

    quotient = []
    for i in range(n):
        quotient.append([
            sum((sym[index(i, 0)][index(j, d)] for d in range(3)), F(0))
            for j in range(n)
        ])
    for row in quotient:
        assert sum(row, F(0)) == 1
    for j in range(n):
        assert sum((quotient[i][j] for i in range(n)), F(0)) == 1
    assert all(sum((quotient[i][j] * base[j] for j in range(n)), F(0)) == 0
               for i in range(n))
    return len(orbit), sum(value != 0 for row in quotient for value in row)


def equalize(state, indices, operations):
    if len(indices) == 1:
        return state
    assert len(indices) % 3 == 0
    third = len(indices) // 3
    chunks = [indices[offset * third:(offset + 1) * third]
              for offset in range(3)]
    for chunk in chunks:
        state = equalize(state, chunk, operations)
    for offset in range(third):
        selected = tuple(chunk[offset] for chunk in chunks)
        state = average(state, selected)
        operations.append(selected)
    return state


def check_zero_padded_support():
    random = Random(20260910)
    checked = 0
    # q=9; all samples have at most nine nonzero positions and n >= q.
    for n in range(9, 31):
        for _ in range(100):
            support_size = random.randrange(1, 10)
            support = random.sample(range(n), support_size)
            values = [F(0) for _ in range(n)]
            for position in support[:-1]:
                values[position] = F(random.randrange(-100, 101))
            values[support[-1]] = -sum(values, F(0))
            if values[support[-1]] == 0:
                values[support[-1]] = F(1)
                values[support[0]] -= 1
            actual_support = [i for i, value in enumerate(values) if value]
            block = actual_support + [i for i, value in enumerate(values)
                                      if not value][:9 - len(actual_support)]
            result = equalize(tuple(values), block, [])
            assert all(value == 0 for value in result)
            checked += 1
    return checked


def check_tripled_low_dimensional_paths():
    examples = [
        ((-3, 0, 1, 1, 1),
         ((0, 3, 4), (0, 5, 6), (3, 5, 7), (4, 6, 8)),
         (1, 2, 5, 9, 10, 11, 12, 13, 14)),
        ((-3, 0, 0, 1, 1, 1),
         ((0, 3, 4), (0, 5, 9), (3, 6, 10), (4, 7, 11)),
         (1, 2, 8, 12, 13, 14, 15, 16, 17)),
    ]
    checked = 0
    for base, prefix, block in examples:
        state = lift(tuple(F(value) for value in base))
        for selected in prefix:
            state = average(state, selected)
        operations = []
        state = equalize(state, block, operations)
        assert all(value == 0 for value in state)
        checked += len(prefix) + len(operations)
    return checked


def main():
    clean = check_clean_orbits()
    obstruction = check_repeated_coordinate_obstruction()
    quotient = check_matrix_quotient()
    padded = check_zero_padded_support()
    low_dimensional = check_tripled_low_dimensional_paths()
    print("clean synchronized orbit steps:", clean, "PASS")
    print("repeated-coordinate orbit orderings:", obstruction, "PASS")
    print("cyclic matrix quotient: orbit size", quotient[0],
          "nonzero quotient entries", quotient[1], "PASS")
    print("zero-padded support samples:", padded, "PASS")
    print("tripled 5/6-point exact path operations:", low_dimensional, "PASS")


if __name__ == "__main__":
    main()
