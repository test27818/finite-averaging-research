"""Uniform (p,p,2) completion for every odd prime p>=5.

The verifier checks the corrected one-carrier ledger, the reflection square,
the CRT state-dependent odd return, and exact terminal congruence matrices.
"""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_even_odd_half_core import I, mod_power
from verify_three_p_minus_one_completion import comm

if not __debug__:
    raise RuntimeError("Assertions are required.")


def det(a): return a[0]*a[3]-a[1]*a[2]


def params(p):
    assert p >= 5 and factors(p) == {p: 1}
    m, n = p+1, 2*p+2
    t = (p-3)//2
    c = -m*(p-1)//2 if p % 4 == 1 else m*m//2
    lam = 1-2*c
    J = (1, -2, c, -1)
    assert J[0]*J[3]-J[1]*J[2] == -lam
    assert mm(J, J) == (lam, 0, 0, lam)
    lower_affine=mm(J,(1,2,0,1))
    assert comm((1,0,0,-1),lower_affine)==(1,0,-2*c,1)
    h = abs(2*c)
    assert h % m == 0 and gcd(h, p) == gcd(m, p) == 1
    M = h*h
    return p,m,n,t,c,lam,h,M,J


def overlap_j(ledger):
    p = ledger.p
    a,b,c = (list(g) for g in ledger.groups)
    t = (p-3)//2
    first_i = (p+1)//2
    fresh = a[:first_i]+b[:t]+c[:1]
    ledger.average(fresh)
    a,b,c = a[first_i:],b[t:],c[1:]
    kept, fresh = fresh[:2], fresh[2:]
    # The formulas below are the parity-specialized form of the general CRT return.
    w = (p-1)//2
    uflag = (p+1-w-1) % 2
    x = (p+1-uflag-w-1)//2
    y = (p+1-uflag-w+1)//2
    v = w-1
    left = a[:x]+b[:y]+c[:uflag]+fresh[:v]
    other = a[x:]+b[y:]+c[uflag:]+fresh[v:]
    assert sorted(left+other+kept) == list(range(2*p+2))
    for g in (left,other): ledger.average(g)
    return [left,other,kept]


def physical(p):
    _,_,_,t,c,lam,h,M,J = params(p)
    count=0
    for u,v in ((1,0),(0,1)):
        raw=[u+v]*p+[u-v]*p+[-p*u]*2
        ledger=Ledger(raw,p)
        ledger.groups=[list(range(p)),list(range(p,2*p)),list(range(2*p,2*p+2))]
        groups=overlap_j(ledger)
        u1=F(J[0]*u+J[1]*v,p*p); v1=F(J[2]*u+J[3]*v,p*p)
        assert [ledger.state[g[0]] for g in groups]==[u1+v1,u1-v1,-p*u1]
        ledger.independent_replay(raw)
        count+=1
        ledger=Ledger(raw,p)
        a,b,cg=list(range(p)),list(range(p,2*p)),list(range(2*p,2*p+2))
        i=(p-1)//2
        left,right=a[:i]+b[:i]+cg[:1],a[i:2*i]+b[i:2*i]+cg[1:]
        for g in (left,right): ledger.average(g)
        fresh=left+right
        kept,fresh=fresh[:2],fresh[2:]
        first,second=a[2*i:]+fresh[:p-1],b[2*i:]+fresh[p-1:]
        for g in (first,second): ledger.average(g)
        expected=(F(u,p*p)+F(v,p),F(u,p*p)-F(v,p),-F(u,p))
        assert all(ledger.state[index]==value for group,value in zip((first,second,kept),expected) for index in group)
        j=(p-1)//2
        left,right=first[:p-j]+second[:j],first[p-j:]+second[j:]
        for g in (left,right): ledger.average(g)
        assert all(ledger.state[index]==F(value,p*p)
                   for group,value in zip((left,right,kept),(u+v,u-v,-p*u)) for index in group)
        ledger.independent_replay(raw)
        count+=1
    return count


