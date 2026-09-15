"""Uniform p=2,3 odd-exponent critical controller; no word search."""
from fractions import Fraction as F
from math import gcd,log,prod
from pathlib import Path
import json

from verify_uniform_odd_middle_cores import mm,invq
from verify_square_arity_controller_and_nine_thirteen import power,sc,delta,det
from verify_even_odd_half_core import I,U,L
from verify_four_prime_entry_and_band import Ledger
from verify_ht_literature_interfaces import factors,local_group,quotient_log,add_basis,PRIMES

if not __debug__:raise RuntimeError('Assertions must be enabled.')

def family(p,s):
    k=p*s*s;r=p*s;n=k+r+1
    A=(1,-F(1,s),0,-F(1,s))
    B=(-r-1,r,-n,k+r);C=(-r-1,1,-n,1);S=(1,-1,0,-1)
    order=4 if p==2 else 6
    assert power(C,order)==sc(I,-k**(order//2))
    assert mm(invq(C),B)==S
    assert mm(S,A)==delta(F(1,s))
    for d in (1,2,p,s,r):
        M=(r*r+r-k,-r*d,r*n,-(r+k)*d)
        assert M==mm(power(C,2),delta(d))
        assert det(M)==k*k*d
    if s%p==0:
        assert mm(delta(F(1,s)),delta(s//p))==delta(F(1,p))
    elif (s-1)%p:
        assert gcd(p,(s-1)**2*n**3)==1
    else:
        H=sc(mm(mm(delta(p),power(C,2)),delta(p)),F(1,p*k))
        assert H==(F((p-1)*s+1,p*s),-F(1,s),F(n,s),-F(p*(s+1),s))
        assert ((p-1)*s+1)%p==0 and det(H)==1
        assert mm(mm(power(C,2),delta(p)),invq(H))==sc(delta(F(1,p)),p*k)
    assert mm(mm(mm(S,delta(s)),S),delta(F(1,s)))==U(F(s-1,s))
    P=(1,-r-1,0,-n)
    assert mm(mm(invq(P),U(1)),P)==U(-n)
    assert mm(mm(mm(mm(invq(P),C),U(k)),invq(C)),P)==L(n)
    if p==3 and s%2:
        H=sc(mm(mm(delta(2),power(C,4)),delta(2)),F(1,2*k*k))
        assert H==(F(s+1,2*s),-F(1,s),F(n,s),-4-F(2,s))
        assert det(H)==1
        assert mm(mm(power(C,4),delta(2)),invq(H))==sc(delta(F(1,2)),2*k*k)
    assert mm(mm(mm(S,delta(2)),S),delta(F(1,2)))==U(F(1,2))
    assert mm(mm(U(-1),sc(C,F(1,k))),delta(k))==L(-F(n,k))
    assert gcd(k-1,n)==1 and gcd(k,n)==1
    assert 2**(r+1)>n
    return s,k,r,n,A,B,C,S

def data(p,a):return family(p,p**a)

def apply_atom(led,groups,k,r,name):
    ga,gb,gc=(list(x) for x in groups)
    if name=='A':
        chosen=ga[:k-r]+gb;new=[chosen,ga[k-r:],gc]
    elif name=='B':
        chosen=ga[:k-1]+gc;new=[chosen,gb,ga[k-1:]]
    elif name=='C':
        chosen=ga[:k-r]+gb[:r-1]+gc;new=[chosen,ga[k-r:],gb[r-1:]]
    else:raise AssertionError(name)
    led.average(chosen);return new

def m_atom(led,groups,k,r,d):
    ga,gb,gc=(list(x) for x in groups);j=r-d
    chosen=ga[:k-j-1]+gb[:j]+gc;led.average(chosen)
    old=ga[k-j-1:];single=old[:1];kept=chosen[:r]
    second=old[1:]+gb[j:]+chosen[r:];led.average(second)
    return [second,kept,single]

def physical(p,a):
    s,k,r,n,A,B,C,S=data(p,a);order=4 if p==2 else 6;count=0
    for x,y in ((1,0),(0,1)):
        raw=[F(x)]*k+[F(x-y)]*r+[-k*x-r*(x-y)]
        for kind in ('cycle',1,2,r):
            led=Ledger(raw,k);groups=[list(range(k)),list(range(k,k+r)),[n-1]]
            if kind=='cycle':
                for _ in range(order):groups=apply_atom(led,groups,k,r,'C')
                mat=sc(I,-F(1,k**(order//2)))
            else:
                groups=m_atom(led,groups,k,r,kind)
                mat=sc(mm(power(C,2),delta(kind)),F(1,k*k))
            xx,yy=mat[0]*x+mat[1]*y,mat[2]*x+mat[3]*y
            values=(xx,xx-yy,-k*xx-r*(xx-yy))
            assert all(led.state[q]==v for g,v in zip(groups,values) for q in g)
            led.independent_replay(raw);count+=1
    return count

def small_units(p,s):
    s,k,r,n,*_=family(p,s);fs=factors(n)
    assert prod(l**e for l,e in fs)==n
    locals=[(l,e,*local_group(l,e)) for l,e in fs]
    primes=sorted({ell for l,e,m,o,g in locals for ell,_ in factors(o)})
    records=[]
    for ell in primes:
        coords=[z for z in locals if z[3]%ell==0];basis={};witness=[]
        for d in [-1]+[z for z in PRIMES if z<=r and n%z]:
            row=[quotient_log(l,e,ell)[pow(d,o//ell,m)] for l,e,m,o,g in coords]
            if add_basis(row,basis,ell):witness.append((d,row))
            if len(basis)==len(coords):break
        assert len(basis)==len(coords),(p,s,n,ell)
        records.append((ell,len(coords),witness))
    return {'p':p,'s':s,'r':r,'n':n,'factorization':fs,'quotients':records}

def entry(p,a):
    s,k,r,n,*_=data(p,a);ells=[ell for ell,_ in factors(n)]
    modulus=prod(ells)
    singles=[(modulus//ell)*pow(modulus//ell,-1,ell)%modulus for ell in ells]
    singles+=[-sum(singles)]+[0]*(r-len(ells))
    raw=[0]*k+singles
    led=Ledger(raw,k);block=list(range(k));positions=list(range(k,n));target=len(positions)-1
    # Force several distinct initial witnesses and an empty target.
    for ell in ells:
        ds=[led.state[i]-led.state[block[0]] for i in positions]
        def res(x):return x.numerator*pow(x.denominator,-1,ell)%ell
        if res(ds[target]):continue
        source=next(i for i,x in enumerate(ds) if res(x));buffer=next(i for i in range(len(ds)) if i not in(source,target))
        periods=[]
        for q in ells:
            if (k+1)%q==0:periods.append(q)
            else:
                v=-pow(k,-1,q)%q;e=1;z=v
                while z!=1:z=z*v%q;e+=1
                periods.append(e)
        from math import lcm
        period=lcm(*periods);exponent=(modulus//ell)*pow(modulus//ell,-1,ell)%modulus
        stages=((source,period-1),(buffer,1),(target,period-1),(buffer,period-1),(source,1),(buffer,1),(target,1),(buffer,period-1))
        for _ in range(exponent):
            for role,times in stages:
                for _ in range(times):
                    old=block[-1];chosen=block[:-1]+[positions[role]]
                    led.average(chosen);block,positions[role]=chosen,old
    w=positions[target];kept=block[-r:]
    final=block[:-r]+[v for i,v in enumerate(positions) if i!=target];led.average(final)
    u,v=led.state[final[0]],led.state[kept[0]]
    for ell in ells:assert (u-v).numerator%ell
    assert led.state[w]==-k*u-r*v
    led.independent_replay(raw)
    return len(led.operations) if hasattr(led,'operations') else 1

def main():
    for p in (2,3):
        for a in range(1,13):data(p,a)
    print('two-three odd-power uniform controller and entry identities: PASS 24')
    count=sum(physical(p,a) for p,a in ((2,1),(2,2),(3,1),(3,2)))
    print('two-three odd-power literal cyclic and multiplier returns: PASS',count)
    for p,a in ((2,1),(3,1)):entry(p,a)
    print('two-three odd-power forced singleton-entry replay: PASS 2')
    records=[small_units(p,p**a) for p,stop in ((2,8),(3,5)) for a in range(1,stop)]
    for p,a in ((2,8),(3,5)):
        s,k,r,n,*_=data(p,a)
        assert r>3*log(n)**2
        # f(s)/s decreases once log(n)>4 because n'/n<2/s.
        assert log(n)>4
    print('two-three odd-power complete finite small-unit certificates: PASS',len(records))
    Path(__file__).with_name('two_three_odd_power_small_units.json').write_text(json.dumps(records,separators=(',',':'))+'\n',encoding='utf-8')
    general=[small_units(m,s) for m in (2,3) for s in range(2,256)]
    for m in (2,3):
        s,k,r,n,*_=family(m,256)
        assert r>3*log(n)**2 and log(n)>4
    Path(__file__).with_name('two_three_square_multiple_small_units.json').write_text(json.dumps(general,separators=(',',':'))+'\n',encoding='utf-8')
    print('two-three square-multiple full finite small-unit certificates: PASS',len(general))
    print('two-three odd-prime-power critical completion interfaces: PASS')

if __name__=='__main__':main()
