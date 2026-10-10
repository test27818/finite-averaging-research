"""Exact structural checks for the rank-three carrier-sweep catalyst."""

from fractions import Fraction as F
from itertools import permutations, product as words
from math import gcd

from explore_carrier_sweep_relations import (
    normalized, product, unipotent_rank_one,
)
from explore_carrier_sweep_smith import content, identity, multiply, word


ORDERS = tuple(permutations(range(3)))
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def evaluate(sequence, boundary=False):
    size = 3 + int(boundary)
    result = tuple(tuple(int(i == j) for j in range(size))
                   for i in range(size))
    for index in sequence:
        result = product(normalized(3, ORDERS[index], boundary), result)
    return result


def outer_factor(matrix):
    delta = [[matrix[i][j] - int(i == j) for j in range(3)]
             for i in range(3)]
    column = next(j for j in range(3) if any(delta[i][j] for i in range(3)))
    u = [delta[i][column] for i in range(3)]
    divisor = gcd(*(abs(value) for value in u))
    u = [value // divisor for value in u]
    pivot = next(i for i, value in enumerate(u) if value)
    f = [delta[pivot][j] // u[pivot] for j in range(3)]
    assert delta == [[u[i] * f[j] for j in range(3)] for i in range(3)]
    assert sum(u[i] * f[i] for i in range(3)) == 0
    return tuple(u), tuple(f)


def flatten(matrix):
    return tuple(F(value) for row in matrix for value in row)


def matrix_add(a, b, coefficient=1):
    return tuple(tuple(a[i][j] + coefficient * b[i][j]
                       for j in range(3)) for i in range(3))


def commutator_linear(a, b):
    return matrix_add(product(a, b), product(b, a), -1)


def rank(vectors):
    rows = [list(map(F, vector)) for vector in vectors]
    if not rows:
        return 0
    columns = len(rows[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, len(rows))
                      if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][column]
        rows[pivot_row] = [entry / value for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            value = rows[row][column]
            rows[row] = [x - value * y
                         for x, y in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def sweep_formula(rank):
    expected = [[0] * rank for _ in range(rank)]
    for i in range(rank):
        if i < rank - 1:
            expected[i][i] = 2
            if i:
                expected[i][i - 1] = 1
            expected[i][-1] = -3
        else:
            if rank > 1:
                expected[i][i - 1] = 1
            expected[i][i] = -1
    matrix = word(rank, tuple(range(rank)))
    assert content(matrix) == 3 ** (rank - 1)
    actual = [[value // 3 ** (rank - 1) for value in row]
              for row in matrix]
    assert actual == expected
    return actual


def verify_sweeps():
    for rank in range(2, 13):
        matrix = sweep_formula(rank)
        determinant = round_determinant(matrix)
        assert determinant == (-1) ** rank
        trace = sum(matrix[i][i] for i in range(rank))
        assert trace == 2 * rank - 3
    matrix = sweep_formula(2)
    cube = multiply(matrix, multiply(matrix, matrix))
    assert cube == [[-int(i == j) for j in range(2)] for i in range(2)]
    print("all-r integral carrier sweep and finite-order rank-two boundary: PASS 11")


def round_determinant(matrix):
    work = [list(map(F, row)) for row in matrix]
    result = F(1)
    for column in range(len(work)):
        pivot = next(row for row in range(column, len(work))
                     if work[row][column])
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        for row in range(column + 1, len(work)):
            ratio = work[row][column] / value
            for j in range(column + 1, len(work)):
                work[row][j] -= ratio * work[column][j]
    assert result.denominator == 1
    return int(result)


def verify_rank_three_roots():
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    assert len(roots) == 24
    inverse_count = 0
    nilpotents = []
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            inverse_count += 1
        u, f = outer_factor(matrix)
        nilpotents.append(tuple(tuple(u[i] * f[j] for j in range(3))
                                for i in range(3)))
    assert inverse_count == 12

    # The balanced inverse pairs contain opposite width-four roots on A2.
    upper = evaluate((0, 3, 5, 2))
    upper_inverse = evaluate((1, 5, 3, 4))
    lower = evaluate((4, 0, 2, 1))
    lower_inverse = evaluate((5, 2, 0, 3))
    assert product(upper, upper_inverse) == I3
    assert product(lower, lower_inverse) == I3
    assert upper == ((1, 0, 0), (-2, 3, 2), (2, -2, -1))
    assert lower == ((3, 2, -2), (-2, -1, 2), (0, 0, 1))

    paired_nilpotents = []
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            u, f = outer_factor(matrix)
            paired_nilpotents.append(
                tuple(tuple(u[i] * f[j] for j in range(3))
                      for i in range(3))
            )

    # The positively invertible half already has full sl3 Lie closure.
    basis = list(paired_nilpotents)
    old_rank = 0
    while True:
        current_rank = rank([flatten(matrix) for matrix in basis])
        if current_rank == old_rank:
            break
        old_rank = current_rank
        snapshot = basis[:]
        for a in snapshot:
            for b in paired_nilpotents:
                basis.append(commutator_linear(a, b))
    assert old_rank == 8

    paired_factors = []
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            paired_factors.append(outer_factor(matrix))
            assert all((sum(matrix[i][j] for i in range(3)) - 1) % 5 == 0
                       for j in range(3))
            assert all((matrix[i][j] - int(i == j)) % 2 == 0
                       for i in range(3) for j in range(3))
    direction_lines = {}
    covector_lines = {}
    for u, f in paired_factors:
        if next(value for value in u if value) < 0:
            u = tuple(-value for value in u)
        divisor = gcd(*(abs(value) for value in f))
        f0 = tuple(value // divisor for value in f)
        if next(value for value in f0 if value) < 0:
            f0 = tuple(-value for value in f0)
        direction_lines[u] = True
        covector_lines[f0] = divisor
    directions = tuple(direction_lines)
    covectors = tuple(tuple(divisor * value for value in f)
                       for f, divisor in covector_lines.items())
    assert len(directions) == len(covectors) == 6
    direction_index = gcd(*(abs(det3(rows)) for rows in combinations3(directions)
                            if det3(rows)))
    covector_index = gcd(*(abs(det3(rows)) for rows in combinations3(covectors)
                           if det3(rows)))
    assert direction_index == 5 and covector_index == 32
    print("rank-three positive unipotents and same-length inverse pairs: PASS", len(roots), inverse_count)
    print("carrier-sweep tangent Lie algebra equals sl3: PASS", old_rank)
    print("root direction and covector lattice indices: PASS", direction_index, covector_index)


def combinations3(values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            for k in range(j + 1, len(values)):
                yield values[i], values[j], values[k]


def det3(rows):
    a, b, c = rows
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def verify_local_collision_orbits():
    modulus = 20
    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    generators = []
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            generators.append(matrix)
    for index in range(3):
        matrix = [list(row) for row in I3]
        matrix[index][index] = -pow(3, -1, modulus)
        for row in range(3):
            if row != index:
                matrix[row][index] = -1
        generators.append(tuple(map(tuple, matrix)))

    def apply(matrix, vector):
        return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) % modulus
                     for i in range(3))

    def terminal(vector):
        return (any(value == 0 for value in vector)
                or any(vector[i] == vector[j]
                       for i in range(3) for j in range(i)))

    remaining = {
        vector for vector in words(range(modulus), repeat=3)
        if gcd(modulus, *vector) == 1
    }
    orbit_count = 0
    while remaining:
        seed = next(iter(remaining))
        orbit = {seed}
        frontier = [seed]
        while frontier:
            vector = frontier.pop()
            for matrix in generators:
                output = apply(matrix, vector)
                if output not in orbit:
                    orbit.add(output)
                    frontier.append(output)
        assert any(terminal(vector) for vector in orbit)
        remaining -= orbit
        orbit_count += 1
    assert orbit_count == 15
    print("root-plus-carrier mod20 collision orbits: PASS", orbit_count)


def verify_local_tangent_lifts():
    from weighted_local_tangent import tangent_rank

    roots = {}
    for sequence in words(range(6), repeat=4):
        matrix = evaluate(sequence)
        if unipotent_rank_one(matrix):
            roots.setdefault(matrix, sequence)
    generators = []
    for matrix in roots:
        inverse = tuple(tuple(2 * int(i == j) - matrix[i][j]
                              for j in range(3)) for i in range(3))
        if inverse in roots:
            generators.append(matrix)
    assert tangent_rank(generators, 5, 5) == (3000, 5)
    assert tangent_rank(generators, 8, 2) == (128, 8)
    assert tangent_rank(generators, 16, 2) == (32768, 8)
    print("local stabilizer tangent ranks at5,8,16: PASS 5 8 8")


def inverse_unipotent(matrix):
    return tuple(tuple(2 * int(i == j) - matrix[i][j]
                       for j in range(3)) for i in range(3))


def conjugate(generator, root):
    return product(generator, product(root, inverse_unipotent(generator)))


def unipotent_power(matrix, exponent):
    return tuple(tuple(int(i == j)
                       + exponent * (matrix[i][j] - int(i == j))
                       for j in range(3)) for i in range(3))


def inverse_matrix(matrix):
    work = [list(map(F, row)) + [F(i == j) for j in range(3)]
            for i, row in enumerate(matrix)]
    for column in range(3):
        pivot = next(row for row in range(column, 3) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(3):
            if row == column:
                continue
            value = work[row][column]
            work[row] = [x - value * y
                         for x, y in zip(work[row], work[column])]
    return tuple(tuple(entry for entry in row[3:]) for row in work)


def elementary(row, column, value):
    matrix = [list(values) for values in I3]
    matrix[row][column] = value
    return tuple(map(tuple, matrix))


def verify_arithmeticity_certificate():
    root = evaluate
    direction_one = conjugate(
        root((3, 4, 1, 5)),
        conjugate(root((5, 2, 0, 3)), root((0, 3, 2, 1))),
    )
    direction_two = conjugate(root((0, 3, 5, 2)), root((0, 3, 2, 1)))
    kernel_one = conjugate(
        root((4, 0, 1, 5)),
        conjugate(root((1, 5, 4, 0)), root((0, 3, 5, 2))),
    )
    kernel_two = conjugate(root((0, 3, 2, 1)), root((0, 3, 5, 2)))

    assert outer_factor(direction_one) == ((-2, -3, 0), (60, -40, 36))
    assert outer_factor(direction_two) == ((-2, -3, 0), (12, -8, -12))
    assert outer_factor(kernel_one) == ((32, 57, 51), (6, 2, -6))
    assert outer_factor(kernel_two) == ((-8, -3, -9), (6, 2, -6))

    basis = ((2, 1, 1), (3, -3, 0), (0, 0, 1))
    basis_inverse = inverse_matrix(basis)

    def change(matrix):
        return product(basis_inverse, product(matrix, basis))

    assert change(direction_two) == elementary(0, 1, -36)
    upper_thirteen = product(direction_one,
                             unipotent_power(direction_two, -5))
    assert change(upper_thirteen) == elementary(0, 2, -96)
    lower_thirty_one = product(kernel_one,
                               unipotent_power(kernel_two, 19))
    assert change(lower_thirty_one) == elementary(2, 0, -2160)
    lower_twenty_one = product(unipotent_power(kernel_one, 3),
                               unipotent_power(kernel_two, 17))
    assert change(lower_twenty_one) == elementary(1, 0, -720)

    level = 4320
    roots_at_level = {
        (0, 1): unipotent_power(change(direction_two), -level // 36),
        (0, 2): unipotent_power(change(upper_thirteen), -level // 96),
        (1, 0): unipotent_power(change(lower_twenty_one), -level // 720),
        (2, 0): unipotent_power(change(lower_thirty_one), -level // 2160),
    }
    assert all(matrix == elementary(i, j, level)
               for (i, j), matrix in roots_at_level.items())

    def group_commutator(a, b):
        return product(a, product(b, product(inverse_unipotent(a),
                                             inverse_unipotent(b))))

    root_23 = group_commutator(roots_at_level[(1, 0)],
                               roots_at_level[(0, 2)])
    root_32 = group_commutator(roots_at_level[(2, 0)],
                               roots_at_level[(0, 1)])
    assert root_23 == elementary(1, 2, level * level)
    assert root_32 == elementary(2, 1, level * level)
    print("explicit opposite horospheres and E3 principal level: PASS",
          level * level)


def verify_boundary_form():
    sequence = (0, 3, 5, 2)
    inverse_sequence = (1, 5, 3, 4)
    matrix = evaluate(sequence, boundary=True)
    inverse_matrix = evaluate(inverse_sequence, boundary=True)
    assert tuple(tuple(value for value in row[:3]) for row in matrix[:3]) == evaluate(sequence)
    assert matrix[-1] == (-24, -24, -24, 81)
    assert inverse_matrix[-1] == (-24, -24, -24, 81)
    combined = product(matrix, inverse_matrix)
    assert combined[:3] == ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0))
    assert combined[-1] == (-1968, -1968, -1968, 6561)
    print("second-carrier obstruction is a one-dimensional boundary cocycle: PASS")


if __name__ == "__main__":
    verify_sweeps()
    verify_rank_three_roots()
    verify_boundary_form()
    verify_local_collision_orbits()
    verify_local_tangent_lifts()
    verify_arithmeticity_certificate()
