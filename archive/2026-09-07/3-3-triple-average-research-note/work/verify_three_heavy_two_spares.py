"""Two-spare three-heavy lemma and bounded diagnostics for the remaining case.

The diagnostic enumerates only two light-type counts. The numbers of selected
anchors are then uniquely determined modulo p, avoiding a third nested loop.
It tests one-step closure, not reachability or a sequence of averaging words.
"""

from collections import Counter
from math import gcd
from random import Random

import verify_prime_arity_large_dimension as base

if not __debug__:
    raise RuntimeError('Assertions are required.')


def choose_three(counts, p):
    a, b, c = sorted(counts)
    assert counts[a] == counts[c] == p and counts[b] >= p+2
    assert sum(x*f for x, f in counts.items()) == 0
    assert len({a % p, b % p, c % p}) == 3
    i = (c-b)*pow(a-c, -1, p) % p
    first = (a,)*i+(c,)*(p-1-i)+(b,)
    if sum(first) != p*b:
        return first, 'one-middle'
    assert 1 <= i <= p-2
    if i == (p-1)//2:
        assert b == 0 and a == -c
        return None, 'opposite-terminal'
    j = 2*i % p
    assert 1 <= j <= p-2
    second = (a,)*j+(c,)*(p-2-j)+(b, b)
    assert sum(second) % p == 0 and sum(second) != p*b
    return second, 'two-middle'


def check_three(counts, p, branches):
    n = sum(counts.values())
    move, branch = choose_three(counts, p)
    branches[branch] += 1
    if move is None:
        return
    after = base.change(counts, move, p)
    assert len(base.heavy(after, p)) >= 2
    for value in set(move):
        assert counts[value] > move.count(value)
    factors = base.protected_primes(n, p)
    if base.legal(counts, factors):
        assert base.legal(after, factors)


def closure_candidate(counts, p, factors):
    a, b = base.heavy(counts, p)
    light = [x for x in counts if x not in (a, b)]
    assert len(light) == 2 and (a-b) % p
    c, d = light
    inverse = pow(a-b, -1, p)
    for k in range(min(p, counts[c])+1):
        for ell in range(min(p-k, counts[d])+1):
            if not k+ell:
                continue
            i = (-k*(c-b)-ell*(d-b))*inverse % p
            j = p-k-ell-i
            if j < 0:
                continue
            move = (a,)*i+(b,)*j+(c,)*k+(d,)*ell
            if len(set(move)) == 1:
                continue
            if sum(move) == 0:
                return move
            after = base.change(counts, move, p)
            if len(base.heavy(after, p)) >= 2 and base.legal(after, factors):
                return move
    return None


def diagnostics():
    random = Random(2026091211)
    tested, barriers = Counter(), []
    for p in (5, 7, 11, 17, 31):
        for extra in range(2, p):
            n = 3*p+extra
            factors = base.protected_primes(n, p)
            if extra < len(factors):
                continue
            for _ in range(120):
                ac, bc = p+random.randrange(p-1), p+random.randrange(p-1)
                light = n-ac-bc
                if not 2 <= light <= 2*p-2:
                    continue
                cc = random.randrange(max(1, light-p+1), min(p-1, light-1)+1)
                dc = light-cc
                a, b, c = [random.randrange(-50, 51)*dc for _ in range(3)]
                d = -(ac*a+bc*b+cc*c)//dc
                common = gcd(a, b, c, d)
                if not common:
                    continue
                a, b, c, d = [x//common for x in (a, b, c, d)]
                if len({a, b, c, d}) < 4 or (a-b) % p == 0:
                    continue
                counts = Counter({a: ac, b: bc, c: cc, d: dc})
                if not base.legal(counts, factors):
                    continue
                tested[p] += 1
                if closure_candidate(counts, p, factors) is None:
                    barriers.append({'p': p, 'n': n, 'counts': dict(sorted(counts.items()))})
                    if sum(x['p'] == p for x in barriers) >= 2:
                        break
            if sum(x['p'] == p for x in barriers) >= 2:
                break
    print('bounded two-heavy diagnostic counts:', dict(tested))
    print('bounded two-heavy one-step barriers:', barriers)


def main():
    random, branches = Random(2026091212), Counter()
    for p in (5, 7, 11, 17, 31, 61):
        for extra in (2, 3, p//2, p-2):
            if extra < 2:
                continue
            n = 3*p+extra
            for _ in range(80):
                a, c = sorted(random.sample(range(-100, 101), 2))
                a, c = (p+extra)*a, (p+extra)*c
                b = -p*(a+c)//(p+extra)
                if not a < b < c or len({a % p, b % p, c % p}) < 3:
                    continue
                check_three(Counter({a:p, b:p+extra, c:p}), p, branches)
            # Force collision of the first controller by solving its exact
            # relation together with the global zero-sum equation.
            for i in range(1, p-1):
                b = p*(p-1-2*i)
                a = b-n*(p-1-i)
                c = b+n*i
                counts = Counter({a:p, b:p+extra, c:p})
                if len({a % p, b % p, c % p}) == 3:
                    check_three(counts, p, branches)
    assert branches['two-middle'] and branches['opposite-terminal']
    print('three-heavy two-spare exact closure: PASS', dict(branches))
    print('three-heavy two-spare lemma: PASS')
    import sys
    if '--diagnostic' in sys.argv:
        diagnostics()


if __name__ == '__main__':
    main()
