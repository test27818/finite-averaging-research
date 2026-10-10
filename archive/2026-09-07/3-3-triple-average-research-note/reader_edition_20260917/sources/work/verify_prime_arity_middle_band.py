"""Three-block transport at n=3p and the same-residue heavy-value lemma.

Transport tables have nine entries. Modular words use integer Euclid and
four-coset rewriting; large translation exponents are not scanned in rewriting.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd
from random import Random

if not __debug__:
    raise RuntimeError('Assertions are required.')

I = (1, 0, 0, 1)
S = (0, -1, 1, 0)
N = ((1, -1, 0), (1, -1, 0), (-2, 2, 0))
SWAP_AB = (1, -1, 0, -1)
SWAP_AC = (-2, 1, -3, 2)


def mm(a, b):
    x, y, z, t = a
    u, v, w, h = b
    return x*u+y*w, x*v+y*h, z*u+t*w, z*v+t*h


def projective(a):
    return tuple(-x for x in a) if next(x for x in a if x) < 0 else a


def upper(t):
    return (1, t, 0, 1)


def lower(t):
    return (1, 0, t, 1)


def transport_table(p, direction):
    assert p >= 5 and p % 3 and direction in (-1, 1)
    epsilon = 1 if p % 3 == 1 else -1
    m = (p-epsilon)//3
    table = tuple(tuple(m+epsilon*((i == j)+direction*N[i][j])
                        for j in range(3)) for i in range(3))
    assert min(x for row in table for x in row) >= 0
    assert all(sum(row) == p for row in table)
    assert all(sum(table[i][j] for i in range(3)) == p for j in range(3))
    return table, epsilon


def bezout(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q = r0//r1
        r0, r1 = r1, r0-q*r1
        s0, s1 = s1, s0-q*s1
        t0, t1 = t1, t0-q*t1
    assert abs(r0) == 1
    return s0*r0, t0*r0


def modular_word(matrix):
    word, current = [], matrix
    while current[2]:
        a, b, c, d = current
        quotient = a//c
        word.extend((('t', quotient), ('s', 1)))
        current = (-c, -d, a-quotient*c, b-quotient*d)
    a, b, c, d = current
    assert a == d and abs(a) == 1
    word.append(('t', b//a))
    product = I
    for kind, power in word:
        product = mm(product, S if kind == 's' else upper(power))
    assert projective(product) == projective(matrix)
    return word


def signed3(x):
    return (x+1) % 3-1


def compile_gamma3(matrix):
    assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1
    assert matrix[2] % 3 == 0
    representative, factors, product = None, [], I
    for kind, exponent in modular_word(matrix):
        if kind == 's':
            if representative is None:
                representative = 0
            elif representative == 0:
                representative = None
            else:
                factors.append(('u', -representative))
                product = mm(product, upper(-representative))
                representative = -representative
        elif representative is None:
            factors.append(('u', exponent))
            product = mm(product, upper(exponent))
        else:
            following = signed3(representative+exponent)
            wraps = (representative+exponent-following)//3
            factors.append(('l', -wraps))
            product = mm(product, lower(-3*wraps))
            representative = following
    assert representative is None
    assert projective(product) == projective(matrix)
    return [(kind, power) for kind, power in reversed(factors) if power]


class Replay:
    def __init__(self, values, p, enter=True):
        assert len(values) == 3*p and sum(values) == 0
        self.p, self.state, self.operations = p, list(map(F, values)), []
        self.blocks = [list(range(i*p, (i+1)*p)) for i in range(3)]
        if enter:
            sums = [sum(values[i] for i in block) for block in self.blocks]
            if len({x % 3 for x in sums}) == 1:
                different = next(i for i, x in enumerate(values) if (x-values[0]) % 3)
                a, b, i, j = 0, different//p, 0, different
                if b == 0:
                    b, j = 1, p
                    i = 0 if (values[0]-values[j]) % 3 else different
                ai, bj = self.blocks[a].index(i), self.blocks[b].index(j)
                self.blocks[a][ai], self.blocks[b][bj] = j, i
            for block in self.blocks:
                self.average(block)
            a, b, c = self.parameters()
            denominator = a.denominator*b.denominator
            x, y = int(a*denominator), int((a-b)*denominator)
            divisor = gcd(x, y)
            assert divisor and (y//divisor) % 3

    def average(self, indices):
        assert len(indices) == len(set(indices)) == self.p
        mean = sum(self.state[i] for i in indices)/self.p
        for i in indices:
            self.state[i] = mean
        self.operations.append(tuple(indices))
        assert sum(self.state) == 0

    def parameters(self):
        values = [self.state[block[0]] for block in self.blocks]
        assert all(all(self.state[i] == x for i in block)
                   for x, block in zip(values, self.blocks))
        assert sum(values) == 0
        return values

    def shear(self, direction):
        table, epsilon = transport_table(self.p, direction)
        before = self.parameters()
        cursors, following = [0, 0, 0], []
        for row in table:
            indices = []
            for j, count in enumerate(row):
                indices += self.blocks[j][cursors[j]:cursors[j]+count]
                cursors[j] += count
            following.append(indices)
        assert cursors == [self.p]*3
        assert len({i for block in following for i in block}) == 3*self.p
        for block in following:
            self.average(block)
        self.blocks = following
        after = self.parameters()
        expected = [F(epsilon, self.p)*(before[i]+direction*sum(N[i][j]*before[j]
                                                                            for j in range(3)))
                    for i in range(3)]
        assert after == expected

    def lower(self, direction):
        # L(-3)=U(-1) P_ac Sigma_ab; reverse this positive word for L(3).
        if direction == -1:
            self.blocks[0], self.blocks[1] = self.blocks[1], self.blocks[0]
            self.blocks[0], self.blocks[2] = self.blocks[2], self.blocks[0]
            self.shear(-1)
        else:
            self.shear(1)
            self.blocks[0], self.blocks[2] = self.blocks[2], self.blocks[0]
            self.blocks[0], self.blocks[1] = self.blocks[1], self.blocks[0]

    def execute(self, factors):
        for kind, power in factors:
            direction = 1 if power > 0 else -1
            for _ in range(abs(power)):
                if kind == 'u':
                    self.shear(direction)
                else:
                    self.lower(direction)

    def finish(self):
        a, b, c = self.parameters()
        assert a == 0 and b == -c
        h = (self.p-1)//2
        for count in (h, h, 1):
            plus = [i for i, x in enumerate(self.state) if x > 0]
            minus = [i for i, x in enumerate(self.state) if x < 0]
            zero = [i for i, x in enumerate(self.state) if not x]
            self.average(plus[:count]+minus[:count]+zero[:self.p-2*count])
        assert not any(self.state)


def solve(values, p):
    replay = Replay(values, p)
    a, b, c = replay.parameters()
    denominator = a.denominator*b.denominator
    x, y = int(a*denominator), int((a-b)*denominator)
    g = gcd(x, y)
    x, y = x//g, y//g
    alpha, beta = bezout(x, y)
    adjust = (-alpha*pow(y, -1, 3)) % 3
    alpha, beta = alpha+adjust*y, beta-adjust*x
    matrix = (y, -x, alpha, beta)
    factors = compile_gamma3(matrix)
    replay.execute(factors)
    assert replay.parameters()[0] == 0
    replay.finish()
    return len(replay.operations)


def same_residue_move(counts, p, factors):
    heavy = sorted(x for x, count in counts.items() if count >= p)
    assert len(heavy) == 2
    a, b = heavy
    assert (a-b) % p == 0
    if counts[b] > p:
        return [a]*(p-1)+[b]
    if counts[a] > p:
        return [b]*(p-1)+[a]
    light = [x for x, count in counts.items() if x not in (a, b) for _ in range(count)]
    protected = set()
    n = sum(counts.values())
    for q in factors:
        residues = Counter()
        for x, count in counts.items():
            residues[x % q] += count
        residue, size = residues.most_common(1)[0]
        if size >= n-p and a % q == b % q == residue:
            protected.add(next(i for i, x in enumerate(light) if x % q != residue))
    pool = [x for i, x in enumerate(light) if i not in protected][:p]
    assert len(pool) == p
    prefix, first = 0, {0: 0}
    segment = None
    for end, x in enumerate(pool, 1):
        prefix = (prefix+x-a) % p
        if prefix in first:
            segment = pool[first[prefix]:end]
            break
        first[prefix] = end
    assert segment
    move = segment+[a]*(p-len(segment))
    if sum(move) == p*b:
        move = segment+[b]*(p-len(segment))
        assert sum(move) != p*a
    return move


def prime_factors(n):
    result, d = [], 2
    while d*d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def main():
    assert mm(upper(-1), mm(SWAP_AC, SWAP_AB)) == lower(-3)
    matrices = 0
    for p in (5, 7, 11, 13, 17, 19, 31, 61, 97, 101):
        for direction in (-1, 1):
            for a, b in ((1, 0), (0, 1)):
                replay = Replay([a]*p+[b]*p+[-a-b]*p, p, enter=False)
                replay.shear(direction)
                matrices += 1
    print('three-p nonnegative transport and literal basis replay: PASS', matrices)

    reps = {None: I, -1: (0, -1, 1, -1), 0: S, 1: (0, -1, 1, 1)}
    edges = 0
    for j, representative in reps.items():
        for generator in (S, upper(1), upper(-1)):
            candidate = mm(representative, generator)
            c, d = candidate[2] % 3, candidate[3] % 3
            following = None if c == 0 else signed3(d*pow(c, -1, 3))
            r = reps[following]
            edge = mm(candidate, (r[3], -r[1], -r[2], r[0]))
            assert edge[2] % 3 == 0
            compile_gamma3(edge)
            edges += 1
    print('three-p complete Gamma0(3) Schreier certificate: PASS', edges)

    random = Random(2026091206)
    paths, longest, obstruction, p_gcd = 0, 0, 0, 0
    for p in (5, 7, 11, 13, 17, 19, 31):
        kappa = 1 if p % 3 == 2 else 2
        example = [-kappa*p-1]*p+[1]*p+[kappa*p]*p
        longest = max(longest, solve(example, p))
        obstruction += 1
        two_values = [2-p]*6+[2]*(3*p-6)
        assert gcd(*(x-two_values[0] for x in two_values)) == p
        longest = max(longest, solve(two_values, p))
        p_gcd += 1
        for _ in range(8):
            while True:
                values = [random.randrange(-12, 13) for _ in range(3*p-1)]
                values.append(-sum(values))
                if len({x % 3 for x in values}) > 1:
                    break
            longest = max(longest, solve(values, p))
            paths += 1
    print('three-p former invariant-obstruction family: PASS', obstruction)
    print('three-p legal G=p complete paths: PASS', p_gcd)
    print('three-p arbitrary-input literal Fraction complete paths: PASS', paths, longest)

    cases = 0
    for p in (3, 5, 7, 11, 17):
        for iteration in range(200):
            n = 3*p+8
            a, b = -p, p
            counts = Counter({a: p, b: p})
            if iteration % 3 == 0:
                counts[a] += 1
            remaining = n-sum(counts.values())
            values = [random.randrange(-40, 41) for _ in range(remaining-1)]
            values.append(-sum(x*c for x, c in counts.items())-sum(values))
            counts.update(values)
            if sorted(x for x, c in counts.items() if c >= p) != [a, b]:
                continue
            factors = [q for q in prime_factors(n) if q != p]
            if any(len({x % q for x in counts}) == 1 for q in factors):
                continue
            move = same_residue_move(counts, p, factors)
            assert len(move) == p and sum(move) % p == 0 and len(set(move)) > 1
            result = counts-Counter(move)
            result[sum(move)//p] += p
            assert sum(c >= p for c in result.values()) >= 2
            assert all(len({x % q for x in result}) > 1 for q in factors)
            cases += 1
    print('three-p-scale same-residue heavy closure: PASS', cases)
    print('prime-arity middle-band structure: PASS')


if __name__ == '__main__':
    main()
