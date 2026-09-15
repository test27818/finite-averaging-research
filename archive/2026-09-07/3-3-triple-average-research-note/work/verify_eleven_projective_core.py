"""Exact local-real descent certificate for the B_11 projective core."""

from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm

from symbolic_two_parameter_macros import b_parameters, b_state, choices, step
from verify_seven_descent_cover import display_root, exact_uncovered_set


def c(u, v):
    return F(u), F(v)


def signature(*values):
    return tuple(sorted(values))


U = c(1, 0)
V = c(0, 1)
W = c(-7, -3)
A = c(F(-7, 3), F(-1, 3))
B = c(F(2, 3), F(1, 3))
C = c(F(1, 3), F(2, 3))
D = c(F(-5, 3), -1)
E = c(F(-7, 9), F(-2, 3))
F1 = c(F(1, 9), F(-1, 3))
G = c(F(-1, 9), F(-1, 9))
H = c(F(7, 9), F(2, 9))


# Eight short, independently replayable return macros generate the certificate.
BASE_PATHS = {
    0: (signature(W, V, V),),
    1: (
        signature(W, V, V),
        signature(A, A, V),
    ),
    4: (
        signature(V, U, U),
        signature(W, B, B),
        signature(V, U, U),
        signature(V, U, U),
    ),
    5: (
        signature(V, U, U),
        signature(V, U, U),
        signature(V, U, U),
        signature(B, B, U),
    ),
    8: (
        signature(W, V, V),
        signature(A, U, U),
        signature(A, U, U),
        signature(A, U, U),
        signature(G, G, U),
    ),
    9: (
        signature(W, U, U),
        signature(D, D, U),
        signature(D, U, U),
        signature(E, F1, U),
        signature(E, F1, U),
    ),
    10: (
        signature(W, U, U),
        signature(V, V, U),
        signature(V, U, U),
        signature(C, B, U),
        signature(C, B, U),
    ),
    14: (
        signature(V, U, U),
        signature(V, U, U),
        signature(V, U, U),
        signature(B, B, U),
        signature(W, H, H),
    ),
}

BASE_MATRICES = {
    0: (3, 0, 0, -1),
    1: (9, 0, 0, 1),
    4: (3, 3, -55, -7),
    5: (3, 3, 77, 29),
    8: (9, -3, 231, -29),
    9: (25, -3, -77, 15),
    10: (1, 1, 11, -5),
    14: (9, 9, -77, -29),
}


# Words are compositions of the replayed base macros, in execution order.
DESCENT_WORDS = (
    (10,),
    (0, 10, 10, 10),
    (9, 10, 0),
    (10, 0, 10),
    (4,),
    (0, 10, 10, 1),
    (1, 10, 10, 0),
    (10, 0, 9),
    (0, 9, 0, 10),
    (4, 9),
    (5,),
    (0,),
)

DESCENT_MATRICES = (
    (1, 1, 11, -5),
    (3, 1, -33, -7),
    (13, -3, 55, -9),
    (1, -1, -11, -1),
    (3, 3, -55, -7),
    (27, 3, -11, -3),
    (27, -1, 33, -3),
    (9, 5, -33, -13),
    (19, 1, 55, 1),
    (5, 2, -22, -7),
    (3, 3, 77, 29),
    (3, 0, 0, -1),
)

TRANSLATE_MINUS_WORD = (1, 9, 10, 1, 10)
TRANSLATE_PLUS_SEED_WORD = (10, 0, 10, 10, 8)
TRANSLATE_MINUS = (1, 0, -44, 1)
TRANSLATE_PLUS_SEED = (3, 0, 44, 3)
TRANSLATE_PLUS = (1, 0, 44, 1)

MATRICES = DESCENT_MATRICES + (TRANSLATE_MINUS, TRANSLATE_PLUS)
MODULUS = 64 * 9


def determinant(matrix):
    a, b, c_, d = matrix
    return a * d - b * c_


def matrix_mul(left, right):
    a, b, c_, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c_ * e + d * g,
        c_ * f + d * h,
    )


def primitive_matrix(matrix):
    divisor = gcd(*(abs(value) for value in matrix))
    result = tuple(value // divisor for value in matrix)
    first = next(value for value in result if value)
    return tuple(-value for value in result) if first < 0 else result


def matrix_of_word(word):
    result = (1, 0, 0, 1)
    for letter in word:
        result = primitive_matrix(matrix_mul(BASE_MATRICES[letter], result))
    return result


def xy_matrix(parameters):
    # (x,y)=(u,7u+4v).
    change = ((F(1), F(0)), (F(7), F(4)))
    inverse = ((F(1), F(0)), (F(-7, 4), F(1, 4)))

    def multiply(left, right):
        return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))

    rational = multiply(change, multiply(parameters, inverse))
    denominator = lcm(*(entry.denominator for row in rational for entry in row))
    entries = tuple(int(entry * denominator) for row in rational for entry in row)
    return primitive_matrix(entries)


def replay_path(path):
    state = b_state(11)
    for selected_values in path:
        selected = next(
            indices
            for indices, candidate in choices(state)
            if candidate == selected_values
        )
        state = step(state, selected)
    parameters = b_parameters(11, state)
    assert len(parameters) == 1
    return xy_matrix(parameters[0])


def valuation(value, prime, cap):
    if value == 0:
        return cap
    exponent = 0
    while exponent < cap and value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def local_scale(x, y):
    # Least h in {1,2,4} for which h(x,y) belongs to y=7x mod 4.
    return 4 // gcd(4, y - 7 * x)


