"""Finite Hecke-algebra and matrix identities, not an automorphic interface.

The final audit distinguishes these exact identities from the unconstructed
classical T_3, Ihara and modular-symbol interpretations.
"""

from fractions import Fraction as F
from math import gcd


def identity(size):
    return tuple(tuple(F(row == column) for column in range(size))
                 for row in range(size))


def add(left, right, scale=1):
    return tuple(tuple(left[row][column] + scale * right[row][column]
                       for column in range(len(left)))
                 for row in range(len(left)))


def scalar(matrix, value):
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def multiply(left, right):
    return tuple(tuple(sum(left[row][index] * right[index][column]
                           for index in range(len(right)))
                       for column in range(len(right[0])))
                 for row in range(len(left)))


def burau(strands, index, parameter):
    matrix = [list(row) for row in identity(strands)]
    matrix[index][index] = F(parameter - 1, parameter)
    matrix[index][index + 1] = F(1, parameter)
    matrix[index + 1][index] = F(1)
    matrix[index + 1][index + 1] = F(0)
    return tuple(tuple(row) for row in matrix)


def verify_finite_hecke_representation():
    checked = 0
    for parameter in (3, 9, 27, 81):
        for strands in range(3, 9):
            generators = tuple(burau(strands, index, parameter)
                               for index in range(strands - 1))
            unit = identity(strands)
            for index, sigma in enumerate(generators):
                hecke = scalar(sigma, parameter)
                assert multiply(add(hecke, scalar(unit, parameter), -1),
                                add(hecke, unit)) == scalar(unit, 0)
                if index + 1 < len(generators):
                    left = multiply(hecke, multiply(
                        scalar(generators[index + 1], parameter), hecke))
                    right_generator = scalar(generators[index + 1], parameter)
                    right = multiply(right_generator,
                                     multiply(hecke, right_generator))
                    assert left == right
                if index + 2 < len(generators):
                    other = scalar(generators[index + 2], parameter)
                    assert multiply(hecke, other) == multiply(other, hecke)
                checked += 1
    print("geometric-chain Iwahori-Hecke relations: PASS", checked)


def affine_permutation(size, digit, arity=3):
    matrix = [[0] * size for _ in range(size)]
    for row in range(size):
        matrix[row][(arity * row + digit) % size] = 1
    assert all(sum(row) == 1 for row in matrix)
    assert all(sum(matrix[row][column] for row in range(size)) == 1
               for column in range(size))
    return matrix


def digit_transfer(size, arity=3):
    matrix = [[0] * size for _ in range(size)]
    for row in range(size):
        for digit in range(arity):
            matrix[row][(arity * row + digit) % size] += 1
    return matrix


def verify_oriented_three_branch_transfer():
    checked = 0
    for size in range(5, 80):
        if gcd(size, 3) != 1:
            continue
        branches = [affine_permutation(size, digit) for digit in range(3)]
        total = [[sum(branch[row][column] for branch in branches)
                  for column in range(size)] for row in range(size)]
        assert total == digit_transfer(size)
        assert all(sum(row) == 3 for row in total)
        assert all(sum(total[row][column] for row in range(size)) == 3
                   for column in range(size))
        checked += 1
    print("three affine branches equal the digit transfer: PASS", checked)


def one_carrier_exchange(rank, index):
    matrix = [list(row) for row in identity(rank)]
    matrix[index] = [F(-1, 3) if column == index else F(-1)
                     for column in range(rank)]
    return tuple(tuple(row) for row in matrix)


def verify_carrier_quadratic_relation():
    checked = 0
    for rank in range(2, 13):
        unit = identity(rank)
        for index in range(rank):
            exchange = one_carrier_exchange(rank, index)
            hecke = scalar(exchange, 3)
            assert multiply(add(hecke, scalar(unit, 3), -1),
                            add(hecke, unit)) == scalar(unit, 0)
            checked += 1
    print("one-carrier q=3 Hecke quadratic relation: PASS", checked)


