"""Linear-size orbit counts for the analytic nonsplit trace formula."""
from fractions import Fraction as F
from math import isqrt
from verify_nonsplit_projective_layers import partition,transition,determinant


def verify():
    count = full = 0
    for p in range(5,1000):
        if p%3 != 2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
            continue
        blocks = partition(0,p)
        label = {x:i for i,block in enumerate(blocks) for x in block}
        adjacent = sum(label[x]==label[(x+1)%p] for x in range(p))
        chi = 1 if p%4==1 else -1
        assert adjacent == 1+chi
        trace = F(adjacent,3)-1
        assert trace == F(chi-2,3)
        if p<=59:
            target = tuple(tuple((x+1)%p for x in block) for block in blocks)
            m = transition(blocks,target)
            assert sum(m[i][i] for i in range(len(m)))-1 == trace
            det = determinant(m)
            r = (p-2)//3
            integer_det = det*3**r
            assert integer_det.denominator == 1
            if chi == 1 and det:
                invariant = trace**(r+1)/det
                assert invariant == F((-1)**(r+1),3*integer_det)
                assert invariant.denominator != 1
            full += 1
        count += 1
    print("nonsplit trace quadratic-character formula: PASS",count)
    print("independent matrix and integral determinant cross-checks: PASS",full)
    print("All p=5 mod12 exclusion uses the analytic proof, not sampling.")
    general = 0
    for p in range(5,300):
        if p%3 != 2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
            continue
        blocks = partition(0,p)
        label = {x:i for i,block in enumerate(blocks) for x in block}
        for c in range(1,p):
            adjacent = sum(label[x]==label[(x-c)%p] for x in range(p)
                           if x not in (0,p-1))
            chi = lambda a: 0 if a%p==0 else (1 if pow(a%p,(p-1)//2,p)==1 else -1)
            d1,d2 = (c-1)*(c+3),(c-3)*(c+1)
            formula = 2+chi(d1)+chi(d2)-int(c==1)-int(c==p-1)
            assert adjacent == formula
            centered = F(formula,3)-1
            assert centered in (F(-1),F(-2,3),F(-1,3),F(0),F(1,3))
            general += 1
    print("all-shift quadratic-character trace values: PASS",general)


if __name__ == "__main__":
    verify()
