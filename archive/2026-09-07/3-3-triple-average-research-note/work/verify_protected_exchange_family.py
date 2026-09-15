"""A general protected-position exchange and a uniform collision family.

All candidates in the stated two-anchor family are classified by type counts,
not by subsets or averaging words. Literal paths for the p=23 example validate
the feasible exchanges and finite zero terminal.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd

import verify_prime_arity_large_dimension as base


def family(p,k):
    assert base.is_prime(p) and p >= 5 and 2 <= k <= p-2
    assert (2*p-1) % k != 0
    b=p
    a,c,d = p+k,p*(k+1),k-p+1
    z = (p-1)*(2*p-1)-(3*p-1)*k-3*p*p
    counts = Counter({a:p,b:p,c:1,d:p-1,z:1})
    assert len(counts) == 5 and sum(counts.values()) == 3*p+1
    assert sum(x*f for x,f in counts.items()) == 0
    return a,b,c,d,z,counts


def candidate_types(p,a,b,c,d):
    # alpha=beta=0, so candidates use one anchor and a subset of c,d^(p-1).
    for padding in (a,b):
        for e in (0,1):
            for t in range(p):
                size=e+t
                if not 1 <= size <= p:
                    continue
                move=(c,)*e+(d,)*t+(padding,)*(p-size)
                if sum(move) % p == 0:
                    yield padding,e,t,move


def main():
    instances,collisions,exchanges=0,0,0
    for p in (5,7,11,13,17,19,23,31,43,61):
        for k in range(2,p-1):
            if (2*p-1)%k==0:
                continue
            a,b,c,d,z,counts=family(p,k)
            types=list(candidate_types(p,a,b,c,d))
            # Two basic zero-residue choices remain, unless extra coincidences
            # of residues create another candidate.
            assert c%p == b%p and d%p not in (a%p,b%p)
            for padding,e,t,move in types:
                expected=a if padding==b else b
                assert sum(move)==p*expected
                after=base.change(counts,move,p)
                assert len(base.heavy(after,p))==1
                collisions+=1
            assert len(types)==2
            instances+=1
            n=3*p+1
            factors=base.protected_primes(n,p)
            if not base.legal(counts,factors):
                continue
            bad={q for q in factors if (a-b)%q==0}
            # For the clean obstructed cases, the only exceptional support is
            # d^(p-1),z and the protected point may be moved from z to d.
            if not bad or any(d%q==b%q or z%q==b%q for q in bad):
                continue
            if (z-d)%p:
                continue
            move=(c,)+(d,)*(k-1)+(z,)+(a,)*(p-k-1)
            assert len(move)==p and sum(move)%p==0
            after=base.change(counts,move,p)
            assert base.legal(after,factors) and len(base.heavy(after,p))>=2
            exchanges+=1
    print('uniform all-collision two-anchor families: PASS',instances,collisions)
    print('protected same-residue exchanges: PASS',exchanges)

    a,b,c,d,z,counts=family(23,7)
    assert (a,b,c,d,z)==(30,23,184,-15,-1073)
    assert base.legal(counts,(2,5,7))
    protected=-1073
    assert {(x%7) for x in counts if x not in (d,z)}=={b%7}
    assert counts[d]+counts[z]==23 and (protected-b)%7
    move=(184,)+(-15,)*6+(-1073,)+(30,)*15
    assert sum(move)==-529 and sum(move)//23==-23
    after=base.change(counts,move,23)
    assert after[-23]==after[23]==23 and after[30]==8 and after[-15]==16
    assert base.legal(after,(2,5,7))
    print('p23 n70 protected-exchange example: PASS')

    paths=0
    for p in (5,11,17,23,29,41,47,59,71,83):
        assert p%3==2
        k=(p-2)//3
        t=(2*p-1)//3
        a,b,c,d=2*t,p,p*(p+1)//3,-t
        z=-(6*p*p+2*p-1)//3
        values=[a]*p+[b]*p+[c]+[d]*(p-1)+[z]
        replay=base.LabelledReplay(values,p)
        # This helper tracks p times the actual values; replay the generated
        # original-label operations independently below with exact fractions.
        moves=[(c,)+(d,)*(k-1)+(z,)+(a,)*(p-k-1),
               (a,d,d)+(b,)*((p-3)//2)+(-b,)*((p-3)//2),
               (a,)*k+(d,)*(2*k)+(0,)*2,
               (b,)*((p-1)//2)+(-b,)*((p-1)//2)+(0,),
               (b,b,-b,-b)+(0,)*(p-4)]
        for move in moves:
            replay.step(tuple(p*x for x in move))
        assert not any(replay.state)
        state=list(map(F,values))
        for positions in replay.word:
            average=sum(state[i] for i in positions)/p
            assert average.denominator==1
            for i in positions:
                state[i]=average
        assert not any(state) and len(replay.word)==5
        assert base.legal(Counter(values),base.protected_primes(len(values),p))
        paths+=1
    print('uniform three-p-plus-one five-step literal paths: PASS',paths)


if __name__=='__main__':
    main()
