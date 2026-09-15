"""Exact constructive certificate for five-number averaging on eleven positions.

The final verifier imports no discovery search and no averaging solver.
Matrix products in prose are conventional; stored words run left to right.
"""

from collections import Counter
from fractions import Fraction as F
from functools import cache
from math import gcd, lcm
from random import Random

if not __debug__:
    raise RuntimeError('Assertions are required.')


I = (1, 0, 0, 1)
S = (1, -1, 0, -1)  # Rename the two blocks in (x,y)=(a,a-b).
RETURNS = {str(j): (-6, j, -11, 2 * j) for j in range(1, 6)}
GENERATORS = dict(RETURNS, s=S)
CYCLES = (('3', '3'),
          ('1', 's', '2', 's') * 2,
          ('3', '5', 's', '4', 's') * 2)


def mul(a, b):
    x, y, z, t = a
    u, v, w, h = b
    return x * u + y * w, x * v + y * h, z * u + t * w, z * v + t * h


def det(a):
    return a[0] * a[3] - a[1] * a[2]


def inverse(a):
    d = det(a)
    return tuple(F(x, d) for x in (a[3], -a[1], -a[2], a[0]))


def primitive(a):
    entries = tuple(map(F, a))
    den = lcm(*(x.denominator for x in entries))
    integers = tuple(int(x * den) for x in entries)
    g = gcd(*integers)
    result = tuple(x // g for x in integers)
    return tuple(-x for x in result) if next(x for x in result if x) < 0 else result


def product(*matrices):
    result = I
    for matrix in matrices:
        result = mul(result, matrix)
    return result


def matrix_word(word, normalize=True):
    result = I
    for letter in word:
        result = mul(GENERATORS[letter], result)
        if normalize:
            result = primitive(result)
    return result


INVERSES = {'s': ('s',)}
for cycle in CYCLES:
    for letter in cycle:
        if letter in INVERSES:
            continue
        index = cycle.index(letter)
        INVERSES[letter] = cycle[index + 1:] + cycle[:index]


def simplify(word):
    stack = []
    for token in word:
        if stack and stack[-1] == token and token in ('s', '3'):
            stack.pop()
        else:
            stack.append(token)
    return tuple(stack)


@cache
def invert_word(word):
    return simplify(t for token in reversed(word) for t in INVERSES[token])


@cache
def positive_diagonal(j):
    assert j in (2, 3, 5)
    return simplify((str(j),) + INVERSES['1'])


D2 = positive_diagonal(2)
HALF = simplify(invert_word(D2) + ('s',) + D2 + ('s',))
UPPER_ONE = simplify(HALF + HALF)
SIGN = simplify(UPPER_ONE + ('s',))


def exponents(value):
    value = F(value)
    assert value
    num, den = abs(value.numerator), value.denominator
    result = []
    for q in (2, 3, 5):
        e = 0
        while num % q == 0:
            num //= q
            e += 1
        while den % q == 0:
            den //= q
            e -= 1
        result.append((q, e))
    assert num == den == 1, ('not a unit in Z[1/30]', value)
    return value < 0, result


@cache
def diagonal_word(value):
    negative, factors = exponents(value)
    result = list(SIGN if negative else ())
    for q, e in factors:
        seed = positive_diagonal(q)
        if e < 0:
            seed = invert_word(seed)
        result.extend(seed * abs(e))
    return simplify(result)


@cache
def upper_word(value):
    value = F(value)
    if not value:
        return ()
    denominator = diagonal_word(value.denominator)
    seed = UPPER_ONE if value > 0 else invert_word(UPPER_ONE)
    return simplify(invert_word(denominator) + seed * abs(value.numerator) + denominator)


LOWER_SIXTH = simplify(diagonal_word(-36) + upper_word(F(1, 6)) + ('1',))
D6 = diagonal_word(6)
LOWER_ELEVEN = simplify(invert_word(D6) + LOWER_SIXTH + D6)


@cache
def lower_word(value):
    coefficient = F(value) / 11
    if not coefficient:
        return ()
    denominator = diagonal_word(coefficient.denominator)
    seed = LOWER_ELEVEN if coefficient > 0 else invert_word(LOWER_ELEVEN)
    return simplify(denominator + seed * abs(coefficient.numerator) + invert_word(denominator))


def upper(x):
    return (1, F(x), 0, 1)


def lower(x):
    return (1, 0, F(x), 1)


def diagonal(x):
    return (1, 0, 0, F(x))


def signed_residue(x):
    x %= 11
    return x if x <= 5 else x - 11


def schreier_matrix(j):
    k = signed_residue(-pow(j, -1, 11))
    return (-k, -1, j * k + 1, j)


@cache
def schreier_word(j):
    a, b, c, d = schreier_matrix(j)
    return simplify(upper_word(F(b, a)) + diagonal_word(F(1, a * a)) + lower_word(F(c, a)))


def bezout(x, y):
    a0, a1, b0, b1 = 1, 0, 0, 1
    r0, r1 = x, y
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    assert abs(r0) == 1
    return a0 * r0, b0 * r0


def transport(x, y):
    assert gcd(x, y) == 1 and y % 11
    a, b = bezout(x, y)
    k = -a * pow(y, -1, 11) % 11
    a, b = a + k * y, b - k * x
    result = (y, -x, a, b)
    assert det(result) == 1 and a % 11 == 0
    assert (result[0] * x + result[1] * y, result[2] * x + result[3] * y) == (0, 1)
    return result


MODULAR_S = (0, -1, 1, 0)


def modular_word(matrix):
    """Return a conventional right-product of S and signed powers of T."""
    current = matrix
    word = []
    while current[2]:
        a, b, c, d = current
        q = a // c
        word.extend([('t', q), ('s', 1)])
        current = (-c, -d, a - q * c, b - q * d)
    a, b, c, d = current
    assert a == d and abs(a) == 1
    word.append(('t', b // a))
    result = I
    for letter, exponent in word:
        result = mul(result, MODULAR_S if letter == 's' else (1, exponent, 0, 1))
    assert primitive(result) == primitive(matrix)
    return word


def compile_gamma(matrix):
    assert det(matrix) == 1 and matrix[2] % 11 == 0
    representative = None
    factors = []
    check = I
    for letter, power in modular_word(matrix):
        if letter == 's':
            if representative is None:
                representative = 0
            elif representative == 0:
                representative = None
            else:
                j = representative
                representative = signed_residue(-pow(j, -1, 11))
                factors.append(schreier_word(j))
                check = primitive(mul(check, schreier_matrix(j)))
        else:
            direction = 1 if power >= 0 else -1
            for _ in range(abs(power)):
                if representative is None:
                    factors.append(upper_word(direction))
                    check = primitive(mul(check, upper(direction)))
                elif representative == 5 and direction == 1:
                    representative = -5
                    factors.append(lower_word(-11))
                    check = primitive(mul(check, lower(-11)))
                elif representative == -5 and direction == -1:
                    representative = 5
                    factors.append(lower_word(11))
                    check = primitive(mul(check, lower(11)))
                else:
                    representative += direction
    assert representative is None and primitive(check) == primitive(matrix)
    word = simplify(token for factor in reversed(factors) for token in factor)
    assert matrix_word(word) == primitive(matrix)
    return word


class PhysicalReplay:
    """Keep all eleven labels; normalization only verifies projective arithmetic."""
    def __init__(self, values, fraction=False):
        self.state = list(map(F, values)) if fraction else list(values)
        self.fraction = fraction
        self.a = list(range(5))
        self.b = list(range(5, 10))
        self.c = 10
        self.operations = []

    def average(self, indices):
        assert len(indices) == len(set(indices)) == 5
        total = sum(self.state[i] for i in indices)
        if self.fraction:
            mean = total / 5
            for i in indices:
                self.state[i] = mean
        else:
            chosen = set(indices)
            raw = [total if i in chosen else 5 * value for i, value in enumerate(self.state)]
            divisor = gcd(*raw)
            self.state = [x // divisor for x in raw] if divisor else raw
        assert sum(self.state) == 0
        self.operations.append(tuple(indices))

    def parameters(self):
        a, b = self.state[self.a[0]], self.state[self.b[0]]
        assert all(self.state[i] == a for i in self.a)
        assert all(self.state[i] == b for i in self.b)
        assert self.state[self.c] == -5 * (a + b)
        return a, a - b

    def letter(self, token):
        before = self.parameters()
        if token == 's':
            self.a, self.b = self.b, self.a
        else:
            j = int(token)
            first = self.a[:j - 1] + self.b[:5 - j] + [self.c]
            leftover_a = self.a[j - 1:]
            leftover_b = self.b[5 - j:]
            second = leftover_a[:5 - j] + leftover_b
            singleton = leftover_a[-1]
            assert not set(first).intersection(second)
            self.average(first)
            self.average(second)
            self.a, self.b, self.c = first, second, singleton
        after = self.parameters()
        expected = GENERATORS[token]
        image = (expected[0] * before[0] + expected[1] * before[1],
                 expected[2] * before[0] + expected[3] * before[1])
        assert after[0] * image[1] == after[1] * image[0]
        if self.fraction:
            scale = 1 if token == 's' else F(1, 5)
            assert after == tuple(scale * x for x in image)

    def word(self, word):
        for token in word:
            self.letter(token)

    def finish(self):
        x, y = self.parameters()
        assert x == 0 and y != 0
        self.average([self.c] + self.a[:4])
        for _ in range(2):
            positive = [i for i, x in enumerate(self.state) if x > 0]
            negative = [i for i, x in enumerate(self.state) if x < 0]
            zeros = [i for i, x in enumerate(self.state) if not x]
            self.average(positive[:2] + negative[:2] + zeros[:1])
        nonzero = [i for i, x in enumerate(self.state) if x]
        zeros = [i for i, x in enumerate(self.state) if not x]
        assert len(nonzero) == 2
        self.average(nonzero + zeros[:3])
        assert not any(self.state)


def enter_core(values):
    assert len(values) == 11 and sum(values) == 0
    assert len({x % 11 for x in values}) > 1
    a, b, c = list(range(5)), list(range(5, 10)), 10
    if (2 * sum(values[i] for i in a) + values[c]) % 11 == 0:
        pair = next((i, j) for i in a for j in b if (values[i] - values[j]) % 11)
        ia, ib = a.index(pair[0]), b.index(pair[1])
        a[ia], b[ib] = b[ib], a[ia]
    replay = PhysicalReplay(values)
    replay.a, replay.b, replay.c = a, b, c
    replay.average(a)
    replay.average(b)
    x, y = replay.parameters()
    assert gcd(x, y) == 1 and y % 11
    return replay


def run_case(values):
    replay = enter_core(values)
    x, y = replay.parameters()
    if x:
        replay.word(compile_gamma(transport(x, y)))
    replay.finish()
    return replay


def main():
    # Literal rational replay supplies the universal coefficient ledger: the
    # matrices are linear, so two independent inputs determine every column.
    for token in GENERATORS:
        for a, b in ((1, 0), (0, 1)):
            replay = PhysicalReplay([a] * 5 + [b] * 5 + [-5 * (a + b)], fraction=True)
            replay.letter(token)
    expected_scalars = (3, -2, 60)
    for cycle, scalar in zip(CYCLES, expected_scalars):
        assert matrix_word(cycle, normalize=False) == (scalar, 0, 0, scalar)
    for token in GENERATORS:
        assert matrix_word(INVERSES[token]) == primitive(inverse(GENERATORS[token]))
        for a, b in ((1, 0), (0, 1)):
            replay = PhysicalReplay([a] * 5 + [b] * 5 + [-5 * (a + b)], fraction=True)
            replay.word((token,) + INVERSES[token])
            x, y = replay.parameters()
            assert x * (a - b) == y * a
    print('five-average eleven physical returns and positive inverses: PASS 5 3', flush=True)

    assert matrix_word(HALF) == primitive(upper(F(1, 2)))
    assert matrix_word(UPPER_ONE) == primitive(upper(1))
    assert matrix_word(SIGN) == primitive(diagonal(-1))
    assert matrix_word(LOWER_SIXTH) == primitive(lower(F(11, 6)))
    assert matrix_word(LOWER_ELEVEN) == primitive(lower(11))
    for value in (F(1), F(-1), F(2), F(3), F(5), F(-36), F(1, 30), F(25, 18)):
        assert matrix_word(diagonal_word(value)) == primitive(diagonal(value))
    roots = 0
    for numerator in (-3, -1, 1, 2):
        for denominator in (1, 2, 3, 4, 5, 6, 25, 30):
            value = F(numerator, denominator)
            assert matrix_word(upper_word(value)) == primitive(upper(value))
            assert matrix_word(lower_word(11 * value)) == primitive(lower(11 * value))
            roots += 2
    print('five-average eleven localized roots and diagonals: PASS', roots, flush=True)

    labels = {None, *range(-5, 6)}
    assert len(labels) == 12
    representatives = {None: I, **{j: (0, -1, 1, j) for j in range(-5, 6)}}
    edges = 0
    for representative, matrix in representatives.items():
        for generator in (MODULAR_S, upper(1), upper(-1)):
            candidate = mul(matrix, generator)
            c, d = int(candidate[2]) % 11, int(candidate[3]) % 11
            following = None if not c else signed_residue(d * pow(c, -1, 11))
            edge = primitive(mul(candidate, inverse(representatives[following])))
            if generator == MODULAR_S:
                expected = I if representative in (None, 0) else schreier_matrix(representative)
            elif representative is None:
                expected = generator
            elif representative == 5 and generator == upper(1):
                expected = lower(-11)
            elif representative == -5 and generator == upper(-1):
                expected = lower(11)
            else:
                expected = I
            assert edge == primitive(expected)
            edges += 1
    assert edges == 36
    for j in range(-5, 6):
        if not j:
            continue
        matrix = schreier_matrix(j)
        assert det(matrix) == 1 and matrix[2] % 11 == 0
        assert matrix_word(schreier_word(j)) == primitive(matrix)
        k = signed_residue(-pow(j, -1, 11))
        left = product(MODULAR_S, upper(j), MODULAR_S, upper(-k), inverse(MODULAR_S))
        assert left == matrix
    print('five-average eleven complete signed Schreier interface: PASS 12 10 36', flush=True)

    transports = 0
    for x in range(-12, 13):
        for y in range(-12, 13):
            if gcd(x, y) != 1 or y % 11 == 0:
                continue
            matrix = transport(x, y)
            word = compile_gamma(matrix)
            assert matrix_word(word) == primitive(matrix)
            transports += 1
    print('five-average eleven exact transport compilation: PASS', transports, flush=True)

    cases = [[a] * 5 + [b] * 5 + [-5 * (a + b)]
             for a, b in ((1, 2), (5, -4), (2, -3), (3, 7), (-2, 5), (7, 9))]
    random = Random(5112026)
    for _ in range(6):
        state = [random.randrange(-7, 8) for _ in range(10)]
        state.append(-sum(state))
        cases.append(state)
    longest = 0
    fraction_replays = 0
    for state in cases:
        if len({x % 11 for x in state}) == 1:
            continue
        replay = run_case(state)
        length = len(replay.operations)
        longest = max(longest, length)
        # A separate literal Fraction replay audits that projective verifier
        # normalization has not introduced a nonphysical operation.
        if fraction_replays < 2 and length <= 6000:
            exact = list(map(F, state))
            for positions in replay.operations:
                mean = sum(exact[i] for i in positions) / 5
                for i in positions:
                    exact[i] = mean
            assert not any(exact)
            fraction_replays += 1
        print('physical complete path', length, 'steps', 'height', max(map(abs, state)), flush=True)
    assert fraction_replays >= 1
    print('five-average eleven complete original-position paths: PASS', len(cases), longest, fraction_replays)
    print('five-average eleven full criterion: PASS')


if __name__ == '__main__':
    main()
