"""Complete B59 congruence and terminal certificate."""
from fractions import Fraction as F
from math import gcd
from explore_b53_schreier_elimination import generators,pivot,triadic
from verify_b59_root_activation import verify as verify_roots
from verify_diagonal_resource_reduction import product,upper,lower,diagonal
from explore_thirteen_modular import Fold,modular_word
from b17_universal_atomic_words import average,nine_word


def verify():
    dilation = verify_roots()
    assert dilation == (1,0,0,F(1,3**9))
    rows = generators(59)
    assert len(rows) == 21
    for row in rows:
        a,b,c,d = map(F,row)
        if c:
            unit,j = next((F(sign*3**(9*j)),j) for j in range(59)
                          for sign in (-1,1)
                          if triadic(F(sign*3**(9*j)-a,c)))
        else:
            unit,j = a,0
        # D(unit) is projectively the (2*j)-th power of the certified dilation.
        assert unit**2 == 3**(18*j)
        t = (unit-a)/c if c else F(0)
        v = c/unit
        w = (b+t*d)/unit
        assert triadic(t) and triadic(v/59) and triadic(w)
        assert product(upper(-t),lower(v),diagonal(unit),upper(w)) == row
    fold = Fold()
    for row in rows:
        fold.loop(modular_word(row))
    table = fold.close()
    nodes = {fold.root(i) for i in range(len(fold.parent))}
    assert len(nodes) == 60
    assert all((node,l) in table for node in nodes for l in "su")
    checked = 0
    for x in range(-30,31):
        for y in range(-30,31):
            if gcd(x,y)!=1 or y%59==0:
                continue
            a = next(a for a in range(abs(y)) if (1-a*x)%y==0)
            b = (1-a*x)//y
            k = -a*pow(y,-1,59)%59
            a,b = a+k*y,b-k*x
            assert a%59==0 and a*x+b*y==1
            checked += 1
    state = [F(0)]*55+[F(1)]*3+[F(-3)]
    for triple in nine_word(tuple(range(50,59))):
        average(state,triple)
    assert not any(state)
    print("B59 complete positive Schreier decompositions: PASS 21")
    print("B59 independent cosets, Bezout transports and terminal: PASS 60",checked)


if __name__ == "__main__":
    verify()
