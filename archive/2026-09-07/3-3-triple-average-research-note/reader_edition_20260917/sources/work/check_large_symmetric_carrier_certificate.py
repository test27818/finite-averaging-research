"""Independently check fixed count certificates; no candidate search.

The 522 parameter cases are exhaustive below307. Infinite quantifiers above
that cutoff are proved in the accompanying document, not by this check.
"""
from fractions import Fraction as F
from math import gcd
import json
from pathlib import Path

from verify_four_prime_entry_and_band import Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_even_odd_half_core import I,U,L,crt_pairs,valuation,mod_power
from verify_upper_band_unrestricted_completion import local_cycle_hit,zy

if not __debug__:
    raise RuntimeError('The proof certificate requires enabled assertions.')

def prime(p):return p>=2 and all(p%d for d in range(2,int(p**.5)+1))
def sc(a,x):return tuple(x*t for t in a)
def det(a):return a[0]*a[3]-a[1]*a[2]
def com(a,b):return mm(mm(mm(a,b),invq(a)),invq(b))


def check_row(p,s,c):
    i,j,k,x,y,u,v=c;r=p+s;n=3*p+s
    assert min(c)>=0 and i+j+k==x+y+u+v==p
    assert 2*i<=p and 2*j<=p and 2*k<=r
    assert x<=p-2*i and y<=p-2*j and u<=r-2*k and v<=p-s
    alpha=i-j; beta=r*j-p*k
    assert alpha>0 and p*(x-y)+alpha*v==beta
    q=p*r*y-p*p*u+v*beta
    mat=(beta,q,-alpha,-beta)
    lam=beta*beta-alpha*q
    assert lam%p==0 and mm(mat,mat)==sc(I,lam)
    assert lam%n==pow(p,4,n)
    return mat,lam//p


def check_pair(p,s,rows):
    a,f=check_row(p,s,rows[0]);b,g=check_row(p,s,rows[1]);n=3*p+s;r=p+s
    step=rows[1][5]-rows[0][5]
    assert step==2 and rows[0][:3]==rows[1][:3] and rows[0][6]==rows[1][6]
    alpha=-a[2]; beta=a[0]
    assert g-f==alpha*n
    t=mm(a,sc(b,F(1,p*f)))
    assert t==(1,-F(beta*n,f),0,F(g,f))
    swap=(-1,r,0,1)
    h=2*beta+r*alpha
    assert com(swap,t)==U(F(n*h,g))
    assert h==n*(2*rows[0][1]+alpha)-2*p*p
    common=gcd(f,g)
    assert gcd(f,n)==1 and common==gcd(f,alpha)
    # Cancelled factors are checked against all reduced multipliers below.
    pmat=(1,beta,0,-alpha)
    assert mm(mm(invq(pmat),U(1)),pmat)==U(-alpha)
    lower=mm(mm(mm(mm(invq(pmat),a),U(det(a))),invq(a)),pmat)
    assert lower==L(alpha)
    return alpha,h,f,g


def literal(p,s,c):
    mat,f=check_row(p,s,c);r=p+s
    for a,z in ((1,0),(0,1)):
        raw=[F(a)]*p+[F(r*z-a)]*p+[F(-p*z)]*r
        led=Ledger(raw,p);groups=[list(range(p)),list(range(p,2*p)),list(range(2*p,3*p+s))]
        for iteration in (1,2):
            ga,gb,gc=groups;i,j,k,x,y,u,v=c
            d=ga[:i]+gb[:j]+gc[:k];e=ga[i:2*i]+gb[j:2*j]+gc[k:2*k]
            led.average(d);led.average(e)
            ga,gb,gc=ga[2*i:],gb[2*j:],gc[2*k:];fresh=d+e
            kept,fresh=fresh[:r],fresh[r:]
            left=ga[:x]+gb[:y]+gc[:u]+fresh[:v]
            right=ga[x:]+gb[y:]+gc[u:]+fresh[v:]
            assert sorted(left+right+kept)==list(range(3*p+s))
            led.average(left);led.average(right);groups=[left,right,kept]
            aa,zz=(F(mat[0]*a+mat[1]*z,p*p),F(mat[2]*a+mat[3]*z,p*p)) if iteration==1 else (F(f*a,p**3),F(f*z,p**3))
            assert all(led.state[q]==val for g0,val in zip(groups,(aa,r*zz-aa,-p*zz)) for q in g0)
        led.independent_replay(raw)


