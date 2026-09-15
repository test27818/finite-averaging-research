"""Exact physical Reynolds identity and fixed-point trace expansions."""
from fractions import Fraction as F
from itertools import product as tuples
from math import isqrt
from verify_nonsplit_projective_layers import partition


def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))


def power(a,k):
    out = tuple(range(len(a)))
    for _ in range(k):
        out = compose(a,out)
    return out


def tau(p,c=0):
    out=[]
    for x in range(p):
        y=(x-c)%p
        if y in (0,p-1):
            z=y
        else:
            z=-pow(y+1,-1,p)%p
        out.append((z+c)%p)
    return tuple(out)


def shift(p,c):
    return tuple((x+c)%p for x in range(p))


def reynolds(permutation):
    n=len(permutation)
    powers=[power(permutation,k) for k in range(3)]
    return [[sum(F(int(q[j]==i),3) for q in powers) for j in range(n)] for i in range(n)]


def trace_product(a,b):
    return sum(a[i][j]*b[j][i] for i in range(len(a)) for j in range(len(a)))


def verify():
    checked=words=0
    for p in range(5,80):
        if p%3!=2 or any(p%q==0 for q in range(2,isqrt(p)+1)):
            continue
        q=tau(p)
        assert power(q,3)==tuple(range(p))
        assert sum(q[i]==i for i in range(p))==2
        matrix=reynolds(q)
        blocks=partition(0,p)
        label={x:i for i,b in enumerate(blocks) for x in b}
        expected=[[F(int(label[i]==label[j]),len(blocks[label[i]]))
                   for j in range(p)] for i in range(p)]
        assert matrix==expected
        for a,b in ((1,2),(2,3),(-1,3)):
            qa, qb = tau(p,a%p),tau(p,b%p)
            direct=trace_product(reynolds(qb),reynolds(qa))
            total=0
            for i,j in tuples(range(3),repeat=2):
                word=compose(power(qb,j),power(qa,i))
                total+=sum(word[x]==x for x in range(p))
                words+=1
            assert direct==F(total,9)
        checked+=1
    print("nonsplit physical C3 Reynolds layers: PASS",checked)
    print("fixed-point trace-word expansions: PASS",words)
    print("No positive unit or all-prime terminal theorem is asserted.")


if __name__=="__main__":
    verify()
