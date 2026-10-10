"""Meet-in-the-middle integral words from a finite positive-cycle library.

Only two-letter states are stored. Determinant square classes filter the
four-letter joins; bounds on modular words and conjugations are explicit.
"""

import argparse
from collections import defaultdict

from compile_bn_integer_templates import compile_returns,primitive_matrix
from explore_b17_integral_return_cover import mul
from explore_thirteen_modular import Fold,modular_word
from verify_twenty_five_arithmetic_group import finite_order


def determinant(m):
    return m[0]*m[3]-m[1]*m[2]


def square_class(value):
    value = abs(value)
    root,base,prime = 1,1,2
    while prime*prime <= value:
        power = 0
        while value % prime == 0:
            value //= prime
            power += 1
        root *= prime**(power//2)
        if power % 2:base *= prime
        prime += 1
    if value > 1:base *= value
    return base,root


def short_modular_word(matrix,limit):
    a,b,c,d = matrix
    length = 0
    while c:
        quotient = a//c
        length += 2*abs(quotient)+1
        if length > limit:return None
        a,b,c,d = -c,-d,a-quotient*c,b-quotient*d
    length += 2*abs(b//d)
    return modular_word(matrix) if length <= limit else None


def cycle_library(n):
    rows,_ = compile_returns(n,True,True,True)
    keys = sorted(rows,key=lambda m:(max(map(abs,m)),m))
    cycles = []
    reversible = set()
    for a in keys:
        for b in keys:
            ab = mul(a,b)
            for c in keys:
                order = finite_order(mul(ab,c))
                if order:
                    cycles.append((a,b,c,order))
                    reversible.update((a,b,c))
    return sorted(reversible,key=lambda m:(max(map(abs,m)),m)),cycles


def inverse_word(word):
    return tuple(-i for i in reversed(word))


def search(n,conjugations=1,modular_limit=2000):
    keys,cycles = cycle_library(n)
    print('exact cycle library',n,len(keys),len(cycles),flush=True)
    basic = {}
    for i,matrix in enumerate(keys,1):
        basic[i] = matrix
        basic[-i] = primitive_matrix((matrix[3],-matrix[1],-matrix[2],matrix[0]))
    states = {(-1,0,0,-1):()}
    states.update({m:(i,) for i,m in basic.items()})
    for i,a in basic.items():
        for j,b in basic.items():
            states.setdefault(primitive_matrix(mul(a,b)),(j,i))
    groups = defaultdict(list)
    for matrix,word in states.items():
        sf,root = square_class(determinant(matrix))
        groups[sf].append((matrix,word,root))
    integral = {}
    joins = 0
    for sf,group in groups.items():
        for a,wa,ra in group:
            for b,wb,rb in group:
                root = sf*ra*rb
                matrix = mul(a,b)
                joins += 1
                if all(x % root == 0 for x in matrix):
                    normalized = primitive_matrix(tuple(x//root for x in matrix))
                    integral.setdefault(normalized,wb+wa)
    positive = {m:w for m,w in integral.items() if determinant(m)==1}
    negative = {m:w for m,w in integral.items() if determinant(m)==-1}
    if negative:
        anchor = min(negative,key=lambda m:(max(map(abs,m)),m))
        for m,w in negative.items():
            positive.setdefault(primitive_matrix(mul(anchor,m)),w+negative[anchor])
    print('two-letter states',len(states),'filtered joins',joins,'integral words',len(positive),flush=True)
    fold = Fold()
    table = fold.close()
    retained = []
    def insert(items):
        nonlocal table
        candidates = []
        for m,w in items.items():
            modular = short_modular_word(m,modular_limit)
            if modular is not None:
                candidates.append((len(modular),modular,w,m))
        for _,modular,w,m in sorted(candidates):
            if fold.contains(modular,table):continue
            fold.loop(modular)
            table = fold.close()
            nodes = {fold.root(i) for i in range(len(fold.parent))}
            missing = sum((node,c) not in table for node in nodes for c in 'su')
            retained.append((w,m))
            print('fold',len(nodes),missing,'word',w,flush=True)
            if not missing:
                print('COMPLETE',len(nodes),'CERTIFICATE',retained,flush=True)
                return True
        return False
    if insert(positive):return keys,cycles,retained
    frontier = positive
    for depth in range(conjugations):
        following = {}
        for m,w in frontier.items():
            for i,g in basic.items():
                target = primitive_matrix(mul(mul(g,m),basic[-i]))
                if determinant(target)==1 and target not in positive:
                    following[target] = (-i,)+w+(i,)
        positive.update(following)
        print('conjugation layer',depth+1,'new',len(following),flush=True)
        if insert(following):return keys,cycles,retained
        frontier = following
    print('BOUND reached; no completed coset certificate',flush=True)
    return keys,cycles,retained


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=41)
    parser.add_argument('--conjugations',type=int,default=1)
    parser.add_argument('--modular-limit',type=int,default=2000)
    args = parser.parse_args()
    search(args.n,args.conjugations,args.modular_limit)
