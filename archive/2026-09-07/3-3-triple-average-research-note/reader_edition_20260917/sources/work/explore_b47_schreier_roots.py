"""Target Schreier generators using known reversible words and a root.

If W and K have equal first rows and determinants up to projective scale,
then W K^-1 is lower unipotent. Membership of its parameter in 47 Z[1/6]
is checked exactly. A negative bounded result is not nonmembership.
"""

from collections import defaultdict,deque
from fractions import Fraction as F
from math import gcd
import json
from pathlib import Path

from compile_bn_integer_templates import primitive_matrix
from explore_b17_integral_return_cover import mul
from explore_thirteen_modular import S,U


I = (-1,0,0,-1)


def det(m):return m[0]*m[3]-m[1]*m[2]


def adj(m):return (m[3],-m[1],-m[2],m[0])


def label(row,p):
    a,b = (v % p for v in row)
    return (1,b*pow(a,-1,p)%p) if a else (0,1)


def schreier(p):
    base = (1,p-1)
    reps = {base:I}
    todo = deque([base])
    generators = {}
    while todo:
        current = todo.popleft()
        r = reps[current]
        for generator in (S,U):
            next_matrix = primitive_matrix(mul(r,generator))
            a,b,c,d = next_matrix
            following = label((a-c,b-d),p)
            if following not in reps:
                reps[following] = next_matrix
                todo.append(following)
            else:
                loop = primitive_matrix(mul(next_matrix,adj(reps[following])))
                if loop != I:generators.setdefault(loop,(current,following))
    assert len(reps) == p+1
    for m in generators:
        assert det(m) == 1 and (m[0]+m[1]-m[2]-m[3]) % p == 0
    return generators


def key(m):
    a,b,_,_ = m
    content = gcd(a,b)
    if a>0 or (not a and b>0):content=-content
    return a//content,b//content,F(det(m),content*content)


def states(depth):
    data = json.loads(Path(__file__).with_name('b47_root_activation_certificate.json').read_text())
    basic = {}
    for index,node in enumerate(data['nodes'],1):
        m = tuple(node['matrix'])
        basic.setdefault(m,(index,))
        basic.setdefault(primitive_matrix(adj(m)),(-index,))
    seen = {I:()}
    frontier = {I:()}
    for _ in range(depth):
        following = {}
        for m,word in frontier.items():
            for n,letter in basic.items():
                result = primitive_matrix(mul(n,m))
                if result not in seen:following.setdefault(result,word+letter)
        seen.update(following)
        frontier = following
    return seen


def allowed(t):
    d = (t/47).denominator
    for prime in (2,3):
        while d % prime == 0:d//=prime
    return d == 1


def search(depth=2):
    words = states(depth)
    index = defaultdict(list)
    for m,w in words.items():index[key(m)].append((m,w))
    targets = schreier(47)
    print('targeted Schreier roots: states',len(words),'targets',len(targets),flush=True)
    successes = {}
    for target in targets:
        for h,wh in words.items():
            left = mul(target,adj(h))
            for g,wg in index.get(key(left),()):
                quotient = mul(left,adj(g))
                a,b,c,d = quotient
                assert b == 0 and a == d != 0
                t = F(c,a)
                if allowed(t):
                    successes[target] = (wh+wg,(t.numerator,t.denominator))
                    break
            if target in successes:break
        print('target',target,'PASS' if target in successes else 'MISSING',
              successes.get(target),flush=True)
    print('TARGET SUMMARY',len(successes),'/',len(targets),flush=True)
    return successes


if __name__ == '__main__':search()
