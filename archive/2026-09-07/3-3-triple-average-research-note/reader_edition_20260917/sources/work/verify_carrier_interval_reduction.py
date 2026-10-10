"""Exact checks of the new written interval proof and the 180-case residue.

No averaging-word search, no large finite-group enumeration. The general
capacity and unit claims are proved in carrier_interval_and_unit_descent.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import json

import check_large_symmetric_carrier_certificate as old


def entry(p,s):
    if s%3:return s,0
    u=s-3+p%3
    return (p-u)//3,u


def family(p,s,alpha,h):
    t=p-3*alpha*h
    start=max(0,2*alpha-t,((s-alpha)*h-alpha+1)//2)
    rows=[]
    for e in range(start,start+4):
        j=alpha*h;i=j+alpha;k=p-2*j-alpha
        rows.append((i,j,k,j-e,k-e,(alpha-s)*h+alpha+2*e,s*h))
    return rows


def choose_direction(p,s,first,second):
    n=3*p+s
    # Exactly16 local choices, independent of p. This is the proof's mod4/9 menu.
    for a in first:
        for b in second:
            mat=old.mm(old.check_row(p,s,a)[0],old.check_row(p,s,b)[0])
            tr=mat[0]+mat[3]
            if n%2==0 and tr%4!=2:continue
            if n%3==0 and (tr*tr-4*old.det(mat))*pow(tr*tr,-1,9)%9==6:continue
            return (a,b)
    raise AssertionError(('direction',p,s))


def check_uniform_instance(p,s,local=False,literal=False):
    a=s//3+1
    families={}
    ag=hg=0
    for alpha in (a,a+1):
        q=p//(3*alpha)
        for h in (q-1,q):
            rows=family(p,s,alpha,h)
            for row in rows:old.check_row(p,s,row)
            aa,hh,f,g=old.check_pair(p,s,rows[:2])
            assert gcd(f,g)==1
            ag=gcd(ag,aa);hg=gcd(hg,hh)
            families[alpha,h]=rows
    n=3*p+s
    assert ag==1 and hg==(1 if n%2 else 2)
    first=families[a,p//(3*a)-1]
    second=families[a+1,p//(3*(a+1))-1]
    direction=choose_direction(p,s,first,second)
    if local:old.check_direction(p,s,direction)
    if literal:
        for row in direction:old.literal(p,s,row)
    if n%4==2:
        odd=a if a%2 else a+1
        rows=families[odd,p//(3*odd)-1]
        _,f=old.check_row(p,s,rows[0]);_,g=old.check_row(p,s,rows[2])
        assert old.valuation(g-f,2)==2


def check_small_residue():
    path=Path(__file__).with_name('large_symmetric_carrier_reduced_certificate.json')
    cases=json.loads(path.read_text(encoding='utf-8'))['cases']
    assert {(c['p'],c['s']) for c in cases}=={(p,s) for p in range(11,97) if old.prime(p) for s in range(1,10)}
    assert len(cases)==180
    reflections=0
    for case in cases:
        p,s=case['p'],case['s'];n=3*p+s
        # Entry and unit-base certificate fields are deliberately absent.
        assert 'entry' not in case
        old.check_entry(p,s,*entry(p,s))
        ag=hg=0;odd_unit=False;values=[];localized=1
        for pair in case['root_pairs']:
            alpha,h,f,g=old.check_pair(p,s,pair);reflections+=2
            ag=gcd(ag,alpha);hg=gcd(hg,h);odd_unit|=bool(alpha%2)
            values.extend((f,g));localized*=abs(f*g)//gcd(f,g)**2
        assert (ag==2 and hg==26) if (p,s)==(11,3) else (ag==1 and hg in (1,2,4))
        if n%2:assert hg==1 and localized%2==0
        elif not odd_unit:assert (p,s)==(11,3)
        for val in values:
            val=abs(val)
            while gcd(val,localized)>1:val//=gcd(val,localized)
            assert val==1
        old.check_direction(p,s,case['direction'])
        if n%4==2:
            assert odd_unit
            if case['binary_unit']:
                a,b=case['binary_unit']
                assert a[:3]==b[:3] and a[6]==b[6]
                _,f=old.check_row(p,s,a);_,g=old.check_row(p,s,b)
                assert old.valuation(g-f,2)==2 and (g-f)%n==0
                assert gcd(f*g,n)==1 # supplementary localization is safe
            else:
                assert (p,s)==(13,3)
                old.special_13()
        if p<=23:
            for row in case['direction']:old.literal(p,s,row)
    old.special_11()
    print('reduced small carrier certificate: PASS',len(cases),reflections)


def check_capacity_bounds():
    # Finite table of inequalities, not the unbounded parameter claim.
    bounds={1:9,2:14,3:9,4:4,5:4}
    rows=0
    for s in range(1,10):
        a=s//3+1
        for alpha in (a,a+1):
            h=bounds[alpha];d=3*alpha-s
            assert min(h-4,d*h-s,d*h-alpha-6,s*h-5*alpha-5+s,
                       s*h-3*alpha-6+s,alpha*h-4*alpha-6+s,alpha*h-3*alpha-3)>=0
            assert 97//(3*alpha)-1>=h
            rows+=1
    print('carrier capacity bound table: PASS',rows)


def check_interval_cover():
    for allowed in combinations((5,7,11,13,17,19),4):
        intervals=sorted((F(b,a+1),F(b,a-1)) for a in allowed for b in range(1,a//2+1))
        edge=F(1,4)
        for lo,hi in intervals:
            if lo<=edge<hi:edge=hi
        assert edge>=F(1,2)
    assert (5*11)%42==13
    print('small-unit interval covers: PASS 15')


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    check_capacity_bounds();check_interval_cover();check_small_residue()
    count=0
    for p in range(97,307):
        if old.prime(p):
            for s in range(1,10):
                old.check_entry(p,s,*entry(p,s))
                check_uniform_instance(p,s,local=True,literal=(p==97));count+=1
    print('former certificate cases replaced by formulas: PASS',count)
    count=0
    for p in (307,311,997,1009,10007):
        for s in range(1,10):
            check_uniform_instance(p,s,local=True);count+=1
    print('large-parameter formula sanity: PASS',count)
    print('carrier interval and unit descent interfaces: PASS')


if __name__=='__main__':main()
