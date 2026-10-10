"""Independent exact checks for diagonal resource reduction."""
from fractions import Fraction as F
from math import isqrt


def product(*matrices):
    out = (F(1), F(0), F(0), F(1))
    for matrix in matrices:
        out = tuple(sum(out[2*i+k]*matrix[2*k+j] for k in range(2))
                    for i in range(2) for j in range(2))
    return out


def upper(x):
    return (F(1), F(x), F(0), F(1))


def lower(x):
    return (F(1), F(0), F(x), F(1))


def diagonal(v):
    v = F(v)
    return (v, F(0), F(0), 1/v)


def roots(v):
    v = F(v)
    return product(upper(1), lower(v-1), upper(-1/v), lower(-v*(v-1)))


def verify():
    count = 0
    for p in range(5, 150):
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        g = next(g for g in range(2, p)
                 if len({pow(g, j, p) for j in range(p-1)}) == p-1)
        logs = {pow(g, j, p): j for j in range(p-1)}
        for a in range(1, p):
            power = g ** logs[a]
            v = F(a, power)
            assert (v.numerator-v.denominator) % p == 0
            assert roots(v) == diagonal(v)
            assert product(roots(v), diagonal(power)) == diagonal(a)
            k = -pow(a, -1, p) % p
            lifted = product(roots(F(k, g**logs[k])), diagonal(g**logs[k]))
            out = product(lower(F(-(a*k+1), k)),
                          tuple(-x for x in lifted), upper(F(1, k)))
            assert out == (-k, -1, a*k+1, a)
            count += 1
    print("one-seed lifts and Schreier decompositions: PASS", count)
    for v in (F(-2), F(1, 4), F(10), F(-8), F(1)):
        assert roots(v) == diagonal(v)
    print("signed and fractional four-root identities: PASS 5")
    verify_torus_absorption()
    verify_finite_localization_seeds()
    print("Physical realizability remains a hypothesis.")


def absorb_diagonals(letters):
    scale = F(1)
    word = []
    for kind, value in letters:
        value = F(value)
        if kind == "D":
            scale *= value
        elif kind == "U":
            word.append((kind, scale**2*value))
        else:
            assert kind == "L"
            word.append((kind, value/scale**2))
    return scale, [(kind, value/scale**2 if kind == "U" else value*scale**2)
                   for kind, value in word]


def evaluate(letters):
    return product(*(dict(U=upper, L=lower, D=diagonal)[kind](value)
                     for kind, value in letters))


def verify_torus_absorption():
    checked = 0
    for p in (7, 11, 17, 29, 47, 53, 59, 431):
        for j in range(1, p):
            k = -pow(j, -1, p) % p
            c = j*k+1
            base = [("L", F(-c, k)), ("D", -k), ("U", F(1, k))]
            # Mixed diagonal/root words test accumulated conjugation, not only one pivot.
            letters = [("D", 2), ("U", F(1, 3))] + base + [
                ("L", F(p, 2)), ("D", F(1, 3)), ("U", -2)]
            h = evaluate(letters)
            scale, roots_only = absorb_diagonals(letters)
            e = evaluate(roots_only)
            assert product(diagonal(scale), e) == h
            for kind, value in roots_only:
                assert value.denominator % p
                if kind == "L":
                    assert value.numerator % p == 0
            # h^{-1}e2 is a legal rational direction; e must send it to scale*e2.
            a, b, c, d = h
            x, y = -b, a
            assert e[0]*x+e[1]*y == 0
            assert e[2]*x+e[3]*y == scale
            assert y.numerator % p
            checked += 1
    print("torus-free root compilation and exact terminal transports: PASS", checked)


def prime(n):
    return n >= 2 and not any(n % d == 0 for d in range(2, isqrt(n)+1))


def verify_finite_localization_seeds():
    counts = [0, 0]
    s = (F(0), F(-1), F(1), F(0))
    si = (F(0), F(1), F(-1), F(0))
    for p in (7, 11, 17, 29, 47, 53, 59):
        h = (p-1)//2
        for q in range(2, h+1):
            if not prime(q):
                continue
            e = next(e for e in range(1, p) if pow(q, e, p) == 1)
            v = q**e
            # The lower factors are integer powers of the single L(p) seed.
            assert (v-1) % p == (-v*(v-1)) % p == 0
            d = roots(v)
            assert d == diagonal(v)
            di = diagonal(F(1, v))
            assert product(di, upper(1), d) == upper(F(1, v*v))
            assert product(d, lower(p), di) == lower(F(p, v*v))
            # Additive powers recover every exponent up to this denominator depth.
            for a in range(2*e+1):
                assert F(q**(2*e-a), v*v) == F(1, q**a)
            counts[0] += 1
        for j in range(-h, h+1):
            if not j:
                continue
            k = -pow(j, -1, p) % p
            if k > h:
                k -= p
            assert 0 < abs(k) <= h
            matrix = product(s, upper(j), s, upper(-k), si)
            assert matrix == (-k, -1, j*k+1, j)
            assert product(lower(F(-(j*k+1), k)), diagonal(-k),
                           upper(F(1, k))) == matrix
            counts[1] += 1
        assert product(s, upper(h), upper(1), upper(h), si) == lower(-p)
    print("finite localization seeds and signed Schreier reduction: PASS", *counts)


if __name__ == "__main__":
    verify()
