"""Generic two-CRT column preparation, with both endpoint physical matrices.

Only exact arithmetic and prescribed choices. No word discovery or orbit search.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from random import Random
from time import perf_counter
import sys, json
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'work'))
from verify_four_prime_entry_and_band import Ledger, factors
from verify_uniform_odd_middle_cores import bezout, mm
from verify_common_shape_and_relation_lattice import primes_below
from verify_square_zero_compiler import check_frozen_files, check_local_links


def append_crt(a, modulus, value, prime):
    assert gcd(modulus, prime) == 1
    return a + modulus * ((value-a) * pow(modulus, -1, prime) % prime), modulus * prime


def prepare(m, Q, q0, u, v, selector):
    assert Q % (2*m) == 0 or (Q % m == 0 and Q % 2 == 0)
    assert gcd(q0,m) == gcd(u,v) == gcd(v,m) == 1 and v % 2
    mv = abs(v)
    a = (u*pow(2,-1,mv)) % mv if mv > 1 else 0
    modulus = mv
    for ell in factors(Q):
        if m % ell == 0 or v % ell == 0:
            continue
        target = (q0*v-1)*pow(m,-1,ell) % ell
        a, modulus = append_crt(a, modulus, target, ell)
    for ell in factors(q0):
        if modulus % ell:
            a, modulus = append_crt(a, modulus, 1, ell)
    assert (2*a-u) % mv == 0 and gcd(a,q0*v) == 1
    u1, v1 = -a, q0*v-m*a
    assert gcd(u1,v1) == gcd(v1,Q) == 1 and v1 % 2
    q, eps = selector(v1)
    assert eps in (-1,1) and gcd(q,m) == 1 and (q*v1-eps)%m == 0
    modv = abs(v1)
    b = (u1*pow(2,-1,modv)) % modv if modv > 1 else 0
    K = Q//m
    if K > 1:
        b += modv * ((((q*v1-eps)//m-b)*pow(modv,-1,K))%K)
    modulus = modv*K
    for ell in factors(q):
        if modulus % ell:
            b, modulus = append_crt(b, modulus, 1, ell)
    assert (2*b-u1) % modv == 0 and gcd(b,q*v1) == 1
    u2, v2 = -b, q*v1-m*b
    assert gcd(u2,v2) == 1 and (v2-eps) % Q == 0
    shift = -u2*pow(v2,-1,Q) % Q
    u3 = u2+shift*v2
    d, A, B = bezout(u3,v2)
    assert d == 1
    correction = -A*pow(v2,-1,Q) % Q
    A, B = A+correction*v2, B-correction*u3
    P = (eps*v2,-eps*u3,eps*A,eps*B)
    assert (P[0]*u3+P[1]*v2,P[2]*u3+P[3]*v2) == (0,eps)
    assert P[0]*P[3]-P[1]*P[2] == 1
    assert tuple(x%Q for x in P) == (1,0,0,1)
    return ((2*a-v,v,q0),(2*b-v1,v1,q))


def endpoint_selector(p,r,v):
    if r == 1:
        m=2*p+1
        j=pow(2*v,-1,m)
        if j>p:
            return 2*(m-j),-1
        return 2*j,1
    m=p+1
    q=pow(v,-1,m)
    return (p,-1) if q == 1 else (q,1)


def literal_endpoint(p,r,u,v,q):
    if r == 1:
        assert q%2 == 0 and 2<=q<=2*p
        m=2*p+1
        A,B,C=F(u+v,2),F(u-v,2),F(-p*u)
        j=q//2
        raw=[A]*p+[B]*p+[C]
        ledger=Ledger(raw,p)
        ga,gb=list(range(p)),list(range(p,2*p))
        first=ga[:j-1]+gb[:p-j]+[2*p]
        second=ga[j-1:p-1]+gb[p-j:]
        keep=ga[p-1:]
        u1,v1=F(-u-v,2*p),F(-m*u+(2*q-m)*v,2*p)
        expected=(F(u1+v1,2),F(u1-v1,2),-p*u1)
    else:
        assert 2<=q<=p
        m=p+1
        A,B,C=u+v,u-v,-p*u
        raw=[A]*p+[B]*p+[C]*2
        ledger=Ledger(raw,p)
        ga,gb=list(range(p)),list(range(p,2*p))
        first=ga[:q-2]+gb[:p-q]+[2*p,2*p+1]
        second=ga[q-2:p-2]+gb[p-q:]
        keep=ga[p-2:]
        u1,v1=F(-u-v,p),F(-m*u+(2*q-m)*v,p)
        expected=(u1+v1,u1-v1,-p*u1)
    ledger.average(first);ledger.average(second)
    assert sorted(first+second+keep)==list(range(2*p+r))
    for group,value in zip((first,second,keep),expected):
        assert all(ledger.state[i]==value for i in group)
    ledger.independent_replay(raw)
    return 2


def literal_weighted_return(p,r,h):
    assert 1<=r<=h<=p
    atoms=0
    for u,v in ((F(1),F(0)),(F(0),F(1))):
        A,B,C=F(u+v,2),F(u-v,2),-F(p,r)*u
        raw=[A]*p+[B]*p+[C]*r
        led=Ledger(raw,p)
        ga,gb,gc=list(range(p)),list(range(p,2*p)),list(range(2*p,2*p+r))
        left=ga[:h-r]+gb[:p-h]+gc
        right=ga[h-r:p-r]+gb[p-h:]
        kept=ga[p-r:]
        assert sorted(left+right+kept)==list(range(2*p+r))
        led.average(left);led.average(right)
        up=F(-r,2*p)*(u+v)
        vp=F(-(2*p+r),2*p)*u+F(4*h-2*p-r,2*p)*v
        expected=(F(up+vp,2),F(up-vp,2),-F(p,r)*up)
        for group,value in zip((left,right,kept),expected):
            assert all(led.state[i]==value for i in group)
        led.independent_replay(raw)
        atoms+=2
    return atoms


def order(value,ell):
    value=F(value)
    if not value:
        return 1000000
    a,b=abs(value.numerator),value.denominator
    result=0
    while a%ell==0:a//=ell;result+=1
    while b%ell==0:b//=ell;result-=1
    return result


def apply(A,v):return (A[0]*v[0]+A[1]*v[1],A[2]*v[0]+A[3]*v[1])
def normval(v,ell):return min(order(x,ell) for x in v)
def content(A,v,ell):return normval(apply(A,v),ell)-normval(v,ell)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    started=perf_counter();rng=Random(20260916)
    general=endpoints=atoms=parities=cocycles=weighted_atoms=0
    for m in range(3,64):
        for aux in (1,5,14):
            Q=2*m*m*aux
            q0=m+1
            for _ in range(5):
                v=2*rng.randrange(-2000,2000)+1
                u=rng.randrange(-2000,2000)
                if gcd(u,v)!=1 or gcd(v,m)!=1:v=1
                prepare(m,Q,q0,u,v,lambda w,m=m:(pow(w,-1,m),1))
                general+=1
    for p in primes_below(150):
        for r in (1,2):
            m=2*p+1 if r==1 else p+1
            q0=2 if r==1 else p
            h=abs(p*p-1) if p%4==1 else (p+1)**2
            Q=2*m if r==1 else h*h
            for _ in range(12):
                v=rng.randrange(-50000,50000)
                u=rng.randrange(-50000,50000)
                if not v or gcd(u,v)!=1 or gcd(v,m)!=1:v=1
                if r==1 and v%2==0:
                    uu,vv=-u-v,-m*u+(4-m)*v
                    common=gcd(uu,vv)
                    u,v=uu//common,vv//common
                    assert u%2 and v%2 and gcd(v,m)==1
                    parities+=1
                assert v%2
                states=prepare(m,Q,q0,u,v,lambda w,p=p,r=r:endpoint_selector(p,r,w))
                if p<=23:
                    for uu,vv,q in states:atoms+=literal_endpoint(p,r,uu,vv,q)
                endpoints+=1
    matrices=((F(1,3),2,0,5),(1,0,0,2),(-1,-1,-8,2),(-1,-1,-9,3))
    for A in matrices:
        for B in matrices:
            for v in ((1,2),(2,1),(3,5),(-2,7)):
                for ell in (2,3,5,7):
                    assert content(mm(A,B),v,ell)==content(A,apply(B,v),ell)+content(B,v,ell)
                    cocycles+=1
    assert content((1,0,0,2),(1,0),2)==0
    assert content((1,0,0,2),(0,1),2)==1
    for p in primes_below(45):
        for r in range(1,p+1):
            assert ((2*p+r)%r==0)==(r in (1,2,p))
            for h in sorted({r,(p+r)//2,p}):
                weighted_atoms+=literal_weighted_return(p,r,h)
    report={'status':'PASS','generic_two_CRT_cases':general,'endpoint_two_CRT_cases':endpoints,
            'odd_endpoint_parity_preparations':parities,'literal_endpoint_matrix_atoms':atoms,
            'general_weighted_return_atoms':weighted_atoms,
            'local_content_cocycle_checks':cocycles,'frozen_files':check_frozen_files(),
            'local_links':check_local_links(),'seconds':round(perf_counter()-started,3),
            'scope':'Generic arithmetic lemma and both physical endpoint matrix families. No new uniform resource-existence theorem; deep congruence and endpoint startup resources retained.'}
    (HERE/'adelic_primitive_line_two_crt_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
