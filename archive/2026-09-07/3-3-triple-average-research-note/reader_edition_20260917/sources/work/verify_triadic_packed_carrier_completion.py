"""One 3-adic CRT controller for r=3b, b in{1,2}, p=b mod3.

Physical carrier packing and one transverse reflection give U(3R) and a deep
principal congruence group. A six-residue phase adjustment and two direct CRT
returns set the exact terminal scale. No averaging-word search.
"""
from fractions import Fraction as F
from functools import cache
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout, normalize_pair
from verify_upper_band_unrestricted_completion import scale, det
from verify_even_odd_half_core import I, U, L
from verify_upper_band_descent_boundary import apply_return
from verify_three_p_minus_one_completion import comm


@cache
def data(p):
    assert p>=7 and factors(p)=={p:1}
    b=p%3
    r,m,n=3*b,p+b,3*(p+b)
    assert r<p
    j=(p-b)//3
    if b==1 and p%9==4:
        k,t,v,u=2,j-2,(p-7)//6,1
        y=(p-v)//3
    else:
        k=b
        t=v=j-b
        u=(2*j)%3
        assert u<=b
        y=(2*j+3*b-u)//3
    x=p-y-u-v
    alpha,beta=p-3*t-b,r*t-p*b
    assert alpha==3*k and beta==-b*b-3*b*k
    assert min(t,x,y,u,v)>=0
    assert 2*x<=p+t+b and 2*y<=p-t and 2*u<=r-b and 2*v<=p-r
    assert x+y+u+v==p
    q=p*r*y-p*p*u+v*beta
    raw=(beta,q,-alpha,-beta)
    basis=(1,1,F(1,b),0)  # (a,z)=(u+v,u/b)
    J=scale(mm(mm(invq(basis),raw),basis),F(1,b*b))
    c=J[2]
    expected_c=-F(m*j,2) if b==1 and p%9==4 else F(m*(b*(2*j+b)-p*u),b**3)
    assert c==expected_c
    assert J==(1,-F(3*k,b),c,-1)
    lam=1-F(3*k,b)*c
    assert mm(J,J)==scale(I,lam) and residue(c,3)==2
    assert gcd(F(lam).numerator,n)==1
    a=(0,-b*b,-1,0)
    B=(3*b,-4*b*b,2,-3*b)
    S=scale(mm(mm(invq(basis),a),basis),F(-1,b))
    T=scale(mm(mm(invq(basis),B),basis),F(-1,b))
    assert S==(1,1,0,-1) and T==(1,-2,0,-1)
    assert mm(S,T)==U(-3)
    F0=(b,r*j,0,p)
    assert mm(mm(invq(basis),F0),basis)==(p,0,0,b)
    P=(1,1,0,c)
    d=det(J)
    assert mm(mm(invq(P),U(3)),P)==U(3*c)
    assert mm(mm(mm(mm(invq(P),J),U(3*d)),invq(J)),P)==L(-3*c)
    g=abs(c.numerator)
    for ell in set(factors(p*b)):
        while g%ell==0:g//=ell
    M=9*g**3
    assert M%n==0 and gcd(M,p*b)==1
    assert gcd(F(lam).numerator,M)==1 and g%3
    for matrix in (U(M),L(M),mm(U(M),L(M))):
        conjugate=mm(mm(invq(P),matrix),P)
        assert tuple(residue(z,9*g*g) for z in conjugate)==I
    return b,r,m,n,j,J,c,lam,g,M,S,(b,t,x,y,u,v),raw


def packing(ledger,groups,p,b,j):
    ga,gb,gc=(list(z) for z in groups)
    r=3*b
    fresh=[]
    for i in range(3):
        group=ga[2*j*i:2*j*(i+1)]+gb[j*i:j*(i+1)]+gc[b*i:b*(i+1)]
        ledger.average(group)
        fresh+=group
    ga,gb,gc=ga[6*j:],gb[3*j:],gc[3*b:]
    assert len(ga)==2*b and len(gb)==b and not gc
    kept,fresh=fresh[:r],fresh[r:]
    left=ga[:b]+fresh[:3*j]
    right=ga[b:]+fresh[3*j:6*j]
    other=gb+fresh[6*j:]
    for group in (left,right,other):ledger.average(group)
    return [left+right,other,kept]


def reflection(ledger,groups,counts,p):
    b,t,x,y,u,v=counts
    ga,gb,gc=(list(z) for z in groups)
    r=len(gc)
    i=p-t-b
    fresh=ga[:i]+gb[:t]+gc[:b]
    ledger.average(fresh)
    ga,gb,gc=ga[i:],gb[t:],gc[b:]
    kept,fresh=fresh[:r],fresh[r:]
    left=ga[:x]+gb[:y]+gc[:u]+fresh[:v]
    right=ga[x:2*x]+gb[y:2*y]+gc[u:2*u]+fresh[v:2*v]
    other=ga[2*x:]+gb[2*y:]+gc[2*u:]+fresh[2*v:]
    assert sorted(left+right+other+kept)==list(range(3*p+r))
    for group in (left,right,other):ledger.average(group)
    return [left+right,other,kept]


