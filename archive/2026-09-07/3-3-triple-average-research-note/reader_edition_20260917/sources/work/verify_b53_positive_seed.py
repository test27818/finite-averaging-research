"""Fixed B53 physical templates and an exact fourth-order projective cycle."""
from fractions import Fraction as F
from verify_bn_integer_templates import replay, physical_matrix
from verify_diagonal_resource_reduction import product

SOURCE = ((-49,-3,1),(0,1,3),(1,0,49))
AFTER = ((-441,-27,1),(0,9,2),(8,1,9),(9,0,41))
ROWS = (
    dict(source=SOURCE, first=dict(counts=(0,1,8),scale=(1,9)),
         after_first=AFTER, middle=dict(counts=(0,0,2,1),scale=(1,3)),
         before_final=((-1323,-81,1),(0,27,2),(24,3,7),(25,2,3),(27,0,40)),
         final=dict(counts=(0,1,6,2,40),singleton=3),
         raw=(78,3,-1299,-51),denominator=3),
    dict(source=SOURCE, first=dict(counts=(0,1,8),scale=(1,9)),
         after_first=AFTER, middle=dict(counts=(0,1,7,19),scale=(1,27)),
         before_final=((-11907,-729,1),(0,243,1),(216,27,2),(227,16,27),(243,0,22)),
         final=dict(counts=(0,1,1,26,21),singleton=3),
         raw=(687,42,-11448,-702),denominator=3),
)


def verify():
    matrices = []
    for row in ROWS:
        calls = replay(53, row)
        assert all(size in (3,9,27,49) for size, *_ in calls)
        matrices.append(physical_matrix(row))
    a, b = matrices
    assert a == tuple(F(-x,27) for x in (-26,-1,433,17))
    assert b == tuple(F(-x,243) for x in (-229,-14,3816,234))
    c = product(b,a)
    square = product(c,c)
    fourth = product(square,square)
    lam = fourth[0]
    assert lam and fourth == (lam,0,0,lam)
    assert square[1] or square[2] or square[0] != square[3]
    # Execution A,B,A,B,A,B,A,B: remove first A or last B for inverse words.
    ainv_scaled = product(b,a,b,a,b,a,b)
    binv_scaled = product(a,b,a,b,a,b,a)
    assert product(ainv_scaled,a) == product(a,ainv_scaled) == fourth
    assert product(binv_scaled,b) == product(b,binv_scaled) == fourth
    assert lam.numerator * pow(lam.denominator,-1,53) % 53 == 1
    print("B53 fixed templates and positive seven-template inverses: PASS 2")
    print("physical cycle scalar", lam)
    ret = (F(26,27), F(1,27), F(-1301,81), F(-49,81))
    # A^{-1} R is an involution; use the already physical scaled inverse.
    flank = ainv_scaled
    cycle = product(flank, ret, flank, ret)
    rho = cycle[0]
    assert rho and cycle == (rho,0,0,rho)
    retinv_scaled = product(flank,ret,flank)
    assert product(retinv_scaled,ret) == product(ret,retinv_scaled) == cycle
    from verify_odd_return_capacity_family import verify as verify_return
    verify_return()
    print("B53 odd return positive inverse from fixed A seed: PASS 1")
    print("B53 completeness and root groups remain unproved.")


if __name__ == "__main__":
    verify()
