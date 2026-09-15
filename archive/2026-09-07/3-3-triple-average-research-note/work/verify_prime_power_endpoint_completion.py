"""Prime-power Schreier charts and compilation into existing positive macros.

No word search: every coset transition and its unit pivot have a closed formula.
Large positive inverses remain acyclic product DAGs; only small words are replayed.
"""

from fractions import Fraction as F
from math import gcd
from random import Random

from verify_uniform_endpoint_controller import Program, Replay, phi, norm
from verify_prime_power_endpoint_entry import prime_power_entry

I, S, T = (1, 0, 0, 1), (0, -1, 1, 0), (1, 1, 0, 1)


def mul(a, b):
    x, y, z, w = a
    e, f, g, h = b
    return x*e+y*g, x*f+y*h, z*e+w*g, z*f+w*h


def inv(a):
    x, y, z, w = a
    assert x*w-y*z == 1
    return w, -y, -z, x


def center(x, q):
    return (x+q//2) % q-q//2


def label(c, d, q, ell):
    assert gcd(c, d, q) == 1
    if c % ell:
        return 'a', center(d*pow(c, -1, q), q)
    return 'b', center(c*pow(d, -1, q), q)


def representatives(q, ell):
    p = q//2
    return {**{('a', j): (0, -1, 1, j) for j in range(-p, p+1)},
            **{('b', t): (1, 0, t, 1) for t in range(-p, p+1) if t % ell == 0}}


def edge_data(key, generator, q, ell):
    kind, value = key
    if generator == S:
        if kind == 'b':
            return ('a', -value), I
        if value % ell == 0:
            return ('b', -value), (-1, 0, 0, -1)
        k = center(-pow(value, -1, q), q)
        return ('a', k), (-k, -1, value*k+1, value)
    epsilon = generator[1]
    assert generator == (1, epsilon, 0, 1) and abs(epsilon) == 1
    if kind == 'a':
        following = center(value+epsilon, q)
        return ('a', following), (1, 0, -(value+epsilon-following), 1)
    following = center(value*pow(1+epsilon*value, -1, q), q)
    return ('b', following), (1-epsilon*following, epsilon,
        value-(1+epsilon*value)*following, 1+epsilon*value)


def factors(n):
    n = abs(n)
    result, d = [], 2
    while d*d <= n:
        while n % d == 0:
            result.append(d)
            n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def verify_charts():
    levels = ((7, 7), (11, 11), (19, 19), (27, 3), (43, 43),
              (243, 3), (343, 7), (1331, 11), (2187, 3))
    checked = rows = 0
    for q, ell in levels:
        p = q//2
        assert p >= 3 and p % 2
        reps = representatives(q, ell)
        assert len(reps) == q+q//ell
        assert len(reps)*phi(q) == q*q-(q//ell)**2
        assert all(label(r[2], r[3], q, ell) == key for key, r in reps.items())
        if q <= 243:
            for c in range(q):
                for d in range(q):
                    if gcd(c, d, q) == 1:
                        chosen = reps[label(c, d, q, ell)]
                        assert (c*chosen[3]-d*chosen[2]) % q == 0
                        rows += 1
        for key, representative in reps.items():
            for generator in (S, T, inv(T)):
                following, loop = edge_data(key, generator, q, ell)
                candidate = mul(representative, generator)
                assert label(candidate[2], candidate[3], q, ell) == following
                assert mul(candidate, inv(reps[following])) == loop
                a, b, c, d = loop
                assert a*d-b*c == 1 and c % q == 0
                assert a and abs(a) <= p+1 and gcd(a, q) == 1
                assert all(r <= p and q % r for r in factors(a))
                gauss = mul((1, 0, F(c, a), 1),
                            mul((F(a), 0, 0, F(1, a)), (1, F(b, a), 0, 1)))
                assert gauss == loop
                checked += 1
    print('prime-power complete two-chart Schreier equations: PASS', len(levels), checked, rows)


class Compiler:
    def __init__(self, p):
        self.program = Program(p)
        self.program.seed()
        self.diagonals = {}

    def diagonal(self, value):
        value = F(value)
        assert value
        if value in self.diagonals:
            return self.diagonals[value]
        program, parts = self.program, []
        if value < 0:
            parts.append(program.sign)
        for r in factors(value.numerator):
            assert r <= program.p and gcd(r, program.q) == 1
            program.unlock_diagonal(r, phi(program.q))
            parts.append(program.d(r))
        for r in factors(value.denominator):
            assert r <= program.p and gcd(r, program.q) == 1
            program.unlock_diagonal(r, phi(program.q))
            parts.append(program.inv(program.d(r)))
        result = program.mul(*parts)
        program.check(result, (1, 0, 0, value))
        self.diagonals[value] = result
        return result

    def upper(self, value):
        value = F(value)
        p = self.program
        diagonal = self.diagonal(value.denominator)
        result = p.mul(diagonal, p.power(p.u, value.numerator), p.inv(diagonal))
        p.check(result, (1, value, 0, 1))
        return result

    def lower(self, value):
        value = F(value)
        p = self.program
        coefficient = value/p.q
        diagonal = self.diagonal(coefficient.denominator)
        result = p.mul(p.inv(diagonal), p.power(p.lower, coefficient.numerator), diagonal)
        p.check(result, (1, 0, value, 1))
        return result

    def gauss(self, matrix):
        a, b, c, d = matrix
        assert a*d-b*c == 1 and c % self.program.q == 0
        result = self.program.mul(self.lower(F(c, a)),
                   self.diagonal(F(1, a*a)), self.upper(F(b, a)))
        self.program.check(result, matrix)
        assert result.back is not None
        return result


def verify_positive_compilation():
    checked = leaves = 0
    for p, ell in ((3, 7), (5, 11), (13, 3)):
        compiler = Compiler(p)
        for key in representatives(2*p+1, ell):
            for generator in (S, T, inv(T)):
                _, matrix = edge_data(key, generator, 2*p+1, ell)
                compiler.gauss(matrix)
                checked += 1
        program = compiler.program
        for index, (key, _, _) in enumerate(program.nodes):
            if key[0] == 'm':
                assert key[1] < index and key[2] < index
            elif key[0] in ('t', 'f'):
                assert gcd(key[1], 2*p+1) == 1
                for a, b in ((1, 0), (0, 1)):
                    replay = Replay(p, a, b)
                    replay.letter(key)
                    x, y = replay.parameters()
                    if key[0] == 't':
                        j = key[1]
                        expected = (F(-(p+1)*a+j*(a-b), p),
                                    F(-(2*p+1)*a+2*j*(a-b), p))
                    else:
                        r = key[1]
                        expected = (a+F(r-p, 2*p)*(a-b), F(r, p)*(a-b))
                    assert (x, y) == expected
                    leaves += 1
    print('prime-power loops compiled to positive acyclic macros: PASS', checked, leaves)


def bezout(a, b):
    old_r, r, old_u, u, old_v, v = a, b, 1, 0, 0, 1
    while r:
        k = old_r//r
        old_r, r = r, old_r-k*r
        old_u, u = u, old_u-k*u
        old_v, v = v, old_v-k*v
    if old_r < 0:
        old_r, old_u, old_v = -old_r, -old_u, -old_v
    assert old_r == 1 and old_u*a+old_v*b == 1
    return old_u, old_v


def verify_transport_and_entries():
    rng, checked = Random(12091227), 0
    for p, ell, exponent in ((13, 3, 3), (121, 3, 5), (171, 7, 3), (1093, 3, 7)):
        q = 2*p+1
        for _ in range(8):
            raw = [rng.randrange(-(1 << 96), 1 << 96) for _ in range(q-1)]
            raw.append(-sum(raw))
            common = gcd(*raw)
            raw = [x//common for x in raw]
            assert gcd(*(x-raw[0] for x in raw)) == 1
            state, groups, _ = prime_power_entry(raw, p, ell, exponent)
            a, b = state[groups[0][0]], state[groups[1][0]]
            x, y = int(p*a), int(p*(a-b))
            common = gcd(x, y)
            x, y = x//common, y//common
            assert gcd(y, q) == 1
            u, v = bezout(x, y)
            k = -u*pow(y, -1, q) % q
            u, v = u+k*y, v-k*x
            matrix = y, -x, u, v
            assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1 and u % q == 0
            assert (matrix[0]*x+matrix[1]*y, matrix[2]*x+matrix[3]*y) == (0, 1)
            checked += 1
    # Full literal paths at n27 using short, already compiled global words.
    program = Program(13)
    program.seed()
    paths = longest = 0
    for element in (program.u, program.mul(program.u, program.lower, program.u)):
        a, b, c, d = program.nodes[element.node][1]
        replay = Replay(13, -b, -b-a)
        assert gcd(a, 27) == 1
        for key in program.letters(element.node):
            replay.letter(key)
        replay.finish()
        paths += 1
        longest = max(longest, replay.count)
    print('prime-power legal entry and exact Bezout transports: PASS', checked)
    print('n27 literal global-controller terminal paths: PASS', paths, longest)


def transpose(m):
    return m[0], m[2], m[1], m[3]


def verify_lattice_and_frozen_scale():
    checked = 0
    for p in range(3, 70, 2):
        q, h = 2*p+1, (p+1)//2
        gram = (p+1, p, p, p+1)
        basis = (1, 0, -1, 1)
        assert mul(transpose(basis), mul(gram, basis)) == (2, -1, -1, p+1)
        adjugate = (p+1, 1, 1, 2)
        assert mul((2, -1, -1, p+1), adjugate) == (q, 0, 0, q)
        assert 1-4*h == -q
        for a in range(-4, 5):
            for b in range(-4, 5):
                s = a+b
                energy = p*a*a+p*b*b+p*p*(a+b)**2
                assert energy == 2*p*(a*a-a*s+h*s*s)
                checked += 1
        for ell in factors(q):
            for s in range(ell):
                y = 1
                image = (y, -q*s)
                assert image[0] % ell and image[1] % ell == 0
    # A local projective inverse cycle fixes the exterior singleton exactly.
    # The local two-dimensional block is contracted, so it is not a global scalar.
    frozen = 0
    for p in (3, 5, 7, 13):
        program = Program(p)
        program.seed()
        h = (p+1)//2
        mu, exterior = F(-1, 2*p+1), F(1)
        replay = Replay(p, 2, -1)
        replay.state = [x+mu for x in replay.state]
        initial = tuple(replay.state)
        # Replay.letter assumes zero local mean; explicitly execute the T_h groups.
        for _ in range(2):
            aa, bb, w = replay.a, replay.b, replay.w
            first = aa[:h-1]+bb[:p-h]+[w]
            ar, br = aa[h-1:], bb[p-h:]
            second, singleton = ar[:p-h]+br, ar[-1]
            replay.average(first)
            replay.average(second)
            replay.a, replay.b, replay.w = first, second, singleton
        scale = F(h, p*p)
        assert replay.state[replay.a[0]] == mu+2*scale
        assert replay.state[replay.b[0]] == mu-scale
        assert sum(replay.state)+exterior == 0
        assert scale != 1 and exterior != scale*exterior
        assert sum(x*x for x in replay.state) < sum(x*x for x in initial)
        frozen += 1
    print('critical norm lattice and frozen-scale identities: PASS', checked, frozen)


if __name__ == '__main__':
    verify_charts()
    verify_positive_compilation()
    verify_transport_and_entries()
    verify_lattice_and_frozen_scale()
    print('prime-power endpoint completion and critical structure: PASS')
