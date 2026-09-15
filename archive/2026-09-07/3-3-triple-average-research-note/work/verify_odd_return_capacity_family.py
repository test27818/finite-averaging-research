"""Exact symbolic coefficient ledger for a sparse odd-return family."""
from fractions import Fraction as F


def verify():
    for h in (2, 4, 6, 8, 10):
        s = 3**h
        m = 6*s-5
        a = (F(2, 3), F(1, 3))
        b = tuple((2*a[d]+(1 if d == 1 else s-3))/s for d in range(2))
        assert b == (F(3*s-5, 3*s), F(5, 3*s))
        background = m-s+1
        chosen_u = m-s
        assert chosen_u > 0 and background-chosen_u == 1
        x = ((a[0]+(s-1)*b[0]+chosen_u)/m,
             (a[1]+(s-1)*b[1])/m)
        assert x == (1-F(1, 3*s), F(1, 3*s))
        y = ((-m+b[0])/3, (-3+1+b[1])/3)
        assert y == (-(m*x[0]+1)/3, -m*x[1]/3)
        assert x[0]*y[1]-x[1]*y[0] == F(1, 9*s)
        if h == 2:
            assert (*x, *y) == (F(26,27), F(1,27), F(-1301,81), F(-49,81))
    print("odd return family coefficient and multiplicity certificates: PASS 5")
    count = 0
    for m in range(7,151):
        for k in (1,3,5,7):
            t = F(1,3**k)
            output = [t]*m + [-m*t/3]*3 + [F(0)]
            assert sum(output) == 0
            positive = sum(max(x,0) for x in output)
            assert positive == m*t
            assert (positive <= 3) == (m <= 3**(k+1))
            for scale in (F(1,9),F(-1,9)):
                assert sum(max(scale*x,0) for x in output) == abs(scale)*m*t
            count += 1
    assert F(82,27) > 3
    print("exact return positive-mass and physical-scale bounds: PASS",count)
    for m in range(7,151):
        for k in (1,3,5,7):
            t = F(1,3**k)
            output = [1-t]*m+[-(m*(1-t)+1)/3]*3+[F(1)]
            positive = sum(max(x,0) for x in output)
            assert sum(output) == 0
            assert positive == m*(1-t)+1
            assert (positive <= m) == (m*t >= 1)
            bound = min(F(3,m*t),F(m,positive))
            for scale in (bound,-bound):
                assert sum(max(scale*x,0) for x in output) <= m
                assert abs(scale)*m*t <= 3
    # For m=97: k<=3 violates the upper bound; every odd k>=5 the lower.
    assert 3**4 < 97 < 3**5
    assert F(97,27)>3 and F(97,243)<1
    print("two-sided exact-return bounds and p101 odd-exponent gap: PASS")
    print("Child solvability is a hypothesis; no positive inverse is asserted.")


if __name__ == "__main__":
    verify()
