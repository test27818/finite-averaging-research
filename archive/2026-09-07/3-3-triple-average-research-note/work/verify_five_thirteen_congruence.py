"""Exact checks for five-averaging in dimension thirteen.

The general principal-congruence containment uses the external theorems
stated in the proof. This checks physical generators and local algebra,
not a finite search for arbitrary averaging words.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, triple_return, band_reduce
from verify_endpoint_congruence_completion import mm, inverse

I = (1, 0, 0, 1)
J = (0, 1, -1, 0)
Q = (0, -12, -1, 0)
S = (-1, 3, 0, 1)
D = (1, 0, 0, -12)
V = mm(mm(J, S), mm(J, S))
W = mm(V, V)


def power(matrix, exponent):
    result = I
    while exponent:
        if exponent & 1:
            result = mm(result, matrix)
        exponent //= 2
        if exponent:
            matrix = mm(matrix, matrix)
    return result


def physical_word(x, z, word):
    raw = [F(x)]*5+[3*F(z)-x]*5+[-5*F(z)]*3
    ledger = Ledger(raw, 5)
    groups = list(range(5)), list(range(5, 10)), list(range(10, 13))
    expected = I
    for letter in word:
        expected = mm(expected, S if letter == 'S' else tuple(F(a, 5) for a in (J if letter == 'J' else Q)))
    for letter in reversed(word):
        if letter == 'S':
            groups = groups[1], groups[0], groups[2]
        else:
            groups = triple_return(ledger, groups, 5, 3, 1 if letter == 'J' else 3)
    xx = expected[0]*x+expected[1]*z
    zz = expected[2]*x+expected[3]*z
    for group, value in zip(groups, (xx, 3*zz-xx, -5*zz)):
        assert all(ledger.state[i] == value for i in group)
    ledger.independent_replay(raw)
    return expected, len(ledger.word)


def generated(modulus, generators):
    seen, queue = {I}, deque([I])
    while queue:
        matrix = queue.popleft()
        for generator in generators:
            nxt = tuple(x % modulus for x in mm(matrix, generator))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def bezout(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        q = old_r//r
        old_r, r = r, old_r-q*r
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    sign = 1 if old_r > 0 else -1
    return sign*old_r, sign*old_s, sign*old_t


def main():
    assert V == (1, -3, -3, 10) and W == (10, -33, -33, 109)
    upper = (1, F(13, 4), 0, 1)
    d_inv = (1, 0, 0, F(-1, 12))
    assert mm(mm(mm(S, D), S), d_inv) == upper
    lower = mm(mm(J, upper), inverse(J))
    assert lower == (1, 0, F(-13, 4), 1)
    root_word = ('S', 'J', 'Q', 'S', 'Q', 'J')
    physical_checks = 0
    for x, z in ((1, 0), (0, 1), (2, 3), (5, -7), (10001, -333)):
        for word in (('J', 'J'), ('Q', 'Q'), root_word, ('J',)+root_word+('J',), ('J', 'S')*4):
            matrix, _ = physical_word(x, z, word)
            if word == root_word:
                assert matrix == tuple(F(-12, 625)*a for a in upper)
            physical_checks += 1
    print('five-thirteen physical returns and roots: PASS', physical_checks)

    u = (1, 13, 0, 1)
    l = (1, 0, 13, 1)
    conjugate = mm(mm(V, u), inverse(V))
    assert conjugate == (40, 13, -117, -38)
    kernel = generated(169, (u, l, conjugate))
    assert len(kernel) == 13**3
    assert all((a-1) % 13 == b % 13 == c % 13 == (d-1) % 13 == 0
               for a, b, c, d in kernel)
    print('five-thirteen first congruence layer: PASS', len(kernel))

    # These three nilpotents span sl2(F13); powers give each higher layer.
    nilpotents = ((0, 1, 0, 0), (0, 0, 1, 0), (3, 1, -9, -3))
    assert 3 % 13 != 0
    layers = 0
    for k in range(1, 9):
        for nilpotent in nilpotents:
            assert mm(nilpotent, nilpotent) == (0, 0, 0, 0)
            atom = tuple(a+13*b for a, b in zip(I, nilpotent))
            assert power(atom, 13**(k-1)) == tuple(a+13**k*b for a, b in zip(I, nilpotent))
            layers += 1
    print('five-thirteen higher-layer identities: PASS', layers)

    chart, chart_inv = (0, 1, 1, 5), (-5, 1, 1, 0)
    assert mm(chart, chart_inv) == I
    assert tuple(x % 13 for x in mm(mm(chart, W), chart_inv)) == (1, 6, 0, 1)
    logs = {pow(2, k, 13): k for k in range(12)}
    assert len(logs) == 12
    directions = 0
    for x in range(13):
        for z in range(13):
            y = (x+5*z) % 13
            if not y:
                continue
            k = (-z*pow(6*y, -1, 13)) % 13
            w = power(W, k)
            assert (w[2]*x+w[3]*z) % 13 == 0
            assert (w[0]*x+w[1]*z) % 13 == y
            assert pow(2, logs[y], 13) == y
            directions += 1
    print('five-thirteen legal residue transport: PASS', directions)

    rng, lifts, entries = Random(2026091413), 0, 0
    while lifts < 160:
        x, z = rng.randrange(-10**8, 10**8), rng.randrange(-10**8, 10**8)
        if gcd(x, z) != 1 or (x+5*z) % 13 == 0:
            continue
        y = (x+5*z) % 13
        k = (-z*pow(6*y, -1, 13)) % 13
        w = power(W, k)
        a, b = w[0]*x+w[1]*z, w[2]*x+w[3]*z
        target = 2**logs[y]
        g, alpha, beta = bezout(a, b)
        assert g == 1
        alpha, beta = target*alpha, target*beta
        adjust = beta*pow(a, -1, 13) % 13
        alpha, beta = alpha+adjust*b, beta-adjust*a
        transport = (F(alpha), F(beta), F(-b, target), F(a, target))
        assert transport[0]*transport[3]-transport[1]*transport[2] == 1
        assert alpha*a+beta*b == target
        assert all((v-i).numerator % 13 == 0 and v.denominator & (v.denominator-1) == 0
                   for v, i in zip(transport, I))
        lifts += 1
    print('five-thirteen exact principal-kernel transport: PASS', lifts)

    while entries < 80:
        raw = [rng.randrange(-1000, 1001) for _ in range(12)]
        raw.append(-sum(raw))
        common = gcd(*raw)
        if not common:
            continue
        raw = [x//common for x in raw]
        if len({x % 13 for x in raw}) == 1:
            continue
        assert band_reduce(raw, 5, 3) <= 6
        entries += 1
    print('five-thirteen existing full-input entries: PASS', entries)
    terminal = Ledger([1]*5+[-1]*5+[0]*3, 5)
    for group in ([0, 1, 5, 6, 10], [2, 3, 7, 8, 11], [4, 9, 0, 1, 2]):
        terminal.average(group)
    assert not any(terminal.state)
    terminal.independent_replay([1]*5+[-1]*5+[0]*3)
    result = {'physical_checks': physical_checks, 'first_layer_size': len(kernel),
              'higher_layer_checks': layers, 'legal_residue_vectors': directions,
              'exact_lifts': lifts, 'entries': entries,
              'scope': 'Explicit local algebra and physical macros; general containment uses cited finite-index and CSP theorems.'}
    (Path(__file__).parent/'five_thirteen_congruence_records.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('five-thirteen congruence completion: PASS')


if __name__ == '__main__':
    main()
