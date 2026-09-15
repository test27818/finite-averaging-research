"""Uniform candidate bridges for (u^(n-4),b,b',c,c'), n=2p.

The p-signatures are symbolic 0,0,0,1,-1; no finite prime sampling is
used. Only mod8 input patterns are enumerated. One solved 8/12 subproblem
is allowed after at most two atomic preparatory steps.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement,product
from math import gcd,lcm
from time import perf_counter


U = (F(1),F(0),F(0),F(0),F(0))
B = (F(0),F(1),F(0),F(0),F(0))
BP = (F(0),F(0),F(1),F(0),F(0))
C = (F(0),F(0),F(0),F(1),F(0))
CP = (F(0),F(0),F(0),F(0),F(1))


def average_coefficients(values):
    return tuple(sum(v[j] for v in values)/len(values) for j in range(5))


def coeff_mod8(value):
    return tuple(x.numerator*pow(x.denominator,-1,8) % 8 for x in value)


def evaluate(coefficients,point,modulus=8):
    return sum(a*b for a,b in zip(coefficients,point)) % modulus


def first_states(depth):
    # n>=22 leaves at least two u positions after two nonconstant
    # preparatory triples and a 12-position call. Use n=26 for discovery.
    start = tuple(sorted(((U,22),(B,1),(BP,1),(C,1),(CP,1))))
    frontier = [(start,())]
    seen = {start}
    yield start,()
    for _ in range(depth):
        following = []
        for items,word in frontier:
            state = Counter(dict(items))
            for triple in combinations_with_replacement(sorted(state),3):
                if len(set(triple)) == 1:
                    continue
                need = Counter(triple)
                if any(state[x] < count for x,count in need.items()):
                    continue
                target = state.copy()
                target.subtract(need)
                target[average_coefficients(triple)] += 3
                key = tuple(sorted((x,c) for x,c in target.items() if c))
                if key in seen:
                    continue
                seen.add(key)
                following.append((key,word+(triple,)))
        for row in following:
            yield row
        frontier = following


def choices(capacities,size):
    suffix = [0]*(len(capacities)+1)
    for i in range(len(capacities)-1,-1,-1):
        suffix[i] = suffix[i+1]+capacities[i]
    def recurse(index,remaining,counts):
        if index == len(capacities):
            if not remaining:
                yield counts
            return
        parity = capacities[index] % 2
        for count in range(parity,min(remaining,capacities[index])+1,2):
            if remaining-count > suffix[index+1]:
                continue
            yield from recurse(index+1,remaining-count,counts+(count,))
    yield from recurse(0,size,())


def away_six(value):
    value = abs(value)
    if not value:
        return 0
    for p in (2,3):
        while value % p == 0:
            value //= p
    return value


def candidates(depth):
    for items,word in first_states(depth):
        capacities = tuple(c for _,c in items)
        for size in (8,12):
            for counts in choices(capacities,size):
                block = tuple((value,count) for (value,_),count in zip(items,counts) if count)
                mean = tuple(sum(value[j]*count for value,count in block)/size for j in range(5))
                remaining = [(value,c-count) for (value,c),count in zip(items,counts) if c>count]
                assert all(c % 2 == 0 for _,c in remaining)
                # Each output has the same coefficient of the common
                # p-residue; differences are rational multiples of delta.
                slopes = [value[3]-value[4] for value,_ in remaining]+[mean[3]-mean[4]]
                denominator = lcm(*(value.denominator for value in slopes))
                content = gcd(*(int(value*denominator) for value in slopes))
                if away_six(content) != 1:
                    continue
                total = tuple(sum(value[j]*count for value,count in block) for j in range(5))
                yield dict(word=word,items=items,counts=counts,size=size,
                           total8=coeff_mod8(total),support8=tuple(coeff_mod8(value) for value,_ in block),
                           mean=mean,slope_content=content,slope_denominator=denominator)


def patterns(n8):
    for u,b,bp,c in product(range(8),repeat=4):
        if (b-u) % 2 == 0 or (bp-u) % 2 == 0 or (c-u) % 2:
            continue
        cp = (-(n8-4)*u-b-bp-c) % 8
        if (cp-u) % 2:
            continue
        yield u,b,bp,c,cp


def cover(depth):
    points = [(n8,p) for n8 in (2,6) for p in patterns(n8)]
    assert len(points) == 1024
    missing = set(range(len(points)))
    proof = {}
    rows = []
    checked = 0
    for candidate in candidates(depth):
        checked += 1
        hits = []
        divisor = 8 if candidate['size'] == 8 else 4
        for index in missing:
            _,point = points[index]
            if evaluate(candidate['total8'],point) % divisor:
                continue
            if len({evaluate(row,point,2) for row in candidate['support8']}) != 2:
                continue
            hits.append(index)
        if hits:
            certificate_index = len(rows)
            rows.append(candidate)
            for index in hits:
                proof[points[index]] = certificate_index
            missing.difference_update(hits)
        if not missing:
            break
    return points,proof,rows,[points[i] for i in sorted(missing)],checked


def run(depth):
    start = perf_counter()
    points,proof,rows,missing,checked = cover(depth)
    print('uniform n=2p symbolic pairing candidates',checked,'retained',len(rows),
          'covered',len(proof),'/',len(points),'depth',depth)
    print('missing by nmod8 and u parity',dict(Counter((n8,p[0]%2) for n8,p in missing)))
    print('first missing',missing[:8])
    print('selected word/call counts',dict(Counter((len(row['word']),row['size']) for row in rows)))
    print('seconds',round(perf_counter()-start,3))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--depth',type=int,choices=(0,1,2),default=2)
    run(parser.parse_args().depth)
