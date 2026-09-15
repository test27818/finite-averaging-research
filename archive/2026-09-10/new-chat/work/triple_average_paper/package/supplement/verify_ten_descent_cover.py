"""Exact local-real descent certificate for the B_10 family."""

from collections import Counter
from fractions import Fraction as F

from explore_ten_descent import image, legal_type, xy_matrix
from symbolic_two_parameter_macros import b_parameters, b_state, choices, step
from verify_seven_descent_cover import display_root, exact_uncovered_set


SELECTED = (
    (1, 1, -5, -1),
    (1, 0, -5, 2),
    (1, -2, 0, 3),
    (1, 1, 5, -3),
    (4, 1, 0, -3),
    (1, -2, 5, 2),
    (1, 0, -10, -1),
)


def c(u, v):
    return F(u), F(v)


U = c(1, 0)
V = c(0, 1)
W = c(-6, -3)
Q = c(F(-5, 3), F(-2, 3))
R = c(F(1, 3), F(2, 3))
S = c(F(2, 3), F(1, 3))
T = c(-2, F(-1, 3))


# Each entry is the sequence of three current linear forms actually averaged.
# The starting state is B_10(u,v)=(u^6,v^3,-6u-3v).
SELECTED_PATHS = {
    (1, 1, -5, -1): (
        tuple(sorted((W, V, U))),
        tuple(sorted((V, U, U))),
        tuple(sorted((V, U, U))),
    ),
    (1, 0, -5, 2): (
        tuple(sorted((W, V, U))),
        tuple(sorted((Q, U, U))),
        tuple(sorted((V, V, U))),
        tuple(sorted((Q, R, U))),
        tuple(sorted((Q, R, U))),
    ),
    (1, -2, 0, 3): (
        tuple(sorted((W, U, U))),
        tuple(sorted((V, U, U))),
        tuple(sorted((V, S, U))),
        tuple(sorted((V, S, U))),
    ),
    (1, 1, 5, -3): (
        tuple(sorted((W, U, U))),
        tuple(sorted((V, U, U))),
        tuple(sorted((V, U, U))),
    ),
    (4, 1, 0, -3): (
        tuple(sorted((W, V, U))),
        tuple(sorted((V, V, U))),
        tuple(sorted((R, U, U))),
        tuple(sorted((R, U, U))),
    ),
    (1, -2, 5, 2): (
        tuple(sorted((V, U, U))),
        tuple(sorted((W, S, U))),
        tuple(sorted((V, S, U))),
        tuple(sorted((V, S, U))),
    ),
    (1, 0, -10, -1): (
        tuple(sorted((W, V, V))),
        tuple(sorted((V, U, U))),
        tuple(sorted((T, S, U))),
        tuple(sorted((T, S, U))),
        tuple(sorted((S, U, U))),
    ),
}

MODULUS = 96  # 2^5 * 3 records every possible gcd and output mod 4 type.


def valuation(value, prime, cap):
    if value == 0:
        return cap
    exponent = 0
    while exponent < cap and value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def determinant(matrix):
    a, b, c, d = matrix
    return a * d - b * c


def local_scale(x, y):
    # The residue represents a primitive pair at 2.
    if (x - y) % 2:
        return 2
    if x % 2 and y % 2 and (x + y) % 4 == 0:
        return 1
    return None


def divisor_and_output_scale(matrix, residue):
    det = abs(determinant(matrix))
    raw = image(matrix, residue)
    exponent_two = min(
        valuation(raw[0], 2, valuation(det, 2, 10)),
        valuation(raw[1], 2, valuation(det, 2, 10)),
    )
    exponent_three = min(
        valuation(raw[0], 3, valuation(det, 3, 10)),
        valuation(raw[1], 3, valuation(det, 3, 10)),
    )
    divisor = 2 ** exponent_two * 3 ** exponent_three
    reduced = raw[0] // divisor, raw[1] // divisor
    return divisor, local_scale(*reduced)


