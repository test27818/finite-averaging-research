"""Two-step initialization with minimal protected witnesses at 3p+d-2."""

from collections import Counter
from random import Random

import verify_prime_arity_large_dimension as base


def pool_move(counts,p,factors,avoid=None):
    n=sum(counts.values())
    values=[x for x,f in sorted(counts.items()) if x!=avoid for _ in range(f)]
    supports=[]
    for q in factors:
        classes=Counter()
        for x,f in counts.items():
            classes[x%q]+=f
        majority=next((r for r,f in classes.items() if f>=n-p),None)
        if majority is None or (avoid is not None and avoid%q!=majority):
            continue
        support={i for i,x in enumerate(values) if x%q!=majority}
        assert 2<=len(support)<=p
        supports.append((q,support))
    protected=set()
    for q,support in supports:
        if not support&protected:
            protected.add(min(support))
    for i in sorted(protected):
        if all(support&(protected-{i}) for q,support in supports):
            protected.remove(i)
    available=[x for i,x in enumerate(values) if i not in protected]
    assert len(available)>=p and len({x%p for x in available})==1
    move=available[:p]
    if avoid is not None and sum(move)==p*avoid:
        assert len(available)>=p+1, 'Private-witness mass obstruction excludes this boundary.'
        extra=available[p]
        i=next(i for i,x in enumerate(move) if x!=extra)
        move[i]=extra
    assert len(set(move))>1
    return tuple(move)


def initialize(counts,p):
    n=sum(counts.values())
    factors=base.protected_primes(n,p)
    assert n>2*p and n>=3*p+len(factors)-2
    assert all(x%p==0 for x in counts) and base.legal(counts,factors)
    operations=[]
    for _ in range(2):
        heavy=base.heavy(counts,p)
        if len(heavy)>=2:
            return operations
        if heavy:
            a=heavy[0]
            if counts[a]>=2*p-1:
                x=next(x for x in counts if x!=a)
                assert a%p==x%p==0
                move=(a,)*(p-1)+(x,)
            else:
                move=pool_move(counts,p,factors,avoid=a)
        else:
            move=pool_move(counts,p,factors)
        operations.append(move)
        counts=base.change(counts,move,p)
        assert base.legal(counts,factors)
    assert len(base.heavy(counts,p))>=2
    return operations


def main():
    random,checked=Random(2026091218),0
    for p in (3,5,7,11,17,31):
        for n in range(3*p-2,3*p+9):
            factors=base.protected_primes(n,p)
            if n<3*p+len(factors)-2:
                continue
            for _ in range(70):
                while True:
                    values=[random.randrange(-15,16) for _ in range(n-1)]
                    values.append(-sum(values))
                    if base.legal(Counter(values),factors):
                        break
                counts=Counter(p*x for x in values)
                word=initialize(counts,p)
                assert len(word)<=2
                for move in word:
                    counts=base.change(counts,move,p)
                    assert base.legal(counts,factors)
                assert len(base.heavy(counts,p))>=2
                checked+=1
    print('minimal-protection initialization at three-p-plus-d-minus-two: PASS',checked)


if __name__=='__main__':
    main()