def inverse_two(matrix):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return ((matrix[1][1] / determinant, -matrix[0][1] / determinant),
            (-matrix[1][0] / determinant, matrix[0][0] / determinant))


def prime(value):
    return value >= 2 and all(value % divisor
                              for divisor in range(2, int(value ** .5) + 1))


def verify_standard_b_kernel_generator():
    checked = 0
    change = ((F(1), F(0)), (F(1), F(1)))
    change_inverse = inverse_two(change)
    unit = identity(2)
    for p in range(5, 200):
        if not prime(p):
            continue
        m = p - 4
        standard = ((F(1), F(0)), (F(-m, 3), F(-1, 3)))
        in_iwahori_basis = multiply(change_inverse,
                                    multiply(standard, change))
        expected = ((F(1), F(0)), (F(-p, 3), F(-1, 3)))
        assert in_iwahori_basis == expected
        hecke = scalar(in_iwahori_basis, 3)
        assert hecke == ((F(3), F(0)), (F(-p), F(-1)))
        assert hecke[0][0] * hecke[1][1] - hecke[0][1] * hecke[1][0] == -3
        assert hecke[1][0] % p == 0
        assert gcd(*(abs(int(value)) for row in hecke for value in row)) == 1
        assert multiply(add(hecke, scalar(unit, 3), -1),
                        add(hecke, unit)) == scalar(unit, 0)
        reflection = ((F(1), F(0)), (F(0), F(-1)))
        backward = multiply(hecke, reflection)
        diagonal = ((F(3), F(0)), (F(0), F(1)))
        level_element = ((F(1), F(0)), (F(-p), F(1)))
        assert backward == multiply(diagonal, level_element)
        checked += 1
    print("standard B_p determinant-three matrix identity: PASS", checked)


def verify_regular_hecke_lattice():
    checked = 0
    regular = ((F(0), F(3)), (F(1), F(2)))
    unit = identity(2)
    assert multiply(add(regular, scalar(unit, 3), -1),
                    add(regular, unit)) == scalar(unit, 0)
    for p in range(5, 200):
        if not prime(p):
            continue
        hecke = ((F(3), F(0)), (F(-p), F(-1)))
        lattice = ((F(1), F(3)), (F(0), F(-p)))
        assert multiply(hecke, lattice) == multiply(lattice, regular)
        determinant = (lattice[0][0] * lattice[1][1]
                       - lattice[0][1] * lattice[1][0])
        assert determinant == -p
        # The image lattice is exactly {(x,y): p divides y}.
        for left, right in ((0, 0), (1, 0), (3, -p), (-5, 2 * p)):
            preimage = multiply(inverse_two(lattice),
                                ((F(left),), (F(right),)))
            assert all(value[0].denominator == 1 for value in preimage)
        checked += 1
    print("regular Hecke module and index-p stable lattice: PASS", checked)


def multiplicative_order(base, modulus):
    value = 1
    for exponent in range(1, modulus):
        value = value * base % modulus
        if value == 1:
            return exponent
    raise AssertionError("base is not a unit")


def type_weights(p, row):
    m = p - 4
    a, b = row
    gamma = (1 - a - b) / p
    return a + m * gamma, b + 3 * gamma, gamma