def image(matrix, vector):
    a, b, c_, d = matrix
    x, y = vector
    return a * x + b * y, c_ * x + d * y


def divisor_and_output_scale(matrix, residue):
    raw = image(matrix, residue)
    det = abs(determinant(matrix))
    exponent_two = min(
        valuation(raw[0], 2, valuation(det, 2, 99)),
        valuation(raw[1], 2, valuation(det, 2, 99)),
    )
    exponent_three = min(
        valuation(raw[0], 3, valuation(det, 3, 99)),
        valuation(raw[1], 3, valuation(det, 3, 99)),
    )
    divisor = 2 ** exponent_two * 3 ** exponent_three
    reduced = raw[0] // divisor, raw[1] // divisor
    return divisor, local_scale(*reduced)


def local_signature(residue):
    return (
        local_scale(*residue),
        tuple(divisor_and_output_scale(matrix, residue) for matrix in MATRICES),
    )


def residue_classes():
    for x in range(MODULUS):
        for y in range(MODULUS):
            if x % 2 == y % 2 == 0 or x % 3 == y % 3 == 0:
                continue
            yield x, y


def descent_polynomial(matrix, input_scale, divisor, output_scale):
    # D(1,t)>0 is exactly the strict primitive-height decrease.
    a, b, c_, d = matrix
    left = input_scale * input_scale * divisor * divisor
    right = output_scale * output_scale
    return (
        77 * left - right * (77 * a * a + 3 * c_ * c_),
        -right * (154 * a * b + 6 * c_ * d),
        3 * left - right * (77 * b * b + 3 * d * d),
    )


def average(state, selected):
    mean = sum((state[index] for index in selected), F(0)) / 3
    result = list(state)
    for index in selected:
        result[index] = mean
    return tuple(result)


def verify_terminal():
    state = (F(0),) * 7 + (F(1),) * 3 + (F(-3),)
    minus_three = state.index(F(-3))
    zeroes = [index for index, value in enumerate(state) if value == 0]
    state = average(state, (minus_three, zeroes[0], zeroes[1]))
    for _ in range(3):
        minus_one = state.index(F(-1))
        zero = state.index(F(0))
        one = state.index(F(1))
        state = average(state, (minus_one, zero, one))
    assert state == (F(0),) * 11


def verify_paths():
    for key, path in BASE_PATHS.items():
        assert replay_path(path) == BASE_MATRICES[key]

    assert tuple(matrix_of_word(word) for word in DESCENT_WORDS) == DESCENT_MATRICES
    assert matrix_of_word(TRANSLATE_MINUS_WORD) == TRANSLATE_MINUS
    assert matrix_of_word(TRANSLATE_PLUS_SEED_WORD) == TRANSLATE_PLUS_SEED
    plus_cube = matrix_mul(
        TRANSLATE_PLUS_SEED,
        matrix_mul(TRANSLATE_PLUS_SEED, TRANSLATE_PLUS_SEED),
    )
    assert primitive_matrix(plus_cube) == TRANSLATE_PLUS

    # Every macro preserves 11 not dividing y, even after primitive reduction.
    for matrix in MATRICES:
        _, _, c_, d = matrix
        assert c_ % 11 == 0 and d % 11 != 0
        assert determinant(matrix) % 11 != 0
        assert not (set(prime_divisors(abs(determinant(matrix)))) - {2, 3})


def prime_divisors(value):
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        result.append(value)
    return tuple(result)


def verify_cover():
    grouped = Counter(local_signature(residue) for residue in residue_classes())
    infinity_signature = local_signature((0, 1))
    failures = []
    terminal_infinity_types = 0

    for local, count in grouped.items():
        input_scale, data = local
        polynomials = [
            descent_polynomial(matrix, input_scale, divisor, output_scale)
            for matrix, (divisor, output_scale) in zip(MATRICES, data)
        ]
        intervals, points, infinity_covered = exact_uncovered_set(polynomials)

        compatible_points = []
        for point in points:
            if not point.rational:
                continue
            slope = point.lo
            pair = slope.denominator, slope.numerator
            if (pair[1] % 11
                    and local_signature((pair[0] % MODULUS,
                                         pair[1] % MODULUS)) == local):
                compatible_points.append(slope)

        infinity_compatible = infinity_signature == local
        bad_infinity = not infinity_covered and infinity_compatible
        if intervals or compatible_points:
            failures.append((count, intervals, compatible_points,
                             [display_root(point) for point in points]))
        if bad_infinity:
            terminal_infinity_types += 1

    assert not failures, failures[:3]
    assert terminal_infinity_types == 1
    assert len(grouped) == 36
    assert sum(grouped.values()) == 221184
    return grouped


def main():
    verify_paths()
    verify_terminal()
    grouped = verify_cover()
    maximum_descent_length = max(
        sum(len(BASE_PATHS[letter]) for letter in word)
        for word in DESCENT_WORDS
    )
    translation_lengths = (
        sum(len(BASE_PATHS[letter]) for letter in TRANSLATE_MINUS_WORD),
        3 * sum(len(BASE_PATHS[letter])
                for letter in TRANSLATE_PLUS_SEED_WORD),
    )
    print("B11 exact projective-core certificate: PASS")
    print("base return macros", len(BASE_PATHS))
    print("descent macros", len(DESCENT_MATRICES),
          "maximum length", maximum_descent_length)
    print("translation lengths", translation_lengths,
          "actions y -> y - 44x and y -> y + 44x")
    print("modulus", MODULUS, "local signatures", len(grouped),
          "residue classes", sum(grouped.values()))
    print("only compatible uncovered direction: x=0 (four-step terminal)")


if __name__ == "__main__":
    main()