def raw_state(p,b,u,v):
    return [F(u+v)]*(2*p)+[F(u-2*v)]*p+[-F(p*u,b)]*(3*b)


def groups(p,b):
    return [list(range(2*p)),list(range(2*p,3*p)),list(range(3*p,3*p+3*b))]


def physical(p):
    b,r,m,n,j,J,c,lam,g,M,S,counts,_=data(p)
    count=0
    for u,v in ((1,0),(0,1)):
        raw=raw_state(p,b,u,v)
        ledger=Ledger(raw,p)
        gs=groups(p,b)
        gs=packing(ledger,gs,p,b,j)
        gs=apply_return(ledger,gs,"C",j,0)
        scalar=F(b*b,p*p)
        expected=(scalar*(u+v),scalar*(u-2*v),-scalar*F(p*u,b))
        assert all(ledger.state[i]==value for group,value in zip(gs,expected) for i in group)
        ledger.independent_replay(raw);count+=1
        ledger=Ledger(raw,p);gs=groups(p,b)
        for stage in range(2):
            gs=reflection(ledger,gs,counts,p)
            if stage==0:
                uu=F(b*b,p*p)*(J[0]*u+J[1]*v)
                vv=F(b*b,p*p)*(J[2]*u+J[3]*v)
            else:
                scalar=F(b**4,p**4)*lam
                uu,vv=scalar*u,scalar*v
            assert all(ledger.state[i]==value for group,value in zip(
                gs,(uu+vv,uu-2*vv,-F(p,b)*uu)) for i in group)
        ledger.independent_replay(raw);count+=1
        ledger=Ledger(raw,p);gs=groups(p,b)
        gs=apply_return(ledger,gs,"B",j-b,b)
        gs=apply_return(ledger,gs,"A",j,b)
        scalar=F(b*b,p*p)
        uu,vv=scalar*(u-3*v),scalar*v
        assert all(ledger.state[i]==value for group,value in zip(
            gs,(uu+vv,uu-2*vv,-F(p,b)*uu)) for i in group)
        ledger.independent_replay(raw);count+=1
    return count


def normalize_phase(p,u,v):
    b,r,m,n,j,J,c,lam,g,M,S,_,_=data(p)
    u,v=normalize_pair(u,v)
    assert gcd(residue(F(m,b)*u+v,n),n)==1
    if v%3==0:
        u,v=normalize_pair(J[0]*u+J[1]*v,J[2]*u+J[3]*v)
    elif (u+v)%3:
        u,v=normalize_pair(u+v,-v)
    assert v%3 and (u+v)%3==0
    if b==2:
        while v%2==0:
            u,v=normalize_pair(u,F(p*v,2))
    assert v%2 and gcd(v,m)==1 and (u+v)%3==0
    return u,v


def extend(a,step,wanted,ell):
    assert gcd(step,ell)==1
    return a+step*((wanted-a)*pow(step,-1,ell)%ell),step*ell


def literal_return(p,u,v,a,q):
    b,r,m,n,*_=data(p)
    if q>0:
        t=q
        prepared=3*a-v
        kind="A"
        assert 2*t<=p and t>=(r+1)//2
    else:
        t=p+q
        prepared=3*a+2*v
        kind="B"
        assert 0<=2*t<=p-r
    assert (prepared-u)%(3*v)==0
    raw=raw_state(p,b,prepared,v)
    ledger=Ledger(raw,p)
    gs=apply_return(ledger,groups(p,b),kind,t,0)
    uu,vv=F(-3*b*a,p),F(3*(m*a-q*v),p)
    assert all(ledger.state[i]==value for group,value in zip(
        gs,(uu+vv,uu-2*vv,-F(p,b)*uu)) for i in group)
    ledger.independent_replay(raw)


