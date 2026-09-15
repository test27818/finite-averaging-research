"""Give an exact finite certificate for descent in the B_7 family.

All real-algebraic checks use integers and Fraction. Floating point is not
used anywhere in the certificate.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, isqrt


K = ((2, -1), (-1, 4))  # twice Q(x,y)=x^2-x*y+2*y^2
A = ((3, 0), (1, -1))
B = ((-3, 3), (-1, 0))

CERTIFICATE_WORDS = (
    "0", "1", "01", "11", "001", "010", "101", "110",
    "0100", "0111", "1100", "1111", "00111", "01110",
    "10111", "11110", "0111101", "1111101",
)

RESIDUE_TYPES = {
    "x unit, y/x = 0 (mod 3)": (1, 0),
    "x unit, y/x = 1 (mod 3)": (1, 1),
    "x unit, y/x = 2 (mod 9)": (1, 2),
    "x unit, y/x = 5 or 8 (mod 9)": (1, 5),
    "3 divides x, y unit": (0, 1),
}


def mul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def transpose(matrix_):
    return ((matrix_[0][0], matrix_[1][0]),
            (matrix_[0][1], matrix_[1][1]))


def matrix(word):
    result = ((1, 0), (0, 1))
    for letter in word:
        result = mul(A if letter == "0" else B, result)
    return result


def valuation(value, cap=99):
    if value == 0:
        return cap
    exponent = 0
    while exponent < cap and value % 3 == 0:
        exponent += 1
        value //= 3
    return exponent


def image(transform, vector):
    return tuple(sum(transform[i][j] * vector[j] for j in range(2))
                 for i in range(2))


def descent_polynomial(transform, exponent):
    image_form = mul(transpose(transform), mul(K, transform))
    difference = tuple(
        tuple(3 ** (2 * exponent) * K[i][j] - image_form[i][j]
              for j in range(2))
        for i in range(2)
    )
    # D(1,t)=a+b*t+c*t^2. D>0 implies strict Q descent after
    # primitive normalization because 3^exponent divides both coordinates.
    return difference[0][0], 2 * difference[0][1], difference[1][1]


def polynomial_value(polynomial, t):
    a, b, c = polynomial
    return a + b * t + c * t * t


def normalize_polynomial(polynomial):
    common = 0
    for coefficient in polynomial:
        common = gcd(common, abs(coefficient))
    if common == 0:
        return polynomial
    result = tuple(coefficient // common for coefficient in polynomial)
    highest = next(coefficient for coefficient in reversed(result) if coefficient)
    if highest < 0:
        result = tuple(-coefficient for coefficient in result)
    return result


@dataclass
class Root:
    key: tuple
    polynomial: tuple | None
    branch: int
    lo: F
    hi: F

    @property
    def rational(self):
        return self.polynomial is None

    def refine(self):
        if self.rational:
            return
        midpoint = (self.lo + self.hi) / 2
        sign = polynomial_value(self.polynomial, midpoint)
        assert sign != 0  # An irreducible quadratic has no rational root.
        if self.branch < 0:
            if sign > 0:
                self.lo = midpoint
            else:
                self.hi = midpoint
        else:
            if sign < 0:
                self.lo = midpoint
            else:
                self.hi = midpoint


def rational_root(value):
    return Root(("rational", value.numerator, value.denominator), None, 0,
                value, value)


def real_roots(polynomial):
    a, b, c = normalize_polynomial(polynomial)
    if c == 0:
        return [] if b == 0 else [rational_root(F(-a, b))]

    discriminant = b * b - 4 * c * a
    if discriminant < 0:
        return []
    root_discriminant = isqrt(discriminant)
    if root_discriminant * root_discriminant == discriminant:
        values = sorted({F(-b - root_discriminant, 2 * c),
                         F(-b + root_discriminant, 2 * c)})
        return [rational_root(value) for value in values]

    # Normalization makes c positive. The vertex separates the two roots,
    # and the Cauchy bound puts both strictly inside [-bound,bound].
    assert discriminant > 0 and c > 0
    ceiling = (max(abs(a), abs(b)) + c - 1) // c
    bound = F(1 + ceiling)
    vertex = F(-b, 2 * c)
    key = (a, b, c)
    return [
        Root(("quadratic", key, -1), key, -1, -bound, vertex),
        Root(("quadratic", key, 1), key, 1, vertex, bound),
    ]


def intervals_disjoint(left, right):
    return left.hi < right.lo or right.hi < left.lo


def isolate_roots(polynomials):
    roots_by_polynomial = []
    unique = {}
    for polynomial in polynomials:
        keys = set()
        for root in real_roots(polynomial):
            keys.add(root.key)
            unique.setdefault(root.key, root)
        roots_by_polynomial.append(keys)

    roots = list(unique.values())
    while True:
        overlap = None
        for index, left in enumerate(roots):
            for right in roots[index + 1:]:
                if not intervals_disjoint(left, right):
                    overlap = left, right
                    break
            if overlap:
                break
        if overlap is None:
            break
        left, right = overlap
        if left.rational and right.rational:
            raise AssertionError("distinct rational roots cannot overlap")
        left.refine()
        right.refine()

    roots.sort(key=lambda root: root.lo)
    return roots, roots_by_polynomial


def exact_uncovered_set(polynomials):
    polynomials = tuple(dict.fromkeys(
        polynomial for polynomial in polynomials
        if polynomial != (0, 0, 0)
    ))
    roots, roots_by_polynomial = isolate_roots(polynomials)

    if roots:
        interval_samples = [roots[0].lo - 1]
        interval_samples.extend((left.hi + right.lo) / 2
                                for left, right in zip(roots, roots[1:]))
        interval_samples.append(roots[-1].hi + 1)
    else:
        interval_samples = [F(0)]

    uncovered_intervals = [
        sample for sample in interval_samples
        if not any(polynomial_value(polynomial, sample) > 0
                   for polynomial in polynomials)
    ]

    uncovered_points = []
    for index, root in enumerate(roots):
        adjacent_sample = interval_samples[index]
        covered = any(
            root.key not in root_keys
            and polynomial_value(polynomial, adjacent_sample) > 0
            for polynomial, root_keys in zip(polynomials, roots_by_polynomial)
        )
        if not covered:
            uncovered_points.append(root)

    infinity_covered = any(polynomial[2] > 0 for polynomial in polynomials)
    return uncovered_intervals, uncovered_points, infinity_covered


def residue_type(residue):
    x, y = residue
    if x % 3:
        slope = y * pow(x, -1, 9) % 9
        if slope % 3 == 0:
            return "x unit, y/x = 0 (mod 3)"
        if slope % 3 == 1:
            return "x unit, y/x = 1 (mod 3)"
        if slope == 2:
            return "x unit, y/x = 2 (mod 9)"
        assert slope in (5, 8)
        return "x unit, y/x = 5 or 8 (mod 9)"
    assert y % 3
    return "3 divides x, y unit"


def exponent_signature(vector, transforms, cap=7):
    return tuple(min(valuation(coordinate, cap)
                     for coordinate in image(transform, vector))
                 for transform in transforms)


def display_root(root):
    if root.rational:
        return root.lo
    a, b, c = root.polynomial
    sign = "-" if root.branch < 0 else "+"
    return f"({-b} {sign} sqrt({b*b - 4*c*a}))/{2*c}"


def verify_certificate(max_depth=7):
    identity = ((1, 0), (0, 1))
    form_a = mul(transpose(A), mul(K, A))
    form_b = mul(transpose(B), mul(K, B))
    assert form_a == ((16, -1), (-1, 4))
    assert form_b == ((16, -15), (-15, 18))
    assert mul(A, identity) == A and mul(B, identity) == B

    transforms = tuple(matrix(word) for word in CERTIFICATE_WORDS)
    expected_signatures = {
        label: exponent_signature(representative, transforms, max_depth)
        for label, representative in RESIDUE_TYPES.items()
    }

    modulus = 3 ** max_depth
    projective_classes = ([(1, t) for t in range(modulus)]
                          + [(3 * t, 1) for t in range(3 ** (max_depth - 1))])
    counts = {label: 0 for label in RESIDUE_TYPES}
    for residue in projective_classes:
        label = residue_type(residue)
        counts[label] += 1
        actual = exponent_signature(residue, transforms, max_depth)
        assert actual == expected_signatures[label], (residue, actual, label)

    expected_exception_keys = {
        rational_root(F(0)).key,
        rational_root(F(2)).key,
    }
    coverage = {}
    compatible_exceptions = {}
    for label, signature in expected_signatures.items():
        polynomials = [descent_polynomial(transform, exponent)
                       for transform, exponent in zip(transforms, signature)]
        intervals, points, infinity_covered = exact_uncovered_set(polynomials)
        point_keys = {point.key for point in points}
        assert not intervals, (label, intervals)
        assert point_keys <= expected_exception_keys, (label, points)
        assert infinity_covered, label
        coverage[label] = tuple(display_root(point) for point in points)

        compatible = []
        for point in points:
            assert point.rational
            direction = (point.lo.denominator, point.lo.numerator)
            if residue_type(tuple(value % modulus for value in direction)) == label:
                compatible.append(point.lo)
        compatible_exceptions[label] = tuple(compatible)

        # y/x=0 is the terminal u+v=0 family.  At y/x=2,
        # Q(x,y)=7*x^2, so the required mod-7 condition fails.
        legal_nonterminal = [
            slope for slope in compatible
            if slope != 0
            and (direction_q := (slope.denominator ** 2
                                 - slope.denominator * slope.numerator
                                 + 2 * slope.numerator ** 2)) % 7
        ]
        assert not legal_nonterminal, (label, legal_nonterminal)

    assert sum(counts.values()) == 4 * 3 ** (max_depth - 1)
    assert max(max(signature) for signature in expected_signatures.values()) < max_depth
    # L=(2,-1) records u-v. Both generators preserve L != 0 modulo 7.
    assert tuple((2 * A[0][j] - A[1][j]) % 7 for j in range(2)) == (5, 1)
    assert tuple((2 * B[0][j] - B[1][j]) % 7 for j in range(2)) == (2, 6)
    return counts, expected_signatures, coverage, compatible_exceptions


def main():
    counts, signatures, coverage, compatible = verify_certificate()
    print("exact certificate: PASS")
    print("words:", len(CERTIFICATE_WORDS), "maximum length:",
          max(map(len, CERTIFICATE_WORDS)))
    print("primitive projective classes:", sum(counts.values()))
    for label in RESIDUE_TYPES:
        print(label)
        print("  classes:", counts[label])
        print("  exponents:", ",".join(map(str, signatures[label])))
        print("  uncovered finite directions:", coverage[label] or "none")
        print("  compatible exceptional directions:", compatible[label] or "none")
    print("The only possible uncovered directions are y/x=0 and y/x=2;")
    print("the first is the terminal family and the second has Q=7*x^2.")


if __name__ == "__main__":
    main()
