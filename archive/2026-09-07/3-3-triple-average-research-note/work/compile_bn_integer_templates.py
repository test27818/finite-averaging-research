"""Integer coefficient compiler for two-stage universal B_n returns.

Each state is a primitive integer coefficient multiset, with its physical
scalar recorded on the certificate path. Supports and multiplicity choices
are cached independently. Fractions are unnecessary in the search loop.
"""

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import gcd
from time import perf_counter


def away_three(value):
    value = abs(value)
    while value and value % 3 == 0:
        value //= 3
    return value


def certificate_size(size):
    """Frozen child library used by the n17/n19/n23/n25/n29 certificates."""
    if size < 3:
        return False
    reduced = away_three(size)
    if reduced == 1:
        return True
    if size < 7:
        return False
    if reduced & (reduced-1) == 0:
        return True
    if reduced in (10,14):
        return True
    dyadic = 0
    while reduced % 2 == 0:
        reduced //= 2
        dyadic += 1
    if dyadic in (1,2):
        return False
    for prime in (5,7,11,13,17,19,23):
        while reduced % prime == 0:
            reduced //= prime
    return reduced == 1


@lru_cache(maxsize=None)
def solved_size(size):
    """Current family: all three-divisible sizes and all split prime factors."""
    if size < 3:
        return False
    if away_three(size) == 1:
        return True
    if size < 7:
        return False
    if size % 3 == 0:
        return True
    for prime in (2,5,11,17,23,29,41,47,53,59):
        while size % prime == 0:
            size //= prime
    divisor = 2
    while divisor*divisor <= size:
        if size % divisor == 0:
            if divisor % 3 != 1:
                return False
            while size % divisor == 0:
                size //= divisor
        divisor += 1
    return size == 1 or size % 3 == 1


@lru_cache(maxsize=None)
def selections(capacities, size):
    suffix = [0]*(len(capacities)+1)
    for i in range(len(capacities)-1,-1,-1):
        suffix[i] = suffix[i+1]+capacities[i]
    result = []
    def walk(index, remaining, counts):
        if index == len(capacities):
            if not remaining:
                result.append(counts)
            return
        low = max(0,remaining-suffix[index+1])
        high = min(capacities[index],remaining)
        for count in range(low,high+1):
            walk(index+1,remaining-count,counts+(count,))
    walk(0,size,())
    return tuple(result)


@lru_cache(maxsize=None)
def lattice_signature(values):
    anchor = values[0]
    rows = tuple((x-anchor[0],y-anchor[1]) for x,y in values[1:])
    determinant_gcd = gcd(*(a*d-b*c for (a,b),(c,d) in combinations(rows,2))) if len(rows)>1 else 0
    if determinant_gcd:
        return 2,away_three(determinant_gcd),rows
    content = gcd(*(x for row in rows for x in row)) if rows else 0
    return (1,away_three(content),rows) if content else (0,0,rows)


def in_lattice(signature, target):
    rank,divisor,rows = signature
    x,y = target
    if rank == 0:
        return x == y == 0
    if rank == 2:
        return divisor == 1 or all((a*y-b*x) % divisor == 0 for a,b in rows)
    return all(a*y == b*x for a,b in rows) and gcd(x,y) % divisor == 0


def total(state, counts):
    return (sum(x*k for (x,y,c),k in zip(state,counts)),
            sum(y*k for (x,y,c),k in zip(state,counts)))


def admissible_mean(state, counts, size):
    x,y = total(state,counts)
    prime_part = away_three(size)
    if x % prime_part or y % prime_part:
        return None
    numerator = x//prime_part,y//prime_part
    denominator = size//prime_part
    values = tuple((a,b) for (a,b,c),k in zip(state,counts) if k)
    anchor = values[0]
    delta = numerator[0]-denominator*anchor[0],numerator[1]-denominator*anchor[1]
    if not in_lattice(lattice_signature(values),delta):
        return None
    return numerator,denominator


