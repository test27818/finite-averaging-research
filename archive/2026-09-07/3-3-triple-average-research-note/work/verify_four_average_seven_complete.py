"""Four-averaging n7: explicit (4,2,1) core and positive dyadic Gamma_0(7).

No seed, period, or averaging-word search. The finite transversal uses signed
powers of two. Original-position replay is independent of projective matrices.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_uniform_endpoint_controller import Program, Element, I, SIGMA, rational_matrix
from verify_prime_power_endpoint_completion import Compiler, S, T, mul, inv, bezout
from verify_four_average_nine_complete import FourCompiler, integer_word
from verify_composite_arity_transfer import primitive_center, gap_gcd, independent_replay


class SevenProgram(Program):
    def __init__(self):
        # There is NO free exchange of the unequal four- and two-position blocks.
        # The physical Sigma below is a positive three-atom word.
        self.p, self.q = 4, 7
        self.nodes, self.cache = [], {}
        self.one = Element(self.make(('i',), I, 0))
        self.one.back = self.one.node
        self.a = Element(self.make(('a',), (2, -1, 0, -1), 1))
        self.b = Element(self.make(('b',), (-3, 2, -7, 6), 1))
        self.c = Element(self.make(('c',), (-3, 1, -7, 1), 1))

    def seed(self):
        self.check(self.power(self.c, 3), I)
        self.give_inverse(self.c, self.power(self.c, 2))
        self.check(self.power(self.mul(self.c, self.a), 2), I)
        self.give_inverse(self.a, self.mul(self.c, self.a, self.c))
        self.swap = self.mul(self.inv(self.c), self.b)
        self.check(self.swap, SIGMA)
        self.give_inverse(self.swap, self.swap)
        half = self.mul(self.swap, self.a)
        self.check(half, (1, 0, 0, F(1, 2)))
        self.d2 = self.inv(half)
        self.uhalf = self.halves(self.d2)
        self.u = self.power(self.uhalf, 2)
        self.sign = self.mul(self.swap, self.u)
        self.check(self.sign, (1, 0, 0, -1))
        quarter = self.mul(self.inv(self.u), self.c, self.power(self.d2, 2))
        self.check(quarter, (1, 0, F(-7, 4), 1))
        self.lower = self.inv(self.mul(self.power(self.d2, 2), quarter,
                                      self.power(self.d2, -2)))
        self.check(self.lower, (1, 0, 7, 1))


class SevenCompiler(FourCompiler):
    def __init__(self):
        self.program = SevenProgram()
        self.program.seed()
        self.diagonals = {}


REP = {j % 7: j for j in (0, 1, -1, 2, -2, 4, -4)}
REPS = {**{j: (0, -1, 1, j) for j in REP.values()}, None: I}


def coset_label(c, d):
    assert gcd(c, d, 7) == 1
    return REP[d*pow(c, -1, 7) % 7] if c % 7 else None


def edge(key, generator):
    candidate = mul(REPS[key], generator)
    following = coset_label(candidate[2], candidate[3])
    if generator == S:
        if key is None:
            expected = I
        elif key == 0:
            expected = (-1, 0, 0, -1)
        else:
            k = REP[-pow(key, -1, 7) % 7]
            assert following == k
            expected = (-k, -1, key*k+1, key)
    else:
        epsilon = generator[1]
        assert generator == (1, epsilon, 0, 1) and abs(epsilon) == 1
        expected = generator if key is None else (1, 0, -(key+epsilon-following), 1)
    loop = mul(candidate, inv(REPS[following]))
    assert loop == expected and loop[2] % 7 == 0
    return following, loop


def compile_integer(matrix, compiler):
    assert matrix[2] % 7 == 0
    program = compiler.program
    key, result = None, program.one
    for generator in integer_word(matrix):
        key, loop = edge(key, generator)
        result = program.mul(result, compiler.gauss(loop))
    assert key is None
    program.check(result, matrix)
    return result


class Replay:
    def __init__(self, u, v):
        self.state = [F(u)]*4 + [F(v)]*2 + [F(-4*u-2*v)]
        self.u, self.v, self.w = list(range(4)), [4, 5], 6
        self.word = []

    def average(self, ids):
        assert len(ids) == len(set(ids)) == 4
        assert all(type(i) is int and 0 <= i < 7 for i in ids)
        mean = sum(self.state[i] for i in ids)/4
        for i in ids:
            self.state[i] = mean
        self.word.append(list(ids))

    def parameters(self):
        u, v = self.state[self.u[0]], self.state[self.v[0]]
        assert len(self.u) == 4 and len(self.v) == 2
        assert sorted(self.u+self.v+[self.w]) == list(range(7))
        assert all(self.state[i] == u for i in self.u)
        assert all(self.state[i] == v for i in self.v)
        assert self.state[self.w] == -4*u-2*v
        return u, u-v

    def letter(self, key):
        name, = key
        if name == 'a':
            chosen, remaining = self.u[:2]+self.v, self.u[2:]
            self.average(chosen)
            self.u, self.v = chosen, remaining
        elif name == 'b':
            chosen, singleton = self.u[:3]+[self.w], self.u[3]
            self.average(chosen)
            self.u, self.w = chosen, singleton
        elif name == 'c':
            chosen = self.u[:2]+self.v[:1]+[self.w]
            remaining, singleton = self.u[2:], self.v[1]
            self.average(chosen)
            self.u, self.v, self.w = chosen, remaining, singleton
        else:
            raise AssertionError('Nonphysical letter: '+str(key))
        self.parameters()

    def finish(self):
        x, y = self.parameters()
        assert x == 0
        if y == 0:
            return
        # Four zeros, two v, and -2v: one original-position operation suffices.
        self.average(self.v+[self.w, self.u[0]])
        assert not any(self.state)


def entry(raw):
    values = primitive_center(raw)
    assert len(values) == 7 and gap_gcd(values) == 1
    i, j = next((i, j) for i, j in combinations(range(7), 2)
                if (values[i]-values[j]) % 7)
    k = next(k for k in range(7) if k not in (i, j))
    outside = [i, j, k]
    first = [t for t in range(7) if t not in outside]
    replay = Replay(0, 0)
    replay.state = list(map(F, values))
    replay.average(first)
    a = replay.state[first[0]]
    residue = a.numerator*pow(a.denominator, -1, 7) % 7
    singleton = next(t for t in outside if values[t] % 7 != residue)
    second = first[:2]+[t for t in outside if t != singleton]
    replay.average(second)
    replay.u, replay.v, replay.w = second, first[2:], singleton
    x, y = replay.parameters()
    assert gap_gcd(replay.state) == 1
    assert y.numerator % 7 and y.denominator % 7
    return replay


def target_matrix(x, y):
    den = lcm(x.denominator, y.denominator)
    x, y = int(x*den), int(y*den)
    common = gcd(x, y)
    x, y = x//common, y//common
    assert gcd(y, 7) == 1
    u, v = bezout(x, y)
    k = -u*pow(y, -1, 7) % 7
    u, v = u+k*y, v-k*x
    result = y, -x, u, v
    assert y*v+x*u == 1 and u % 7 == 0
    return result


def main():
    compiler = SevenCompiler()
    program = compiler.program
    # Actual scales, not just projective normalization.
    a, b, c = (F(1), F(-1, 2), F(0), F(-1, 2)), tuple(F(x, 4) for x in (-3, 2, -7, 6)), tuple(F(x, 4) for x in (-3, 1, -7, 1))
    assert mul(mul(c, c), c) == (F(1, 8), 0, 0, F(1, 8))
    ca = mul(c, a)
    assert mul(ca, ca) == (F(1, 8), 0, 0, F(1, 8))
    assert mul(mul(c, c), b) == tuple(F(x, 8) for x in SIGMA)
    leaves = 0
    for name, matrix in (('a', a), ('b', b), ('c', c)):
        for u, v in ((1, 0), (0, 1)):
            replay = Replay(u, v)
            replay.letter((name,))
            x, y = replay.parameters()
            assert (x, y) == (matrix[0]*u+matrix[1]*(u-v), matrix[2]*u+matrix[3]*(u-v))
            leaves += 1
    rows = loops = 0
    pivots = set()
    for c0, d0 in product(range(7), repeat=2):
        if gcd(c0, d0, 7) == 1:
            r = REPS[coset_label(c0, d0)]
            assert (c0*r[3]-d0*r[2]) % 7 == 0
            rows += 1
    for key in REPS:
        for generator in (S, T, inv(T)):
            _, loop = edge(key, generator)
            pivots.add(abs(loop[0]))
            compiler.gauss(loop)
            loops += 1
    assert len(REPS) == 8 and pivots == {1, 2, 4}
    for i, (key, _, _) in enumerate(program.nodes):
        assert key[0] in ('i', 'a', 'b', 'c', 'm')
        if key[0] == 'm':
            assert key[1] < i and key[2] < i
    print('four-average n7 physical periods and dyadic Schreier cover: PASS', leaves, rows, loops)
    # All ordered initial residues with first entry fixed at0; translation
    # removes a redundant factor7, and centering supplies an exact zero-sum lift.
    entries = 0
    for prefix in product(range(7), repeat=5):
        xs = [0]+list(prefix)
        xs.append(-sum(xs))
        if max(xs) == min(xs):
            continue
        # gcd7 of all differences cannot occur with first0 and some nonzero residue.
        replay = entry(xs)
        assert gap_gcd(replay.state) == 1
        entries += 1
    rng = Random(40760912)
    for _ in range(80):
        while True:
            xs = [rng.randrange(-(1 << 96), 1 << 96) for _ in range(6)]
            xs.append(-sum(xs))
            if gap_gcd(xs) == 1:
                break
        replay = entry(xs)
        x, y = replay.parameters()
        matrix = target_matrix(x, y)
        assert matrix[0]*x+matrix[1]*y == 0
    print('four-average n7 exact-entry residue and large-integer audits: PASS', entries, 80)
    records = []
    for _ in range(12):
        while True:
            raw = [rng.randrange(-3, 4) for _ in range(7)]
            if gap_gcd(raw) == 1:
                break
        replay = entry(raw)
        x, y = replay.parameters()
        element = compile_integer(target_matrix(x, y), compiler)
        for letter in program.letters(element.node):
            replay.letter(letter)
        assert replay.parameters()[0] == 0
        replay.finish()
        independent_replay(raw, replay.word, 4)
        records.append({'input': raw, 'G': gap_gcd(raw), 'steps': len(replay.word),
                        'operations': [[i+1 for i in atom] for atom in replay.word]})
    Path(__file__).with_name('four_average_seven_witnesses.json').write_text(
        json.dumps({'index_base': 1, 'seed': 40760912, 'cases': records}, indent=2)+'\n', encoding='utf-8')
    print('four-average n7 literal full paths: PASS', len(records), max(x['steps'] for x in records))
    print('four-average seven-position complete criterion: PASS')


if __name__ == '__main__':
    main()
