"""Check exact shallow-kernel lifting and the162-case current certificate.

No large orbit enumeration. Tangent systems have dimension3; even direction
correction tries at most8 classes. General group inclusion is proved in text.
"""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

import check_large_symmetric_carrier_certificate as old
from verify_carrier_interval_reduction import family, entry, check_interval_cover
from verify_uniform_odd_middle_cores import mm,invq,residue
from verify_even_odd_half_core import I,mod_power,valuation
from verify_upper_band_unrestricted_completion import zy
from verify_padic_quadratic_group import padd,pmul


def symbolic_determinant():
    one={(0,0,0,0):1}
    a,b,c,d=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
    neg=lambda q:{e:-v for e,v in q.items()}
    add=padd;mul=pmul
    t=add(a,d);D=add(mul(a,d),neg(mul(b,c)))
    # Numerator of det(X0,X1,X2), denominator D^3.
    left=add(neg(mul(mul(b,d),mul(mul(b,b),mul(t,t)))),
             mul(mul(b,b),mul(mul(b,t),add(mul(b,c),mul(d,d)))))
    right=neg(mul(mul(mul(b,b),b),mul(t,D)))
    assert left==right
    print('three conjugate tangent determinant: PASS')


def add(A,B):return tuple(x+y for x,y in zip(A,B))
def scale(t,A):return tuple(t*x for x in A)
def mod(A,m):return tuple(residue(x,m) for x in A)
def conjugate(T,X):return mm(mm(T,X),invq(T))
def coordinates(A):return A[0],A[1],A[2]


def solve3(columns,target):
    A=[[F(columns[j][i]) for j in range(3)]+[F(target[i])] for i in range(3)]
    for j in range(3):
        k=next(i for i in range(j,3) if A[i][j])
        A[j],A[k]=A[k],A[j]
        v=A[j][j];A[j]=[x/v for x in A[j]]
        for i in range(3):
            if i!=j:
                v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[j])]
    return [r[-1] for r in A]