def check_entry(p,s,t,u):
    n=3*p+s;r=p+s
    assert 0<=u<=s and 0<=t<=p and t+u>=s and t+u<=p
    q=3*t+u
    assert gcd(q,n)==1
    # From (A^(2p),B^p,C^s), average a group leaving p+s old A.
    d=p-3*t-u;b=s*t-p*u
    change=(d,b,-1,0)
    assert det(change)!=0
    assert (change[0]+p*change[2])%n==(-q)%n
    assert (change[1]+p*change[3])%n==(-p*q)%n
    if p<=23:
        for a,z in ((1,0),(0,1)):
            raw=[F(a)]*(2*p)+[F(-2*a+s*z)]*p+[F(-p*z)]*s
            led=Ledger(raw,p);ga=list(range(2*p));gb=list(range(2*p,3*p));gc=list(range(3*p,n))
            h=p-t-u;fresh=ga[:h]+gb[:t]+gc[:u];led.average(fresh)
            ga=ga[h:];gb=gb[t:];gc=gc[u:];kept=ga[:r];ga=ga[r:]
            other=ga+gb+gc;assert len(other)==p;led.average(other)
            aa=F(d*a+b*z,p);zz=-F(a,p)
            assert all(led.state[q]==aa for q in fresh)
            assert all(led.state[q]==r*zz-aa for q in other)
            assert all(led.state[q]==raw[kept[0]] for q in kept)
            led.independent_replay(raw)


def check_direction(p,s,rows):
    j0,f0=check_row(p,s,rows[0]);j1,f1=check_row(p,s,rows[1])
    alpha=-j0[2];assert -j1[2]==alpha+1
    n=3*p+s
    t=sc(zy(mm(j0,j1),p),F(1,p**4))
    assert tuple(residue(x,n) for x in t)==(1,residue(F(-1,p*p),n),0,1)
    trace=t[0]+t[3]
    if n%2==0:assert residue(trace,4)==2
    if n%3==0:
        c=1-4*det(t)/(trace*trace)
        assert residue(c,3)==0 and residue(c,9)!=6
    # Actual local lift for an integer primitive legal column, simultaneously.
    remaining=n; fs=[]
    ell=2
    while ell*ell<=remaining:
        if remaining%ell==0:
            e=0
            while remaining%ell==0:remaining//=ell;e+=1
            fs.append((ell,e))
        ell+=1
    if remaining>1:fs.append((remaining,1))
    pairs=[];pair=(17*n+5,19*n+1)
    for ell,e in fs:
        exponent=4*e+(6 if ell==2 else 0)
        power=local_cycle_hit(t,ell,exponent,pair)
        pairs.append((power,ell**exponent))
    power=crt_pairs(pairs)
    modulus=1
    for _,q in pairs:modulus*=q
    out=mod_power(t,power,modulus)
    aa=(out[0]*pair[0]+out[1]*pair[1])%modulus
    bb=(out[2]*pair[0]+out[3]*pair[1])%modulus
    assert aa==0 and gcd(bb,modulus)==1


def check_unit_base(p,n):
    subgroup={1}
    for q in [-1]+[q for q in range(2,p+1) if prime(q) and gcd(q,n)==1]:
        q%=n
        if q in subgroup:continue
        old=list(subgroup);v=q
        while v not in subgroup:
            subgroup.update(v*x%n for x in old);v=v*q%n
    assert len(subgroup)==sum(gcd(x,n)==1 for x in range(n))


def special_11():
    # Matrices give two transverse unipotents modulo13. No group enumeration.
    d=(6,9,0,11);e=(11,0,8,6)
    ja=(-27,568,-2,27);jb=(-27,172,-2,27)
    t=mm(invq(ja),jb)
    d_full=sc(mm(t,t),1/t[3])
    transverse=(-52,905,-3,52)
    assert check_row(11,3,[4,1,6,2,7,1,1])==(transverse,-1)
    assert check_row(11,3,[3,2,6,0,4,1,6])[0]==(-38,267,-1,38)
    e_full=mm(mm(transverse,d_full),invq(transverse))
    assert tuple(residue(x,13) for x in d_full)==d
    assert tuple(residue(x,13) for x in e_full)==e
    assert det(d_full)==det(e_full)==1
    w=mm(d,mm(mm(e,e),e))
    w=tuple(x%13 for x in w)
    assert w==(5,7,7,10) and (w[0]+w[3])%13==2
    assert all(x%13==0 for x in mm(tuple(x-y for x,y in zip(w,I)),tuple(x-y for x,y in zip(w,I))))
    v=(1,5);dv=((d[0]+5*d[1])%13,(d[2]+5*d[3])%13)
    assert (v[0]*dv[1]-v[1]*dv[0])%13!=0
    assert tuple(residue(x,36) for x in d_full)==I
    assert tuple(residue(x,36) for x in e_full)==I
    assert gcd(26*36,32*36**2)==2*36
    assert 37==1+36 # exact principal-unit depth at both dangerous primes
    literal(11,3,[4,1,6,2,7,1,1])


