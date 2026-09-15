"""Formula-driven positive controller; no averaging-word discovery search.

Expressions are acyclic, hash-consed product DAGs. Large powers use repeated
squaring; only small certificates are expanded into labelled physical paths.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd

if not __debug__:
    raise RuntimeError('Assertions are required.')

I = (1, 0, 0, 1)
SIGMA = (1, -1, 0, -1)


def norm(a):
    g = gcd(*a)
    assert g
    a = tuple(x // g for x in a)
    return tuple(-x for x in a) if next(x for x in a if x) < 0 else a


def mm(a, b):
    x, y, z, t = a
    u, v, w, h = b
    return norm((x*u+y*w, x*v+y*h, z*u+t*w, z*v+t*h))


def rational_matrix(a):
    from math import lcm
    a = tuple(map(F, a))
    d = lcm(*(x.denominator for x in a))
    return norm(tuple(int(d*x) for x in a))


@dataclass
class Element:
    node: int
    back: int | None = None


class Program:
    def __init__(self, p):
        self.p, self.q, self.h = p, 2*p+1, (p+1)//2
        self.nodes, self.cache = [], {}
        self.one = Element(self.make(('i',), I, 0))
        self.one.back = self.one.node
        self.swap = Element(self.make(('s',), SIGMA, 0))
        self.swap.back = self.swap.node
        self.ts, self.fs, self.ds, self.cs = {}, {}, {}, {}
        self.chain = []

    def make(self, key, matrix, size):
        if key in self.cache:
            return self.cache[key]
        idx = len(self.nodes)
        self.nodes.append((key, norm(matrix), size))
        self.cache[key] = idx
        return idx

    def product_nodes(self, a, b):
        if a == self.one.node:
            return b
        if b == self.one.node:
            return a
        return self.make(('m', a, b), mm(self.nodes[a][1], self.nodes[b][1]),
                         self.nodes[a][2] + self.nodes[b][2])

    def mul(self, *args):
        node, back = self.one.node, self.one.node
        for a in args:
            node = self.product_nodes(node, a.node)
            back = (self.product_nodes(a.back, back)
                    if back is not None and a.back is not None else None)
        return Element(node, back)

    def inv(self, a):
        assert a.back is not None
        return Element(a.back, a.node)

    def give_inverse(self, a, b):
        assert mm(self.nodes[a.node][1], self.nodes[b.node][1]) == I
        a.back = b.node

    def power(self, a, n):
        if n < 0:
            return self.power(self.inv(a), -n)
        answer = self.one
        while n:
            if n & 1:
                answer = self.mul(answer, a)
            n >>= 1
            if n:
                a = self.mul(a, a)
        return answer

    def check(self, a, expected):
        assert self.nodes[a.node][1] == rational_matrix(expected)
        if a.back is not None:
            assert mm(self.nodes[a.node][1], self.nodes[a.back][1]) == I

    def t(self, j):
        assert 1 <= j <= self.p and gcd(j, self.q) == 1
        if j not in self.ts:
            self.ts[j] = Element(self.make(('t', j),
                (-(self.p+1), j, -self.q, 2*j), 2))
        return self.ts[j]

    def f(self, r):
        assert r % 2 and abs(r) <= self.p and gcd(r, self.q) == 1
        if r not in self.fs:
            self.fs[r] = Element(self.make(('f', r),
                (2*self.p, r-self.p, 0, 2*r), 2))
        return self.fs[r]

    def c(self, r):
        if r not in self.cs:
            self.cs[r] = self.mul(self.f(r), self.inv(self.f(1)))
            self.check(self.cs[r], (1, F(r-1, 2), 0, r))
        return self.cs[r]

    def affine_pair(self, a, b):
        product = self.mul(a, b)
        matrix = self.nodes[product.node][1]
        assert matrix[2] == 0 and matrix[0] == matrix[3]
        inverse = self.mul(self.swap, product, self.swap)
        self.give_inverse(a, self.mul(b, inverse))
        self.give_inverse(b, self.mul(inverse, a))

    def trace_inverse(self, t, b):
        word = self.mul(t, b)
        matrix = self.nodes[word.node][1]
        assert matrix[0] + matrix[3] == 0
        self.give_inverse(t, self.mul(b, word))
        self.give_inverse(b, self.mul(word, t))

    def d(self, j):
        if j not in self.ds:
            self.ds[j] = self.mul(self.inv(self.j), self.t(j), self.dh)
            self.check(self.ds[j], (1, 0, 0, j))
        return self.ds[j]

    def halves(self, d2):
        half = self.mul(self.swap, d2, self.swap, self.inv(d2))
        self.check(half, (1, F(1, 2), 0, 1))
        return half

    def seed(self):
        p, q, h = self.p, self.q, self.h
        self.j = self.t(h)
        self.give_inverse(self.j, self.j)
        sign = 1 if p % 4 == 1 else -1
        a = (q + sign*p)//4
        self.trace_inverse(self.t(a), self.f(sign))
        if sign == -1:
            self.give_inverse(self.f(1), self.mul(self.inv(self.f(-1)), self.swap))

        dhi = self.mul(self.inv(self.j), self.t(1))
        if h % 2:
            ch = self.c(h)
        else:
            dhalf = self.mul(self.inv(self.j), self.t(h//2))
            self.check(dhalf, (1, 0, 0, F(1, 2)))
            d2 = self.inv(dhalf)
            c2 = self.mul(self.halves(d2), d2)
            odd, valuation = h, 0
            while odd % 2 == 0:
                odd //= 2
                valuation += 1
            ch = self.mul(self.power(c2, valuation), self.c(odd))
        self.affine_pair(dhi, ch)
        self.dh = self.inv(dhi)
        self.check(self.dh, (1, 0, 0, h))
        self.give_inverse(self.t(1), self.mul(self.dh, self.inv(self.j)))

        if h % 2 == 0:
            self.give_inverse(self.d(2), self.inv(d2))
        else:
            r = 1
            self.give_inverse(self.c(1), self.one)
            seen = set()
            while True:
                assert r not in seen and r % 2 and 1 <= r <= p
                seen.add(r)
                signed = r if r % 4 == 1 else -r
                j = (q + signed)//4
                assert 1 <= j <= p and gcd(j, q) == 1
                ci = self.inv(self.c(r))
                if signed < 0:
                    ci = self.mul(ci, self.swap)
                self.trace_inverse(self.t(j), ci)
                dj = self.d(j)
                self.give_inverse(dj, self.mul(self.inv(self.dh),
                    self.inv(self.t(j)), self.j))
                self.chain.append((r, signed, j))
                if j % 2 == 0:
                    dhalf = self.mul(self.inv(dj), self.d(j//2))
                    self.give_inverse(self.d(2), dhalf)
                    break
                self.affine_pair(self.inv(dj), self.c(j))
                r = j
            assert len(seen) <= (p+1)//2

        d2 = self.d(2)
        self.uhalf = self.halves(d2)
        self.u = self.power(self.uhalf, 2)
        self.sign = self.mul(self.swap, self.u)
        self.check(self.sign, (1, 0, 0, -1))
        negative4h = self.mul(self.sign, self.power(d2, 2), self.dh)
        lower = self.mul(self.j, self.uhalf, negative4h)
        self.check(lower, (1, 0, F(q, 2*h), 1))
        d2h = self.mul(d2, self.dh)
        self.lower = self.mul(d2h, lower, self.inv(d2h))
        self.check(self.lower, (1, 0, q, 1))
        self.check(self.u, (1, 1, 0, 1))

    def unlock_diagonal(self, j, exponent):
        dj = self.d(j)
        if dj.back is not None:
            return
        t = j**exponent
        assert (t-1) % self.q == 0
        tail = self.mul(self.u, self.power(self.lower, (t-1)//self.q))
        word = self.mul(self.sign, self.power(dj, exponent), tail)
        matrix = self.nodes[word.node][1]
        assert matrix[0] + matrix[3] == 0
        dt_inverse = self.mul(tail, word, self.sign)
        self.give_inverse(dj, self.mul(self.power(dj, exponent-1), dt_inverse))

    def letters(self, node):
        stack = [node]
        while stack:
            key = self.nodes[stack.pop()][0]
            if key[0] == 'm':
                stack.extend((key[1], key[2]))
            elif key[0] != 'i':
                yield key


def phi(n):
    result, r, prime = n, n, 2
    while prime*prime <= r:
        if r % prime == 0:
            result -= result//prime
            while r % prime == 0:
                r //= prime
        prime += 1
    return result - result//r if r > 1 else result


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5)+1))


class Replay:
    def __init__(self, p, a, b):
        self.p = p
        self.state = [F(a)]*p + [F(b)]*p + [F(-p*(a+b))]
        self.a, self.b, self.w = list(range(p)), list(range(p, 2*p)), 2*p
        self.count = 0

    def average(self, indices):
        assert len(indices) == len(set(indices)) == self.p
        mean = sum(self.state[i] for i in indices)/self.p
        for i in indices:
            self.state[i] = mean
        self.count += 1

    def parameters(self):
        a, b = self.state[self.a[0]], self.state[self.b[0]]
        assert all(self.state[i] == a for i in self.a)
        assert all(self.state[i] == b for i in self.b)
        assert self.state[self.w] == -self.p*(a+b)
        return a, a-b

    def letter(self, key):
        p = self.p
        if key[0] == 's':
            self.a, self.b = self.b, self.a
        elif key[0] == 't':
            j = key[1]
            first = self.a[:j-1] + self.b[:p-j] + [self.w]
            ar, br = self.a[j-1:], self.b[p-j:]
            second, singleton = ar[:p-j] + br, ar[-1]
            self.average(first)
            self.average(second)
            self.a, self.b, self.w = first, second, singleton
        elif key[0] == 'f':
            j = (p+key[1])//2
            first = self.a[:j] + self.b[:p-j]
            second = self.a[j:] + self.b[p-j:]
            self.average(first)
            self.average(second)
            self.a, self.b = first, second
        else:
            raise AssertionError(key)
        assert sum(self.state) == 0
        self.parameters()

    def finish(self):
        x, y = self.parameters()
        assert x == 0 and y
        self.average([self.w] + self.a[:-1])
        h = (self.p-1)//2
        for count in (h, h, 1):
            plus = [i for i, value in enumerate(self.state) if value > 0]
            minus = [i for i, value in enumerate(self.state) if value < 0]
            zero = [i for i, value in enumerate(self.state) if value == 0]
            self.average(plus[:count] + minus[:count] + zero[:self.p-2*count])
        assert not any(self.state)


def main():
    programs = []
    arities = tuple(range(3, 44, 2)) + (53, 73, 97, 127)
    atomic = 0
    for p in arities:
        program = Program(p)
        program.seed()
        exponent = phi(2*p+1)
        indices = range(1, p+1) if p <= 43 else (2, p)
        for j in indices:
            if gcd(j, 2*p+1) == 1:
                program.unlock_diagonal(j, exponent)
        for key, matrix, _ in tuple(program.nodes):
            if key[0] not in ('t', 'f'):
                continue
            for a, b in ((1, 0), (0, 1)):
                replay = Replay(p, a, b)
                replay.letter(key)
                x, y = replay.parameters()
                if key[0] == 't':
                    j = key[1]
                    expected = (F(-(p+1)*a+j*(a-b), p), F(-(2*p+1)*a+2*j*(a-b), p))
                else:
                    r = key[1]
                    expected = (a+F(r-p, 2*p)*(a-b), F(r, p)*(a-b))
                assert (x, y) == expected
                atomic += 1
        programs.append(program)
    print('uniform endpoint original-position return replay: PASS', atomic)
    print('uniform endpoint formula-only seed and terminating index chain: PASS', len(programs))

    diagonals = sum(sum(a.back is not None for a in v.ds.values()) for v in programs)
    print('uniform endpoint Euler positive diagonal inverses: PASS', diagonals)

    edges, loops = 0, 0
    for program in programs:
        p, q = program.p, program.q
        if not isprime(q) or p > 43:
            continue
        reps = {None: I, **{j: (0, -1, 1, j) for j in range(-p, p+1)}}
        for j in range(-p, p+1):
            if not j:
                continue
            k = (-pow(j, -1, q)) % q
            if k > p:
                k -= q
            assert abs(k) <= p and program.d(abs(k)).back is not None
            a = mm(rational_matrix((1, 0, F(-j*k-1, k), 1)),
                   mm(rational_matrix((-k, 0, 0, F(-1, k))),
                      rational_matrix((1, F(1, k), 0, 1))))
            assert a == norm((-k, -1, j*k+1, j))
            loops += 1
        for label, representative in reps.items():
            for generator in ((0, -1, 1, 0), (1, 1, 0, 1), (1, -1, 0, 1)):
                candidate = mm(representative, generator)
                c, d = candidate[2] % q, candidate[3] % q
                following = None if not c else d*pow(c, -1, q) % q
                if following is not None and following > p:
                    following -= q
                rep = reps[following]
                edge = mm(candidate, (rep[3], -rep[1], -rep[2], rep[0]))
                assert edge[2] % q == 0
                if generator == (0, -1, 1, 0) and label not in (None, 0):
                    k = following
                    assert edge == norm((-k, -1, label*k+1, label))
                elif label is None and generator[2] == 0:
                    assert edge == norm(generator)
                elif generator[2] == 0 and label == p and generator[1] == 1:
                    assert edge == norm((1, 0, -q, 1))
                elif generator[2] == 0 and label == -p and generator[1] == -1:
                    assert edge == norm((1, 0, q, 1))
                else:
                    assert edge == I
                edges += 1
    print('uniform prime-dimension complete Schreier interfaces: PASS', loops, edges)

    paths, longest = 0, 0
    for program in programs:
        if program.p not in (3, 5, 7, 11, 17):
            continue
        for element in (program.u, program.mul(program.u, program.lower, program.u)):
            length = program.nodes[element.node][2]
            if length > 6000:
                continue
            a, b, c, d = program.nodes[element.node][1]
            replay = Replay(program.p, -b, -b-a)
            for key in program.letters(element.node):
                replay.letter(key)
            x, y = replay.parameters()
            assert x == 0 and y
            replay.finish()
            paths += 1
            longest = max(longest, replay.count)
    print('uniform endpoint literal Fraction complete terminal paths: PASS', paths, longest)
    for program in programs:
        if program.p in (3, 5, 7, 17, 97):
            print('seed summary:', program.p, 'chain', program.chain,
                  'U atoms', program.nodes[program.u.node][2],
                  'L atoms', program.nodes[program.lower.node][2])
    print('uniform endpoint controller: PASS')


if __name__ == '__main__':
    main()
