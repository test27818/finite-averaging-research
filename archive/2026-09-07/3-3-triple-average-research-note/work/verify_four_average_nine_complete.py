"""Explicit positive dyadic controller for four-averaging on nine positions.

No seed or word search: a fixed involution, affine inverse pairing, complete
12-coset Schreier equations, Euclid and Bezout supply the construction.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_uniform_endpoint_controller import Program, Element, Replay, norm
from verify_prime_power_endpoint_completion import (
    Compiler, I, S, T, mul, inv, representatives, edge_data, label, bezout,
)
from verify_composite_arity_transfer import gap_gcd, primitive_center, independent_replay


class FourProgram(Program):
    def __init__(self):
        super().__init__(4)

    def f(self, r):
        assert r % 2 == 0 and 0 < abs(r) <= 4 and gcd(r, 9) == 1
        if r not in self.fs:
            self.fs[r] = Element(self.make(('f', r), (8, r-4, 0, 2*r), 2))
        return self.fs[r]

    def seed(self):
        j = self.t(2)
        self.check(self.mul(j, self.swap, j, self.swap), I)
        self.give_inverse(j, self.mul(self.swap, j, self.swap))
        self.d2 = self.mul(self.inv(j), self.t(4))
        self.check(self.d2, (1, 0, 0, 2))
        f = self.f(2)
        self.affine_pair(self.d2, f)
        quarter = self.mul(self.d2, f)
        self.check(quarter, (1, F(-1, 4), 0, 1))
        self.give_inverse(quarter, self.mul(self.swap, quarter, self.swap))
        self.u = self.power(quarter, -4)
        self.sign = self.mul(self.swap, self.u)
        self.check(self.sign, (1, 0, 0, -1))
        upper_minus_half = self.power(quarter, 2)
        diagonal_minus_quarter = self.mul(self.sign, self.power(self.d2, -2))
        lower18 = self.mul(upper_minus_half, self.t(1), diagonal_minus_quarter)
        self.check(lower18, (1, 0, 18, 1))
        self.give_inverse(lower18, self.mul(self.sign, lower18, self.sign))
        self.lower = self.mul(self.inv(self.d2), lower18, self.d2)
        self.check(self.lower, (1, 0, 9, 1))


class FourCompiler(Compiler):
    def __init__(self):
        self.program = FourProgram()
        self.program.seed()
        self.diagonals = {}

    def diagonal(self, value):
        value = F(value)
        assert value != 0
        p = self.program
        result = p.one
        if value < 0:
            result = p.sign
        a, b = abs(value.numerator), value.denominator
        exponent = 0
        while a % 2 == 0:
            a //= 2
            exponent += 1
        while b % 2 == 0:
            b //= 2
            exponent -= 1
        assert a == b == 1, value
        result = p.mul(result, p.power(p.d2, exponent))
        p.check(result, (1, 0, 0, value))
        return result


class OriginalReplay(Replay):
    def __init__(self, initial, first, second, singleton):
        super().__init__(4, 0, 0)
        self.state = list(map(F, initial))
        self.a, self.b, self.w = first[:], second[:], singleton
        self.word = []
        self.average(first)
        self.average(second)
        self.parameters()

    def average(self, indices):
        super().average(indices)
        self.word.append(list(indices))

    def finish(self):
        x, y = self.parameters()
        assert x == 0
        if y == 0:
            return
        self.average([self.w] + self.a[:3])
        for _ in range(2):
            plus = [i for i, x in enumerate(self.state) if x > 0]
            minus = [i for i, x in enumerate(self.state) if x < 0]
            self.average(plus[:2] + minus[:2])
        assert not any(self.state)


def entry(values, singleton=0):
    assert len(values) == 9 and sum(values) == 0 and gap_gcd(values) == 1
    normalized = primitive_center(values)
    rest = [i for i in range(9) if i != singleton]
    first, second = rest[:4], rest[4:]
    if (sum(normalized[i] for i in first) - sum(normalized[i] for i in second)) % 3 == 0:
        i, j = next((i, j) for i in first for j in second if (normalized[i] - normalized[j]) % 3)
        first[first.index(i)], second[second.index(j)] = j, i
    replay = OriginalReplay(values, first, second, singleton)
    x, y = replay.parameters()
    denominator = lcm(x.denominator, y.denominator)
    xx, yy = int(x*denominator), int(y*denominator)
    assert (yy // gcd(xx, yy)) % 3 and gap_gcd(replay.state) == 1
    return replay


def integer_word(matrix):
    """SL2(Z) -> a finite list of S and T^+-1; no group-word search."""
    a, b, c, d = matrix
    assert a*d-b*c == 1
    prefix = []
    while c:
        k = a // c
        prefix += [T if k > 0 else inv(T)] * abs(k)
        # In PSL2, S inverse equals S; the scalar sign is immaterial.
        prefix.append(S)
        a, b, c, d = -c, -d, a-k*c, b-k*d
    assert abs(a) == 1 and d == a
    k = b // a
    prefix += [T if k > 0 else inv(T)] * abs(k)
    computed = I
    for generator in prefix:
        computed = mul(computed, generator)
    assert norm(computed) == norm(matrix)
    return prefix


def compile_integer(matrix, compiler):
    assert matrix[2] % 9 == 0
    p = compiler.program
    key, result = ('b', 0), p.one
    for generator in integer_word(matrix):
        key, loop = edge_data(key, generator, 9, 3)
        result = p.mul(result, compiler.gauss(loop))
    assert key == ('b', 0)
    p.check(result, matrix)
    return result


def target_matrix(x, y):
    denominator = lcm(F(x).denominator, F(y).denominator)
    x, y = int(x*denominator), int(y*denominator)
    common = gcd(x, y)
    x, y = x//common, y//common
    assert gcd(y, 9) == 1
    u, v = bezout(x, y)
    k = -u*pow(y, -1, 9) % 9
    u, v = u+k*y, v-k*x
    return y, -x, u, v


def main():
    for p in range(4, 65, 2):
        j = (-(p+1), p//2, -(2*p+1), p)
        js = mul(j, (1, -1, 0, -1))
        assert mul(js, js) == (-p//2, 0, 0, -p//2)
    compiler = FourCompiler()
    program = compiler.program
    # All mathematical group generators used for the 12-coset certificate.
    loops, rows = 0, 0
    pivots = set()
    reps = representatives(9, 3)
    assert len(reps) == 12
    for c, d in product(range(9), repeat=2):
        if gcd(c, d, 9) == 1:
            r = reps[label(c, d, 9, 3)]
            assert (c*r[3] - d*r[2]) % 9 == 0
            rows += 1
    for key, representative in reps.items():
        for generator in (S, T, inv(T)):
            following, loop = edge_data(key, generator, 9, 3)
            assert mul(mul(representative, generator), inv(reps[following])) == loop
            assert label(*mul(representative, generator)[2:], 9, 3) == following
            compiler.gauss(loop)
            pivots.add(abs(loop[0]))
            loops += 1
    assert pivots == {1, 2, 4}
    leaves = 0
    for index, (key, matrix, size) in enumerate(program.nodes):
        if key[0] == 'm':
            assert key[1] < index and key[2] < index
        elif key[0] in ('t', 'f'):
            for a, b in ((1, 0), (0, 1)):
                replay = Replay(4, a, b)
                replay.letter(key)
                x, y = replay.parameters()
                if key[0] == 't':
                    j = key[1]
                    assert (x, y) == (F(-5*a+j*(a-b), 4), F(-9*a+2*j*(a-b), 4))
                else:
                    r = key[1]
                    assert (x, y) == (a+F(r-4, 8)*(a-b), F(r, 4)*(a-b))
                leaves += 1
    print('four-average n9 positive seeds and complete Schreier cover: PASS', loops, rows, leaves)
    entries = 0
    # Every admissible mod3 multiplicity pattern and every possible singleton.
    for zero in range(10):
        for one in range(10-zero):
            two = 9-zero-one
            if (one+2*two) % 3 or max(zero, one, two) == 9:
                continue
            xs = [0]*zero + [1]*one + [2]*two
            xs[-1] -= sum(xs)
            for singleton in range(9):
                entry(xs, singleton)
                entries += 1
    rng, transport = Random(40920260912), 0
    for _ in range(50):
        while True:
            xs = [rng.randrange(-(1 << 80), 1 << 80) for _ in range(8)]
            xs.append(-sum(xs))
            if gap_gcd(xs) == 1:
                break
        replay = entry(xs, rng.randrange(9))
        x, y = replay.parameters()
        matrix = target_matrix(x, y)
        assert matrix[0]*x + matrix[1]*y == 0
        assert matrix[0]*matrix[3] - matrix[1]*matrix[2] == 1 and matrix[2] % 9 == 0
        transport += 1
    print('four-average n9 universal-entry finite audits: PASS', entries, transport)
    records = []
    for _ in range(6):
        while True:
            raw = [rng.randrange(-2, 3) for _ in range(8)]
            raw.append(-sum(raw))
            if gap_gcd(raw) == 1:
                break
        replay = entry(primitive_center(raw))
        x, y = replay.parameters()
        element = compile_integer(target_matrix(x, y), compiler)
        for letter in program.letters(element.node):
            replay.letter(letter)
        assert replay.parameters()[0] == 0
        replay.finish()
        independent_replay(raw, replay.word, 4)
        records.append({'input': raw, 'steps': len(replay.word),
                        'operations': [[i+1 for i in group] for group in replay.word]})
    Path(__file__).with_name('four_average_nine_witnesses.json').write_text(
        json.dumps({'index_base': 1, 'cases': records}, indent=2)+'\n', encoding='utf-8')
    print('four-average n9 literal full consensus paths: PASS', len(records), max(x['steps'] for x in records))
    print('four-average nine-position complete criterion: PASS')


if __name__ == '__main__':
    main()