def special_13():
    j,f=check_row(13,3,[4,2,7,2,7,1,3]);assert f==97
    # Same first two averages, different complementary output groups.
    counts=(4,2,7,1,2,0,10)
    i,jj,k,x,y,u,v=counts;p=13;r=16
    assert x+y+u+v==p and x<=p-2*i and y<=p-2*jj and u<=r-2*k and v<=2*p-r
    alpha=i-jj;beta=r*jj-p*k
    m=(p*(x-y)+alpha*v,p*r*y-p*p*u+beta*v,-alpha,-beta)
    assert m==(7,-174,-2,59) and det(m)==65 and gcd(det(m),42)==1
    assert mm(m,invq(j))==(-F(5,97),-F(192,97),0,1)
    # Thus97 is localized after5;97/13 supplies the missing binary unit.
    assert residue(F(97,13),42)==1 and valuation(97-13,2)==2
    for a,z in ((1,0),(0,1)):
        raw=[F(a)]*p+[F(r*z-a)]*p+[F(-p*z)]*r
        led=Ledger(raw,p);ga=list(range(p));gb=list(range(p,2*p));gc=list(range(2*p,2*p+r))
        d=ga[:i]+gb[:jj]+gc[:k];e=ga[i:2*i]+gb[jj:2*jj]+gc[k:2*k]
        led.average(d);led.average(e)
        ga,gb,gc=ga[2*i:],gb[2*jj:],gc[2*k:];fresh=d+e
        kept,fresh=fresh[:r],fresh[r:]
        left=ga[:x]+gb[:y]+gc[:u]+fresh[:v]
        right=ga[x:]+gb[y:]+gc[u:]+fresh[v:]
        led.average(left);led.average(right)
        aa,zz=F(m[0]*a+m[1]*z,p*p),F(m[2]*a+m[3]*z,p*p)
        assert all(led.state[t]==val for g0,val in zip((left,right,kept),(aa,r*zz-aa,-p*zz)) for t in g0)
        led.independent_replay(raw)


def check_small():
    data=json.loads(Path(__file__).with_name('large_symmetric_carrier_small_certificate.json').read_text(encoding='utf-8'))['cases']
    assert {(x['p'],x['s']) for x in data}=={(p,s) for p in range(11,307) if prime(p) for s in range(1,10)}
    assert len(data)==522
    reflections=0
    for case in data:
        p,s=case['p'],case['s'];n=3*p+s
        check_entry(p,s,*case['entry'])
        ag=hg=0;odd_unit=False
        values=[];localized=1
        for pair in case['root_pairs']:
            alpha,h,f,g=check_pair(p,s,pair);reflections+=2
            values.extend((f,g));localized*=abs(f*g)//gcd(f,g)**2
            ag=gcd(ag,alpha);hg=gcd(hg,h)
            odd_unit |= bool(alpha%2)
        if (p,s)!=(11,3):assert ag==1 and hg in (1,2,4)
        else:assert ag==2 and hg==26
        if n%2:assert hg==1 and localized%2==0
        elif not odd_unit:assert (p,s)==(11,3)
        for val in values:
            val=abs(val)
            while gcd(val,localized)>1:val//=gcd(val,localized)
            assert val==1 # no unproved assertion that cancelled factors are units
        check_direction(p,s,case['direction'])
        check_unit_base(p,n)
        if n%4==2:
            assert odd_unit
            if case['binary_unit']:
                assert case['binary_unit'][0][:3]==case['binary_unit'][1][:3]
                assert case['binary_unit'][0][6]==case['binary_unit'][1][6]
                a,f=check_row(p,s,case['binary_unit'][0]);b,g=check_row(p,s,case['binary_unit'][1])
                assert valuation(g-f,2)==2 and (g-f)%n==0
            else:
                assert (p,s)==(13,3)
                special_13()
        if p<=23:
            for row in case['direction']:literal(p,s,row)
    special_11()
    print('large symmetric carrier finite parameter certificate: PASS',len(data),reflections)


def check_uniform():
    count=0
    for p in (307,311,317,331,367,401,499,997,1009,10007):
        for s in range(1,10):
            families={}
            for alpha in (s,s+1):
                low=(p-alpha-s+6+3*alpha+s-1)//(3*alpha+s)
                assert low+1<=(p-2*alpha)//(3*alpha)
                for h in (low,low+1):
                    rows=[]
                    for e in range(4):
                        j=alpha*h;i=j+alpha;k=p-2*j-alpha;v=s*h
                        x=j-e;y=k-e;u=(alpha-s)*h+alpha+2*e
                        row=[i,j,k,x,y,u,v];check_row(p,s,row);rows.append(row)
                    check_pair(p,s,rows[:2]);families[alpha,h]=rows
                    count+=4
            ag=hg=0
            for (alpha,h),rows in families.items():
                aa,hh,f,g=check_pair(p,s,rows[:2]);ag=gcd(ag,aa);hg=gcd(hg,hh)
            assert ag==1 and hg in(1,2,4)
            # At most16 fixed pairs adjust the two low-prime conditions.
            h0=min(h for a,h in families if a==s);h1=min(h for a,h in families if a==s+1)
            good=[]
            for a in families[s,h0]:
                for b in families[s+1,h1]:
                    t=mm(check_row(p,s,a)[0],check_row(p,s,b)[0]);tr=t[0]+t[3]
                    if (3*p+s)%2==0:
                        if tr%4!=2:continue
                    if (3*p+s)%3==0 and (tr*tr-4*det(t))*pow(tr*tr,-1,9)%9==6:continue
                    good.append((a,b))
            assert good
            check_direction(p,s,good[0])
    print('large symmetric carrier uniform formulas and local lifts: PASS',count)


if __name__=='__main__':
    check_small();check_uniform()
    print('large symmetric carrier completion interfaces: PASS')
