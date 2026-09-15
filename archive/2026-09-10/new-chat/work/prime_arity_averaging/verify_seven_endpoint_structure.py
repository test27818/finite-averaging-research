"""Exact seven-point endpoint certificate without the 18-word cover."""

from fractions import Fraction as F
from math import gcd, lcm

if not __debug__:
    raise RuntimeError('Assertions are required.')

I = (1, 0, 0, 1)
SIGMA = (1, -1, 0, -1)
T = {j: (-4, j, -7, 2 * j) for j in (1, 2, 3)}
CYCLES = ((2, 2), (1, 0) * 3, (3, 0) * 6)
POSITIVE_INVERSES = {0: (0,)}
for cycle in CYCLES:
    for letter in cycle:
        if letter not in POSITIVE_INVERSES:
            i = cycle.index(letter)
            POSITIVE_INVERSES[letter] = cycle[i + 1:] + cycle[:i]


def mul(a, b):
    x, y, z, t = a
    u, v, w, h = b
    return x * u + y * w, x * v + y * h, z * u + t * w, z * v + t * h


def inverse(a):
    det = a[0] * a[3] - a[1] * a[2]
    return tuple(F(x, det) for x in (a[3], -a[1], -a[2], a[0]))


def product(*matrices):
    answer = I
    for matrix in matrices:
        answer = mul(answer, matrix)
    return answer


