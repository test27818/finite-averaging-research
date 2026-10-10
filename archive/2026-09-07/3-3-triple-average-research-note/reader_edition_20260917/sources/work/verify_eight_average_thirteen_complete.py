"""Eight-averaging n13: explicit (8,4,1) core, periods, dyadic Gamma_0(13).

The period is now a fixed exact identity; this verifier does not run the
bounded discovery script.  Every nonidentity DAG leaf is a true eight-average.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_uniform_endpoint_controller import Program, Element, I, SIGMA
from verify_prime_power_endpoint_completion import S, T, mul, inv, bezout
from verify_four_average_nine_complete import FourCompiler, integer_word
from verify_composite_arity_transfer import primitive_center, gap_gcd, independent_replay


class EightProgram(Program):
    def __init__(self):
        self.p, self.q = 8, 13
        self.nodes, self.cache = [], {}
        self.one = Element(self.make(('i',), I, 0))
        self.one.back = self.one.node
        self.a = Element(self.make(('a',), (2,-1,0,-1), 1))
        self.b = Element(self.make(('b',), (-5,4,-13,12), 1))
        self.c = Element(self.make(('c',), (-5,1,-13,1), 1))

    def seed(self):
        self.check(self.power(self.c,4), I)
        self.give_inverse(self.c,self.power(self.c,3))
        w = self.mul(self.a,self.a,self.c,self.c)
        self.check(self.power(w,3),I)
        self.give_inverse(self.a,self.mul(self.a,self.c,self.c,self.power(w,2)))
        self.swap = self.mul(self.inv(self.c),self.b)
        self.check(self.swap,SIGMA)
        self.give_inverse(self.swap,self.swap)
        half = self.mul(self.swap,self.a)
        self.check(half,(1,0,0,F(1,2)))
        self.d2 = self.inv(half)
        self.uhalf = self.halves(self.d2)
        self.u = self.power(self.uhalf,2)
        self.sign = self.mul(self.swap,self.u)
        self.check(self.sign,(1,0,0,-1))
        lower = self.mul(self.inv(self.u),self.c,self.power(self.d2,3))
        self.check(lower,(1,0,F(-13,8),1))
        self.lower = self.inv(self.mul(self.power(self.d2,3),lower,self.power(self.d2,-3)))
        self.check(self.lower,(1,0,13,1))


class EightCompiler(FourCompiler):
    def __init__(self):
        self.program = EightProgram()
        self.program.seed()
        self.diagonals = {}


REP = {j % 13:j for j in [0]+[sgn*2**k for k in range(6) for sgn in (1,-1)]}
REPS = {**{j:(0,-1,1,j) for j in REP.values()},None:I}


def label(c,d):
    assert gcd(c,d,13) == 1
    return REP[d*pow(c,-1,13) % 13] if c % 13 else None


def edge(key,generator):
    candidate = mul(REPS[key],generator)
    following = label(candidate[2],candidate[3])
    loop = mul(candidate,inv(REPS[following]))
    if generator == S:
        expected = I if key is None else (-1,0,0,-1) if key == 0 else (
            -following,-1,key*following+1,key)
    elif key is None:
        expected = generator
    else:
        expected = (1,0,-(key+generator[1]-following),1)
    assert expected == loop and loop[2] % 13 == 0
    return following,loop


def compile_integer(matrix,compiler):
    assert matrix[2] % 13 == 0
    key,result = None,compiler.program.one
    for generator in integer_word(matrix):
        key,loop = edge(key,generator)
        result = compiler.program.mul(result,compiler.gauss(loop))
    assert key is None
    compiler.program.check(result,matrix)
    return result


class Replay:
    def __init__(self,u,v):
        self.state = [F(u)]*8+[F(v)]*4+[F(-8*u-4*v)]
        self.u,self.v,self.w = list(range(8)),list(range(8,12)),12
        self.word = []

    def average(self,ids):
        assert len(ids) == len(set(ids)) == 8
        assert all(type(i) is int and 0 <= i < 13 for i in ids)
        mean = sum(self.state[i] for i in ids)/8
        for i in ids:
            self.state[i] = mean
        self.word.append(ids[:])

    def parameters(self):
        u,v = self.state[self.u[0]],self.state[self.v[0]]
        assert len(self.u) == 8 and len(self.v) == 4
        assert sorted(self.u+self.v+[self.w]) == list(range(13))
        assert all(self.state[i] == u for i in self.u)
        assert all(self.state[i] == v for i in self.v)
        assert self.state[self.w] == -8*u-4*v
        return u,u-v

    def letter(self,key):
        if key == ('a',):
            chosen,remaining = self.u[:4]+self.v,self.u[4:]
            self.average(chosen)
            self.u,self.v = chosen,remaining
        elif key == ('b',):
            chosen,singleton = self.u[:7]+[self.w],self.u[7]
            self.average(chosen)
            self.u,self.w = chosen,singleton
        elif key == ('c',):
            chosen = self.u[:4]+self.v[:3]+[self.w]
            remaining,singleton = self.u[4:],self.v[3]
            self.average(chosen)
            self.u,self.v,self.w = chosen,remaining,singleton
        else:
            raise AssertionError(key)
        self.parameters()

    def finish(self):
        x,y = self.parameters()
        assert x == 0
        if y:
            self.average(self.v+[self.w]+self.u[:3])
        assert not any(self.state)


def entry(raw):
    xs = primitive_center(raw)
    assert len(xs) == 13 and gap_gcd(xs) == 1
    i,j = next((i,j) for i,j in combinations(range(13),2) if (xs[i]-xs[j]) % 13)
    outside = [i,j]+[k for k in range(13) if k not in (i,j)][:3]
    first = [i for i in range(13) if i not in outside]
    replay = Replay(0,0)
    replay.state = list(map(F,xs))
    replay.average(first)
    a = replay.state[first[0]]
    residue = a.numerator*pow(a.denominator,-1,13) % 13
    singleton = next(i for i in outside if xs[i] % 13 != residue)
    second = first[:4]+[i for i in outside if i != singleton]
    replay.average(second)
    replay.u,replay.v,replay.w = second,first[4:],singleton
    x,y = replay.parameters()
    assert y.numerator % 13 and gap_gcd(replay.state) == 1
    return replay


def target_matrix(x,y):
    den = lcm(x.denominator,y.denominator)
    x,y = int(x*den),int(y*den)
    common = gcd(x,y)
    x,y = x//common,y//common
    alpha,beta = bezout(x,y)
    k = -alpha*pow(y,-1,13) % 13
    alpha,beta = alpha+k*y,beta-k*x
    assert alpha % 13 == 0
    return y,-x,alpha,beta


def main():
    compiler = EightCompiler()
    program = compiler.program
    a = (F(1),F(-1,2),0,F(-1,2))
    b = tuple(F(x,8) for x in (-5,4,-13,12))
    c = tuple(F(x,8) for x in (-5,1,-13,1))
    c2 = mul(c,c)
    assert mul(c2,c2) == (F(-1,64),0,0,F(-1,64))
    w = mul(mul(a,a),c2)
    assert w == tuple(F(x,64) for x in (-1,-1,13,-3))
    assert mul(mul(w,w),w) == (F(1,4096),0,0,F(1,4096))
    leaves = 0
    for name,matrix in (('a',a),('b',b),('c',c)):
        for u,v in ((1,0),(0,1)):
            replay = Replay(u,v)
            replay.letter((name,))
            assert replay.parameters() == (matrix[0]*u+matrix[1]*(u-v),matrix[2]*u+matrix[3]*(u-v))
            leaves += 1
    rows = loops = 0
    for c0,d0 in product(range(13),repeat=2):
        if gcd(c0,d0,13) == 1:
            r = REPS[label(c0,d0)]
            assert (c0*r[3]-d0*r[2]) % 13 == 0
            rows += 1
    pivots = set()
    for key in REPS:
        for generator in (S,T,inv(T)):
            _,loop = edge(key,generator)
            compiler.gauss(loop)
            pivots.add(abs(loop[0]))
            loops += 1
    assert len(REPS) == 14 and pivots == {1,2,4,8,16,32}
    for i,(key,_,_) in enumerate(program.nodes):
        assert key[0] in ('i','a','b','c','m')
        if key[0] == 'm':
            assert key[1] < i and key[2] < i
    print('eight-average n13 actual periods and complete Schreier cover: PASS',leaves,rows,loops)
    rng = Random(81360912)
    for _ in range(120):
        while True:
            raw = [rng.randrange(-(1 << 80),1 << 80) for _ in range(13)]
            if gap_gcd(raw) == 1:
                break
        replay = entry(raw)
        x,y = replay.parameters()
        matrix = target_matrix(x,y)
        assert matrix[0]*x+matrix[1]*y == 0
    print('eight-average n13 large-integer entry and Bezout: PASS 120')
    records = []
    for _ in range(5):
        while True:
            raw = [rng.randrange(-2,3) for _ in range(12)]
            raw.append(-sum(raw))
            if gap_gcd(raw) == 1:
                break
        replay = entry(raw)
        x,y = replay.parameters()
        result = compile_integer(target_matrix(x,y),compiler)
        for letter in program.letters(result.node):
            replay.letter(letter)
        replay.finish()
        independent_replay(raw,replay.word,8)
        records.append({'input':raw,'G':1,'steps':len(replay.word),
                        'operations':[[i+1 for i in atom] for atom in replay.word]})
    Path(__file__).with_name('eight_average_thirteen_witnesses.json').write_text(
        json.dumps({'index_base':1,'cases':records},indent=2)+'\n',encoding='utf-8')
    print('eight-average n13 literal full paths: PASS',len(records),max(x['steps'] for x in records))
    print('eight-average thirteen-position complete criterion: PASS')


if __name__ == '__main__':
    main()
