"""Prime-power complement traps and a uniform four-step square network.

The report proves arbitrary parameters. Finite checks audit every transition
from sampled high-gap states, not unbounded word trees. Independent matrix
replay certifies full-input networks. No third-party libraries are used.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json


def factors(n):
    result, p = {}, 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def supported(g, q):
    if g == 0:
        return True
    while g > 1:
        common = gcd(g, q)
        if common == 1:
            return False
        g //= common
    return True


def val(x, p):
    x = F(x)
    if not x:
        return float('inf')
    a, b, out = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p
        out += 1
    while b % p == 0:
        b //= p
        out -= 1
    return out


def types(counts, cardinality):
    items = list(counts.items())
    def visit(i, remaining, chosen):
        if i == len(items):
            if remaining == 0:
                yield tuple(chosen)
            return
        x, f = items[i]
        for k in range(min(f, remaining)+1):
            chosen.append((x, k))
            yield from visit(i+1, remaining-k, chosen)
            chosen.pop()
    yield from visit(0, cardinality, [])


def trap_block(counts, q, p, h):
    lowest = min(val(x, p) for x in counts)
    lows = [x for x in counts if val(x, p) == lowest]
    assert len(lows) == 1 and counts[lows[0]] == q
    assert all(val(x, p) >= lowest+h for x in counts if x != lows[0])
    return lows[0], lowest


def transition(counts, complement, q):
    # Zero sum means the selected sum is minus the complement sum.
    assert sum(x*f for x, f in counts.items()) == 0
    outside = Counter({x: f for x, f in complement if f})
    assert not (outside-counts)
    mean = -sum(x*f for x, f in outside.items()) / q
    result = outside.copy()
    result[mean] += q
    return result


def critical_data(q):
    candidates = [(p**((a+1)//2), p, a) for p, a in factors(q).items()]
    s, p, a = max(candidates)
    boundary_g = q//s+1
    exception = supported(boundary_g, q)
    return {'q': q, 'p': p, 'exponent': a, 'scale': s,
            'boundary_n': q+s, 'boundary_G': boundary_g,
            'boundary_survives_G': exception,
            'first_possible': q+s+(not exception)}


def four_step_network(q, r):
    """q=kr, and k+1 divides r. Four q-sets average all q+r positions."""
    assert q % r == 0
    k = q//r
    assert r % (k+1) == 0
    n, h = q+r, q*r//(q+r)
    first = list(range(q))
    a = list(range(q-r, q))
    b = list(range(q-r)) + list(range(q, n))
    second = b[:]
    third = a[:h]+b[:q-h]
    last_original = a[h:]+b[q-h:]
    assert len(last_original) == r
    fourth = last_original+third[:q-r]
    return [first, second, third, fourth]


def matrix_replay(n, word, q):
    matrix = [[F(i == j) for j in range(n)] for i in range(n)]
    for atom in word:
        assert len(atom) == len(set(atom)) == q
        assert all(0 <= i < n for i in atom)
        mean = [sum(matrix[i][j] for i in atom)/q for j in range(n)]
        for i in atom:
            matrix[i] = mean[:]
    assert all(x == F(1, n) for row in matrix for x in row)


def verify_traps():
    rng = Random(202609120468)
    checks = exits = 0
    arities = (4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 25, 27, 28, 30,
               32, 36, 42, 49, 54, 56, 64, 72, 81, 120, 125)
    for q in arities:
        for p, a in factors(q).items():
            s = p**((a+1)//2)
            h = a-((a+1)//2-1)
            for r in sorted({2, max(2, s-1), s}):
                if r > s:
                    continue
                counts = Counter({F(-1): q, F(q): 1})
                counts[F(0)] = r-1
                for step in range(8):
                    low, valuation = trap_block(counts, q, p, h)
                    continuing = []
                    for complement in types(counts, r):
                        # Number of original outside positions selected equals
                        # the number of low-block positions left in complement.
                        k = dict(complement).get(low, 0)
                        after = transition(counts, complement, q)
                        if k == s:
                            assert r == s
                            target = Counter({-low*F(s, q): q, low: s})
                            assert after == target
                            assert supported(q//s+1, q) == (a == 1 and supported(q//s+1, p))
                            exits += 1
                        elif k:
                            new, newval = trap_block(after, q, p, h)
                            assert newval == valuation+val(k, p)-a < valuation
                            continuing.append(after)
                        else:
                            assert after == counts
                        checks += 1
                    if not continuing:
                        break
                    counts = rng.choice(continuing)
    print('composite critical prime-power trap transitions: PASS', checks, exits)
    return checks, exits


def main():
    verify_traps()
    data = [critical_data(q) for q in range(2, 201)]
    for row in data:
        q, s, p, a = (row[k] for k in ('q', 'scale', 'p', 'exponent'))
        assert s <= q
        if row['boundary_survives_G']:
            assert a == 1 and q == p*(row['boundary_G']-1)
            assert set(factors(row['boundary_G'])) == {p}
        if len(factors(q)) == 1 and a >= 2:
            assert row['first_possible'] == q+s+1
    print('composite critical lower-edge arithmetic: PASS', len(data))
    networks = []
    for m in range(2, 11):
        q, n = m*(m-1), m*m
        word = four_step_network(q, m)
        matrix_replay(n, word, q)
        lower = critical_data(q)
        networks.append({'q': q, 'n': n, 'universal_steps': 4,
                         'first_possible': lower['first_possible'],
                         'first_success_proved': lower['first_possible'] == n,
                         'operations': [[i+1 for i in atom] for atom in word]})
    for q, r in ((8, 8), (12, 6), (18, 9), (24, 8), (40, 10)):
        matrix_replay(q+r, four_step_network(q, r), q)
    print('composite critical universal four-step networks: PASS', len(networks)+5)
    # Additional exact first-success claims rely on the same general formulas,
    # even where a full n-by-n basis replay is unnecessary.
    exact = []
    for m in range(2, 31):
        q, n = m*(m-1), m*m
        if critical_data(q)['first_possible'] == n:
            exact.append([q, n])
    Path(__file__).with_name('composite_critical_scale_results.json').write_text(
        json.dumps({'scope': 'proved necessary lower edge; equality outside matched network cases is conjectural',
                    'lower_edges': data, 'network_certificates': networks,
                    'exact_first_success_square_family': exact}, indent=2)+'\n', encoding='utf-8')
    print('composite exact first-success square-family pairs:', exact)
    print('composite prime-power critical scale and square networks: PASS')


if __name__ == '__main__':
    main()
