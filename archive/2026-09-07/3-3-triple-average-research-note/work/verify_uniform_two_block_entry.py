"""Uniform two-round witness transfer, without a period or gcd condition.

Counts are selected by the existing short residue sieve. Each resulting
operation is independently replayed on the original coordinates. The checks
support the general proof and do not assert that every even core is solved.
"""

from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, factors, residue, is_legal, carrier_period
from verify_carrier_energy_and_pair_reduction import safe_flatten
from verify_upper_band_three_value_reduction import full_support, mix, select_parameter
from verify_upper_band_descent_boundary import apply_return as upper_return
from verify_uniform_odd_middle_cores import mm, invq

if not __debug__:
    raise RuntimeError('Assertions are required.')


def transfer(ledger, first, second, singles, anchor, primes):
    """Given first-anchor a local unit, make first-second a local unit."""
    p = ledger.p
    a, b, w = (ledger.state[index] for index in (first[0], second[0], anchor))
    assert all(residue(a-w, ell) for ell in primes)
    first_conditions = []
    exceptional = []
    for ell in primes:
        if (2*p-1) % ell:
            alpha = p*a-(p-1)*b-w
            beta = F(2*p-1, p)*(b-a)
        else:
            assert ell != 2
            # This is the NEXT round's constant, evaluated after this round.
            alpha, beta = w+(a-3*b)/2, 4*(b-a)
            exceptional.append(ell)
        first_conditions.append((ell, residue(alpha, ell), residue(beta, ell)))
    k = select_parameter(p, first_conditions)
    first, second = mix(ledger, first, second, k)
    role = singles.index(anchor)
    second, singles[role] = ledger.swap(second, anchor)
    anchor = singles[role]
    a1, b1, w1 = (ledger.state[index] for index in (first[0], second[0], anchor))
    assert is_legal(ledger.state, primes)
    for ell in primes:
        if ell in exceptional:
            actual = p*a1-(p-1)*b1-w1
            expected = w+(a-3*b)/2+4*k*(b-a)
            assert residue(actual-expected, ell) == 0 and residue(actual, ell)
        else:
            assert residue(a1-b1, ell)
    second_conditions = [(ell, residue(p*a1-(p-1)*b1-w1, ell),
                          residue(F(2*p-1, p)*(b1-a1), ell)) for ell in primes]
    h = select_parameter(p, second_conditions)
    first, second = mix(ledger, first, second, h)
    second, singles[role] = ledger.swap(second, anchor)
    assert all(residue(ledger.state[first[0]]-ledger.state[second[0]], ell) for ell in primes)
    return first, second, singles, {'first_k': k, 'second_k': h, 'exceptional_primes': exceptional}


def replay(raw, ledger, groups, p, r):
    primes = tuple(factors(len(raw)))
    state = list(map(F, raw))
    for group in ledger.word:
        assert len(group) == len(set(group)) == p
        assert all(0 <= index < len(raw) for index in group)
        average = sum(state[index] for index in group)/p
        for index in group:
            state[index] = average
        assert sum(state) == 0 and is_legal(state, primes)
    assert state == ledger.state
    assert list(map(len, groups)) == [p, p, r]
    assert sorted(index for group in groups for index in group) == list(range(len(raw)))
    values = [state[group[0]] for group in groups]
    assert all(state[index] == value for group, value in zip(groups, values) for index in group)
    assert p*(values[0]+values[1])+r*values[2] == 0


def uniform_entry(raw, p, r):
    n = len(raw)
    primes = tuple(factors(n))
    assert p >= 5 and n == 2*p+r and 1 <= r < p and r >= len(primes)
    assert sum(raw) == 0 and gcd(*raw) == 1 and is_legal(raw, primes)
    _, blocks, singles = safe_flatten(raw, p, 2, ledger=True)
    ledger = Ledger(raw, p)
    for block in blocks:
        ledger.average(block)
    anchor = singles[0]
    first, second, singles, phases = full_support(ledger, *blocks, singles, anchor, primes)
    first, second, singles, record = transfer(ledger, first, second, singles, anchor, primes)
    kept, merged = first[p-r:], first[:p-r]+singles
    ledger.average(merged)
    groups = [merged, second, kept]
    assert len(ledger.word) <= 9+3*len(primes)
    replay(raw, ledger, groups, p, r)
    record.update({'p': p, 'n': n, 'input': raw, 'operations': ledger.word,
                   'groups': groups, 'support_phases': len(phases)})
    return record


def forced_midpoint():
    # At ell=3, p=5, a=1,b=3,w=2 form the formerly obstructing midpoint.
    p, r = 5, 2
    raw = [1]*p+[3]*p+[2, -22]
    ledger = Ledger(raw, p)
    first, second, singles, record = transfer(
        ledger, list(range(p)), list(range(p, 2*p)), [2*p, 2*p+1], 2*p, (2, 3))
    assert record['exceptional_primes'] == [3]
    kept, merged = first[p-r:], first[:p-r]+singles
    ledger.average(merged)
    replay(raw, ledger, [merged, second, kept], p, r)
    return record


def weighted_formulas():
    count = 0
    for p in (5, 7, 11, 13, 17):
        for m in (1, 2):
            for r in range(1, p):
                n = (m+1)*p+r
                for a, z in ((1, 0), (0, 1), (-7, 3), (4, -5)):
                    assert gcd(a, z) == 1
                    y, w = a+p*z, (m+1)*a-r*z
                    values = (a, -m*a+r*z, -p*z)
                    assert gcd(*values) == 1
                    assert gcd(values[0]-values[1], values[0]-values[2]) == gcd(y, n)
                    energy = m*p*values[0]**2+p*values[1]**2+r*values[2]**2
                    assert (m+1)*energy == p*(m*w*w+r*n*z*z)
                    for s in range(min(r, 2)+1):
                        j = (p-s)//2
                        yy, zz = p*p-n*j, p-(m+1)*j-s
                        aa = yy-p*zz
                        assert (p-(m+1)*j-s)*aa+(r*j-p*s)*zz == 0
                        assert gcd(yy, n) == 1
                    count += 1
    return count


