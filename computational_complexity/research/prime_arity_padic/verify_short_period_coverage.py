"""Finite counterexample and ingredients of the period-length lower bound.

The all-length existence theorem is the counting argument in the paper.
This verifier does not claim to enumerate every large family in that proof.
"""
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json
from p_plus_three_periodic_policy import decide_periodic_core
from verify_p_plus_three_periodic_policy import literal_step,policy_oracle


def egcd(a,b):
    old_r,r=a,b;old_s,s=1,0;old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r;old_s,s=s,old_s-q*s;old_t,t=t,old_t-q*t
    return (old_r,old_s,old_t) if old_r>0 else (-old_r,-old_s,-old_t)


def normal(word,p=5):
    h=(1,1,1)
    for mask in reversed(word):
        i=mask.bit_length()-1;total=sum(h)
        h=tuple(-total if j==i else p*x for j,x in enumerate(h))
    return h


def basis(h):
    a,b,c=h;g,s,t=egcd(a,b)
    return (b//g,-a//g,0),(-s*c,-t*c,g)


def main():
    counts=[]
    for L in range(1,9):
        directions=set()
        for word in product((1,2,4),repeat=L):
            h=normal(word)
            assert gcd(*h)==1
            assert len({x%8 for x in h})==1 and h[0]%2
            opposite=tuple(-x for x in h)
            directions.add(min(h,opposite))
        assert len(directions)==3**L
        counts.append({'length':L,'different_success_hyperplanes':len(directions)})
    rng=Random(20261018);ingredients=0
    for p in (5,7,11):
        for _ in range(100):
            word=tuple(rng.choice((1,2,4)) for _ in range(rng.randrange(1,21)))
            h=normal(word,p);b1,b2=basis(h);T=rng.randrange(-10**6,10**6)
            u=tuple(x+T*y for x,y in zip(b1,b2))
            assert gcd(*u)==1 and sum(u)%(p+3)==0
            assert sum(x*y for x,y in zip(u,h))==0
            assert max(map(abs,u))<=2*max(map(abs,h))**2*(abs(T)+1)
            current=u
            for mask in word+(7,):
                current=literal_step(current,mask,p)
                assert current is not None
            assert not any(current)
            ingredients+=1

    u=(-14499189653022,25049625636965,97)
    witness=(2,1,2,1,4,1,2,4,4,4,7)
    current=u
    for mask in witness:
        current=literal_step(current,mask,5)
        assert current is not None
    assert not any(current)
    rejected=0
    for L in range(1,4):
        for word in product(range(1,7),repeat=L):
            answer=decide_periodic_core(u,word)
            assert not answer['possible']
            assert not policy_oracle(u,word,5)
            rejected+=1
    assert rejected==258
    a=-sum(u)//8
    record={'scope':'A finite all-short-period counterexample and exact ingredients; the linear-period lower bound is proved in the paper.',
            'hyperplane_counts':counts,'primitive_lattice_and_witness_checks':ingredients,
            'short_period_counterexample':{'core':u,'source':(a,)*5+tuple(a+x for x in u),
                'successful_word':witness,'periods_rejected_for_all_repetitions':rejected,
                'maximum_period_length':3}}
    Path(__file__).with_name('short_period_coverage_verification.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,indent=2))


if __name__=='__main__':main()
