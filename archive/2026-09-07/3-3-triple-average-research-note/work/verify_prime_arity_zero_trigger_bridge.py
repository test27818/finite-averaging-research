"""Support transfer after a real zero-sum p-average; no path discovery.

The upper half of the middle interval uses the independently proved three-p
controller. The lower half only uses the explicit zero-coordinate tail.
"""

from fractions import Fraction as F
from math import gcd
from random import Random

import verify_prime_arity_middle_band as middle

if not __debug__:
    raise RuntimeError('Assertions are required.')


def canonical_g(values):
    common = gcd(*values)
    assert common
    values = [x//common for x in values]
    return gcd(*(x-values[0] for x in values))


class GlobalReplay:
    def __init__(self, values, p):
        self.state = list(map(F, values))
        self.p, self.operations = p, []
        assert sum(self.state) == 0

    def average(self, indices):
        assert len(indices) == len(set(indices)) == self.p
        mean = sum(self.state[i] for i in indices)/self.p
        for i in indices:
            self.state[i] = mean
        self.operations.append(tuple(indices))
        assert sum(self.state) == 0

    def active(self, size):
        support = [i for i, x in enumerate(self.state) if x]
        zeros = [i for i, x in enumerate(self.state) if not x]
        assert len(support) <= size-1 and size <= len(self.state)
        chosen = support+zeros[:size-len(support)]
        chosen_set = set(chosen)
        assert len(chosen) == size and sum(self.state[i] for i in chosen) == 0
        assert any(not self.state[i] for i in chosen)
        assert all(not x for i, x in enumerate(self.state) if i not in chosen_set)
        return chosen

    def small_tail(self):
        p = self.p
        active = self.active(2*p+1)
        zero = next(i for i in active if not self.state[i])
        rest = [i for i in active if i != zero]
        self.average(rest[:p])
        self.average(rest[p:])
        if not any(self.state):
            return
        h = (p-1)//2
        for count in (h, h, 1):
            plus = [i for i in active if self.state[i] > 0]
            minus = [i for i in active if self.state[i] < 0]
            zeros = [i for i in active if not self.state[i]]
            self.average(plus[:count]+minus[:count]+zeros[:p-2*count])
        assert not any(self.state)

    def three_p_tail(self):
        active = self.active(3*self.p)
        initial = [self.state[i] for i in active]
        assert all(x.denominator == 1 for x in initial)
        common = gcd(*(x.numerator for x in initial))
        if not common:
            return
        local = middle.Replay([int(x/common) for x in initial], self.p)
        a, b, c = local.parameters()
        denominator = a.denominator*b.denominator
        x, y = int(a*denominator), int((a-b)*denominator)
        divisor = gcd(x, y)
        x, y = x//divisor, y//divisor
        alpha, beta = middle.bezout(x, y)
        shift = (-alpha*pow(y, -1, 3)) % 3
        alpha, beta = alpha+shift*y, beta-shift*x
        local.execute(middle.compile_gamma3((y, -x, alpha, beta)))
        local.finish()
        for operation in local.operations:
            self.average([active[i] for i in operation])
        assert not any(self.state)


def main():
    random = Random(2026091207)
    low, high, longest = 0, 0, 0
    for p in (5, 7, 11, 17):
        for n in range(2*p+1, 4*p):
            for _ in range(3):
                selected = [random.randrange(-7, 8) for _ in range(p-1)]
                selected.append(-sum(selected))
                other = [random.randrange(-7, 8) for _ in range(n-p-1)]
                other.append(-sum(other))
                replay = GlobalReplay(selected+other, p)
                replay.average(list(range(p)))
                assert replay.state[:p] == [0]*p
                if n <= 3*p:
                    replay.small_tail()
                    assert len(replay.operations) <= 6
                    low += 1
                else:
                    replay.three_p_tail()
                    high += 1
                assert not any(replay.state)
                longest = max(longest, len(replay.operations))
    print('zero-trigger lower band literal original-position tails: PASS', low)
    print('zero-trigger upper band literal original-position tails: PASS', high, longest)

    boundary = 0
    for p in (3, 5, 7, 11, 17, 31, 61, 101):
        n, m = 2*p+2, 2*p+1
        example = [1]*(2*p)+[2, -n]
        assert sum(example) == 0 and canonical_g(example) == 1
        assert all(gcd(x, m) == 1 for x in example)
        assert canonical_g([1]*m+[-m]) == n
        assert gcd(n, p) == 1
        boundary += 1
    print('codimension-one consensus and unavailable initial child: PASS', boundary)

    weighted = 0
    for p in (3, 5, 7, 11, 17, 31):
        for r in range(1, 2*p):
            weights = (p, p, r)
            common = gcd(*weights)
            primitive = tuple(w//common for w in weights)
            level = sum(primitive)
            assert gcd(*primitive) == 1
            for a, b in ((1, 2), (2, -3), (-3, 5)):
                values = (r*a, r*b, -p*(a+b))
                assert sum(w*x for w, x in zip(weights, values)) == 0
                assert level % canonical_g(values) == 0
                weighted += 1
        assert (3*p)//gcd(p, p, p) == 3
        assert (2*p+1)//gcd(p, p, 1) == 2*p+1
    print('primitive block weights and the mean-lattice quotient: PASS', weighted)

    support = 0
    for p in (3, 5, 7, 11, 17, 31, 61):
        for n in range(2*p+1, 6*p+1):
            if n <= 3*p:
                m = 2*p+1
            elif n < 4*p:
                m = 3*p
            elif n < 5*p:
                m = 4*p
            else:
                assert n >= 4*p+(p-1).bit_length()+1
                continue
            assert n-p <= m-1 and m <= n
            support += 1
    print('all-dimension zero-trigger support cover: PASS', support)
    print('prime-arity zero-trigger bridge: PASS')


if __name__ == '__main__':
    main()
