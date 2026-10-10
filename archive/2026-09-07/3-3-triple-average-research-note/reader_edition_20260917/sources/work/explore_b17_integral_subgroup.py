"""Find integral subgroups of the certified positive B17/B19/B23 libraries."""

import argparse
from math import gcd
from time import perf_counter

from explore_thirteen_modular import Fold, modular_word
from explore_b17_integral_return_cover import mul
from verify_b17_positive_arithmetic import INTEGER


def normalize(matrix):
    content = gcd(*matrix)
    result = tuple(x//content for x in matrix)
    return min(result,tuple(-x for x in result))


def det(matrix):
    return matrix[0]*matrix[3]-matrix[1]*matrix[2]


def generators(depth, integer_generators=INTEGER):
    basic = {}
    for name,matrix in integer_generators.items():
        a,b,c,d = matrix
        basic[name] = matrix
        basic[name.lower()] = (d,-b,-c,a)
    initial = normalize((1,0,0,1))
    seen = {initial}
    frontier = [(initial,'')]
    integral = {}
    reversal = None
    for length in range(1,depth+1):
        following = []
        for matrix,word in frontier:
            for letter,generator in basic.items():
                target = normalize(mul(generator,matrix))
                if target in seen:
                    continue
                seen.add(target)
                text = word+letter
                following.append((target,text))
                if abs(det(target)) == 1:
                    integral[target] = text
                    if det(target) == -1 and reversal is None:
                        reversal = target,text
        frontier = following
        print('depth',length,'new matrices',len(frontier),'integral',len(integral),flush=True)
    result = {m:w for m,w in integral.items() if det(m) == 1}
    if reversal:
        reflection,word = reversal
        for m,w in integral.items():
            if det(m) == -1:
                result.setdefault(normalize(mul(reflection,m)),w+word)
    return result


def run(depth, integer_generators=INTEGER):
    started = perf_counter()
    integral = generators(depth,integer_generators)
    candidates = sorted(((modular_word(matrix),word,matrix) for matrix,word in integral.items()),
                        key=lambda item:(len(item[0]),len(item[1]),item[1]))
    fold = Fold()
    table = fold.close()
    retained = []
    for modular,word,matrix in candidates:
        if fold.contains(modular,table):
            continue
        fold.loop(modular)
        table = fold.close()
        nodes = {fold.root(i) for i in range(len(fold.parent))}
        missing = sum((node,letter) not in table for node in nodes for letter in 'su')
        retained.append((word,matrix,len(nodes),missing))
        print('fold',retained[-1],flush=True)
        if not missing:
            print('COMPLETE INTEGRAL INDEX',len(nodes),flush=True)
            break
    print('retained certificate',retained)
    print('seconds',round(perf_counter()-started,3))
    return retained


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,choices=(17,19,23),default=17)
    parser.add_argument('--depth',type=int,default=3)
    args = parser.parse_args()
    limit = 8 if args.n == 23 else 5
    if not 1 <= args.depth <= limit:
        parser.error(f'depth must be in 1..{limit} for this library')
    chosen = INTEGER
    if args.n == 19:
        from verify_nineteen_arithmetic_group import INTEGER as chosen
    elif args.n == 23:
        from verify_twenty_three_arithmetic_group import INTEGER as chosen
    run(args.depth,chosen)
