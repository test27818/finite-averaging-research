"""Exact checks of the written local quadratic-group theorem.

The proof of unbounded levels is in the document. These tests check symbolic
identities, fixed torsion/defect examples, and all180 retained direction macros.
No averaging-word search and no enumeration at deep local levels.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

from verify_uniform_odd_middle_cores import mm, invq, residue
from verify_even_odd_half_core import I, mod_power
from verify_upper_band_unrestricted_completion import zy, local_cycle_hit
from check_large_symmetric_carrier_certificate import check_row, prime


def padd(a,b):
    result=dict(a)
    for e,v in b.items():
        result[e]=result.get(e,0)+v
        if not result[e]:del result[e]
    return result


def pmul(a,b):
    result={}
    for e,v in a.items():
        for f,w in b.items():
            g=tuple(x+y for x,y in zip(e,f))
            result[g]=result.get(g,0)+v*w
    return {e:v for e,v in result.items() if v}


def symbolic_checks():
    one={(0,0,0,0):1}
    variables=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
    c,x,y,z=variables
    # Rational functions as unreduced numerator/denominator polynomial pairs.
    def add(a,b):return padd(pmul(a[0],b[1]),pmul(b[0],a[1])),pmul(a[1],b[1])
    def mul(a,b):return pmul(a[0],b[0]),pmul(a[1],b[1])
    def div(a,b):return pmul(a[0],b[1]),pmul(a[1],b[0])
    def neg(a):return {e:-v for e,v in a[0].items()},a[1]
    def eq(a,b):return pmul(a[0],b[1])==pmul(b[0],a[1])
    one=(one,one);c,x,y,z=[(v,one[0]) for v in variables]
    def group(a,b):return div(add(a,b),add(one,mul(c,mul(a,b))))
    assert eq(group(group(x,y),z),group(x,group(y,z)))
    assert eq(group(x,neg(x)),({},one[0]))
    two=add(one,one);three=add(two,one)
    assert eq(group(one,one),div(two,add(one,c)))
    assert eq(group(group(one,one),one),div(add(three,c),add(one,mul(three,c))))
    print('quadratic local group symbolic identities: PASS 4')


def val(x,ell):
    x=F(x)
    if x==0:return None
    n,d=x.numerator,x.denominator;v=0
    while n%ell==0:n//=ell;v+=1
    while d%ell==0:d//=ell;v-=1
    return v


def power_parameter(c,k,modulus):
    a,b=1,0;u,v=1,1
    while k:
        if k&1:a,b=(a*u+c*b*v)%modulus,(a*v+b*u)%modulus
        u,v=(u*u+c*v*v)%modulus,(2*u*v)%modulus
        k//=2
    return b*pow(a,-1,modulus)%modulus


def finite_cycles():
    count=0
    for ell,c in ((2,0),(2,2),(3,0),(3,3),(3,6),(3,24),(3,-3),(5,5),(7,7)):
        numerator=sum(comb(ell,2*j+1)*c**j for j in range((ell+1)//2))
        depth=val(numerator,ell)
        for e in (1,2,3,4):
            modulus=ell**e
            expected=ell if depth is None else ell**(1+max(0,e-depth))
            seen=set();cycles=0
            for start in range(modulus):
                if start in seen:continue
                x=start;length=0
                while x not in seen:
                    seen.add(x);length+=1
                    x=(x+1)*pow(1+c*x,-1,modulus)%modulus
                assert x==start and length==expected,(ell,c,e,length,expected)
                cycles+=1
            assert cycles==modulus//expected
            count+=1
    # Deep levels: repeated squaring only, no state enumeration.
    for ell,c in ((3,6),(3,24),(3,-3),(5,5),(2,2)):
        numerator=sum(comb(ell,2*j+1)*c**j for j in range((ell+1)//2))
        d=val(numerator,ell);e=40;modulus=ell**e
        order=ell if d is None else ell**(1+max(0,e-d))
        assert power_parameter(c,order,modulus)==0
        assert power_parameter(c,order//ell,modulus)!=0
    print('local defect cycles and deep orders: PASS',count,5)


def actual_certificate_directions():
    data=json.loads(Path(__file__).with_name('large_symmetric_carrier_reduced_certificate.json').read_text(encoding='utf-8'))['cases']
    count=0;count2=0
    for case in data:
        p,s=case['p'],case['s'];n=3*p+s
        j0,_=check_row(p,s,case['direction'][0]);j1,_=check_row(p,s,case['direction'][1])
        T=tuple(F(x,p**4) for x in zy(mm(j0,j1),p))
        factors=[ell for ell in range(2,n+1) if n%ell==0 and prime(ell)]
        trace=T[0]+T[3];tau=trace/2
        N=tuple(v/tau-int(i in (0,3)) for i,v in enumerate(T))
        c=mm(N,N)[0]
        assert mm(N,N)==(c,0,0,c)
        basis=(N[1],0,N[3],1)
        normal=mm(mm(invq(basis),N),basis)
        assert normal==(0,1,c,0)
        for ell in factors:
            assert val(tau,ell)==0 and val(N[1],ell)==0
            assert c==0 or val(c,ell)>=1
            numer=sum(F(comb(ell,2*j+1))*c**j for j in range((ell+1)//2))
            assert val(numer,ell)==1
            count+=1
            if ell==2:count2+=1
        # Existing digit solver vs exact p-adic group prediction.
        for ell in factors:
            normal_T=(1,1,c,1)
            k=local_cycle_hit(normal_T,ell,8,(11,1))
            power=mod_power(normal_T,k,ell**8)
            assert (power[0]*11+power[1])%(ell**8)==0
    print('retained certificate quadratic normal forms: PASS',len(data),count,count2)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    symbolic_checks();finite_cycles();actual_certificate_directions()
    print('p-adic quadratic group and orbit defect interfaces: PASS')


if __name__=='__main__':main()