def normalize(a):
    a = tuple(map(F, a))
    denominator = lcm(*(x.denominator for x in a))
    integers = tuple(int(x * denominator) for x in a)
    common = gcd(*integers)
    integers = tuple(x // common for x in integers)
    return tuple(-x for x in integers) if next(x for x in integers if x) < 0 else integers


def invert_word(word):
    return tuple(-x for x in reversed(word))


def positive(word):
    return tuple(t for letter in word for t in
                 ((letter,) if letter >= 0 else POSITIVE_INVERSES[-letter]))


def word_matrix(word, normalized=True):
    result = I
    for letter in word:
        matrix = SIGMA if letter == 0 else (T[letter] if letter > 0 else inverse(T[-letter]))
        result = mul(matrix, result)
        if normalized:
            result = normalize(result)
    return result


D2, D3 = (2, -1), (3, -1)
HALF = invert_word(D2) + (0,) + D2 + (0,)
ONE = HALF * 2
SIGN = ONE + (0,)


def diag_word(value):
    value = F(value)
    result = SIGN if value < 0 else ()
    num, den = abs(value.numerator), value.denominator
    for prime, word in ((2, D2), (3, D3)):
        power = 0
        while num % prime == 0:
            num //= prime
            power += 1
        while den % prime == 0:
            den //= prime
            power -= 1
        result += (word if power >= 0 else invert_word(word)) * abs(power)
    assert num == den == 1
    return result


def upper_word(t):
    t = F(t)
    diagonal = diag_word(t.denominator)
    middle = (ONE if t >= 0 else invert_word(ONE)) * abs(t.numerator)
    return invert_word(diagonal) + middle + diagonal


LOWER_QUARTER = diag_word(-16) + upper_word(F(1, 4)) + (1,)
LOWER_SEVEN = invert_word(diag_word(4)) + LOWER_QUARTER + diag_word(4)


def lower_word(t):
    t = F(t) / 7
    diagonal = diag_word(t.denominator)
    middle = (LOWER_SEVEN if t >= 0 else invert_word(LOWER_SEVEN)) * abs(t.numerator)
    return diagonal + middle + invert_word(diagonal)


def upper(t):
    return (1, F(t), 0, 1)


def lower(t):
    return (1, 0, F(t), 1)


def diagonal(t):
    return (1, 0, 0, F(t))


class Replay:
    def __init__(self, a, b):
        self.state = list(map(F, [a] * 3 + [b] * 3 + [-3 * (a + b)]))
        self.a, self.b, self.c = [0, 1, 2], [3, 4, 5], 6
        self.operations = []

    def parameters(self):
        a, b = self.state[self.a[0]], self.state[self.b[0]]
        assert all(self.state[i] == a for i in self.a)
        assert all(self.state[i] == b for i in self.b)
        assert self.state[self.c] == -3 * (a + b)
        return a, a - b

    def average(self, indices):
        assert len(indices) == len(set(indices)) == 3
        mean = sum(self.state[i] for i in indices) / 3
        for i in indices:
            self.state[i] = mean
        self.operations.append(tuple(indices))
        assert sum(self.state) == 0

    def letter(self, j):
        before = self.parameters()
        if j == 0:
            self.a, self.b = self.b, self.a
            expected = (before[0] - before[1], -before[1])
        else:
            first = self.a[:j - 1] + self.b[:3 - j] + [self.c]
            leftover_a, leftover_b = self.a[j - 1:], self.b[3 - j:]
            second = leftover_a[:3 - j] + leftover_b
            singleton = leftover_a[-1]
            assert not set(first).intersection(second)
            self.average(first)
            self.average(second)
            self.a, self.b, self.c = first, second, singleton
            matrix = T[j]
            expected = ((matrix[0] * before[0] + matrix[1] * before[1]) / 3,
                        (matrix[2] * before[0] + matrix[3] * before[1]) / 3)
        assert self.parameters() == expected

    def word(self, word):
        for letter in positive(word):
            self.letter(letter)

    def finish(self):
        x, y = self.parameters()
        assert x == 0 and y
        self.average([self.c] + self.a[:2])
        for _ in range(3):
            plus = next(i for i, x in enumerate(self.state) if x > 0)
            minus = next(i for i, x in enumerate(self.state) if x < 0)
            zero = next(i for i, x in enumerate(self.state) if x == 0)
            self.average([plus, minus, zero])
        assert not any(self.state)


def signed(x):
    x %= 7
    return x if x <= 3 else x - 7


def main():
    for p in (2, 3, 5, 7, 11, 17):
        e1 = (-F(1, p), 0, -1, 1)
        e2 = (1, -1, 0, -F(1, p))
        v = (p - 1, -p, 1, -1)
        assert mul(e2, e1) == tuple(F(x, p) for x in v)
        assert v[0] * v[3] - v[1] * v[2] == 1
        assert (v[0] + v[3]) ** 2 - 4 == p * (p - 4)
        if p == 3:
            assert product(v, v, v) == (-1, 0, 0, -1)
    print('two-block carrier sweep and spectral boundary: PASS 6')

    for cycle, scalar in zip(CYCLES, (2, -1, -27)):
        assert word_matrix(cycle, normalized=False) == (scalar, 0, 0, scalar)
    for j in (1, 2, 3):
        assert word_matrix(POSITIVE_INVERSES[j]) == normalize(inverse(T[j]))
        for a, b in ((1, 0), (0, 1)):
            replay = Replay(a, b)
            replay.letter(j)
            replay.word((-j,))
            x, y = replay.parameters()
            assert x * (a - b) == y * a
    print('seven endpoint real returns and positive cycles: PASS 3 3')

    targets = [(HALF, upper(F(1, 2))), (ONE, upper(1)), (SIGN, diagonal(-1)),
               (LOWER_QUARTER, lower(F(7, 4))), (LOWER_SEVEN, lower(7))]
    for t in (F(-3, 2), F(1, 6), F(5, 12), F(-1, 9)):
        targets.extend([(upper_word(t), upper(t)), (lower_word(7 * t), lower(7 * t))])
    for word, matrix in targets:
        assert word_matrix(word) == normalize(matrix)
        assert word_matrix(positive(word)) == normalize(matrix)
    print('seven endpoint full localized-root seed identities: PASS', len(targets))

    modular_s = (0, -1, 1, 0)
    representatives = {None: I, **{j: (0, -1, 1, j) for j in range(-3, 4)}}
    loops = {}
    for j in range(-3, 4):
        if not j:
            continue
        k = signed(-pow(j, -1, 7))
        matrix = (-k, -1, j * k + 1, j)
        word = upper_word(F(1, k)) + diag_word(F(1, k * k)) + lower_word(F(-j * k - 1, k))
        assert word_matrix(word) == normalize(matrix)
        assert word_matrix(positive(word)) == normalize(matrix)
        loops[j] = (matrix, word)
    edges = 0
    for j, representative in representatives.items():
        for generator in (modular_s, upper(1), upper(-1)):
            candidate = mul(representative, generator)
            c, d = int(candidate[2]) % 7, int(candidate[3]) % 7
            next_label = None if not c else signed(d * pow(c, -1, 7))
            edge = normalize(mul(candidate, inverse(representatives[next_label])))
            if generator == modular_s:
                expected = I if j in (None, 0) else loops[j][0]
            elif j is None:
                expected = generator
            elif j == 3 and generator == upper(1):
                expected = lower(-7)
            elif j == -3 and generator == upper(-1):
                expected = lower(7)
            else:
                expected = I
            assert edge == normalize(expected)
            edges += 1
    assert edges == 24
    print('seven endpoint complete signed Schreier certificate: PASS 8 6 24')

    test_words = [word for matrix, word in loops.values()]
    test_words += [loops[a][1] + loops[b][1] for a, b in ((-3, 2), (-2, 3), (2, -1), (3, 1))]
    longest = 0
    for word in test_words:
        matrix = word_matrix(word)
        x, y = -matrix[1], matrix[0]
        assert gcd(x, y) == 1 and y % 7
        replay = Replay(x, x - y)
        replay.word(word)
        replay.finish()
        longest = max(longest, len(replay.operations))
    print('seven endpoint literal Fraction terminal paths: PASS', len(test_words), longest)
    print('seven exact-threshold structural proof: PASS')


if __name__ == '__main__':
    main()