def prepare_unit(p,u,v,physical_check=False):
    b,r,m,n,j,J,c,lam,g,M,S,_,_=data(p)
    u,v=normalize_phase(p,u,v)
    a,step=((u+v)//3)%abs(v),abs(v)
    for ell in factors(M):
        if ell==3:
            a,step=extend(a,step,-v,ell)
        elif m%ell==0 or v%ell==0:
            continue
        else:
            a,step=extend(a,step,(1-p*v)*pow(m,-1,ell),ell)
    if v%p:
        a,step=extend(a,step,1,p)
    if b==2:
        a,step=extend(a,step,0,2)
    assert gcd(a,v)==gcd(a,p)==1
    if physical_check:literal_return(p,u,v,a,-p)
    pair=(-b*a,m*a+p*v)
    assert gcd(*pair)==1 and gcd(pair[1],M)==1 and sum(pair)%3==0
    assert gcd(residue(F(m,b)*pair[0]+pair[1],n),n)==1
    return pair


def digit(p,v):
    b,r,m,n,j,J,c,lam,g,M,S,_,_=data(p)
    d=pow(v,-1,m)
    unit=F(1)
    if 2*d>m:
        d,unit=m-d,-unit
    if b==2:
        if d==1:
            d,unit=2,2*unit
        elif 2*d==m-1:
            d,unit=2,-4*unit
    assert d*v%m==residue(unit,m)
    if d>=(r+1)//2 and d%3:
        q=d
    else:
        q=d-m
        assert 0<=2*(d-b)<=p-r
    assert q%3 and q*v%m==residue(unit,m)
    assert (r+1)//2<=q<=p//2 if q>0 else 0<=2*(q+p)<=p-r
    epsilon=-unit
    if residue(epsilon+q*v,3):
        epsilon*=F(-p,b)
    assert residue(epsilon+q*v,n)==0
    return q,epsilon


def transport(p,u,v,physical_check=False):
    b,r,m,n,j,J,c,lam,g,M,S,_,_=data(p)
    u,v=prepare_unit(p,u,v,physical_check)
    q,epsilon=digit(p,v)
    K=M//m
    representative=residue(epsilon,M)
    assert (q*v+representative)%m==0
    wanted=(q*v+representative)//m
    a,step=((u+v)//3)%abs(v),abs(v)
    a,step=extend(a,step,wanted,K)
    if b==2:
        a,step=extend(a,step,q+1,2)
    for ell in factors(abs(q)):
        if step%ell:
            a,step=extend(a,step,1,ell)
    assert gcd(a,v)==gcd(a,q)==1 and a%3==0
    if physical_check:literal_return(p,u,v,a,q)
    u,v=-b*a,m*a-q*v
    assert gcd(u,v)==1 and residue(v-epsilon,M)==0
    assert gcd(residue(F(m,b)*u+v,n),n)==1
    k=(-u//3)*pow(v,-1,M//3)%(M//3)
    u+=3*k*v
    assert u%M==0
    _,alpha,beta=bezout(u,v)
    t=-alpha*pow(v,-1,M)%M
    alpha,beta=alpha+t*v,beta-t*u
    final=(v/epsilon,-u/epsilon,epsilon*alpha,epsilon*beta)
    assert det(final)==1 and tuple(residue(z,M) for z in final)==I
    assert (final[0]*u+final[1]*v,final[2]*u+final[3]*v)==(0,epsilon)
    assert all(set(factors(F(z).denominator))<=set(factors(p*b)) for z in final)
    return q,epsilon


def main():
    rng=Random(2026091511)
    systems=literal=transports=0
    branches=set()
    for p in range(7,500):
        if factors(p)!={p:1}:
            continue
        b,r,m,n,*_=data(p)
        systems+=1
        if p<=43:
            literal+=physical(p)
        for _ in range(9):
            u,v=rng.randrange(-100000,100000),rng.randrange(1,100000)
            u,v=normalize_pair(u,v)
            if gcd(residue(F(m,b)*u+v,n),n)!=1:
                u,v=0,1
            q,epsilon=transport(p,u,v,p<=31)
            branches.add((b,q>0,F(epsilon).denominator>1))
            transports+=1
    carry_checks=0
    for p in (7,11,13,17,19,23,29,31,37,41,43):
        for b in (1,2):
            r,n=3*b,3*(p+b)
            candidates=[t for t in range((r+1)//2,p//2+1) if gcd(t,n)==1]
            if not candidates:continue
            t=candidates[0]
            z=next(v for v in range(1,n+1) if gcd(v,3)==1 and gcd(3+p*v,n)==1)
            raw=[3]*(2*p)+[-6+r*z]*p+[-p*z]*r
            ledger=Ledger(raw,p)
            gs=apply_return(ledger,groups(p,b),"A",t,0)
            a1,z1=p-3*t+b*t*z,-1
            expected=tuple(F(3,p)*v for v in (a1,-2*a1+r*z1,-p*z1))
            assert all(ledger.state[i]==value for group,value in zip(gs,expected) for i in group)
            assert gcd(a1+p*z1,n)==1
            ledger.independent_replay(raw)
            carry_checks+=1
    print("triadic carrier conditional primitive3-carry: PASS",carry_checks)
    print("triadic carrier common reflection and deep-level interfaces: PASS",systems)
    print("triadic carrier literal packing and reflection cycles: PASS",literal)
    print("triadic carrier CRT exact terminal transports: PASS",transports)
    print("triadic carrier digit branches: PASS",sorted(branches))
    print("offset3-residue1 and offset6-residue2 completion interfaces: PASS")


if __name__=="__main__":main()
