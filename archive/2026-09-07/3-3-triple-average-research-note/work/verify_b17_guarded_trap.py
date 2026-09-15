"""Exact local invariance and height checks for the current B17 library."""

from math import gcd

from explore_b17_guarded_returns import generate, edges, primitive, height


def verify():
    rows = generate()
    assert len(rows) == 10
    assert {row["guard"] for row in rows} == {
        (-2,-2,13), (-3,-1,13), (-1,-2,14), (-2,-1,14), (-1,-1,5),
    }
    # A has slope t -> -(13+t)/3 at every auxiliary prime.
    assert (-(13+3)*pow(3,-1,5)) % 5 == 3
    assert (-(13+2)*pow(3,-1,7)) % 7 == 2
    squares = {x*x % 13 for x in range(1,13)}
    nonsquares = set(range(1,13))-squares
    assert 2 in nonsquares and 12 in squares and 10 in squares
    assert {(4*x) % 13 for x in nonsquares} == nonsquares
    assert (1+2*2) % 7 and (2+2) % 7
    assert (1+3) % 5

    # Exact coefficient identity H(A z)-H(z)=221 u^2.
    assert height((3,-13))-height((1,0)) == 221
    assert height((0,-1))-height((0,1)) == 0
    assert height((3,-14))-height((1,1)) == 221

    checked = 0
    for j in range(20):
        u, v = 1, 93+23205*j
        initial = height((u,v))
        assert gcd(u,v) == 1 and (u-v) % 17
        for k in range(30):
            canonical = primitive(u,v)
            actual = list(edges(canonical, rows))
            assert len(actual) == 1 and actual[0][1] == "A"
            assert actual[0][0] == primitive(3*u,-13*u-v)
            assert gcd(u,v) == 1 and (u+v) % 3
            assert u == 3**k
            assert height((u,v)) == initial+221*((9**k-1)//8)
            next_u, next_v = 3*u, -13*u-v
            assert gcd(next_u,next_v) == 1
            assert height((next_u,next_v))-height((u,v)) == 221*u*u > 0
            assert next_u != 0 and next_v != 0
            u,v = next_u,next_v
            checked += 1
    print("B17 guarded library local trap: PASS")
    print("B17 only-A trajectories and exact height growth: PASS", checked)


if __name__ == "__main__":
    verify()
