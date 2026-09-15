"""Exact finite root resources and targeted trace activation."""
import json
from pathlib import Path
from fractions import Fraction as F
from verify_b59_inverse_closure import verify as verify_closure
from verify_b53_inverse_closure import inverse
from verify_diagonal_resource_reduction import product,lower,upper


def in_ring(x):
    d = F(x).denominator
    for q in (2,3,5,7,11,17,19,23):
        while d%q == 0:
            d//=q
    return d == 1


def verify():
    verify_closure()
    data = json.loads(Path(__file__).with_name("b59_expanded_inverse_closure_certificate.json")
                      .read_text(encoding="utf-8"))
    ms = [tuple(map(F,n["matrix"])) for n in data["nodes"]]
    def normalized(m):
        return tuple(x/m[0] for x in m)
    assert normalized(product(ms[6],ms[0])) == lower(F(59,12))
    f = normalized(product(ms[0],ms[5]))
    g = normalized(product(ms[0],inverse(ms[12])))
    assert f == (1,0,24,F(16,7))
    assert g == (1,0,F(-936,19),F(-48,19))
    resources = [f,g]
    for i,j,slope in ((0,23,F(48,11)),(4,28,F(17,11)),
                       (7,24,F(-2,23)),(18,21,F(-6,35))):
        m = normalized(product(ms[i],inverse(ms[j])))
        assert m[1] == 0 and m[3] == slope
        resources.append(m)
    for m in resources:
        assert normalized(product(m,lower(59),inverse(m))) == lower(59*m[3])
    letters = [(i,sign,m if sign==1 else inverse(m)) for i,m in enumerate(ms) for sign in (1,-1)]
    flanks = [(str((i,s)),m) for i,s,m in letters]
    flanks += [(str((i,s,j,t)),product(m,n)) for i,s,m in letters for j,t,n in letters]
    activated = 0
    for target in ((-3,0,55,1),(-78,-3,1457,55)):
        found = None
        for label,flank in flanks:
            for _ in (0,):
                z = product(flank,target)
                if not z[1]:
                    continue
                t = -(z[0]+z[3])/z[1]
                if in_ring(t/59):
                    d = product(lower(t),flank)
                    cycle = product(d,target)
                    sq = product(cycle,cycle)
                    assert sq[0] and sq == (sq[0],0,0,sq[0])
                    assert product(d,target,d,target) == sq
                    found = (label,str(t))
                    break
            if found:
                break
        print("lower-root target activation",target,found)
        activated += bool(found)
    print("B59 lower root localization: PASS 6; lower-root activated targets",activated)
    cbase = (F(1),F(0),F(1),F(1))
    def upper_affine(index):
        z = product(inverse(cbase),ms[index],cbase)
        correction = -z[2]/z[0]
        assert in_ring(correction/59)
        f = product(lower(correction),z)
        return tuple(x/f[0] for x in f),correction
    f1,q1 = upper_affine(1)
    f8,q8 = upper_affine(8)
    assert q1 == q8 == F(118,21)
    root49 = product(f1,inverse(f8))
    assert root49 == upper(F(49,81))
    root27 = product(inverse(f1),root49,f1)
    assert root27 == upper(F(1,27))
    root1 = product(*([root27]*27))
    assert root1 == upper(1)
    f7,q7 = upper_affine(7)
    assert q7 == F(59,3) and f7[3] == F(2,2187)
    half_big = product(f7,root1,inverse(f7))
    half = product(half_big,*([inverse(root1)]*1093))
    assert half == upper(F(1,2))
    quarter_big = product(f7,half,inverse(f7))
    three_quarters = product(quarter_big,*([inverse(root1)]*546))
    quarter = product(root1,inverse(three_quarters))
    assert quarter == upper(F(1,4))
    eighth_big = product(f7,quarter,inverse(f7))
    three_eighths = product(eighth_big,*([inverse(root1)]*273))
    eighth = product(half,inverse(three_eighths))
    target_root = product(eighth,inverse(root1))
    assert target_root == upper(F(-7,8))
    # All following factors stay in C coordinates. No original-basis flank is used.
    f5,q5 = upper_affine(5)
    assert q5 == F(59,3) and f5 == (1,F(4,81),0,F(-7,243))
    # U(Z[1/(2*3*7)]) follows from U(1) and the invertible affine
    # slopes 3/49 and 2/2187, via coprime Bezout combinations.
    q_one = product(f1,upper(-f1[1]))
    q_five = product(f5,upper(-f5[1]))
    dilation = product(q_one,q_five,q_five)
    assert dilation == (1,0,0,F(1,3**9))
    assert product(dilation,root1,inverse(dilation)) == upper(3**9)
    assert product(inverse(dilation),root1,dilation) == upper(F(1,3**9))
    print("B59 basis-consistent unit upper root and ninth-power dilation: PASS")
    return dilation


if __name__ == "__main__":
    verify()
