"""Guarded B17 returns using solved 13/14/15-point subproblems.

This is a bounded controller experiment, not a proof of B17 reachability.
Every retained schema has an exact local divisibility guard, plus an
explicit output-legality check at each numerical application.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd, lcm
from time import perf_counter
import argparse

from verify_fifteen_via_subblocks import centered_g, actual_average, is_three_power


def primitive(x, y):
    content = gcd(x, y)
    if not content:
        return 0, 0
    x, y = x//content, y//content
    return min((x,y),(-x,-y))


def height(pair):
    u,v = pair
    return 91*u*u+39*u*v+6*v*v


def generate():
    u,v = (F(1),F(0)), (F(0),F(1))
    w = (F(-13),F(-3))
    rows = []
    for size in (13,14,15):
        for beta in (1,2,3):
            alpha = size-beta-1
            mu = tuple((alpha*u[i]+beta*v[i]+w[i])/size for i in (0,1))
            state = Counter()
            for value,count in ((u,13-alpha),(v,3-beta),(mu,size)):
                if count:
                    state[value] += count
            for triple in combinations_with_replacement(tuple(sorted(state)),3):
                need = Counter(triple)
                # A constant triple is allowed: it records a block
                # contraction that already returns to B17 without repair.
                if any(state[x] < c for x,c in need.items()):
                    continue
                after = state.copy()
                for x in triple:
                    after[x] -= 1
                    if not after[x]:
                        del after[x]
                average = tuple(sum(x[i] for x in triple)/3 for i in (0,1))
                after[average] += 3
                if sorted(after.values()) != [1,3,13]:
                    continue
                first = next(x for x,c in after.items() if c == 13)
                second = next(x for x,c in after.items() if c == 3)
                singleton = next(x for x,c in after.items() if c == 1)
                assert singleton == tuple(-13*first[i]-3*second[i] for i in (0,1))
                matrix = first+second
                if matrix[0]*matrix[3]-matrix[1]*matrix[2] == 0:
                    continue
                denominator = lcm(*(x.denominator for x in matrix))
                integer = tuple(int(x*denominator) for x in matrix)
                divisor = gcd(*integer)
                integer = tuple(x//divisor for x in integer)
                modulus = size
                while modulus % 3 == 0:
                    modulus //= 3
                guard = (alpha-13,beta-3,modulus)
                rows.append({"size":size,"alpha":alpha,"beta":beta,"guard":guard,
                             "triple":triple,"actual":matrix,"matrix":integer})
    unique = {}
    for row in rows:
        key = row["matrix"],row["guard"]
        unique.setdefault(key,row)
    return list(unique.values())


def edges(pair, rows):
    u,v = pair
    # The ordinary one-step return is always allowed, preserves G=1 at 17.
    yield primitive(3*u,-13*u-v), "A"
    for i,row in enumerate(rows):
        a,b,modulus = row["guard"]
        if (a*u+b*v) % modulus:
            continue
        a,b,c,d = row["matrix"]
        output = primitive(a*u+b*v,c*u+d*v)
        if output != (0,0) and (output[0]-output[1]) % 17 == 0:
            continue
        yield output, i


def check_schemas(rows, bound=8):
    checked = 0
    for u in range(-bound,bound+1):
        for v in range(-bound,bound+1):
            if gcd(u,v) != 1 or (u-v) % 17 == 0:
                continue
            for row in rows:
                a,b,modulus = row["guard"]
                if (a*u+b*v) % modulus:
                    continue
                source = Counter([F(u)]*13+[F(v)]*3+[F(-13*u-3*v)])
                block = [F(u)]*row["alpha"]+[F(v)]*row["beta"]+[F(-13*u-3*v)]
                assert is_three_power(centered_g(block))
                mu = sum(block)/row["size"]
                assert is_three_power(mu.denominator)
                for x,c in Counter(block).items():
                    assert source[x] >= c
                    source[x] -= c
                    if not source[x]:
                        del source[x]
                source[mu] += row["size"]
                triple = tuple(a*u+b*v for a,b in row["triple"])
                source = actual_average(source,triple)
                a,b,c,d = row["actual"]
                x,y = a*u+b*v,c*u+d*v
                expected = Counter([x]*13+[y]*3+[-13*x-3*y])
                assert source == expected
                checked += 1
    print("B17 guarded schema interface replay: PASS",checked,flush=True)


def search_descending(pair, rows, depth):
    """Find lower height or a coordinate-zero known terminal in a short walk."""
    initial = height(pair)
    frontier = [(pair,())]
    seen = {pair}
    for _ in range(depth):
        following = []
        for current,path in frontier:
            for target,label in edges(current,rows):
                word = path+(label,)
                if target[0]*target[1] == 0 or height(target) < initial:
                    return word
                if target not in seen:
                    seen.add(target)
                    following.append((target,word))
        frontier = following
    return None


def run(bound,depth):
    started = perf_counter()
    rows = generate()
    check_schemas(rows)
    print("B17 guarded non-atomic schemas",len(rows),flush=True)
    counts = Counter()
    missing = []
    for u in range(bound+1):
        for v in range(-bound,bound+1):
            if gcd(u,v) != 1 or (u-v) % 17 == 0 or (u==0 and v<0):
                continue
            pair = primitive(u,v)
            if u*v == 0:
                counts[0] += 1
                continue
            word = search_descending(pair,rows,depth)
            if word is not None:
                counts[len(word)] += 1
            else:
                missing.append(pair)
    missing.sort(key=lambda p:(height(p),p))
    print("B17 bounded descent counts",dict(sorted(counts.items())),
          "uncovered",len(missing),"first",missing[:12],flush=True)
    print("seconds",round(perf_counter()-started,3))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound",type=int,default=24)
    parser.add_argument("--depth",type=int,default=4)
    args = parser.parse_args()
    if args.bound < 1 or args.depth < 1:
        parser.error("bound and depth must be positive")
    run(args.bound,args.depth)
