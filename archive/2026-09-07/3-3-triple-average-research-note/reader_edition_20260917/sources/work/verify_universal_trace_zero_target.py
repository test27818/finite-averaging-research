"""Exact checks for the symbolic trace-zero return target and scale boundary."""
from fractions import Fraction as F
from verify_diagonal_resource_reduction import product
from math import isqrt


def verify():
    checked=0
    for p in range(11,200):
        if any(p%q==0 for q in range(2,isqrt(p)+1)):
            continue
        m=p-4
        t=F(9,2*p+1)
        a=(F(1),0,F(-m,3),F(-1,3))
        r=(1-t,t,-F(m*(1-t)+1,3),-F(m*t,3))
        x=product(r,a)
        assert x[0]+x[3]==0
        assert product(x,x)==(F(1,2*p+1),0,0,F(1,2*p+1))
        h=next(h for h in range(1,p) if pow(3,h,p)==1)
        k0=1
        residue=3%p
        k=k0+3*h
        lam=F((2*p+1)*residue,3**k)
        assert 0<lam<1
        for value in (lam*t,lam*(1-t),(1-lam)/p):
            d=value.denominator
            while d%3==0:d//=3
            assert d==1
        targets=((lam*(1-t),lam*t),
                 (-lam*(m*(1-t)+1)/3,-lam*m*t/3),(lam,F(0)))
        for aa,bb in targets:
            gamma=(1-aa-bb)/p
            alpha,beta=aa+m*gamma,bb+3*gamma
            assert min(alpha,beta,gamma)>=0 and alpha+beta+gamma==1
        checked+=1
    print("universal trace-zero matrix identities: PASS",checked)
    print("periodic-exponent legal scales and nonnegative triadic margins: PASS")
    print("Original-position transport factorization remains open.")


if __name__=="__main__":verify()
