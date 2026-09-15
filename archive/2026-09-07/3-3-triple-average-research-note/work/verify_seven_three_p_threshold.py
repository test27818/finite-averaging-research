"""Seven averaging: n=23..26 via symmetrized collision-mass certificate.

Compressed rows follow from within-residue permutation averaging. A partial
row also forces each repeated residue class to have a single actual value.
No exploration module is imported and no averaging-word search is performed.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import gcd
from random import Random

import verify_five_three_p_threshold as five

previous = five.previous
base,linear,middle,old = five.base,five.linear,five.middle,five.old
P=7

CERTIFICATE=(
    (1,2,0,(2,),(6,),(2,)),
    (1,3,0,(2,),(5,),(2,)),
    (1,3,0,(2,3),(4,1),(2,3)),
    (1,4,0,(2,),(4,),(2,)),
    (1,4,0,(2,3),(3,1),(2,3)),
    (1,4,0,(2,4),(3,1),(2,4)),
    (1,4,0,(2,3),(2,2),(2,3)),
    (2,3,0,(2,),(6,),(2,)),
    (2,4,0,(2,),(5,),(2,)),
    (2,4,0,(2,3),(4,1),(2,3)),
    (3,4,0,(2,),(6,),(2,)),
)


def equations(alpha,beta,residues,frequencies):
    for j,r in enumerate(residues):
        if r in (0,1):
            yield tuple(int(i==j) for i in range(len(residues))), 7 if r==0 else -6
    for counts in product(*(range(f+1) for f in frequencies)):
        size=sum(counts)
        if not 1<=size<=7:
            continue
        residue=sum(r*k for r,k in zip(residues,counts))%7
        i=-residue%7
        if i<=min(alpha,7-size):
            if 7-size-i<=beta:
                yield (0,)*len(residues),1
                return
            yield counts,7-i
        j=(residue-size)%7
        if j<=min(beta,7-size):
            yield counts,size+j-7


def eliminate(rows,width):
    pivots={}
    for coefficients,rhs in rows:
        row=tuple(coefficients)+(rhs,)
        for j,pivot in sorted(pivots.items()):
            if row[j]:
                a,b=pivot[j],row[j]
                row=tuple(a*x-b*y for x,y in zip(row,pivot))
                common=gcd(*row)
                if common:
                    row=tuple(x//common for x in row)
        j=next((i for i in range(width) if row[i]),None)
        if j is None:
            if row[-1]:
                return None
        else:
            pivots[j]=row
    assert len(pivots)==width
    values=[F(0)]*width
    for j,row in sorted(pivots.items(),reverse=True):
        values[j]=(F(row[-1])-sum(row[k]*values[k] for k in range(j+1,width)))/row[j]
    return tuple(values)


def verify_certificate():
    expected={(e,a,b,r,f):tuple(map(F,v)) for e,a,b,r,f,v in CERTIFICATE}
    observed,systems={},0
    for extra in range(1,6):
        for alpha in range(5):
            for beta in range(min(alpha,4-alpha)+1):
                length=7+extra-alpha-beta
                for sequence in combinations_with_replacement(range(7),length):
                    bins=Counter(sequence)
                    if max(bins.values())>=7 or bins[0]>1 or bins[1]>1:
                        continue
                    residues,frequencies=tuple(bins),tuple(bins.values())
                    result=eliminate(equations(alpha,beta,residues,frequencies),len(bins))
                    systems+=1
                    if result is None:
                        continue
                    rows=list(equations(alpha,beta,residues,frequencies))
                    assert all(sum(x*k for x,k in zip(result,row))==rhs for row,rhs in rows)
                    for j,f in enumerate(frequencies):
                        assert f==1 or any(0<row[j]<f for row,rhs in rows)
                    assert all(x.denominator==1 and x%7==r for x,r in zip(result,residues))
                    mass=7+alpha+sum(x*f for x,f in zip(result,frequencies))
                    assert 0<mass<21+extra and mass.denominator==1
                    observed[(extra,alpha,beta,residues,frequencies)]=result
    assert observed==expected and systems==57026
    return systems,len(observed)


def choose(counts,factors):
    n=sum(counts.values())
    assert n in (23,24,25,26)
    heavy=sorted(base.heavy(counts,7))
    if len(heavy)>=3:
        a,b,c=heavy[:3]
        if len(counts)==3 and counts[a]==counts[c]==7 and len({x%7 for x in heavy})==3:
            move,branch=previous.triple.choose_three(counts,7)
            return move,'three-'+branch,c if move is None else None
        return old.choose(counts,n,7,factors)
    a,b=sorted(heavy,key=lambda x:counts[x],reverse=True)
    if max(counts[a],counts[b])>=13:
        return linear.choose(counts,n,7,factors)
    if (a-b)%7==0:
        return tuple(middle.same_residue_move(counts,7,factors)),'same-residue',None
    for anchor,other in ((a,b),(b,a)):
        for x in counts:
            if x in (a,b) or (x-anchor)%7:
                continue
            move=(anchor,)*6+(x,)
            if sum(move)!=7*other:
                return move,'anchor-residue-single',None
            if counts[x]>=2:
                return (anchor,)*5+(x,x),'anchor-residue-double',None
    if counts[a]+counts[b]>=19:
        move,branch=previous.combined_reserve(counts,a,b,7)
        return move,branch,None
    light,protected,private,_=five.protected_light(counts,a,b,factors,p=7)
    for target,padding in ((a,b),(b,a)):
        pool=[target]*(counts[target]-7)+light
        for move in five.candidates(pool,padding,p=7):
            if len(set(move))==1:
                continue
            after=base.change(counts,move,7)
            if len(base.heavy(after,7))>=2:
                assert base.legal(after,factors)
                return move,'protected-modular-fiber',None
    raise AssertionError(('The complete mass certificate excludes all-collision failure',n,counts,private))


def solve(initial):
    n,branches=len(initial),Counter()
    factors=base.protected_primes(n,7)
    replay=base.LabelledReplay(initial,7)
    for move in base.initialize(replay.counts(),n,7,factors):
        replay.step(move)
    while any(replay.state):
        move,branch,delta=choose(replay.counts(),factors)
        branches[branch]+=1
        if move is None:
            for _ in range(replay.counts()[delta]):
                replay.step((delta,-delta)+(0,)*5)
            break
        replay.step(move)
        assert base.legal(replay.counts(),factors) and len(base.heavy(replay.counts(),7))>=2
    old.previous.replay_original(initial,replay.word,7)
    return len(replay.word),branches


def main():
    print('seven-average symmetrized complete collision certificate: PASS',*verify_certificate())
    random,local,branches=Random(2026091217),0,Counter()
    for n in (23,24,25,26):
        factors=base.protected_primes(n,7)
        for _ in range(1800):
            count=random.randrange(3,9)
            weights=[7,7]+[1]*(count-2)
            for _ in range(n-sum(weights)):
                weights[random.randrange(count)]+=1
            values=[random.randrange(-10**12,10**12)*weights[-1] for _ in range(count-1)]
            values.append(-sum(x*f for x,f in zip(values,weights))//weights[-1])
            counts=Counter()
            for x,f in zip(values,weights):
                counts[x]+=f
            if not base.legal(counts,factors) or len(base.heavy(counts,7))<2:
                continue
            move,branch,delta=choose(counts,factors)
            if move is not None:
                after=base.change(counts,move,7)
                assert base.legal(after,factors) and len(base.heavy(after,7))>=2
            branches[branch]+=1
            local+=1
    print('seven-average n23-n26 exact large-integer closure: PASS',local)
    paths,longest=0,0
    for n in (23,24,25,26):
        for magnitude in (20,10000):
            for _ in range(12):
                while True:
                    values=[random.randrange(-magnitude,magnitude+1) for _ in range(n-1)]
                    values.append(-sum(values))
                    if base.legal(Counter(values),base.protected_primes(n,7)):
                        break
                length,used=solve(values)
                longest=max(longest,length)
                paths+=1
                branches.update(used)
    print('seven-average n23-n26 literal one-digit full paths: PASS',paths,longest)
    print('seven-average observed branches:',dict(sorted(branches.items())))
    print('seven-average uniform threshold at most twenty-three: PASS')


if __name__=='__main__':
    main()
