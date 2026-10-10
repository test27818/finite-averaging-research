"""Exact integer exit and local protection for upper-band weighted cores.

Every path is one explicit average; candidate legality counts use only the
three type multiplicities. No averaging-word search or numerical fitting.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

if not __debug__:
    raise RuntimeError('Assertions are required.')
ROOT = Path(__file__).resolve().parent


def factors(n):
    ans, q = [], 2
    while q*q <= n:
        if n % q == 0:
            ans.append(q)
            while n % q == 0:
                n //= q
        q += 1
    return ans+([n] if n > 1 else [])


def pair_distance(values):
    ordered = sorted(values)
    return sum((2*i-len(ordered)+1)*v for i, v in enumerate(ordered))


def legal(values, n):
    rational = list(map(F, values))
    return all(len({x.numerator*pow(x.denominator, -1, q) % q for x in rational}) > 1
               for q in factors(n))


def core_values(p, r, y, z):
    assert gcd(y, z) == 1 and gcd(y, 3*p+r) == 1
    return y-p*z, -2*y+(2*p+r)*z, -p*z


def exit_core(p, r, values):
    n = 3*p+r
    a, b, c = values
    assert len(set(values)) == 3
    assert 2*p*a+p*b+r*c == 0 and gcd(a-b, a-c) == 1
    if (a-b) % p == 0:
        counts, branch = (p-1, 1, 0), 'congruent-heavy'
    else:
        i = -(c-b)*pow(a-b, -1, p) % p
        counts, branch = (i, p-1-i, 1), 'one-carrier'
    i, j, s = counts
    mean = F(i*a+j*b+s*c, p)
    assert mean.denominator == 1 and mean != a
    raw = [a]*(2*p)+[b]*p+[c]*r
    positions = list(range(i))+list(range(2*p, 2*p+j))+list(range(3*p, 3*p+s))
    assert len(positions) == len(set(positions)) == p
    result = raw[:]
    for index in positions:
        result[index] = int(mean)
    assert sum(result) == 0 and legal(result, n)
    assert result.count(a) >= p and result.count(int(mean)) >= p
    loss = sum(x*x for x in raw)-sum(x*x for x in result)
    assert loss == sum((raw[i]-mean)**2 for i in positions) >= 2
    assert pair_distance(raw)-pair_distance(result) >= 2*(p-1)
    return {'p': p, 'r': r, 'n': n, 'values': list(values), 'branch': branch,
            'type_counts': list(counts), 'new_value': int(mean),
            'operation_1based': [i+1 for i in positions],
            'square_energy_drop': int(loss),
            'pair_distance_drop': pair_distance(raw)-pair_distance(result)}


def verify_core_safety():
    states, selections = 0, 0
    for p in (5, 7, 11, 13, 17):
        for r in range(1, p):
            n = 3*p+r
            for y, z in ((1, 0), (1, 1), (1, 2)):
                a, b, c = core_values(p, r, y, z)
                assert legal((a, b, c), n)
                dangerous = []
                for q in factors(n):
                    sizes = Counter()
                    for x, weight in ((a, 2*p), (b, p), (c, r)):
                        sizes[x % q] += weight
                    if max(sizes.values()) >= n-p:
                        dangerous.append(q)
                assert dangerous == ([3] if r % 3 == 0 else [])
                for s in range(r+1):
                    for j in range(p-s+1):
                        i = p-s-j
                        mean = F(i*a+j*b+s*c, p)
                        after = [x for x, weight in ((a, 2*p-i), (b, p-j), (c, r-s)) if weight]
                        after.append(mean)
                        strong_safe = legal(after, n)
                        assert strong_safe == (r % 3 != 0 or s != r)
                        selections += 1
                states += 1
    print('core protection exactly mod3 only: PASS', states, selections)


def verify_exits():
    rng, records = Random(2026091407), []
    for p in (5, 7, 11, 13, 17, 19, 23, 31):
        for r in range(1, p):
            n = 3*p+r
            for _ in range(8):
                while True:
                    y, z = rng.randrange(-(1 << 48), 1 << 48), rng.randrange(-(1 << 48), 1 << 48)
                    if gcd(y, z) == 1 and gcd(y, n) == 1:
                        break
                records.append(exit_core(p, r, core_values(p, r, y, z)))
    assert {x['branch'] for x in records} == {'one-carrier', 'congruent-heavy'}
    assert any(x['r'] == 1 and x['branch'] == 'congruent-heavy' for x in records)
    assert any(x['n'] % 3 == 0 for x in records)
    print('upper-band core one-step integer exits: PASS', len(records), dict(Counter(x['branch'] for x in records)))
    (ROOT/'core_exit_potential_records.json').write_text(json.dumps({
        'scope': 'One-step integer exit from legal (2p,p,r) cores only; four-value continuation remains open.',
        'records': records}, indent=2)+'\n', encoding='utf-8')


def verify_nonquadratic():
    rng, checks = Random(2026091408), 0
    for k in (2, 3, 4, 5, 7, 11):
        for _ in range(30):
            selected = [rng.randrange(-50, 51) for _ in range(k-1)]
            selected.append(-sum(selected))
            if not any(selected):
                selected[0], selected[-1] = -1, 1
            extra = [rng.randrange(-80, 81) for _ in range(15)]
            raw = selected+extra
            result = [0]*k+extra
            assert pair_distance(raw)-pair_distance(result) >= 2*(k-1)
            checks += 1
    print('nonquadratic pair-distance integer decrease: PASS', checks)


if __name__ == '__main__':
    verify_core_safety()
    verify_exits()
    verify_nonquadratic()
    print('core exit and energy uniqueness scope: PASS')
