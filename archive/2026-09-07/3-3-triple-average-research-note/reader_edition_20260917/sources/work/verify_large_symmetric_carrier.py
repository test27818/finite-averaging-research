"""Exact four-atom reflections on (p,p,p+s), not a word search.

First average two disjoint (A^i,B^j,C^k) groups. Retain p+s
new entries, average one selected p-group and its p-entry complement.
"""
from math import gcd
from fractions import Fraction as F
import json
from pathlib import Path
import sys

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq

CERTIFICATE=Path(__file__).with_name('large_symmetric_carrier_small_certificate.json')


def entry_counts(p,s):
    n=3*p+s
    if s%3:return (s,0)
    return next((t,1) for t in range(s-1,p) if gcd(3*t+1,n)==1)


def build_certificate():
    result=[]
    for p in range(11,307):
        if factors(p)!={p:1}:continue
        for s in range(1,10):
            n=3*p+s
            menu=list(candidates(p,s))
            selected=[]; ag=hg=0
            for alpha,j,rows in menu:
                if len(rows)<2:continue
                h=n*(2*j+alpha)-2*p*p
                if gcd(ag,alpha)!=ag or gcd(hg,h)!=hg:
                    selected.append(rows[:2])
                    ag=gcd(ag,alpha);hg=gcd(hg,h)
                if ag==1 and hg in(1,2,4):break
            # One additional row gives a principal unit of exact binary depth2.
            binary=None
            if n%4==2:
                for alpha,j,rows in menu:
                    if len(rows)>=2 and alpha%4==2:
                        binary=[rows[0][0],rows[1][0]];break
                    if len(rows)>=3 and alpha%2:
                        binary=[rows[0][0],rows[2][0]];break
            pair=direction_pair(p,s,menu)
            assert pair is not None
            result.append({'p':p,'s':s,'entry':entry_counts(p,s),
                'root_pairs':[[r[0] for r in pair0] for pair0 in selected],
                'direction':[r[0] for r in pair], 'binary_unit':binary})
    CERTIFICATE.write_text(json.dumps({'format':1,'scope':'all primes11<=p<307, all offsets1<=s<=9',
        'fields':'Counts are i,j,k,x,y,u,v. No input vectors or averaging words are searched.',
        'cases':result},ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print('saved complete parameter certificate',len(result))


def candidates(p, s, max_rows=4):
    r, n = p+s, 3*p+s
    for alpha in range(1, (p-1)//2+1):
        inverse = pow(alpha, -1, p)
        lo = max(0, (p-s-2*alpha+3)//4)
        hi = (p-2*alpha)//2
        for j in range(lo, hi+1):
            i, k = j+alpha, p-2*j-alpha
            v = s*j*inverse % p
            if v > p-s:
                continue
            beta = n*j-p*(p-alpha)
            delta = (beta-alpha*v)//p
            assert beta-alpha*v == p*delta
            a0, b0, c0 = p-2*i, p-2*j, r-2*k
            lower = max(0, p-v+delta-2*a0, p-v-delta-2*b0)
            upper = min(c0, p-v-abs(delta))
            lower += (p-v+delta-lower) % 2
            rows = []
            for u in range(lower, min(upper+1,lower+2*max_rows), 2):
                x, y = (p-v-u+delta)//2, (p-v-u-delta)//2
                counts = (i,j,k,x,y,u,v)
                q = p*r*y-p*p*u+v*beta
                mat = (beta,q,-alpha,-beta)
                lam = beta*beta-alpha*q
                assert lam % p == 0 and lam % n == pow(p,4,n)
                assert all(t>=0 for t in counts)
                assert i+j+k == x+y+u+v == p
                assert 2*i<=p and 2*j<=p and 2*k<=r
                assert x<=a0 and y<=b0 and u<=c0 and v<=p-s
                rows.append((counts,mat,lam//p))
            if rows:
                yield alpha,j,rows


def unit_image(p,n):
    # Prime generators suffice; composite digits add no new subgroup.
    generators=[n-1]+[q for q in range(2,p+1)
                         if (q%2 or n%2) and gcd(q,n)==1 and factors(q)=={q:1}]
    subgroup={1}
    for q in generators:
        if q in subgroup:continue
        old=list(subgroup)
        power=q
        while power not in subgroup:
            subgroup.update(power*x%n for x in old)
            power=power*q%n
    return subgroup


def direction_pair(p,s,menu):
    n=3*p+s
    byalpha={}
    for alpha,j,rows in menu:
        bucket=byalpha.setdefault(alpha,{})
        for row in rows:
            signature=tuple(x%36 for x in row[1])
            bucket.setdefault(signature,row)
    for alpha,first in byalpha.items():
        second=byalpha.get(alpha+1,{})
        for m0,row0 in first.items():
            for m1,row1 in second.items():
                t=mm(m0,m1)
                trace=t[0]+t[3]
                det=t[0]*t[3]-t[1]*t[2]
                if n%2==0 and trace%4!=2: continue
                if n%3==0 and (trace*trace-4*det)*pow(trace*trace,-1,9)%9==6:continue
                return row0,row1
    return None


def formula_rows(p,s,alpha,h,epsilon):
    j=alpha*h
    i,k=j+alpha,p-2*j-alpha
    v=s*h
    x,y=j-epsilon,k-epsilon
    u=(alpha-s)*h+alpha+2*epsilon
    beta=(3*p+s)*j-p*(p-alpha)
    q=p*(p+s)*y-p*p*u+v*beta
    lam=beta*beta-alpha*q
    assert lam % p == 0
    return (i,j,k,x,y,u,v),(beta,q,-alpha,-beta),lam//p


def replay(p,s,row):
    counts,mat,f=row
    i,j,k,x,y,u,v=counts
    r=p+s
    for a,z in ((1,0),(0,1)):
        raw=[F(a)]*p+[F(r*z-a)]*p+[F(-p*z)]*r
        ledger=Ledger(raw,p)
        groups=[list(range(p)),list(range(p,2*p)),list(range(2*p,2*p+r))]
        for step in range(2):
            ga,gb,gc=groups
            d1=ga[:i]+gb[:j]+gc[:k]
            d2=ga[i:2*i]+gb[j:2*j]+gc[k:2*k]
            ledger.average(d1); ledger.average(d2)
            ga,gb,gc=ga[2*i:],gb[2*j:],gc[2*k:]
            fresh=d1+d2
            kept,fresh=fresh[:r],fresh[r:]
            left=ga[:x]+gb[:y]+gc[:u]+fresh[:v]
            right=ga[x:]+gb[y:]+gc[u:]+fresh[v:]
            assert len(left)==len(right)==p
            assert sorted(left+right+kept)==list(range(3*p+s))
            ledger.average(left); ledger.average(right)
            groups=[left,right,kept]
            av,zv=(F(mat[0]*a+mat[1]*z,p*p),F(mat[2]*a+mat[3]*z,p*p)) if step==0 else (F(f*a,p**3),F(f*z,p**3))
            assert all(ledger.state[t]==val for group,val in zip(groups,(av,r*zv-av,-p*zv)) for t in group)
        ledger.independent_replay(raw)


def main():
    failures=[]; direction_failures=[]; unit_failures=[]; two_unit_failures=[]; total=0
    for p in range(11,307):
        if factors(p)!={p:1}: continue
        for s in range(1,10):
            menu=list(candidates(p,s))
            paired=[(a,j,rows) for a,j,rows in menu if len(rows)>=2]
            ag=hg=0
            for a,j,rows in paired:
                ag=gcd(ag,a)
                hg=gcd(hg,(3*p+s)*(2*j+a)-2*p*p)
            total+=1
            if ag!=1 or hg not in (1,2,4):
                failures.append((p,s,len(menu),len(paired),ag,hg))
            if direction_pair(p,s,menu) is None:
                direction_failures.append((p,s))
            if len(unit_image(p,3*p+s)) != sum(gcd(x,3*p+s)==1 for x in range(3*p+s)):
                unit_failures.append((p,s))
            if (3*p+s)%4==2 and not any(a%4==2 or (a%2==1 and len(rows)>=3) for a,j,rows in paired):
                two_unit_failures.append((p,s))
    print('small-parameter paired-reflection interface',total,'failures',failures)
    print('small-parameter common direction failures',direction_failures)
    print('small-parameter common unit failures',unit_failures)
    print('small-parameter second binary unit failures',two_unit_failures)
    total=0
    for p in range(307,1000):
        if factors(p)!={p:1}:continue
        for s in range(1,10):
            for alpha in (s,s+1):
                h0=(p-alpha-s+6+3*alpha+s-1)//(3*alpha+s)
                assert h0+1 <= (p-2*alpha)//(3*alpha)
                for h in (h0,h0+1):
                    for e in range(4):
                        row=formula_rows(p,s,alpha,h,e)
                        i,j,k,x,y,u,v=row[0]
                        assert min(row[0])>=0 and i+j+k==x+y+u+v==p
                        assert 2*i<=p and 2*j<=p and 2*k<=p+s
                        assert x<=p-2*i and y<=p-2*j and u<=p+s-2*k and v<=p-s
                        total+=1
    print('uniform large-parameter count formula',total)
    for p,s in ((11,1),(11,9),(13,3),(17,7),(307,9)):
        for a,j,rows in list(candidates(p,s))[:2]:
            replay(p,s,rows[0])
    print('literal four-atom reflections PASS')


if __name__=='__main__':
    if '--build-certificate' in sys.argv:build_certificate()
    else:main()
