"""Compile universal B17 returns through an additional solved subblock.

Enumerate multiplicity vectors, reject nontriadic coefficient means before
row-lattice tests, and reuse identical intermediate coefficient states.
All final calls have sizes 13/14/15; the middle calls use proved sizes.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, lcm
from time import perf_counter

from explore_b17_nine_thirteen_bridges import U,V,W,add,scale,primitive_matrix
from explore_b17_universal_subblocks import universal_call, generate, away_three


def selections(state, size):
    values, capacities = zip(*state)
    suffix = [0]*(len(capacities)+1)
    for i in range(len(capacities)-1,-1,-1):
        suffix[i] = suffix[i+1]+capacities[i]
    def walk(i, remaining, counts):
        if i == len(capacities):
            if not remaining:
                yield counts
            return
        for count in range(max(0,remaining-suffix[i+1]),min(capacities[i],remaining)+1):
            yield from walk(i+1,remaining-count,counts+(count,))
    yield from walk(0,size,())


def sum_coefficients(state, counts):
    return add(*(scale(x,c) for (x,_),c in zip(state,counts)))


def triadic_mean(total, size):
    modulus = away_three(size)
    if any(x.numerator % modulus for x in total):
        return None
    return scale(total,F(1,size))


def contract(state, counts, mean):
    result = Counter({x:c-k for (x,c),k in zip(state,counts) if c>k})
    result[mean] += sum(counts)
    return tuple(sorted(result.items()))


def middle_states():
    prefixes = {}
    firsts = {}
    for row in generate((3,6,9)):
        firsts.setdefault(row['first_block'],row['a'])
    # Include first blocks which had no one-call return in the old compiler.
    for size in (3,9):
        for beta in range(4):
            for gamma in range(2):
                alpha = size-beta-gamma
                if alpha < 0 or beta == gamma == 0:
                    continue
                block = tuple((x,c) for x,c in ((U,alpha),(V,beta),(W,gamma)) if c)
                mean = scale(add(*(scale(x,c) for x,c in block)),F(1,size))
                firsts[block] = mean
    for first,mean in firsts.items():
        state = Counter({U:13,V:3,W:1})
        for x,c in first:
            state[x] -= c
        state[mean] += sum(c for _,c in first)
        state = tuple(sorted((x,c) for x,c in state.items() if c))
        for size in (3,7,8,9,10,11,12,13,14,15,16):
            complement = size > 8
            for chosen in selections(state,17-size if complement else size):
                counts = tuple(c-k for (_,c),k in zip(state,chosen)) if complement else chosen
                block = tuple((x,c) for (x,_),c in zip(state,counts) if c)
                if len(block) == 1:
                    continue
                total = sum_coefficients(state,counts)
                mu = triadic_mean(total,size)
                if mu is None or not universal_call(block,mu):
                    continue
                target = contract(state,counts,mu)
                prefixes.setdefault(target,(first,block))
    return prefixes


def final_returns(state):
    result = {}
    for size in (13,14,15):
        for counts in selections(state,17-size):
            leftover = tuple((x,c) for (x,_),c in zip(state,counts) if c)
            total = sum_coefficients(state,counts)
            mu = triadic_mean(scale(total,-1),size)
            if mu is None:
                continue
            block = tuple((x,c-k) for (x,c),k in zip(state,counts) if c>k)
            if not universal_call(block,mu):
                continue
            for singleton,_ in leftover:
                repair = Counter(dict(leftover))
                repair[singleton] -= 1
                repair[mu] += size-13
                repair = tuple(sorted((x,c) for x,c in repair.items() if c))
                second = scale(add(*(scale(x,c) for x,c in repair)),F(1,3))
                assert add(scale(mu,13),scale(second,3),singleton) == (0,0)
                matrix = mu+second
                if matrix[0]*matrix[3] == matrix[1]*matrix[2]:
                    continue
                integer = primitive_matrix(matrix)
                if (integer[0]*integer[3]-integer[1]*integer[2]) % 17 == 0:
                    continue
                result.setdefault(integer,dict(matrix=matrix,final=block,repair=repair))
    return result


@lru_cache(maxsize=1)
def compile_returns():
    prefixes = middle_states()
    result = {}
    for state,(first,middle) in prefixes.items():
        for integer,row in final_returns(state).items():
            result.setdefault(integer,dict(row,first=first,middle=middle,integer=integer))
    return result,len(prefixes)


def run():
    start = perf_counter()
    rows,prefix_count = compile_returns()
    old = {row['integer'] for row in generate()}
    novel = {m:r for m,r in rows.items() if m not in old}
    crossing = {}
    prime_seven = {}
    for m,row in novel.items():
        if any(all(value % 3 == 0 for value in column) for column in ((m[0],m[2]),(m[1],m[3]))):
            crossing[m] = row
        if (m[0]*m[3]-m[1]*m[2]) % 7 == 0:
            prime_seven[m] = row
    print('intermediate coefficient states',prefix_count,'returns',len(rows),'new',len(novel))
    print('new returns annihilating a 3-adic axis',len(crossing),'determinant divisible by7',len(prime_seven))
    for m,row in sorted(crossing.items(),key=lambda item:max(map(abs,item[0])))[:12]:
        print('axis candidate',m,'det',m[0]*m[3]-m[1]*m[2],row)
    for m,row in sorted(prime_seven.items(),key=lambda item:max(map(abs,item[0])))[:8]:
        print('prime-7 candidate',m,'det',m[0]*m[3]-m[1]*m[2],row)
    print('seconds',round(perf_counter()-start,3),flush=True)


if __name__ == '__main__':
    run()
