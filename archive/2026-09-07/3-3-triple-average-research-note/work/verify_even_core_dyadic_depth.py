"""A uniform state-dependent descent through all even lower-band cores.

No word search, arithmetic-group theorem, or formal inverse is used. Each
stage is one explicit return, preceded at most by an existing involution.
Primitive normalization is used only to select subsequent original indices.
"""

from fractions import Fraction as F
from math import gcd, lcm
from random import Random
from pathlib import Path
import json

from verify_four_prime_entry_and_band import Ledger, factors, triple_return

if not __debug__:
    raise RuntimeError('Assertions are required.')


def primitive_pair(a,z):
    denominator=lcm(F(a).denominator,F(z).denominator)
    a,z=int(a*denominator),int(z*denominator)
    common=gcd(a,z)
    assert common
    return a//common,z//common


def twos(x):
    assert x
    x=abs(x)
    return (x & -x).bit_length()-1


def return_counts(p,r):
    if r % 4 == 2:
        return p,0
    n=2*p+r
    odd=n//(n & -n)
    q=n//3
    if n % 3 == 0:
        q-=1 if (q-1) % 3 else 2
    assert r-1 <= q <= p-1 and gcd(q,odd)==1
    return q-1,2


def apply_return(ledger,groups,j,s):
    p,r=ledger.p,len(groups[2])
    aa,bb,cc=[list(g) for g in groups]
    kept,aa=aa[-r:],aa[:-r]
    i=p-j-s
    assert 0<=i<=p-r and 0<=j<=p and 0<=s<=r
    first=aa[:i]+bb[:j]+cc[:s]
    second=aa[i:]+bb[j:]+cc[s:]
    ledger.average(first)
    ledger.average(second)
    return [first,second,kept]


def canonical_legal(state,p):
    denominator=lcm(*(x.denominator for x in state))
    values=[int(x*denominator) for x in state]
    common=gcd(*values)
    if not common:
        return True
    values=[x//common for x in values]
    difference=gcd(*(x-values[0] for x in values))
    return all(q==p for q in factors(difference))


def descend(p,r,a,z):
    assert a*z and gcd(a,z)==gcd(a+p*z,2*p+r)==1
    initial_pair=[a,z]
    actual_a,actual_z=F(a),F(z)
    raw=[F(a)]*p+[F(r*z-a)]*p+[F(-p*z)]*r
    ledger=Ledger(raw,p)
    groups=[list(range(p)),list(range(p,2*p)),list(range(2*p,2*p+r))]
    initial=twos(a*z)
    history=[initial]
    swaps=0
    j,s=return_counts(p,r)
    delta=r*j-p*s
    assert twos(delta)==1 and gcd(delta,(2*p+r)//((2*p+r)&-(2*p+r)))==1
    while twos(a*z)>1:
        before=twos(a*z)
        if a % 2:
            groups=triple_return(ledger,groups,p,r,r-1)
            swaps+=1
            a,z=primitive_pair(ledger.state[groups[0][0]],-ledger.state[groups[2][0]]/p)
            assert a % 2 == 0 and z % 2 and twos(a*z)==before
        assert a % 4 == 0 and z % 2
        old_a,old_z=ledger.state[groups[0][0]],-ledger.state[groups[2][0]]/p
        groups=apply_return(ledger,groups,j,s)
        actual_a,actual_z=ledger.state[groups[0][0]],-ledger.state[groups[2][0]]/p
        assert actual_a == F(p-2*j-s,p)*old_a+F(delta,p)*old_z
        assert actual_z == -old_a/p
        a,z=primitive_pair(actual_a,actual_z)
        assert gcd(a,z)==gcd(a+p*z,2*p+r)==1
        assert twos(a*z)==before-1
        history.append(before-1)
    assert history==list(range(initial,0,-1))
    assert len(ledger.word)<=4*(initial-1)
    state=list(raw)
    for group in ledger.word:
        assert len(group)==len(set(group))==p
        assert all(0<=index<len(raw) for index in group)
        mean=sum(state[index] for index in group)/p
        for index in group:
            state[index]=mean
        assert sum(state)==0 and canonical_legal(state,p)
    assert state==ledger.state and twos(a*z)==1
    assert all(state[index]==value for group,value in zip(groups,(actual_a,r*actual_z-actual_a,-p*actual_z))
               for index in group)
    return {'p':p,'r':r,'input_parameters':initial_pair,'initial_depth':initial,'depths':history,
            'involution_count':swaps,'operations':ledger.word,'final_parameters':[a,z]}


def main():
    rng=Random(2026091461)
    records=[]
    systems=0
    for p in (5,7,11,13,17,19,23,31):
        for r in range(2,p,2):
            j,s=return_counts(p,r)
            delta=r*j-p*s
            n=2*p+r
            assert twos(delta)==1 and gcd(delta,n//(n & -n))==1
            systems+=1
            for depth in (1,2,4,7):
                for orientation in (0,1):
                    while True:
                        a=(2**depth)*rng.randrange(1,50,2)
                        z=rng.randrange(1,100,2)
                        if orientation:
                            a,z=z,a
                        if gcd(a,z)==gcd(a+p*z,n)==1:
                            break
                    records.append(descend(p,r,a,z))
    print('all-even-core valuation-one return counts: PASS',systems)
    print('all-even-core literal depth descents: PASS',len(records))
    print('all-even-core total strictly descending stages: PASS',sum(x['initial_depth']-1 for x in records))
    record={'scope':'Universal descent to v2(a*z)=1 for every legal even lower core; '
                    'does not assert final terminal reachability or a general threshold.',
            'parameter_systems':systems,'records':records}
    (Path(__file__).parent/'even_core_dyadic_depth_records.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('uniform even-core dyadic-depth descent: PASS')


if __name__=='__main__':
    main()
