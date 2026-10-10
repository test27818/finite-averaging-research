"""Independent exact replay and arithmetic checks for two six-step macros."""

from collections import Counter
from fractions import Fraction as F
from math import gcd

from verify_bn_arithmetic_structure import core, average, form_value, reduced_forms


T = (9, 6, -6, -7)
S = (0, 3, -9, -8)
BASE_FORM = (6, 4, 1)


def symbolic_words():
    u, v = (F(1), F(0)), (F(0), F(1))
    w = (F(-8), F(-3))
    output = {}
    for name in ("T", "S"):
        state = core(u, v)
        word = []

        def take(triple):
            word.append(triple)
            return average(state, triple)

        a = take((w, u, u))
        if name == "T":
            b = take((a, u, u))
            for _ in range(3):
                c = take((b, v, u))
            d = take((a, c, u))
        else:
            b = take((a, a, u))
            c = take((b, v, u))
            d = take((a, c, u))
            for _ in range(2):
                assert take((b, v, u)) == c
        assert state == core(c, d)
        expected = T if name == "T" else S
        assert c+d == tuple(F(x, 27) for x in expected)
        output[name] = tuple(word)
    return output


def pullback(form, matrix):
    A, B, C = form
    a, b, c, d = matrix
    return (A*a*a+B*a*c+C*c*c,
            2*A*a*b+B*(a*d+b*c)+2*C*c*d,
            A*b*b+B*b*d+C*d*d)


def verify():
    words = symbolic_words()
    assert all(len(word) == 6 for word in words.values())
    expected_forms = {"T": (306, 336, 97), "S": (81, 36, 22)}
    checked = 0
    for name, M in (("T", T), ("S", S)):
        image_form = pullback(BASE_FORM, M)
        assert image_form == expected_forms[name]
        A, B, C = (243*x-y for x, y in zip(BASE_FORM, image_form))
        assert A > 0 and C > 0 and 4*A*C-B*B > 0
        for u in range(-70, 71):
            for v in range(-70, 71):
                if gcd(abs(u), abs(v)) != 1:
                    continue
                a, b, c, d = M
                x, y = a*u+b*v, c*u+d*v
                g = gcd(abs(x), abs(y))
                expected_g = gcd(27, v-3*u if name == "T" else 9*u+8*v)
                assert g == expected_g
                if (u-v) % 2:
                    assert (x//g-y//g) % 2
                if g == 27:
                    assert 3*form_value(BASE_FORM, x//g, y//g) < form_value(BASE_FORM, u, v)
                if (u-v) % 3:
                    condition = (v-(30 if name == "T" else 36)*u) % 81 == 0
                    assert ((x//g-y//g) % 3 == 0) == condition
                checked += 1

    # Iterated R pullbacks stay primitive and their discriminants grow.
    R = (6, 3, -19, -8)
    f = BASE_FORM
    for k in range(1, 5):
        f = pullback(f, R)
        A, B, C = f
        assert gcd(A, gcd(B, C)) == 1
        assert B*B-4*A*C == -8*3**(4*k)
        if k <= 2:
            assert len(reduced_forms(-8*3**(4*k))) == 2*3**(2*k-1)
    print("B12 six-step symbolic replay and local descent: PASS", checked)
    print("B12 iterated pullback conductor growth: PASS")


if __name__ == "__main__":
    verify()
