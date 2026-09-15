"""Uniform r=9, p=1 mod3 completion using existing four returns.

The only new choice is a short one-forbidden-residue sieve for the3-adic
return. Unit representatives use the existing n/3 argument, with one exact
unit basis for p=13. No averaging-word or finite-group search.
"""
from fractions import Fraction as F
from math import gcd
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_upper_band_four_return_congruence import system
from verify_upper_band_descent_boundary import apply_return
from verify_uniform_odd_middle_cores import mm, residue
from verify_upper_band_unrestricted_completion import (
    scale, zy, apply_mod, local_cycle_hit, pure_prime_order, unit_lift)
from verify_even_odd_half_core import mod_power, valuation, crt_pairs, principal_unit_log


def choose_three_return(p):
    n=3*p+9
    lo,hi=3,p//2
    blocked=bytearray(hi+1)
    for ell in factors(n):
        forbidden=0 if ell==2 else 1 if ell==3 else (-2*pow(3,-1,ell))%ell
        for t in range(forbidden,hi+1,ell):blocked[t]=1
    t=next(t for t in range(lo,hi+1) if not blocked[t])
    q=3*t+2
    assert t%2 and t%3!=1 and gcd(q,n)==1
    matrix=(p-q,9*t-2*p,-1,0)
    assert p-t-2>=0 and 2*(p-t-2)<=2*p-9 and 2*t<=p
    normalized=scale(zy(matrix,p),F(1,p))
    c=F((p+q)**2-4*n*t,(p-q)**2)
    assert residue(c,3)==0 and residue(c,9)!=6
    return normalized,t,q


def unit(p,wanted):
    n=3*p+9
    if p==13:
        value=next((-1)**c*5**a*13**b for c in range(2) for a in range(4) for b in range(2)
                   if (-1)**c*5**a*13**b%n==wanted%n)
        return F(value)
    return unit_lift(p,9,wanted)


def transport(p,pair):
    n=3*p+9
    level=81*n**4
    entries=system(p,9)
    aa=entries[0][2]
    bb=entries[2][2]
    if n%4==2 and sum(mm(bb,aa)[::3])%4!=2:
        bb=entries[3][2]
    v=scale(zy(mm(bb,aa),p),F(1,p*p))
    triple,_,_=choose_three_return(p)
    e3=valuation(level,3)
    k=local_cycle_hit(triple,3,e3,pair)
    pair=apply_mod(mod_power(triple,k,level),pair,level)
    congruences=[(0,pure_prime_order(v,3,e3))]
    for ell,e in factors(n).items():
        if ell==3:continue
        congruences.append((local_cycle_hit(v,ell,4*e,pair),ell**(4*e)))
    pair=apply_mod(mod_power(v,crt_pairs(congruences),level),pair,level)
    assert pair[0]==0 and gcd(pair[1],level)==1
    first=unit(p,pair[1]%n)
    target=pair[1]*pow(residue(first,level),-1,level)%level
    k0=F(entries[1][3],entries[0][3])
    k1=F(entries[3][3],entries[2][3])
    if n%4==2:
        flag=int(target%4!=1)
        target=target*pow(residue(k0,level),-flag,level)%level
        base,start=k1,2*n
    else:
        flag,base,start=0,k0,n
    power=principal_unit_log(base,target,level,start,False)
    lifted=residue(first,level)*pow(residue(k0,level),flag,level)*pow(residue(base,level),power,level)
    assert lifted%level==pair[1]


def physical(p):
    matrix,t,q=choose_three_return(p)
    n=3*p+9
    count=0
    for a,z in ((1,0),(0,1)):
        raw=[a]*(2*p)+[-2*a+9*z]*p+[-p*z]*9
        ledger=Ledger(raw,p)
        groups=[list(range(2*p)),list(range(2*p,3*p)),list(range(3*p,n))]
        groups=apply_return(ledger,groups,"A",t,2)
        av,zv=F((p-q)*a+(9*t-2*p)*z,p),-F(a,p)
        assert all(ledger.state[i]==v for group,v in zip(groups,(av,-2*av+9*zv,-p*zv)) for i in group)
        ledger.independent_replay(raw);count+=1
    return count


def main():
    rng=Random(2026091512)
    systems=literal=units=transports=0
    for p in range(13,500,3):
        if factors(p)!={p:1}:continue
        n=3*p+9
        j=(p-1)//3
        entries=system(p,9)
        assert entries[0][1]==j-1 and entries[2][1]==j-4
        assert tuple(e[3] for e in entries)==(p+12,3-2*p,3-2*p,4*p+21)
        choose_three_return(p)
        systems+=1
        if p<=43:literal+=physical(p)
        for wanted in range(1,n):
            if gcd(wanted,n)==1:
                assert residue(unit(p,wanted),n)==wanted
                units+=1
        for _ in range(3):
            u,v=rng.randrange(-10**7,10**7),rng.randrange(1,10**7)
            if gcd(v,n)!=1:v=1
            transport(p,(u,v));transports+=1
    print("offset9 residue1mod3 exact four-return systems: PASS",systems)
    print("offset9 residue1mod3 literal3-adic returns: PASS",literal)
    print("offset9 residue1mod3 complete unit lifts: PASS",units)
    print("offset9 residue1mod3 complete direction-scale transports: PASS",transports)
    print("offset9 residue1mod3 completion interfaces: PASS")


if __name__=="__main__":main()

