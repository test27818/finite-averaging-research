"""Exact checks for the arithmetic-geometric structure of triple averaging."""

from math import gcd


EXPECTED_FORMS = {
    5: ((1, 3, 6), -15),
    6: ((1, 2, 2), -4),
    7: ((2, 3, 2), -7),
    8: ((5, 6, 3), -24),
    9: ((5, 5, 2), -15),
    10: ((7, 6, 2), -20),
    11: ((28, 21, 6), -231),
}

TEN_MACROS = (
    (1, 1, -5, -1),
    (1, 0, -5, 2),
    (1, -2, 0, 3),
    (1, 1, 5, -3),
    (4, 1, 0, -3),
    (1, -2, 5, 2),
    (1, 0, -10, -1),
)


def content(values):
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def primitive_form(n):
    m = n - 4
    raw = (m * (m + 1), 6 * m, 12)
    divisor = content(raw)
    form = tuple(value // divisor for value in raw)
    a, b, c = form
    return form, b * b - 4 * a * c, divisor


def determinant(matrix):
    a, b, c, d = matrix
    return a * d - b * c


def image(matrix, vector):
    a, b, c, d = matrix
    x, y = vector
    return a * x + b * y, c * x + d * y


def prime_support(value):
    value = abs(value)
    result = set()
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            result.add(prime)
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        result.add(value)
    return result


def local_lattice_scale(n, primitive_vector):
    """Least h > 0 such that h(a,b) lies in y = (n-4)x mod 4."""
    a, b = primitive_vector
    return 4 // gcd(4, b - (n - 4) * a)


def verify_forms():
    for n, expected in EXPECTED_FORMS.items():
        form, discriminant, divisor = primitive_form(n)
        assert (form, discriminant) == expected
        m = n - 4
        assert discriminant * divisor * divisor == -12 * n * m


def verify_lattice_height():
    checked = 0
    for n in range(5, 31):
        m = n - 4
        for u in range(-20, 21):
            for v in range(-20, 21):
                if (u, v) == (0, 0) or gcd(abs(u), abs(v)) != 1:
                    continue
                x, y = u, m * u + 4 * v
                divisor = gcd(abs(x), abs(y))
                a, b = x // divisor, y // divisor
                h = local_lattice_scale(n, (a, b))
                assert h == divisor
                assert (h * b - m * h * a) % 4 == 0

                energy = m * u * u + 3 * v * v + (m * u + 3 * v) ** 2
                q_value = m * n * a * a + 3 * b * b
                assert 4 * energy == h * h * q_value
                checked += 1
    return checked


def verify_gcd_divides_determinant():
    checked = 0
    for matrix in TEN_MACROS:
        det = abs(determinant(matrix))
        for x in range(-40, 41):
            for y in range(-40, 41):
                if (x, y) == (0, 0) or gcd(abs(x), abs(y)) != 1:
                    continue
                raw = image(matrix, (x, y))
                divisor = gcd(abs(raw[0]), abs(raw[1]))
                assert det % divisor == 0
                checked += 1
    return checked


def is_ten_energy_similitude(matrix):
    """Test M^T diag(5,1) M = lambda diag(5,1)."""
    a, b, c, d = matrix
    q11 = 5 * a * a + c * c
    q12 = 5 * a * b + c * d
    q22 = 5 * b * b + d * d
    return q12 == 0 and q11 == 5 * q22


def verify_ten_macro_arithmetic():
    determinants = tuple(determinant(matrix) for matrix in TEN_MACROS)
    assert determinants == (4, 2, 3, -8, -12, 12, -1)
    assert all(prime_support(det) <= {2, 3} for det in determinants)
    assert all(matrix[2] % 5 == 0 and matrix[3] % 5 != 0
               for matrix in TEN_MACROS)
    # The descent system is not merely the automorphism group of its form.
    assert not any(is_ten_energy_similitude(matrix) for matrix in TEN_MACROS)
    return determinants


def main():
    verify_forms()
    lattice_samples = verify_lattice_height()
    determinant_samples = verify_gcd_divides_determinant()
    determinants = verify_ten_macro_arithmetic()
    print("arithmetic-geometric structure certificate: PASS")
    print("primitive quadratic forms n=5..11: PASS")
    print("parameter-lattice height samples", lattice_samples)
    print("gcd-divides-determinant samples", determinant_samples)
    print("ten-macro determinants", determinants)
    print("ten macros are non-similitude descent maps: PASS")


if __name__ == "__main__":
    main()
