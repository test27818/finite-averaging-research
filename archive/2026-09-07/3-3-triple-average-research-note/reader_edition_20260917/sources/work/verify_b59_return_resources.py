"""Exact B59 resource inventory and conditional Schreier elimination."""
from fractions import Fraction as F
from compile_bn_integer_templates import compile_returns
from verify_bn_integer_templates import replay,physical_matrix
from audit_bn_current_cycles import a_power_candidates
from explore_b53_schreier_elimination import generators,pivot,triadic
from verify_diagonal_resource_reduction import product,upper,lower,diagonal


def verify():
    rows,_ = compile_returns(59,True,True,True)
    hits = {}
    for key,row in rows.items():
        a,b,c,d = physical_matrix(row)
        scale = a+b
        if not scale:
            continue
        t = b/scale
        if (c/scale,d/scale) != (-(55*(1-t)+1)/3,-55*t/3):
            continue
        replay(59,row)
        assert scale == 1
        assert 1 <= 55*t <= 3
        assert not a_power_candidates(59,key)
        hits[t] = key
    assert set(hits) == {F(4,81),F(13,243),F(1,27),
                         F(26,729),F(38,729),F(37,729)}
    assert len([t for t in hits if t.numerator%2 == 0]) == 3
    print("B59 physical return inventory and all-exponent A-power boundary: PASS 6")
    targets = generators(59)
    assert len(targets) == 21
    for matrix in targets:
        a,b,c,d = map(F,matrix)
        result = pivot(matrix)
        assert result is not None
        unit,j = result
        t = (unit-a)/c if c else F(0)
        v = c/unit
        w = (b+t*d)/unit
        assert triadic(t) and triadic(v/59) and triadic(w)
        assert abs(unit) == 3**j
        assert product(upper(-t),lower(v),diagonal(unit),upper(w)) == matrix
    print("B59 conditional complete triadic Schreier decompositions: PASS 21")
    print("Missing physical inverse/root hypotheses: B59 remains unresolved.")


if __name__ == "__main__":
    verify()