def verify_second_hecke_reflection_target():
    checked = 0
    change = ((F(1), F(0)), (F(1), F(1)))
    change_inverse = inverse_two(change)
    for p in range(5, 200):
        if not prime(p) or p == 3:
            continue
        standard = ((F(-3), F(0)), (F(p - 4), F(1)))
        second = ((F(-3), F(0)), (F(2 * p - 12), F(9)))
        standard_c = multiply(change_inverse, multiply(standard, change))
        second_c = multiply(change_inverse, multiply(second, change))
        assert standard_c == ((F(-3), F(0)), (F(p), F(1)))
        assert second_c == ((F(-3), F(0)), (F(2 * p), F(9)))
        assert multiply(second_c, standard_c) == scalar(
            ((F(1), F(0)), (F(p, 3), F(1))), 9)
        assert multiply(standard_c, second_c) == scalar(
            ((F(1), F(0)), (F(-p, 9), F(1))), 9)
        a, b, c, d = (entry for row in second for entry in row)
        assert 3 * (a + d) ** 2 + 4 * (a * d - b * c) == 0

        order = multiplicative_order(3, p)
        exponent = 1 + order
        delta = F(p - 1, 3 ** exponent)
        while delta >= F(1, 3 * (2 * p - 1)):
            exponent += order
            delta /= 3 ** order
        assert (-3 * delta - 1).numerator % p == 0
        first = (-3 * delta, F(0))
        second_row = ((2 * p - 12) * delta, 9 * delta)
        singleton = (-3 * (p - 8) * delta, -27 * delta)
        margins = tuple(type_weights(p, row)
                        for row in (first, second_row, singleton))
        assert all(value > 0 for margin in margins for value in margin)
        m = p - 4
        for source in range(3):
            demand = m * margins[0][source] + 3 * margins[1][source] \
                     + margins[2][source]
            assert demand == (m, 3, 1)[source]
        checked += 1
    print("second Hecke reflection roots and positive transport: PASS", checked)


def verify_affine_hecke_wall_family():
    checked = 0
    change = ((F(1), F(0)), (F(1), F(1)))
    change_inverse = inverse_two(change)
    parameters = (F(-2), F(-1), F(0), F(1, 3), F(2, 3), F(1),
                  F(4, 3), F(2))
    for p in range(5, 100):
        if not prime(p):
            continue
        standard = ((F(-3), F(0)), (F(p), F(1)))
        for parameter in parameters:
            old_basis = ((F(-1), F(0)), (parameter * p - 4, F(3)))
            wall = multiply(change_inverse, multiply(old_basis, change))
            assert wall == ((F(-1), F(0)), (parameter * p, F(3)))
            a, b, c, d = (entry for row in wall for entry in row)
            assert 3 * (a + d) ** 2 + 4 * (a * d - b * c) == 0
            assert multiply(wall, standard) == scalar(
                ((F(1), F(0)), (p * (1 - parameter), F(1))), 3)
            assert multiply(standard, wall) == scalar(
                ((F(1), F(0)), (F(p * (parameter - 1), 3), F(1))), 3)
            if parameter == 1:
                assert multiply(wall, standard) == scalar(identity(2), 3)
            else:
                assert multiply(wall, standard)[1][0]

            order = multiplicative_order(3, p)
            exponent = order
            delta = F(p - 1, 3 ** exponent)
            rows = (
                (F(-1), F(0)),
                (parameter * p - 4, F(3)),
                (p + 8 - 3 * parameter * p, F(-9)),
            )
            margins = tuple(type_weights(
                p, tuple(delta * value for value in row)) for row in rows)
            while not all(value > 0 for margin in margins for value in margin):
                exponent += order
                delta /= 3 ** order
                margins = tuple(type_weights(
                    p, tuple(delta * value for value in row))
                                for row in rows)
            assert all(value > 0 for margin in margins for value in margin)
            assert (-delta - 1).numerator % p == 0
            m = p - 4
            for source in range(3):
                demand = m * margins[0][source] + 3 * margins[1][source] \
                         + margins[2][source]
                assert demand == (m, 3, 1)[source]
            checked += 1
    print("affine q=3 Hecke wall family and p-roots: PASS", checked)


def transpose(matrix):
    return tuple(zip(*matrix))