def unified_returns():
    count = bad_prime_terminal_checks = 0
    for p in (5, 7, 11, 13):
        for m in (1, 2):
            for r in range(1, p):
                n = (m+1)*p+r
                chart = (0, 1, 1, p)
                for ell in factors(m+1):
                    if n % ell == 0 and r >= ell-1:
                        residues = {(p-s)*pow(p*p, -1, ell) % ell for s in range(ell)}
                        assert residues == set(range(ell))
                        bad_prime_terminal_checks += 1
                for carrier in ('A', 'B'):
                    for s in range(r//m+1):
                        for j in range(p//m+1):
                            i = p-j-s
                            if i < 0 or m*i > m*p-(r if carrier == 'A' else 0):
                                continue
                            if m*j > p-(r if carrier == 'B' else 0):
                                continue
                            matrix = ((p-(m+1)*j-s, r*j-p*s, -1, 0)
                                      if carrier == 'A' else
                                      (p-(m+1)*j-s, r*j-p*s, m, -r))
                            # General returns may be singular; they remain valid maps.
                            transformed = mm(mm(chart, matrix), invq(chart))
                            expected = ((p, -1, n*j, -((m+1)*j+s))
                                        if carrier == 'A' else
                                        (-(m*p+r), m, n*(j-p), (m+1)*p-(m+1)*j-s))
                            assert transformed == expected
                            for a, z in ((1, 0), (0, 1)):
                                raw = [F(a)]*(m*p)+[-m*F(a)+r*z]*p+[-p*F(z)]*r
                                ledger = Ledger(raw, p)
                                groups = [list(range(m*p)), list(range(m*p, (m+1)*p)),
                                          list(range((m+1)*p, n))]
                                if m == 2:
                                    groups = upper_return(ledger, groups, carrier, j, s)
                                else:
                                    aa, bb, cc = [list(g) for g in groups]
                                    if carrier == 'A':
                                        kept, aa = aa[-r:], aa[:-r]
                                    else:
                                        kept, bb = bb[-r:], bb[:-r]
                                    row = aa[:i]+bb[:j]+cc[:s]
                                    other = aa[i:]+bb[j:]+cc[s:]
                                    ledger.average(row)
                                    ledger.average(other)
                                    groups = [row, other, kept]
                                ap = F(matrix[0]*a+matrix[1]*z, p)
                                zp = F(matrix[2]*a+matrix[3]*z, p)
                                expected_values = (ap, -m*ap+r*zp, -p*zp)
                                assert all(ledger.state[index] == value
                                           for group, value in zip(groups, expected_values)
                                           for index in group)
                                ledger.independent_replay(raw)
                                count += 1
    return count, bad_prime_terminal_checks


def scope_obstructions():
    units = {(sign*pow(5, exponent, 24)) % 24 for sign in (-1, 1) for exponent in range(2)}
    assert units == {1, 5, 19, 23} and pow(7, -1, 24) not in units
    assert gcd(7, 24) == 1
    matrix, tangent = (3, 2, 4, 3), (1, 1, 2, 1)
    assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1
    square = mm(matrix, matrix)
    naive = tuple(delta+4*x for delta, x in zip((1, 0, 0, 1), tangent))
    assert tuple(x % 8 for x in square) != tuple(x % 8 for x in naive)
    print('unit-scale and first-dyadic-layer distinctions: PASS 2')


def main():
    rng = Random(2026091429)
    records, old_density_failures, old_gcd_failures, both_failures = [], 0, 0, 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 61):
        for r in range(1, p):
            n = 2*p+r
            primes = tuple(factors(n))
            if r < len(primes):
                continue
            for _ in range(2):
                while True:
                    raw = [rng.randrange(-1000, 1001) for _ in range(n-1)]
                    raw.append(-sum(raw))
                    if gcd(*raw) == 1 and is_legal(raw, primes):
                        break
                records.append(uniform_entry(raw, p, r))
                density_bad = sum((F(1, carrier_period(p, ell)) for ell in primes), F(0)) >= 1
                gcd_bad = gcd(2*p-1, n) != 1
                old_density_failures += density_bad
                old_gcd_failures += gcd_bad
                both_failures += density_bad and gcd_bad
    forced = forced_midpoint()
    assert both_failures and old_density_failures and old_gcd_failures
    weighted = weighted_formulas()
    returns, terminal_checks = unified_returns()
    scope_obstructions()
    print('uniform two-round original-position entries: PASS', len(records))
    print('former density/gcd/both restrictions removed: PASS', old_density_failures, old_gcd_failures, both_failures)
    print('exceptional-prime midpoint repair: PASS', forced)
    print('unified weighted lattice and terminal formulas: PASS', weighted)
    print('unified two-band physical return formulas: PASS', returns)
    print('terminal coverage at block-count primes: PASS', terminal_checks)
    data = {'scope': 'Exact finite checks of the general two-round proof; no general even-core completion claim.',
            'entry_count': len(records), 'old_density_failures': old_density_failures,
            'old_gcd_failures': old_gcd_failures, 'both_old_failures': both_failures,
            'weighted_formula_checks': weighted, 'physical_returns': returns,
            'bad_prime_terminal_checks': terminal_checks,
            'forced_midpoint': forced, 'entries': records}
    (Path(__file__).parent/'uniform_two_block_entry_records.json').write_text(
        json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print('uniform weighted-core entry: PASS')


if __name__ == '__main__':
    main()
