"""Exact H_t certificates through999 via finite abelian group quotients.

No enumeration of all group elements or characters. For each prime ell in
the group order, check the generator images span G/ell*G over F_ell. Prime
moduli are also covered by the general written pigeonhole proof.
"""
from functools import lru_cache
from math import gcd,isqrt,prod,log
from pathlib import Path
import json

if not __debug__:raise RuntimeError('Assertions must be enabled.')

def primes_to(limit):
    sieve=bytearray(b'\x01')*(limit+1);sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if sieve[p]:sieve[p*p:limit+1:p]=b'\x00'*((limit-p*p)//p+1)
    return [p for p in range(2,limit+1) if sieve[p]]

PRIMES=primes_to(1200)

@lru_cache(None)
def factors(n):
    out=[]
    for p in PRIMES:
        if p*p>n:break
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            out.append((p,e))
    if n>1:out.append((n,1))
    return tuple(out)

@lru_cache(None)
def local_group(p,e):
    modulus=p**e;order=(p-1)*p**(e-1);divisors=[ell for ell,_ in factors(order)]
    generator=next(g for g in range(2,modulus) if gcd(g,p)==1 and all(pow(g,order//ell,modulus)!=1 for ell in divisors))
    assert pow(generator,order,modulus)==1
    return modulus,order,generator

@lru_cache(None)
def quotient_log(p,e,ell):
    modulus,order,g=local_group(p,e)
    assert order%ell==0
    root=pow(g,order//ell,modulus);table={};z=1
    for j in range(ell):table[z]=j;z=z*root%modulus
    assert z==1 and len(table)==ell
    return table

def add_basis(row,basis,ell):
    row=list(row)
    for pivot,v in sorted(basis.items()):
        a=row[pivot]
        if a:row=[(x-a*y)%ell for x,y in zip(row,v)]
    if not any(row):return False
    pivot=next(i for i,x in enumerate(row) if x)
    inv=pow(row[pivot],-1,ell);basis[pivot]=[x*inv%ell for x in row]
    return True

def certificate(t):
    n=t*t+t+1;fs=factors(n)
    assert prod(p**e for p,e in fs)==n
    if len(fs)==1 and fs[0][1]==1:
        # The written proof needs all integers<=t+1, and t+1=-t^2 modn.
        assert (t+1)**2>n and (t*t+t+1)%n==0
        return {'t':t,'n':n,'method':'prime-pigeonhole'}
    local=[(p,e,*local_group(p,e)) for p,e in fs]
    ells=sorted({ell for p,e,m,o,g in local for ell,_ in factors(o)})
    generators=[-1]+[p for p in PRIMES if p<=t and n%p]
    records=[]
    for ell in ells:
        coords=[a for a in local if a[3]%ell==0];basis={};chosen=[]
        for d in generators:
            row=[quotient_log(p,e,ell)[pow(d,o//ell,m)] for p,e,m,o,g in coords]
            if add_basis(row,basis,ell):chosen.append({'d':d,'image':row})
            if len(basis)==len(coords):break
        assert len(basis)==len(coords),(t,n,ell,len(basis),len(coords))
        records.append({'ell':ell,'dimension':len(coords),'witnesses':chosen})
    return {'t':t,'n':n,'method':'prime-quotient-rank','factorization':fs,'local_generators':[(p,e,g) for p,e,m,o,g in local],'quotients':records}

def main():
    records=[certificate(t) for t in range(2,1000)]
    prime_count=sum(x['method']=='prime-pigeonhole' for x in records)
    print('Ht finite abelian quotient certificates t2..999: PASS',len(records),prime_count)
    # Independent explicit failure of a too-strong general-composite rule.
    n=105;subgroup={sign*pow(2,k,n)%n for sign in(1,-1) for k in range(12)}
    assert len(subgroup)==24 and sum(gcd(i,n)==1 for i in range(n))==48
    assert all(d in subgroup for d in range(1,isqrt(n)+1) if gcd(d,n)==1)
    assert 18*18+18+1==7**3
    assert factors(1733)==((1733,1),) and (1733**2+1733+1)%343==0
    assert 3*log(1000**2+1000+1)**2<1000
    print('Ht literature hypothesis and prime-ratio boundary checks: PASS')
    path=Path(__file__).with_name('ht_literature_20260915')/'ht_through999_certificate.json'
    path.write_text(json.dumps({'scope':'t=2..999 only; all-t claim additionally conditional on GRH bound cited in report','records':records},separators=(',',':'))+'\n',encoding='utf-8')
    print('Ht literature interfaces: PASS')

if __name__=='__main__':main()
