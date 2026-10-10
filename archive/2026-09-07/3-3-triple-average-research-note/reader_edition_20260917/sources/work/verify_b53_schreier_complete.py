"""Complete finite Schreier realization using previously physical B53 roots."""
from fractions import Fraction as F
from math import gcd
from explore_b53_schreier_elimination import generators,pivot,triadic
from verify_diagonal_resource_reduction import product,upper,lower,diagonal
from verify_b53_triadic_roots import verify as verify_roots
from explore_thirteen_modular import Fold,modular_word
from b17_universal_atomic_words import average,nine_word


def verify():
    verify_roots()
    rows = generators(53)
    assert len(rows) == 20
    fold = Fold()
    for row in rows:
        fold.loop(modular_word(row))
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 54
    assert all((node,letter) in table for node in nodes for letter in "su")
    for row in rows:
        a,b,c,d = map(F,row)
        assert a*d-b*c == 1 and c%53 == 0
        result = pivot(row)
        assert result is not None
        unit,exponent = result
        assert abs(unit) == 3**exponent
        t = (unit-a)/c if c else F(0)
        v = c/unit
        w = (b+t*d)/unit
        assert triadic(t) and triadic(v/53) and triadic(w)
        assert product(upper(-t),lower(v),diagonal(unit),upper(w)) == row
        # Corrected standard macro supplies D(unit) projectively by even powers.
        dilation = (F(1),F(0),F(0),F(-1,3))
        power = product(*([dilation]*(2*exponent)))
        assert tuple(x*unit for x in power) == diagonal(unit)
    checked = 0
    for x in range(-30,31):
        for y in range(-30,31):
            if gcd(x,y) != 1 or y%53 == 0:
                continue
            a = next(a for a in range(abs(y)) if (1-a*x)%y == 0)
            b = (1-a*x)//y
            k = -a*pow(y,-1,53)%53
            a,b = a+k*y,b-k*x
            assert a%53 == 0 and a*x+b*y == 1
            assert y*b+x*a == 1
            checked += 1
    print("B53 all complete Schreier loops positively decomposed: PASS 20")
    print("B53 legal Bezout transports: PASS",checked)
    state = [F(0)]*49+[F(1)]*3+[F(-3)]
    for triple in nine_word(tuple(range(44,53))):
        average(state,triple)
    assert not any(state)
    print("B53 independent complete cosets and physical terminal: PASS 54")
    print("General coverage follows from Schreier generation and Bezout proof.")


if __name__ == "__main__":
    verify()
