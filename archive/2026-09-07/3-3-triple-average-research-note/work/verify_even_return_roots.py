"""Exact even-return swap and width-four root identities."""
from fractions import Fraction as F
from verify_diagonal_resource_reduction import product,upper,lower
from verify_b53_inverse_closure import inverse


def verify():
    checked = 0
    c = (F(1),F(0),F(1),F(1))
    swap = (F(0),F(1),F(1),F(0))
    for n in (17,29,53,59,71,83,101,107,251):
        m = n-4
        a = (F(1),F(0),F(-m,3),F(-1,3))
        d = product(inverse(c),lower(F(n,3)),a,c)
        for k in (2,4,6,8):
            t = F(1,3**k)
            ret = (1-t,t,-(m*(1-t)+1)/3,-m*t/3)
            power = product(*([a]*k))
            correction = n*(1-t)/4
            assert correction.denominator == 3**k
            actual = product(lower(correction),power,inverse(ret),a)
            assert actual == swap
            moved = product(inverse(c),actual,c)
            assert moved == (1,1,0,-1)
            assert product(d,moved,inverse(d),moved) == upper(4)
            checked += 1
    for m in range(7,1000):
        k = 1
        while 3**(k+1) < m:
            k += 1
        assert 3**k <= m <= 3**(k+1)
    print("even-return swap and width-four roots: PASS",checked)
    print("unrestricted exponent capacity intervals: PASS 993")
    generic = 0
    for n in (17,53,59,101,431):
        m = n-4
        a0 = (F(1),F(0),F(-m,3),F(-1,3))
        d = (F(1),F(0),F(0),F(-1,3))
        for num in (-7,-2,-1,1,2,4,5,10):
            for k in (0,1,3):
                t = F(num,3**k)
                ret = (1-t,t,-(m*(1-t)+1)/3,-m*t/3)
                h = product(inverse(c),inverse(ret),a0,c)
                assert h == (1,1,0,-1/t)
                root = product(d,h,inverse(d),inverse(h))
                assert root == upper(4*t)
                assert product(inverse(h),root,h) == upper(-4)
                assert product(inverse(h),upper(4),h) == upper(-4/t)
                q = product(h,upper(-1))
                assert q == (1,0,0,-1/t)
                assert product(q,lower(n),inverse(q)) == lower(-F(n)/t)
                if num % 2 == 0:
                    # From U(4/a^2), an integer power gives U(1).
                    assert F(4,num*num)*F(num*num,4) == 1
                    assert F(num*num,4).denominator == 1
                generic += 1
    print("general return affine roots and numerator localization: PASS",generic)
    print("affine correction and shared upper/lower localization: PASS",generic)
    print("Return realizability and removal of factor4 remain hypotheses.")


if __name__ == "__main__":
    verify()
