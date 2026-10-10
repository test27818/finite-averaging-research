"""One controller for n=3p+r, r in {2,4,8}.

Carrier packing gives a genuine positive inverse; an orientation-reversing
affine map and one monomial reflection yield n-roots with no auxiliary primes.
Closed capacities and exact arithmetic only; no averaging-word search.
"""
from fractions import Fraction as F
from functools import cache
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout, normalize_pair, power
from verify_upper_band_unrestricted_completion import scale, det, zy, apply_mod, ceildiv
from verify_upper_band_descent_boundary import apply_return
from verify_even_odd_half_core import I, U, L, mod_power


def comm(a,b):
    return mm(mm(mm(a,b),invq(a)),invq(b))


def a_counts(p,r,t,u):
    i=p-t-u
    assert min(i,t,u)>=0 and 2*i<=2*p-r and 2*t<=p and 2*u<=r
    return (p-3*t-u,r*t-p*u,-1,0)


@cache
def data(p,r):
    assert r>=2 and r%2==0 and r%3 and p>=5 and r<p and factors(p)=={p:1}
    assert p>=2*r or r in (2,4,8)
    assert (p,r)!=(5,4)  # This dimension satisfies the earlier inverse-EGZ bound.
    m=1 if p%3==r%3 else 2
    b=r//m
    j=(p-b)//3
    T=p-m*j
    assert b%3==p%3 and r==m*b and j>=1 and T>0
    f=(b,r*j,0,p)
    packing=scale((p,-r*j,0,b),F(T,p*p))
    assert mm(packing,scale(f,F(1,p)))==scale(I,F(b*T,p*p))
    B=(b,r*j,2,-r)
    enough_b = 2*j<=p-r
    C=(-2,r,0,1)
    if m==1 or b%2==0:
        fneg=(-b//2,r*(p+b//2)//3,0,p)
        assert (p+b//2)%3==0 and 2*((p+b//2)//3)<=p
        assert mm(fneg,invq(f))==invq(C)
        u=b//2 if m==1 else 3*(b//3)
        t=j+b//2 if m==1 else j+b-u//3
        new=a_counts(p,r,t,u)
        period=mm(invq(C),new)
        assert period[0]+period[3]==0 and det(period)
        assert gcd(det(new),3*p+r)==1
        activation=("inverse-first",t,u)
    else:
        assert b%2==1 and m==2 and p>=4*b
        fneg=(-2*b,r*(p+2*b)//3,0,p)
        assert 2*((p+2*b)//3)<=p
        assert mm(fneg,invq(f))==C
        activation=("forward-first",None,None)
    if m==1:
        assert B[0]+B[3]==0
        J=mm(invq(C),a_counts(p,r,j+b//2,b//2))
        d=F(b*j,4)
        numerator=j
    else:
        assert sum(mm(C,B)[::3])==0
        J=a_counts(p,r,j,b)
        d=-b*T
        numerator=j+b
    assert J==(0,d,-1,0) and mm(J,J)==scale(I,-d)
    n=3*p+r
    if enough_b:
        H=mm(mm(J,power(C,m)),B)
        H=scale(H,1/F(H[3]))
        lam=F(numerator,2*(2*j+b))
        assert H==(lam,-r*lam/2,0,1)
        assert comm(C,H)==U(F(r*n,4*(2*j+b)))
        rho=-lam/2
        diagonal=mm(H,invq(C))
        assert rho==1-F(n,4*(2*j+b))
    else:
        assert (p,r)==(13,8)
        second=a_counts(p,r,j+1,b-3)
        assert second[0]==0 and second[1]==d+n
        H=mm(invq(J),second)
        assert comm(C,H)==U(F(r*n,second[1]))
        rho=F(d,second[1])
        diagonal=scale(H,rho)
        assert rho==1-F(n,second[1])
    assert mm(mm(J,U(1)),invq(J))==L(-F(1)/d)
    assert diagonal==(rho,0,0,1)
    principal=scale(mm(diagonal,diagonal),1/rho)
    assert principal==(rho,0,0,1/rho)
    assert tuple(residue(x,n) for x in principal)==I
    assert gcd(2*p*b*numerator*(2*j+b),n)==1
    v=zy(comm(C,J),p)
    assert tuple(residue(x,n) for x in v)==(1,residue(F(-3,2*p),n),0,1)
    if m==1:
        three=a_counts(p,r,r//2,r//2)
        assert three[1]==-3*j*r//2
    else:
        three=a_counts(p,r,(p-3)//2,b)
        assert three[1]==-3*b
    assert gcd(three[1],n)==1
    return m,b,j,T,f,B,C,J,H,rho,v,activation


def packing_return(ledger,groups,p,r):
    m,b,j,T,*_=data(p,r)
    a,c,d=(list(x) for x in groups)
    fresh=[]
    for k in range(m):
        group=a[k*2*j:(k+1)*2*j]+c[k*j:(k+1)*j]+d[k*b:(k+1)*b]
        ledger.average(group)
        fresh+=group
    a,c,d=a[2*m*j:],c[m*j:],d[m*b:]
    assert not d and len(a)==2*T and len(c)==T
    kept,fresh=fresh[:r],fresh[r:]
    left=a[:T]+fresh[:m*j]
    right=a[T:]+fresh[m*j:2*m*j]
    other=c+fresh[2*m*j:]
    assert sorted(left+right+other+kept)==list(range(3*p+r))
    for group in (left,right,other):
        ledger.average(group)
    return [left+right,other,kept]


def physical(p,r):
    m,b,j,T,f,B,C,J,H,rho,v,activation=data(p,r)
    count=0
    for aa,zz in ((1,0),(0,1)):
        raw=[aa]*(2*p)+[-2*aa+r*zz]*p+[-p*zz]*r
        ledger=Ledger(raw,p)
        groups=[list(range(2*p)),list(range(2*p,3*p)),list(range(3*p,3*p+r))]
        groups=packing_return(ledger,groups,p,r)
        a=F(T*(p*aa-r*j*zz),p*p)
        z=F(b*T*zz,p*p)
        assert all(ledger.state[i]==x for group,x in zip(groups,(a,-2*a+r*z,-p*z)) for i in group)
        groups=apply_return(ledger,groups,"C",j,0)
        scalar=F(b*T,p*p)
        assert all(ledger.state[i]==x for group,x in zip(groups,(scalar*aa,scalar*(-2*aa+r*zz),-scalar*p*zz)) for i in group)
        ledger.independent_replay(raw)
        count+=1
        # The inverse activation uses C^{-1}A (even b) or C B (b=1).
        ledger=Ledger(raw,p)
        groups=[list(range(2*p)),list(range(2*p,3*p)),list(range(3*p,3*p+r))]
        for k in range(2):
            if activation[0]=="inverse-first":
                groups=apply_return(ledger,groups,"A",activation[1],activation[2])
                tneg=(p+b//2)//3
            else:
                groups=apply_return(ledger,groups,"B",j,0)
                tneg=(p+2*b)//3
            groups=packing_return(ledger,groups,p,r)
            groups=apply_return(ledger,groups,"C",tneg,0)
        actual=ledger.state[groups[0][0]]
        actualz=-ledger.state[groups[2][0]]/p
        assert actual*zz-actualz*aa==0 and (actual or actualz)
        ledger.independent_replay(raw)
        count+=1
    return count


def unit_lift(p,r,wanted):
    n=3*p+r
    b=wanted%n
    multiplier=F(1)
    if 2*b>n:
        b=n-b
        multiplier=F(-1)
    while 4*b>n:
        multiplier*=3 if 3*b>n else -3
        b=abs(n-3*b)
    if r==2:
        assert 1<=b<=p
        t,u=(b//2,0) if b%2==0 else ((p-b)//2,1)
        mat=a_counts(p,r,t,u)
        unit=abs(mat[1])
        assert unit==b
    else:
        low,high=r//2+2,3*(p//2)+r//2
        while b<low:
            b*=3
            multiplier*=3
        assert low<=b<=high
        t=max(0,ceildiv(b-r//2,3))
        u=b-3*t
        mat=a_counts(p,r,t,u)
        unit=F(-mat[1],p)
    answer=unit/multiplier
    assert residue(answer,n)==wanted%n
    return answer


def transport(p,r,pair,exact=False):
    n=3*p+r
    v=data(p,r)[10]
    k=residue(F(2*p,3),n)*pair[0]*pow(pair[1],-1,n)%n
    result=apply_mod(mod_power(v,k,n),pair,n)
    assert result[0]==0 and gcd(result[1],n)==1
    epsilon=unit_lift(p,r,result[1])
    assert residue(epsilon,n)==result[1]
    if not exact:
        return
    mat=power(v,k)
    z,y=normalize_pair(mat[0]*pair[0]+mat[1]*pair[1],mat[2]*pair[0]+mat[3]*pair[1])
    assert z%n==0 and gcd(y,n)==1
    epsilon=unit_lift(p,r,y%n)
    _,alpha,beta=bezout(z,y)
    q=-alpha*pow(y,-1,n)%n
    alpha,beta=alpha+q*y,beta-q*z
    final=(y/epsilon,-z/epsilon,epsilon*alpha,epsilon*beta)
    assert det(final)==1 and tuple(residue(x,n) for x in final)==I
    assert (final[0]*z+final[1]*y,final[2]*z+final[3]*y)==(0,epsilon)


def main():
    rng=Random(2026091510)
    systems=literal=units=transports=exact=0
    for p in range(5,251):
        if factors(p)!={p:1}:
            continue
        for r in (2,4,8):
            if r>=p or (p,r)==(5,4):
                continue
            data(p,r)
            systems+=1
            if p<=31:
                literal+=physical(p,r)
            for wanted in range(1,3*p+r):
                if gcd(wanted,3*p+r)==1:
                    unit_lift(p,r,wanted)
                    units+=1
            for _ in range(3):
                pair=(rng.randrange(-10**5,10**5),rng.randrange(1,10**5))
                if gcd(pair[1],3*p+r)!=1:
                    pair=(pair[0],1)
                do_exact=p<=19
                transport(p,r,pair,do_exact)
                transports+=1
                exact+=int(do_exact)
    broader=0
    for p in (101,211,401):
        for r in range(2,p//2+1,2):
            if r%3==0:
                continue
            data(p,r)
            unit_lift(p,r,2)
            transport(p,r,(1,1))
            broader+=1
    print("even nontriadic general remainder controllers: PASS",broader)
    print("even nontriadic low-offset common controllers: PASS",systems)
    print("even nontriadic low-offset literal inverse cycles: PASS",literal)
    print("even nontriadic low-offset complete unit lifts: PASS",units)
    print("even nontriadic low-offset terminal transports: PASS",transports,exact)
    print("all-prime offsets2-4-8 completion interfaces: PASS")


if __name__=="__main__":
    main()