def contract(state, counts, numerator, denominator):
    following = Counter()
    for (x,y,count),selected in zip(state,counts):
        if count > selected:
            following[x*denominator,y*denominator] += count-selected
    following[numerator] += sum(counts)
    content = gcd(*(x for row in following for x in row))
    assert content
    target = tuple(sorted((x//content,y//content,c) for (x,y),c in following.items()))
    assert sum(x*c for x,y,c in target) == sum(y*c for x,y,c in target) == 0
    return target,(content,denominator)


def primitive_matrix(matrix):
    divisor = gcd(*matrix)
    reduced = tuple(x//divisor for x in matrix)
    return min(reduced,tuple(-x for x in reduced))


def middle_states(n, include_six=False, current_library=False, expanded_first=False):
    r = n-4
    source = ((-r,-3,1),(0,1,3),(1,0,r))
    firsts = {}
    size_test = solved_size if current_library else certificate_size
    middle_sizes = tuple(s for s in range(3,n) if size_test(s))
    first_sizes = (3,6,9) if include_six else (3,9)
    if expanded_first:
        first_sizes = sorted(set(middle_sizes)|({6} if include_six else set()))
    for size in first_sizes:
        if size > n:
            continue
        for beta in range(4):
            for gamma in range(2):
                alpha = size-beta-gamma
                if not 0 <= alpha <= r or beta == gamma == 0:
                    continue
                if size == 6 and (alpha,beta,gamma) != (4,2,0):
                    continue
                counts = gamma,beta,alpha
                mean = admissible_mean(source,counts,size)
                if mean is None:
                    continue
                state,scale = contract(source,counts,*mean)
                firsts.setdefault(state,dict(counts=counts,scale=scale))
    prefixes = {}
    tested = 0
    for state,first in firsts.items():
        capacities = tuple(c for x,y,c in state)
        for size in middle_sizes:
            complement = size > n//2
            for chosen in selections(capacities,n-size if complement else size):
                counts = tuple(c-k for c,k in zip(capacities,chosen)) if complement else chosen
                if sum(k > 0 for k in counts) == 1:
                    continue
                tested += 1
                mean = admissible_mean(state,counts,size)
                if mean is None:
                    continue
                target,scale = contract(state,counts,*mean)
                prefixes.setdefault(target,dict(first=first,middle=dict(counts=counts,scale=scale),
                                               after_first=state))
    return source,prefixes,tested


def compile_returns(n, include_six=False, current_library=False, expanded_first=False):
    if n < 11:
        raise ValueError('this compiler assumes distinct multiplicities n-4, 3, 1 with n>=11')
    source,prefixes,tested = middle_states(n,include_six,current_library,expanded_first)
    size_test = solved_size if current_library else certificate_size
    r = n-4
    modulus = away_three(n)
    result = {}
    final_tested = 0
    for state,prefix in prefixes.items():
        capacities = tuple(c for x,y,c in state)
        for size in range(r,r+3):
            if not size_test(size):
                continue
            for leftover in selections(capacities,n-size):
                counts = tuple(c-k for c,k in zip(capacities,leftover))
                final_tested += 1
                mean = admissible_mean(state,counts,size)
                if mean is None:
                    continue
                (x,y),denominator = mean
                sx,sy = total(state,leftover)
                for index,((a,b,c),count) in enumerate(zip(state,leftover)):
                    if not count:
                        continue
                    second = denominator*(sx-a)+(size-r)*x,denominator*(sy-b)+(size-r)*y
                    raw = 3*x,3*y,second[0],second[1]
                    determinant = raw[0]*raw[3]-raw[1]*raw[2]
                    if not determinant:
                        continue
                    matrix = primitive_matrix(raw)
                    determinant = matrix[0]*matrix[3]-matrix[1]*matrix[2]
                    if gcd(determinant,modulus) != 1:
                        continue
                    assert (matrix[0]+matrix[1]-matrix[2]-matrix[3]) % modulus == 0
                    result.setdefault(matrix,dict(prefix,source=source,before_final=state,
                        final=dict(counts=counts,singleton=index),raw=raw,denominator=3*denominator))
    return result,dict(prefixes=len(prefixes),middle_tests=tested,final_tests=final_tested,
                      selection_cache=selections.cache_info()._asdict(),
                      lattice_cache=lattice_signature.cache_info()._asdict())


def run(n,compare,include_six=False,current_library=False,expanded_first=False):
    start = perf_counter()
    rows,stats = compile_returns(n,include_six,current_library,expanded_first)
    elapsed = perf_counter()-start
    print('integer universal compiler n',n,'returns',len(rows),'seconds',round(elapsed,4))
    print('operation and cache counts',stats)
    if compare:
        if n != 17:
            raise ValueError('the independent legacy comparison is only available for n=17')
        from explore_b17_two_stage_universal import compile_returns as legacy
        old,_ = legacy()
        assert set(rows) == set(old)
        print('all 95 B17 projective matrices match the independent Fraction compiler: PASS')
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=17)
    parser.add_argument('--compare',action='store_true')
    parser.add_argument('--include-six',action='store_true')
    parser.add_argument('--current-library',action='store_true',
                        help='use all currently proved sizes instead of the frozen certificate library')
    parser.add_argument('--expanded-first',action='store_true',
                        help='allow every library size at the first call, preserving the old default')
    args = parser.parse_args()
    run(args.n,args.compare,args.include_six,args.current_library,args.expanded_first)
