"""Exact identity checks for explicit gap bounds and the common Hecke form."""
from fractions import Fraction as F
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_five_bounded_runs import evaluate,q5

A=(-3,0,-1,1)
B=(1,-1,0,-3)
T=(1,2,0,3)
U=(0,1,1,1)
I=(1,0,0,1)

def mul(X,Y):
    return (X[0]*Y[0]+X[1]*Y[2],X[0]*Y[1]+X[1]*Y[3],
            X[2]*Y[0]+X[3]*Y[2],X[2]*Y[1]+X[3]*Y[3])

def det(X):return X[0]*X[3]-X[1]*X[2]

def mv(M,z):return (M[0]*z[0]+M[1]*z[1],M[2]*z[0]+M[3]*z[1])

def norm(z):return z[0]*z[0]+z[0]*z[1]-z[1]*z[1]

def line(z,q):
    a,b=z
    if a%3:return (1,b*pow(a,-1,q)%q)
    return (a*pow(b,-1,q)%q,1)

def scalar_orbit(m):
    q=3**m;period=4*3**(m-1);V=I;orbit={}
    for j in range(period):
        key=line((V[0],V[2]),q)
        assert key not in orbit
        orbit[key]=(j,V)
        V=mul(U,V)
    assert line((V[0],V[2]),q)==(1,0)
    assert len(orbit)==period
    return orbit

def hecke_checks():
    checked=0;levels=[]
    for L in range(7):
        f=3**(L+1);orbit=scalar_orbit(L+1)
        for bits in product((0,1),repeat=L):
            W=I
            for bit in bits:W=mul(W,(A,B)[bit])
            M=mul(T,W);j,V=orbit[line(mv(M,(1,-1)),f)]
            assert j%4==0
            va,vb,vc,vd=V
            N=mul((vd,-vb,-vc,va),M)
            dv=det(V)
            assert all(x%dv==0 for x in N)
            N=tuple(x//dv for x in N)
            assert N[2]%f==N[3]%f==0
            C=(N[0],N[1],N[2]//f,N[3]//f)
            assert det(C)==(-1)**L
            assert mul(V,mul((1,0,0,f),C))==M
            a,b,c,d=W
            coeff=(a*a+7*a*c+c*c,2*a*b+7*(a*d+b*c)+2*c*d,b*b+7*b*d+d*d)
            assert gcd(gcd(coeff[0],coeff[1]),coeff[2])==1
            assert coeff[1]**2-4*coeff[0]*coeff[2]==5*f*f
            for z in ((1,-1),(2,3),(-4,5)):
                x,y=mv(C,z)
                assert q5(mv(W,z))==x*x+f*x*y-f*f*y*y
                assert q5(z)==norm(mv(T,z))
            checked+=1
        levels.append({'word_length':L,'unit_projective_orbit_size':len(orbit),'words':2**L})
    return {'levels':levels,'unimodular_reductions_checked':checked}

def ceil_log3(n):
    c=0;q=1
    while q<n:q*=3;c+=1
    return c

def gap_checks():
    rng=Random(20260917);checked=0;table=[]
    for r in range(1,7):
        C=ceil_log3(46*r*16**r);Kmax=C*(3**r-1)//2
        table.append({'runs':r,'C':C,'Kmax':Kmax})
        samples=[tuple([1]*r),tuple(range(1,r+1)),tuple([100]*r)]
        samples += [tuple(rng.randrange(1,121) for _ in range(r)) for _ in range(40)]
        for exps in samples:
            ordered=sorted(exps);K=0;cut=None
            for a in ordered:
                if a>2*K+C:cut=a;break
                K+=a
            assert K<=Kmax
            ts=[F(1,(-3)**a) for a in exps]
            rounded=[F(0) if cut is not None and a>=cut else t for a,t in zip(exps,ts)]
            z=evaluate(ts);y=evaluate(rounded)
            H=4**r*3**K
            assert all((H*t).denominator==1 for t in y)
            assert all((t.numerator*pow(t.denominator,-1,5))%5==e for t,e in zip(y,(1,4)))
            assert abs(q5(y))>=F(1,H*H)
            if cut is not None:
                assert abs(q5(z)-q5(y))<=F(23*r,3**cut)
                assert F(23*r,3**cut)<F(1,2*H*H)
            assert abs(q5(z))>=F(1,2*H*H)
            checked+=1
    return {'explicit_constants':table,'gap_rounding_instances':checked}

def valuation(n):
    assert n
    v=0
    while n%3==0:n//=3;v+=1
    return v

def pell_checks():
    u,v=1,-1;checked=0
    for k in range(1,1001):
        u,v=-7*u-v,u
        assert q5((u,v))==-5
        assert valuation(u)==valuation(2*k+1)
        assert valuation(v)==valuation(2*k-1)
        length=valuation(2*k+1)+valuation(2*k-1)
        assert 3**length<=2*k+1
        checked+=1
    return {'Pell_valuation_instances':checked,'scope':'Exact first-run formula only; not full D1 classification.'}

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    result={'explicit_gap':gap_checks(),'common_hecke_form':hecke_checks(),
            'D1_first_run':pell_checks(),
            'scope':'General proofs in accompanying note; finite checks do not prove arbitrary-switch fixed-D finiteness.'}
    Path(__file__).with_name('five_explicit_gap_and_hecke_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