def local_lift_checks():
    E=(0,0,1,0);count=0
    # Includes the actual order3 local matrix: long single orbits are not needed.
    for ell,T in ((3,(1,1,-3,1)),(3,(1,1,6,1)),(5,(1,1,5,1)),(2,(1,1,2,1))):
        roots=[E,conjugate(T,E),conjugate(mm(T,T),E)]
        for a in (2,3,4):
            binary=ell==2;start=a+int(binary);m=ell**(2*a)
            columns=[coordinates(X) for X in roots]
            for u,v,w in ((1,2,3),(4,1,2),(2,5,1)):
                level=ell**start;unit=1+level*w
                target=mm(mm((1,level*u,0,1),(unit,0,0,F(1,unit))),(1,0,level*v,1))
                current=I
                for k in range(start,2*a):
                    error=mod(mm(target,invq(current)),m)
                    assert all((error[i]-I[i])%(ell**k)==0 for i in range(4))
                    desired=tuple(((error[i]-I[i])//ell**k)%ell for i in (0,1,2))
                    coefficients=solve3(columns,tuple((2 if binary else 1)*x for x in desired))
                    assert all(F(x).denominator%ell for x in coefficients)
                    step=I;power=ell**(k-int(binary))
                    for coeff,X in zip(coefficients,roots):
                        scalar=residue(coeff,ell**2)*power
                        step=mod(mm(add(I,scale(scalar,X)),step),m)
                    current=mod(mm(step,current),m)
                assert mod(target,m)==current,(ell,a,target,current)
                count+=1
    print('exact layer corrections without orbit enumeration: PASS',count)


def V_of(p,s,rows):
    a,_=old.check_row(p,s,rows[0]);b,_=old.check_row(p,s,rows[1])
    return tuple(F(x,p**4) for x in zy(mm(a,b),p))


def shallow_direction(p,s,delta,rows,do_replay=False):
    n=3*p+s;V=V_of(p,s,rows)
    assert mod(V,n)==(1,residue(F(-1,p*p),n),0,1)
    trace=V[0]+V[3]
    Q=n if n%2 else 2*delta*n
    assert gcd(trace.numerator,n)==1 if n%2 else valuation(trace.numerator,2)==1
    for ell in range(3,n+1,2):
        if n%ell==0 and old.prime(ell):assert residue(trace,ell)!=0
    cap=Q//n
    for z,y in ((5*n+7,3*n+1),(-n-3,n+1),(2*n,1)):
        k=p*p*z*pow(y,-1,n)%n
        found=False
        for j in range(cap):
            M=mod_power(V,k+j*n,Q)
            out=((M[0]*z+M[1]*y)%Q,(M[2]*z+M[3]*y)%Q)
            if out[0]==0 and gcd(out[1],Q)==1:found=True;break
        assert found,(p,s,delta,z,y,Q)
    if do_replay:
        for row in rows:old.literal(p,s,row)


def retained():
    data=json.loads(Path(__file__).with_name('large_symmetric_carrier_shallow_certificate.json').read_text(encoding='utf-8'))['cases']
    assert {(c['p'],c['s']) for c in data}=={(p,s) for p in range(11,83) if old.prime(p) for s in range(1,10)}
    assert len(data)==162
    roots_count=0
    for case in data:
        p,s=case['p'],case['s'];n=3*p+s
        old.check_entry(p,s,*entry(p,s))
        ag=delta=0;vals=[];localized=1;units=[]
        for pair in case['root_pairs']:
            alpha,H,f,g=old.check_pair(p,s,pair);roots_count+=2
            ag=gcd(ag,alpha);delta=gcd(delta,H)
            vals.extend((f,g));localized*=abs(f*g)//gcd(f,g)**2
            units.append(F(g,f))
        if (p,s)==(11,3):
            assert ag==2 and delta==26;delta=2;units.append(F(37))
        else:assert ag==1 and delta in (1,2,4)
        for val in vals:
            val=abs(val)
            while gcd(val,localized)>1:val//=gcd(val,localized)
            assert val==1
        if n%2:assert delta==1 and localized%2==0
        shallow_direction(p,s,delta,case['direction'],do_replay=p<=23)
        if n%4==2:
            if case['binary_unit']:
                a,b=case['binary_unit'];assert a[:3]==b[:3] and a[6]==b[6]
                _,f=old.check_row(p,s,a);_,g=old.check_row(p,s,b)
                assert valuation(g-f,2)==2 and (g-f)%n==0
                units.append(F(g,f))
            else:assert (p,s)==(13,3);units.append(F(97,13))
        if n%2==0:
            Q=2*delta*n;known={1};queue=[1]
            generators=[residue(u,Q) for u in units]
            assert all(g%n==1 for g in generators)
            for x in queue:
                for g in generators:
                    v=x*g%Q
                    if v not in known:known.add(v);queue.append(v)
            assert len(known)==2*delta # at most8, independent of n
    old.special_11();old.special_13()
    print('shallow-kernel retained physical certificates: PASS',len(data),roots_count)


def uniform():
    bounds={1:7,2:12,3:8,4:4,5:4}
    for s in range(1,10):
        for a in (s//3+1,s//3+2):
            h=bounds[a];d=3*a-s
            assert min(h-4,d*h-s,d*h-a-4,s*h-5*a-3+s,s*h-3*a-4+s,a*h-4*a-4+s,a*h-3*a-2)>=0
            assert 83//(3*a)-1>=h
    count=0
    for p in list(filter(old.prime,range(83,307)))+[307,997,10007]:
        for s in range(1,10):
            a=s//3+1;groups={};delta=0
            for alpha in (a,a+1):
                q=p//(3*alpha)
                for h in (q-1,q):
                    rows=family(p,s,alpha,h)[:3]
                    for row in rows:old.check_row(p,s,row)
                    _,H,_,_=old.check_pair(p,s,rows[:2]);delta=gcd(delta,H)
                    groups[alpha,h]=rows
            n=3*p+s;assert delta==(1 if n%2 else 2)
            first=groups[a,p//(3*a)-1];second=groups[a+1,p//(3*(a+1))-1]
            pair=None
            for x in first[:2]:
                for y in second[:2]:
                    V=V_of(p,s,(x,y))
                    if n%2 or residue(V[0]+V[3],4)==2:pair=x,y;break
                if pair:break
            assert pair
            shallow_direction(p,s,delta,pair,do_replay=p==83)
            if n%4==2:
                alpha=a if a%2 else a+1
                rows=groups[alpha,p//(3*alpha)-1]
                _,f=old.check_row(p,s,rows[0]);_,g=old.check_row(p,s,rows[2])
                assert valuation(g-f,2)==2
            count+=1
    print('three-row uniform formulas from83: PASS',count)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    symbolic_determinant();local_lift_checks();retained();uniform();check_interval_cover()
    print('transverse root lifting and shallow terminal interfaces: PASS')


if __name__=='__main__':main()
