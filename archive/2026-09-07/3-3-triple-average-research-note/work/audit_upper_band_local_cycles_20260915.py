"""Independent finite audit of the local-cycle lemma used by the new proofs.

No research implementation is imported. These exhaustive finite checks test the
stated hypotheses and small-prime exceptions; the unbounded lift is a written
binomial/Cayley-Hamilton argument, not inferred from these counts.
"""

from math import gcd


def orbit_length(matrix, modulus):
    a, b, c, d = matrix
    reciprocals = {u: pow(u, -1, modulus) for u in range(modulus)
                   if gcd(u, modulus) == 1}
    visited = set()
    x = 0
    while x not in visited:
        visited.add(x)
        x = (a*x+b)*reciprocals[(c*x+d) % modulus] % modulus
    assert x == 0, (matrix, modulus, x)
    return len(visited)


def exhaustive_layer(ell, modulus):
    accepted = excluded = 0
    for a in range(modulus):
        if a % ell == 0:
            continue
        for d in range(a % ell, modulus, ell):
            for b in range(modulus):
                if b % ell == 0:
                    continue
                for c in range(0, modulus, ell):
                    trace, determinant = a+d, a*d-b*c
                    if ell == 2 and trace % 4 != 2:
                        excluded += 1
                        continue
                    if ell == 3:
                        discriminant_ratio = ((trace*trace-4*determinant)
                                              * pow(trace*trace, -1, 9)) % 9
                        if discriminant_ratio == 6:
                            excluded += 1
                            continue
                    matrix = (a, b, c, d)
                    assert orbit_length(matrix, modulus) == modulus, matrix
                    accepted += 1
    print(f"local cycle modulus={modulus}: PASS accepted={accepted} excluded={excluded}")


def finite_deep_root_factorization(modulus, h):
    assert modulus % (h*h) == 0

    def multiply(x, y):
        a, b, c, d = x
        e, f, g, k = y
        return ((a*e+b*g) % modulus, (a*f+b*k) % modulus,
                (c*e+d*g) % modulus, (c*f+d*k) % modulus)

    count = 0
    for a in range(1, modulus, h*h):
        for b in range(0, modulus, h*h):
            for c in range(0, modulus, h*h):
                reciprocal = pow(a, -1, modulus)
                d = (1+b*c)*reciprocal % modulus
                assert d % (h*h) == 1
                t = (a-1)//h
                word = ((1, 0, c*reciprocal, 1), (1, h, 0, 1),
                        (1, 0, t, 1), (1, -h*reciprocal, 0, 1),
                        (1, 0, -t*a, 1), (1, b*reciprocal, 0, 1))
                result = (1, 0, 0, 1)
                for factor in word:
                    assert factor[1] % h == factor[2] % h == 0
                    result = multiply(result, factor)
                assert result == (a, b, c, d)
                count += 1
    print(f"deep roots modulus={modulus} h={h}: PASS matrices={count}")


def main():
    if not __debug__:
        raise RuntimeError("Assertions are required.")
    for ell, modulus in ((2, 16), (3, 27), (5, 25)):
        exhaustive_layer(ell, modulus)
    assert orbit_length((1, 1, 6, 1), 9) == 3
    assert orbit_length((1, 1, 0, 3), 8) == 4
    print("excluded mod9 and mod4 hypotheses: PASS two negative controls")
    for modulus, h in ((16, 2), (81, 3)):
        finite_deep_root_factorization(modulus, h)
    print("independent upper-band common-lemma audit: PASS")


if __name__ == "__main__":
    main()
