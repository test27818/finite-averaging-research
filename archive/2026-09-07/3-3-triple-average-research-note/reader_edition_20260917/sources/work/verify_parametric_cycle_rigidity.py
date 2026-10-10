"""Exact polynomial coefficient checks for the B59 isolated cycle."""
from fractions import Fraction as F
from verify_diagonal_resource_reduction import product


def matrices(p):
    return ((77,4,-24*p-16,-p-21),(60,3,-5*p+14,-10))


def verify():
    checked = 0
    for p in range(-50,151):
        a,b = matrices(p)
        ba = product(b,a)
        assert ba[0]+ba[3] == 4838-82*p
        assert a[0]*a[3]-a[1]*a[2] == 19*p-1553
        assert b[0]*b[3]-b[1]*b[2] == 15*p-642
        assert (ba[0]+ba[3] == 0) == (p == 59)
        checked += 1
    a,b = matrices(59)
    ba = product(b,a)
    square = product(ba,ba)
    assert square == (104976,0,0,104976)
    physical = product(tuple(F(x,2187) for x in b),
                       tuple(F(x,81) for x in a))
    assert product(physical,physical) == (F(16,3**14),0,0,F(16,3**14))
    print("B59 parametric isolated-cycle identities: PASS",checked)
    print("General finite-hit statement is polynomial, not sampled extrapolation.")


if __name__ == "__main__":
    verify()
