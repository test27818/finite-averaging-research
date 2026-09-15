"""Exact composite forms, exploratory real coverage for A/B then one F14.

Words are grouped by their inverse local signature before interval union.
Floating intervals are discovery diagnostics only. Integer gap witnesses
are checked against every retained exact form; this is a bounded library.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import atan, gcd, inf, isqrt, sqrt
from time import perf_counter

from explore_b17_nine_thirteen_bridges import projective, points
from explore_b17_guarded_returns import height
from verify_b17_universal_subblocks import FOURTEEN_WORDS


I = (1, 0, 0, 1)
GENERATORS = {'A': (3, 0, -13, -1), 'B': (7, 2, -33, -9)}
RETURNS = {'A': (-3, -6, 13, 12), 'B': (-6, -3, 12, 13)}


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def image(matrix, pair):
    a,b,c,d = matrix
    x,y = pair
    return a*x+b*y, c*x+d*y


def composite(word):
    matrix = I
    for letter in word:
        matrix = mul(GENERATORS[letter], matrix)
    return mul(RETURNS[word[-1]], matrix)


def difference_form(matrix, denominator=42):
    a,b,c,d = matrix
    first, last = height((a,c)), height((b,d))
    return (first-denominator**2*91,
            height((a+b,c+d))-first-last-denominator**2*39,
            last-denominator**2*6)


def value(poly, pair):
    a,b,c = poly
    x,y = pair
    return a*x*x+b*x*y+c*y*y


def source_signature(matrix, last):
    a,b,c,d = matrix
    inverse = d,-b,-c,a
    target = ((0,1),(1,3)) if last == 'A' else ((1,0),(1,5))
    return tuple(projective(image(inverse, point), prime)
                 for point, prime in zip(target, (2,7)))


def negative_intervals(poly):
    """Floating discovery intervals; never a proof of real coverage."""
    a,b,c = poly
    if c == 0:
        if b == 0:
            return [(-inf,inf)] if a < 0 else []
        root = -a/b
        return [(-inf,root)] if b > 0 else [(root,inf)]
    discriminant = b*b-4*a*c
    if discriminant < 0:
        return [(-inf,inf)] if c < 0 else []
    if discriminant == 0:
        return [(-inf,-b/(2*c)),(-b/(2*c),inf)] if c < 0 else []
    q = -0.5*(b+(sqrt(discriminant) if b >= 0 else -sqrt(discriminant)))
    left, right = sorted((q/c, a/q))
    return [(left,right)] if c > 0 else [(-inf,left),(right,inf)]


def merge(intervals):
    result = []
    for left,right in sorted(intervals):
        if result and left < result[-1][1]:
            result[-1] = result[-1][0], max(right,result[-1][1])
        else:
            result.append((left,right))
    return result


def catalogue(depth):
    groups = defaultdict(list)
    frontier = [(I,'')]
    for length in range(1,depth+1):
        following = []
        for matrix,word in frontier:
            for letter,generator in GENERATORS.items():
                target = mul(generator,matrix)
                text = word+letter
                signature = source_signature(target,letter)
                final = mul(RETURNS[letter],target)
                poly = difference_form(final)
                groups[signature].append((poly,text,final))
                following.append((target,text))
        frontier = following
    return groups


def audit_table():
    histogram = Counter()
    for row in FOURTEEN_WORDS:
        for word in row:
            poly = difference_form(composite(word))
            a,b,c = poly
            discriminant = b*b-4*a*c
            kind = 'positive-definite' if a > 0 and discriminant < 0 else 'indefinite'
            histogram[kind] += 1
    assert histogram == {'indefinite': 23, 'positive-definite': 1}
    matrix = composite('BBBBBB')
    poly = difference_form(matrix)
    assert poly == (24086484,8401842,735624)
    assert 4*poly[0]*poly[2]-poly[1]**2 > 0
    print('original 24-word composite audit:', dict(histogram))
    print('B^6 then F2 strictly increases H throughout its domain:', matrix, poly)


def run(depth):
    start = perf_counter()
    audit_table()
    groups = catalogue(depth)
    all_witnesses = []
    for signature in ((p2,p7) for p2 in points(2) for p7 in points(7)):
        rows = groups[signature]
        intervals = merge([interval for poly,_,_ in rows for interval in negative_intervals(poly)])
        fraction = sum(atan(right)-atan(left) for left,right in intervals)/(2*atan(inf))
        witness = None
        for denominator in range(1,81):
            for numerator in range(-12*denominator, 5*denominator+1):
                if gcd(denominator,numerator) != 1:
                    continue
                pair = denominator,numerator
                if all(value(poly,pair) >= 0 for poly,_,_ in rows):
                    witness = pair
                    break
            if witness:
                break
        all_witnesses.append(witness)
        print('signature',signature,'words',len(rows),'angular-cover',round(fraction,6),
              'exact-real-gap-witness',witness,flush=True)
    print('bounded signatures without the tested rational gap witnesses',all_witnesses.count(None),'/24')
    print('depth',depth,'words',sum(map(len,groups.values())),'seconds',round(perf_counter()-start,3))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--depth',type=int,default=10)
    args = parser.parse_args()
    if not 1 <= args.depth <= 14:
        parser.error('depth must be between 1 and 14')
    run(args.depth)