def literal_mq(p,u,v,a,q):
    assert (2*a-u-v)%v==0
    prepared=2*a-v
    raw=[prepared+v]*p+[prepared-v]*p+[-p*prepared]*2
    ledger=Ledger(raw,p)
    first,second,carriers=list(range(p)),list(range(p,2*p)),list(range(2*p,2*p+2))
    left=first[:q-2]+second[:p-q]+carriers
    right=first[q-2:p-2]+second[p-q:]
    kept=first[p-2:]
    for group in (left,right): ledger.average(group)
    uu,vv=-a,q*v-(p+1)*a
    expected=tuple(F(2*x,p) for x in (uu+vv,uu-vv,-p*uu))
    assert all(ledger.state[index]==value
               for group,value in zip((left,right,kept),expected) for index in group)
    ledger.independent_replay(raw)


def choose_a(p,u,v,modulus):
    m=p+1
    modv=abs(v)
    a0=((u+v)*pow(2,-1,modv)) % modv if modv>1 else 0
    a,step=a0,modv
    for ell in factors(modulus):
        if m % ell == 0 or v % ell == 0:
            continue
        wanted=(p*v-1)*pow(m,-1,ell)%ell
        a += step*((wanted-a)*pow(step,-1,ell)%ell)
        step *= ell
    if v % p:
        a += step*((1-a)*pow(step,-1,p)%p)
    assert (2*a-u-v)%modv==0
    return a


def normalize_pair(p,u,v,check_physical=False):
    m,n,t,c,lam,h,M,J=params(p)[1:]
    if (u+v)%2: u += v
    a=choose_a(p,u,v,M)
    if check_physical: literal_mq(p,u,v,a,p)
    u1,v1=-a,p*v-m*a
    assert gcd(a,v)==1 and gcd(a,p)==1
    assert gcd(v1,M)==1
    return u1,v1


def target_pair(p,u,v,check_physical=False):
    p,m,n,t,c,lam,h,M,J=params(p)
    u1,v1=normalize_pair(p,u,v,check_physical)
    q=pow(v1,-1,m)%m
    eps=1
    if q==1: q,eps=p,-1
    assert 2<=q<=p and q%2 and gcd(q,m)==1
    modv=abs(v1)
    a0=((u1+v1)*pow(2,-1,modv))%modv if modv>1 else 0
    K=M//m
    target=((q*v1-eps)//m)%K
    a=a0 if modv else 0
    step=modv if modv else 1
    if K>1:
        g=gcd(step,K)
        assert g==1
        a += step*((target-a)*pow(step,-1,K)%K)
        step*=K
    for ell in factors(q):
        if step % ell:
            a += step*((1-a)*pow(step,-1,ell)%ell)
            step *= ell
    assert gcd(a,q)==1
    if check_physical: literal_mq(p,u1,v1,a,q)
    u2,v2=-a,q*v1-m*a
    assert v2%M==eps%M and gcd(u2,v2)==1
    k=(-u2*pow(v2,-1,M))%M
    u3=u2+k*v2
    _,aa,bb=bezout(u3,v2)
    adjust=-aa*pow(v2,-1,M)%M
    aa,bb=aa+adjust*v2,bb-adjust*u3
    matrix=(eps*v2,-eps*u3,eps*aa,eps*bb)
    assert det(matrix)==1 and tuple(x%M for x in matrix)==I
    assert (matrix[0]*u3+matrix[1]*v2,matrix[2]*u3+matrix[3]*v2)==(0,eps)
    return (u3,v2), (q,eps,a)


def main():
    rng=Random(20260915)
    literal=sum(physical(p) for p in range(5,80) if factors(p)=={p:1})
    systems=0
    for p in range(5,1000):
        if factors(p)!={p:1}: continue
        _,m,n,t,c,lam,h,M,J=params(p)
        for _ in range(12):
            v=2*rng.randrange(-10**7,10**7)+1
            u=rng.randrange(-10**7,10**7)
            if gcd(u,v)!=1 or gcd(v,m)!=1:
                v=1;u=rng.randrange(-10**7,10**7)
            final,meta=target_pair(p,u,v,p<=31)
            assert final[0]%M==0 and gcd(final[1],M)==1
        systems+=1
    target_pair(29,4,7,True)
    print("2p+2 corrected one-carrier reflection returns: PASS", systems)
    print("2p+2 original-position reflection replays: PASS", literal)
    print("2p+2 state-dependent M_p/M_q CRT normalization: PASS", systems*12)
    print("2p+2 former p29 two-prime descent obstruction: PASS")
    print("2p+2 exact terminal congruence interface: PASS")
if __name__=="__main__": main()
