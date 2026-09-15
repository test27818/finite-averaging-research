"""Exact one-return descent audit and a second carrier involution.

Menus enumerate integer row counts for one disjoint partition of the core,
not words or arbitrary rational transport matrices. Integer height auditing
uses the true primitive G condition, allowing cancellable common factors.
"""

from math import gcd, lcm
from fractions import Fraction as F
from pathlib import Path
import json

from verify_four_prime_entry_and_band import Ledger, factors
from verify_upper_band_three_value_reduction import core_state, replay_and_record

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).parent


def norm(p, r, y, z):
    n = 3*p+r
    return 6*y*y-4*n*y*z+n*(2*p+r)*z*z


def menu(p, r):
    n = 3*p+r
    result = []
    for k in range(1, p//2+1):
        result.append(('C', k, 0, (p-3*k, n*k, 0, p)))
    for carrier in ('A', 'B'):
        for s in range(r//2+1):
            for j in range(p//2+1):
                i = p-j-s
                if i < 0 or 2*i > 2*p-(r if carrier == 'A' else 0):
                    continue
                if 2*j > p-(r if carrier == 'B' else 0):
                    continue
                matrix = (-(3*j+s), n*j, -1, p) if carrier == 'A' else (
                    3*p-3*j-s, n*(j-p), 2, -(2*p+r))
                assert matrix[0]*matrix[3]-matrix[1]*matrix[2]
                result.append((carrier, j, s, matrix))
    return result


def primitive(y, z):
    g = gcd(y, z)
    if not g:
        return 0, 0
    y, z = y//g, z//g
    return (-y, -z) if z < 0 or z == 0 and y < 0 else (y, z)


def terminals(p, r):
    n = 3*p+r
    return {primitive(p*p-n*j, p-3*j-s)
            for s in range(r+1) for j in range(p-s+1)}


def apply_return(ledger, groups, carrier, j, s):
    a, b, c = groups
    p, r = ledger.p, len(c)
    i = p-j-s
    if carrier == 'A':
        kept, a = a[-r:], a[:-r]
    elif carrier == 'B':
        kept, b = b[-r:], b[:-r]
    else:
        assert carrier == 'C' and s == 0
        kept, c = c, []
    left = a[:i]+b[:j]+c[:s]
    right = a[i:2*i]+b[j:2*j]+c[s:2*s]
    other = a[2*i:]+b[2*j:]+c[2*s:]
    for g in (left, right, other):
        ledger.average(g)
    return [left+right, other, kept]


def audit(height=40):
    records, total, traps = [], 0, 0
    for p, r in ((5, 1), (7, 1), (11, 1), (13, 1), (7, 4), (11, 4), (13, 6)):
        n, candidates, target = 3*p+r, menu(p, r), terminals(p, r)
        count, frozen, examples = 0, 0, []
        for z in range(height+1):
            for y in range(-height, height+1):
                if gcd(y, z) != 1 or gcd(y, n) != 1 or primitive(y, z) in target:
                    continue
                count += 1
                before = norm(p, r, y, z)
                descending = False
                successor_data = []
                for carrier, j, s, (a, b, c, d) in candidates:
                    yy, zz = primitive(a*y+b*z, c*y+d*z)
                    legal = gcd(yy, n) == 1
                    after = norm(p, r, yy, zz)
                    if legal and (after < before or (yy, zz) in target):
                        descending = True
                        break
                    successor_data.append({'carrier': carrier, 'j': j, 's': s,
                                           'parameters': [yy, zz], 'legal': legal,
                                           'norm': after, 'terminal': (yy, zz) in target})
                if not descending:
                    frozen += 1
                    if len(examples) < 3:
                        examples.append({'y': y, 'z': z, 'norm': before,
                                         'successors': successor_data})
        total += count
        traps += frozen
        records.append({'p': p, 'r': r, 'n': n, 'menu_size': len(candidates),
                        'checked': count, 'traps': frozen, 'examples': examples})
        print('one-return audit:', p, r, len(candidates), count, frozen,
              [(x['y'], x['z']) for x in examples])
    (ROOT/'upper_band_one_return_descent_audit.json').write_text(
        json.dumps({'height': height, 'scope': 'No one-return energy decrease or terminal hit in the explicit disjoint-row family; not a reachability obstruction.',
                    'cases': records}, indent=2)+'\n', encoding='utf-8')
    print('one-return finite descent diagnostic: PASS', total, traps)


def verify_second_involutions():
    checked, capacities = 0, 0
    for p in range(5, 160):
        if factors(p) != {p: 1}:
            continue
        for r in range(1, p):
            n = 3*p+r
            choices = [j for carrier, j, s, matrix in menu(p, r)
                       if carrier == 'A' and p == 3*j+s]
            assert choices or r < 4
            capacities += 1
            if p > 31:
                continue
            for j in choices:
                s = p-3*j
                mu = p*p-n*j
                assert mu and all(mu % q == p*p % q for q in factors(n))
                for y, z in ((1, 0), (1, 1)):
                    raw = core_state(p, r, y, z)
                    ledger = Ledger(raw, p)
                    groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
                    groups = apply_return(ledger, groups, 'A', j, s)
                    yy, zz = F(-p*y+n*j*z, p), F(-y+p*z, p)
                    assert [ledger.state[g[0]] for g in groups] == [yy-p*zz, -2*yy+(2*p+r)*zz, -p*zz]
                    groups = apply_return(ledger, groups, 'A', j, s)
                    scale = F(mu, p*p)
                    assert [ledger.state[g[0]] for g in groups] == [scale*(y-p*z), scale*(-2*y+(2*p+r)*z), -scale*p*z]
                    replay_and_record(raw, ledger, groups, {})
                    checked += 1
    print('second-carrier global involutions: PASS', capacities, checked)


def replay_g(raw, ledger):
    state = list(map(F, raw))
    for group in ledger.word:
        assert len(group) == len(set(group)) == ledger.p
        average = sum(state[i] for i in group)/ledger.p
        for i in group:
            state[i] = average
        assert sum(state) == 0
        denominator = lcm(*(x.denominator for x in state))
        integers = [int(x*denominator) for x in state]
        common = gcd(*integers)
        if common:
            integers = [x//common for x in integers]
            difference = gcd(*(x-integers[0] for x in integers))
            assert all(q == ledger.p for q in factors(difference))
    assert state == ledger.state


def verify_explicit_trap():
    p, r, y, z = 7, 1, 23, 3
    raw, target = core_state(p, r, y, z), terminals(p, r)
    assert raw == [2]*14+[-1]*7+[-21] and norm(p, r, y, z) == 72
    assert primitive(y, z) not in target
    # A group containing -21 has mean at most -9/7, whereas a group
    # without it has mean at least -1. Thus equal rows both omit -21,
    # and their counts of 2 and -1 must coincide. This menu is complete
    # for this input, even allowing state-specific coincidental equalities.
    assert F(-21+6*2, 7) < -1
    successors = []
    for carrier, j, s, (a, b, c, d) in menu(p, r):
        ledger = Ledger(raw, p)
        groups = [list(range(14)), list(range(14, 21)), [21]]
        groups = apply_return(ledger, groups, carrier, j, s)
        yy, zz = F(a*y+b*z, p), F(c*y+d*z, p)
        assert [ledger.state[g[0]] for g in groups] == [yy-p*zz, -2*yy+15*zz, -p*zz]
        ledger.independent_replay(raw)
        yy, zz = primitive(a*y+b*z, c*y+d*z)
        good = gcd(yy, 22) == 1
        energy = 7*norm(p, r, yy, zz)
        assert not good or energy > 504 and (yy, zz) not in target
        if good:
            replay_g(raw, ledger)
        successors.append({'carrier': carrier, 'j': j, 'primitive_yz': [yy, zz],
                           'legal': good, 'energy': energy})
    assert len(successors) == 10
    (ROOT/'upper_band_explicit_core_trap.json').write_text(
        json.dumps({'p': 7, 'n': 22, 'input': list(map(int, raw)), 'energy': 504,
                    'scope': 'All nonidentity returns made from three disjoint seven-groups; excludes overlapping returns and longer words.',
                    'successors': successors}, indent=2)+'\n', encoding='utf-8')
    print('explicit core trap complete disjoint-return audit: PASS', len(successors))


def verify_uniform_escape():
    records = []
    for p in range(5, 500):
        if factors(p) != {p: 1}:
            continue
        raw = [2]*(2*p)+[-1]*p+[-3*p]
        ledger = Ledger(raw, p)
        aa, bb, singleton = list(range(2*p)), list(range(2*p, 3*p)), 3*p
        if p % 3 == 1:
            first_a, first_b, middle = (p-1)//3, 2*(p-1)//3, -3
            second_b = 4*p % 5
            second_d = (2*p-3*second_b)//5
            second_a = (3*p-2*second_b)//5
        else:
            first_a, first_b, middle = (2*p-1)//3, (p-2)//3, -2
            second_a, second_b, second_d = (p-1)//2, 2, (p-3)//2
        first = aa[:first_a]+bb[:first_b]+[singleton]
        ledger.average(first)
        assert ledger.state[first[0]] == middle
        remaining_a, remaining_b = aa[first_a:], bb[first_b:]
        assert 0 <= second_a <= len(remaining_a) and 0 <= second_b <= len(remaining_b)
        assert 0 <= second_d <= p and second_a+second_b+second_d == p
        second = remaining_a[:second_a]+remaining_b[:second_b]+first[:second_d]
        ledger.average(second)
        assert all(ledger.state[i] == 0 for i in second)
        assert all(x.denominator == 1 for x in ledger.state)
        replay_g(raw, ledger)
        records.append({'p': p, 'n': 3*p+1, 'input': raw,
                        'operations': [[i+1 for i in group] for group in ledger.word],
                        'zero_positions': [i+1 for i in second]})
    (ROOT/'upper_band_uniform_two_step_escape.json').write_text(
        json.dumps({'scope': 'Two integer averages create p zeros for (2^(2p),(-1)^p,-3p); completion uses the existing zero-trigger theorem.',
                    'records': records}, indent=2)+'\n', encoding='utf-8')
    print('uniform two-step overlapping integer escape: PASS', len(records))


def verify_fringe():
    p, n = 761, 3045
    assert factors(p) == {p: 1} and n == 4*p+1
    assert factors(n) == {3: 1, 5: 1, 7: 1, 29: 1}
    assert n < 4*p-2+len(factors(n))
    print('upper fringe not covered by previous inequality: PASS', p, n)


if __name__ == '__main__':
    verify_second_involutions()
    audit()
    verify_explicit_trap()
    verify_uniform_escape()
    verify_fringe()