def verify_energy_star_structure():
    checked = 0
    for p in range(5, 200):
        if not prime(p):
            continue
        gram = ((F(p * (p - 1)), F(3 * p)),
                (F(3 * p), F(12)))
        standard = ((F(1), F(0)), (F(-p, 3), F(-1, 3)))
        assert multiply(transpose(standard), gram) == multiply(gram, standard)
        pulled = multiply(transpose(standard), multiply(gram, standard))
        defect = add(gram, pulled, -1)
        expected = ((F(2 * p * p, 3), F(8 * p, 3)),
                    (F(8 * p, 3), F(32, 3)))
        assert defect == expected
        diagonal_change = ((F(1), F(0)), (F(p), F(4)))
        transformed = multiply(diagonal_change,
                               multiply(standard, inverse_two(diagonal_change)))
        assert transformed == ((F(1), F(0)), (F(0), F(-1, 3)))
        checked += 1
    print("Hecke self-adjoint energy and rank-one defect: PASS", checked)


def verify_local_eigenprojectors():
    checked = 0
    unit = identity(2)
    zero = scalar(unit, 0)
    for p in range(5, 200):
        if not prime(p):
            continue
        standard = ((F(1), F(0)), (F(-p, 3), F(-1, 3)))
        spherical = scalar(add(scalar(standard, 3), unit), F(1, 4))
        steinberg = scalar(add(unit, standard, -1), F(3, 4))
        assert add(spherical, steinberg) == unit
        assert multiply(spherical, spherical) == spherical
        assert multiply(steinberg, steinberg) == steinberg
        assert multiply(spherical, steinberg) == zero
        assert spherical == ((F(1), F(0)), (F(-p, 4), F(0)))
        assert steinberg == ((F(0), F(0)), (F(p, 4), F(1)))
        spherical_line = ((F(4),), (F(-p),))
        sign_line = ((F(0),), (F(1),))
        assert multiply(spherical, spherical_line) == spherical_line
        assert multiply(steinberg, sign_line) == sign_line
        assert multiply(spherical, sign_line) == ((F(0),), (F(0),))
        assert multiply(steinberg, spherical_line) == ((F(0),), (F(0),))
        checked += 1
    print("local eigenprojectors and terminal line: PASS", checked)


def simple_degeneracy_matrix(p, first, second):
    m = p - 4
    values = {
        "u": (F(1), F(0)),
        "v": (F(0), F(1)),
        "w": (F(-m), F(-3)),
    }
    mean = tuple(-(values[first][index] + values[second][index]) / (p - 2)
                 for index in range(2))
    triple = tuple((values[first][index] + 2 * mean[index]) / 3
                   for index in range(2))
    return mean + triple


def verify_simple_degeneracy_boundary():
    polynomials = {
        ("u", "u"): lambda p: 36,
        ("u", "v"): lambda p: 4 * p + 17,
        ("u", "w"): lambda p: 9 * p * p - 66 * p + 105,
        ("v", "u"): lambda p: p * p - 18 * p + 57,
        ("v", "v"): lambda p: (p - 6) ** 2,
        ("v", "w"): lambda p: 20 * p * p - 104 * p + 132,
        ("w", "u"): lambda p: 12 * p - 15,
        ("w", "v"): lambda p: -4 * (p * p - 6 * p + 7),
    }
    for p in range(11, 200):
        for roles, polynomial in polynomials.items():
            a, b, c, d = simple_degeneracy_matrix(p, *roles)
            obstruction = 3 * (a + d) ** 2 + 4 * (a * d - b * c)
            cleared = obstruction * 3 * (p - 2) ** 2
            assert cleared == polynomial(p)
            assert cleared
    print("p-minus-two simple degeneracy has no Hecke wall: PASS",
          len(polynomials))


def verify():
    verify_finite_hecke_representation()
    verify_oriented_three_branch_transfer()
    verify_carrier_quadratic_relation()
    verify_standard_b_kernel_generator()
    verify_regular_hecke_lattice()
    verify_second_hecke_reflection_target()
    verify_affine_hecke_wall_family()
    verify_energy_star_structure()
    verify_local_eigenprojectors()
    verify_simple_degeneracy_boundary()
    print("finite Hecke and matrix identities only: PASS")


if __name__ == "__main__":
    verify()
