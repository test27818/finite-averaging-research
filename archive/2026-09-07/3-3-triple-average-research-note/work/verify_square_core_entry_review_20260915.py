"""Exact original-position checks for the square-core entry review.

The universal entry lemma is proved in the accompanying review. These are
finite exact replays and a finite unit-image diagnostic, not a uniform core
termination proof. No project implementation is imported.
"""

from fractions import Fraction as F
from math import gcd, isqrt, lcm, prod
from random import Random


def factors(n):
    found = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            found.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        found.append(n)
    return found


def residue(x, m):
    x = F(x)
    return x.numerator*pow(x.denominator, -1, m) % m


def enter(t, raw, first=None):
    q, n = t*t, t*t+t+1
    primes = factors(n)
    assert len(raw) == n and sum(raw) == 0 and gcd(*raw) == 1
    assert all(any((x-raw[0]) % ell for x in raw) for ell in primes)
    state, word = list(map(F, raw)), []

    def average(indices):
        assert len(indices) == len(set(indices)) == q
        value = sum(state[i] for i in indices)/q
        for i in indices:
            state[i] = value
        word.append(list(indices))

    if first is None:
        protected = {0}
        for ell in primes:
            protected.add(next(i for i, x in enumerate(raw) if (x-raw[0]) % ell))
        block = [i for i in range(n) if i not in protected][:q]
    else:
        block = list(first)
    average(block)
    singles = [i for i in range(n) if i not in set(block)]
    bad = [ell for ell in primes if (q-1) % ell == 0]
    assert set(bad) <= {3}
    target = next(i for i, pos in enumerate(singles)
                  if not bad or residue(state[pos]-state[block[0]], 3))
    periods = []
    for ell in primes:
        if (q+1) % ell == 0:
            periods.append(ell)
        else:
            lam = -pow(q, -1, ell) % ell
            power, value = 1, lam
            while value != 1:
                value = value*lam % ell
                power += 1
            periods.append(power)
    period = lcm(*periods)
    nondegenerate = [ell for ell in primes if ell not in bad]
    modulus = prod(nondegenerate)
    transfers = 0
    for ell in nondegenerate:
        delta = [state[pos]-state[block[0]] for pos in singles]
        if residue(delta[target], ell):
            continue
        source = next(i for i, d in enumerate(delta) if residue(d, ell))
        buffer = next(i for i in range(len(singles)) if i not in (source, target))
        exponent = (modulus//ell)*pow(modulus//ell, -1, ell) % modulus
        runs = ((source, period-1), (buffer, 1), (target, period-1),
                (buffer, period-1), (source, 1), (buffer, 1),
                (target, 1), (buffer, period-1))
        for _ in range(exponent):
            for role, repeats in runs:
                for _ in range(repeats):
                    old = block[-1]
                    group = block[:-1]+[singles[role]]
                    average(group)
                    block, singles[role] = group, old
        for prime in primes:
            if prime == ell or residue(delta[target], prime):
                assert residue(state[singles[target]]-state[block[0]], prime)
        transfers += 1
    assert all(residue(state[singles[target]]-state[block[0]], ell) for ell in primes)
    singleton = singles[target]
    kept = block[-t:]
    final = block[:-t]+[pos for i, pos in enumerate(singles) if i != target]
    average(final)
    u, v, w = state[final[0]], state[kept[0]], state[singleton]
    assert q*u+t*v+w == 0
    assert all(residue(u-v, ell) for ell in primes)
    assert sorted(final+kept+[singleton]) == list(range(n))

    replay = list(map(F, raw))
    for indices in word:
        assert len(indices) == len(set(indices)) == q
        value = sum(replay[i] for i in indices)/q
        for i in indices:
            replay[i] = value
        assert sum(replay) == 0
    assert replay == state
    return len(word), transfers


def main():
    if not __debug__:
        raise RuntimeError('Assertions are required.')
    rng = Random(20260915041)
    paths = transfers = atoms = 0
    for t in (2, 3, 4, 7, 9):
        q, n = t*t, t*t+t+1
        primes = factors(n)
        for forced in (False, True):
            if forced:
                m = prod(primes)
                values = [(m//ell)*pow(m//ell, -1, ell) % m for ell in primes]
                values += [-sum(values)]
                raw = [0]*q+values+[0]*(t+1-len(values))
                common = gcd(*raw)
                raw = [x//common for x in raw]
            else:
                while True:
                    raw = [rng.randrange(-20, 21) for _ in range(n-1)]
                    raw += [-sum(raw)]
                    common = gcd(*raw)
                    if common:
                        raw = [x//common for x in raw]
                    if common and all(any((x-raw[0]) % ell for x in raw) for ell in primes):
                        break
            length, moved = enter(t, raw, range(q) if forced else None)
            paths += 1
            transfers += moved
            atoms += length
    print('square entry literal exact paths: PASS', paths, transfers, atoms)
    failures = []
    for t in range(2, 201):
        n = t*t+t+1
        assert gcd(t*t-1, n) == gcd(t+2, 3)
        assert len(factors(n)) <= t
        subgroup = {1}
        generators = [-1]+[d for d in range(2, t+1) if gcd(d, n) == 1]
        for g in generators:
            g %= n
            if g in subgroup:
                continue
            old, v = list(subgroup), g
            while v not in subgroup:
                subgroup.update(v*x % n for x in old)
                v = v*g % n
        phi = sum(gcd(x, n) == 1 for x in range(n))
        if len(subgroup) != phi:
            failures.append((t, n, phi//len(subgroup)))
        # Every one-step zero-sum terminal of the core has y-scale in H_t.
        for b in range(t+1):
            g0 = gcd(b, t*t)
            g1 = gcd(t-b, t+1)
            assert (t*t//g0) % n in subgroup
            assert ((t+1)//g1) % n in subgroup
    print('finite unit-image diagnostic t=2..200:', len(failures), 'failures', failures)
    print('square entry and terminal-class review checks: PASS')


if __name__ == '__main__':
    main()