def signature(residue):
    return tuple(divisor_and_output_scale(matrix, residue) for matrix in SELECTED)


def descent_polynomial(matrix, input_scale, divisor, output_scale):
    # D(1,t)>0 is exactly W(input)-W(primitive output)>0.
    a, b, c, d = matrix
    left = input_scale * input_scale * divisor * divisor
    right = output_scale * output_scale
    return (
        5 * left - right * (5 * a * a + c * c),
        -right * (10 * a * b + 2 * c * d),
        left - right * (5 * b * b + d * d),
    )


def residue_classes():
    for x in range(MODULUS):
        for y in range(MODULUS):
            if x % 2 == y % 2 == 0 or x % 3 == y % 3 == 0:
                continue
            input_scale = local_scale(x, y)
            if input_scale is not None:
                yield (x, y), input_scale


def direction_signature(x, y):
    assert legal_type(x, y) is not None
    return legal_type(x, y), signature((x % MODULUS, y % MODULUS))


def replay_path(path):
    state = b_state(10)
    for signature_value in path:
        selected = next(
            selected
            for selected, candidate in choices(state)
            if candidate == signature_value
        )
        state = step(state, selected)
    parameters = b_parameters(10, state)
    assert len(parameters) == 1
    return parameters[0]


def verify():
    assert set(SELECTED_PATHS) == set(SELECTED)
    for matrix, path in SELECTED_PATHS.items():
        assert len(path) <= 5
        assert xy_matrix(replay_path(path)) == matrix

    # Every selected macro preserves Y != 0 mod 5.
    for matrix in SELECTED:
        _, _, c, d = matrix
        assert c % 5 == 0 and d % 5 != 0

    grouped = Counter((scale, signature(residue)) for residue, scale in residue_classes())
    infinity_signature = direction_signature(0, 1)

    failures = []
    coverage = []
    for local, count in grouped.items():
        input_scale, data = local
        polynomials = [
            descent_polynomial(matrix, input_scale, divisor, output_scale)
            for matrix, (divisor, output_scale) in zip(SELECTED, data)
            if output_scale is not None
        ]
        intervals, points, infinity_covered = exact_uncovered_set(polynomials)
        compatible_points = []
        for point in points:
            if not point.rational:
                # An isolated irrational direction contains no rational input.
                continue
            slope = point.lo
            pair = slope.denominator, slope.numerator
            if legal_type(*pair) is not None and direction_signature(*pair) == local:
                terminal_label = {F(3): "Y=3X", F(-1): "Y=-X"}.get(slope)
                compatible_points.append((slope, terminal_label))

        infinity_compatible = infinity_signature == local
        bad_infinity = not infinity_covered and infinity_compatible
        nonterminal = [
            slope for slope, terminal_label in compatible_points if terminal_label is None
        ]
        if intervals or nonterminal:
            failures.append((local, intervals, points, infinity_covered, compatible_points))
        coverage.append((
            count,
            len(polynomials),
            intervals,
            compatible_points,
            infinity_covered,
            infinity_compatible,
        ))

    assert not failures, failures[:3]
    assert sum(grouped.values()) == len(list(residue_classes()))
    return grouped, coverage


def main():
    grouped, coverage = verify()
    print("B10 exact local-real descent certificate: PASS")
    print("selected macros", len(SELECTED), "maximum length",
          max(map(len, SELECTED_PATHS.values())))
    print("modulus", MODULUS, "local signatures", len(grouped), "residue classes", sum(grouped.values()))
    for matrix in SELECTED:
        print(" matrix", matrix, "det", determinant(matrix),
              "length", len(SELECTED_PATHS[matrix]))
    exceptional = Counter()
    for _, _, intervals, points, infinity, infinity_compatible in coverage:
        assert not intervals
        for point, label in points:
            exceptional[(point, label)] += 1
        if not infinity and infinity_compatible:
            exceptional[("infinity", "X=0")] += 1
    print("compatible uncovered terminal directions", dict(exceptional))


if __name__ == "__main__":
    main()
