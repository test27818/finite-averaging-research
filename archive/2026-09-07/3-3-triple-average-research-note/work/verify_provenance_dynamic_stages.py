"""Exact checks for core-successor continuation and arithmetic stage bounds.

Type counts and one modular inverse replace position-subset enumeration.
General claims are proved in the accompanying document, not by these samples.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import argparse
import json

from verify_core_exit_and_potential_scope import core_values, factors, exit_core
from verify_binary_collision_lattice import one_light_move, three_heavy_move

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).resolve().parent


def residue(x, q):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, q) % q


def safe(values, weights, selected, mean):
    live = [x for x, w, s in zip(values, weights, selected) if w > s]
    live.append(mean)
    return all(len({residue(x, q) for x in live}) > 1 for q in factors(sum(weights)))


def replay(values, weights, counts, p):
    assert len(values) == len(weights) == len(counts)
    assert sum(counts) == p and all(0 <= s <= w for s, w in zip(counts, weights))
    raw = [F(x) for x, w in zip(values, weights) for _ in range(w)]
    group, offset = [], 0
    for w, s in zip(weights, counts):
        group.extend(range(offset, offset + s))
        offset += w
    assert len(group) == len(set(group)) == p
    mean = sum(raw[i] for i in group) / p
    after = raw[:]
    for index in group:
        after[index] = mean
    assert sum(after) == sum(raw) == 0
    assert mean.denominator == 1
    assert len({raw[i] for i in group}) > 1
    assert safe(values, weights, counts, mean)
    assert sum(v >= p for v in Counter(after).values()) >= 2
    assert sum(x*x for x in after) < sum(x*x for x in raw)
    return after, {'counts': list(counts), 'mean': int(mean),
                   'positions_1based': [i+1 for i in group]}


def primitive_g(raw):
    denominator = 1
    for x in raw:
        denominator = denominator*x.denominator//gcd(denominator, x.denominator)
    integers = [int(x*denominator) for x in raw]
    content = gcd(*integers)
    if content == 0:
        return 0, 0, integers
    primitive = [x//content for x in integers]
    return gcd(*(x-primitive[0] for x in primitive)), content, primitive


def apply_types(raw, selection, p):
    """Independently choose distinct physical positions with these values."""
    group = []
    for value, count in selection:
        available = [i for i, x in enumerate(raw) if x == value and i not in group]
        assert len(available) >= count
        group.extend(available[:count])
    assert len(group) == len(set(group)) == p
    before = sum(x*x for x in raw)
    mean = sum(raw[i] for i in group)/p
    result = raw[:]
    for index in group:
        result[index] = mean
    assert sum(result) == 0
    assert sum(x*x for x in result) < before
    assert primitive_g(result)[0] == 1 or not any(result)
    return result, {'group_1based': [i+1 for i in group], 'mean': str(mean)}


def verify_provenance_boundaries():
    # Every operation is integer and G=1, but the last state is integer-frozen.
    p, initial = 5, [F(23)]*10 + [F(-48)]*5 + [F(10)]
    raw, trace = initial[:], []
    menu = [((23, 2), (-48, 2), (10, 1)),
            ((-48, 3), (-8, 2)),
            ((-32, 2), (23, 3)),
            ((-32, 2), (23, 3)),
            ((-32, 1), (-8, 1), (1, 2), (23, 1)),
            ((-8, 1), (-3, 2), (1, 1), (23, 1)),
            ((-3, 1), (2, 4))]
    alternate = None
    for index, selection in enumerate(menu):
        if index == 6:
            zero, alternate = apply_types(raw, ((-8, 1), (2, 4)), p)
            assert zero.count(0) >= p
        raw, record = apply_types(raw, selection, p)
        assert all(x.denominator == 1 for x in raw)
        trace.append(record)
    assert Counter(raw) == Counter({F(1): 12, F(-3): 2, F(-8): 1, F(2): 1})
    values = tuple(sorted(Counter(raw)))
    weights = tuple(raw.count(v) for v in values)
    nonconstant_integer = 0
    for counts in count_choices(weights, p):
        total = sum(v*k for v, k in zip(values, counts))
        if total % p == 0 and sum(k > 0 for k in counts) > 1:
            nonconstant_integer += 1
    assert nonconstant_integer == 0
    assert [int((x-1) % p) for x in raw if x != 1] == [1]*4
    # On r=1, the old source equation eliminates to current zero sum exactly.
    rng = Random(2026091410)
    tautologies = 0
    for p in (5, 7, 11, 13, 17, 23):
        for i in range(p):
            a, b = rng.randrange(-1000, 1000), rng.randrange(-1000, 1000)
            m = -F((2*p-i)*a+(i+1)*b, p)
            c = p*m-i*a-(p-1-i)*b
            assert c == -2*p*a-p*b
            tautologies += 1
    print('provenance closure counterexample and r1 elimination: PASS', len(trace), tautologies)
    return {'initial': [int(x) for x in initial], 'trace': trace,
            'frozen': [[int(v), w] for v, w in sorted(Counter(raw).items())],
            'alternate_zero_trigger_before_last_step': alternate}


def verify_fixed_anchor_boundary():
    checks = 0
    for p in (5, 7, 11, 13, 17, 19, 23, 31, 43, 67, 101):
        a, b, c, m = p, -2*p-2, 2*p, p+1
        raw = [F(a)]*(2*p)+[F(b)]*p+[F(c)]
        raw, _ = apply_types(raw, ((a, p-1), (c, 1)), p)
        assert Counter(raw) == Counter({F(a): p+1, F(b): p, F(m): p})
        for k in range(p+1):
            for ell in range(p-k+1):
                rest = p-k-ell
                total = k*b+ell*a+rest*m
                assert total != 0
                if total % p == 0 and sum(x > 0 for x in (k, ell, rest)) > 1:
                    assert k > 0 and total//p != b
        checks += 1
    print('uniform fixed-heavy-anchor obstruction: PASS', checks)
    return checks


def verify_arithmetic_stages():
    # A raw all-zero residue is not necessarily a normalized G obstruction.
    raw = [F(-9)]*10+[F(24)]*5+[F(-10)]*3
    after, record = apply_types(raw, ((-9, 1), (24, 1), (-10, 3)), 5)
    assert all(x % 3 == 0 for x in after)
    difference_g, content, primitive = primitive_g(after)
    assert content == 3 and difference_g == 1
    assert Counter(primitive) == Counter({-3: 9, 8: 4, -1: 5})

    # A safe five-atom fractional excursion that returns to the same integer lattice.
    stages = []
    for p in (3, 5, 7, 11, 13, 17, 23, 31, 43):
        raw = [F(1)]*(p-1)+[F(2)]+[F(1)]*(p-1)+[F(0)]+[F(1)]*p+[F(-3*p-2), F(2)]
        initial_energy, trace = sum(x*x for x in raw), []
        raw, step = apply_types(raw, ((1, p-1), (2, 1)), p)
        trace.append(step)
        raw, step = apply_types(raw, ((1, p-1), (0, 1)), p)
        trace.append(step)
        u, v, half = F(p+1, p), F(p-1, p), (p-1)//2
        for selection in (((u, half), (v, half), (1, 1)),
                          ((u, half), (v, half), (1, 1)),
                          ((u, 1), (v, 1), (1, p-2))):
            raw, step = apply_types(raw, selection, p)
            trace.append(step)
        assert all(x.denominator == 1 for x in raw)
        assert sum(x*x for x in raw) == initial_energy-2
        stages.append({'p': p, 'trace': trace, 'energy_drop': 2})

    # With original A,C retained, clearing a genuine denominator has content 1.
    floor_checks, distance_checks = 0, 0
    for p in (5, 7, 11, 13, 17, 23, 31, 43, 67, 101):
        for r in range(1, p):
            a, b, c = core_values(p, r, 1, 1)
            assert gcd(a, c) == 1
            initial_energy = 2*p*a*a+p*b*b+r*c*c
            assert p*p*(a*a+c*c) > initial_energy
            floor_checks += 1
        n, free, total = 3*p+1, 3*p-1, p*(2*p-1)
        rem = total % free
        initial_phi = p*(n*(2*p+1)-6*p)
        continuous_floor = p*(1+n*(2*p-1))
        assert initial_phi-continuous_floor == p
        assert continuous_floor+rem*(free-rem) > initial_phi
        assert p*p*(1+n*(2*p-1)) > initial_phi
        k = p//3
        expected = (5*k+1)*(4*k+1) if p % 3 == 1 else (2*k+1)*(7*k+4)
        assert rem*(free-rem) == expected > p
        distance_checks += 1
    # Two disjoint fractional packets followed by two complementary integer groups
    # would need a==b and a+b==0 mod p, impossible for nonzero residues at odd p.
    four_step_checks = 0
    for p in (3, 5, 7, 11, 13, 17, 23):
        for a in range(1, p):
            for b in range(1, p):
                for k in range(1, p):
                    assert not ((k*a+(p-k)*b) % p == 0 and (a+b) % p == 0)
                    four_step_checks += 1
    print('normalization-aware protection and five-step returns: PASS', len(stages), content)
    print('anchored denominator floor and four-step obstruction: PASS', floor_checks, four_step_checks)
    print('anchored integer pair-distance obstruction at r1: PASS', distance_checks)
    return {'raw_collapse_safe_step': record, 'raw_content': content,
            'five_step_returns': stages, 'anchor_floor_checks': floor_checks,
            'four_step_residue_checks': four_step_checks,
            'pair_distance_floor_checks': distance_checks}


def successor_move(p, r, a, b, c, i):
    """r>=2 single-carrier successor; use the proof's O(p) menu."""
    assert 2 <= r < p and 0 <= i < p
    j, alpha = p - 1 - i, p - i
    m = F(i*a + j*b + c, p)
    assert m.denominator == 1 and len({a, b, m}) == 3
    m = int(m)
    values, weights = (a, b, c, m), (2*p-i, i+1, r-1, p)
    if (a-m) % p == 0:
        return values, weights, (1, 0, 0, p-1), 'congruent-A-M'
    if i == p-1:
        if (b-m) % p == 0:
            for k in (1, 2):
                counts = (0, k, 0, p-k)
                if sum(v*s for v, s in zip(values, counts)) != p*a:
                    return values, weights, counts, 'three-heavy-congruent'
        else:
            inv = pow(b-m, -1, p)
            for carrier, slot in ((a, 0), (c, 2)):
                k = -(carrier-m)*inv % p
                counts = [0, k, 0, p-1-k]
                counts[slot] = 1
                if sum(v*s for v, s in zip(values, counts)) != p*a:
                    return values, weights, tuple(counts), 'three-heavy-carrier'
        raise AssertionError('Two carrier collision equations cannot both hold.')
    inv = pow(a-m, -1, p)
    t = F(b-m, a-m)
    for ell in range(1, i+2):
        k = -ell*(b-m)*inv % p
        if k <= alpha and k+ell <= p:
            counts = (k, ell, 0, p-k-ell)
            if sum(v*s for v, s in zip(values, counts)) != p*a:
                return values, weights, counts, 'reservoir-noncollision'
    assert t.denominator == 1 and 2 <= t <= p
    assert (i+1)*(t-1) < p
    assert abs(a-m) == 1
    for ell in range(i+1):
        k = -((c-m)+ell*(b-m))*inv % p
        if k <= alpha and k+ell <= p-1:
            counts = (k, ell, 1, p-k-ell-1)
            assert sum(v*s for v, s in zip(values, counts)) != p*a
            return values, weights, counts, 'unit-gap-carrier'
    raise AssertionError('The two residue intervals must intersect twice.')


def danger_supports(values, weights):
    n, p = sum(weights), weights[-1]
    result = {}
    for q in factors(n):
        buckets = Counter()
        for value, weight in zip(values, weights):
            buckets[residue(value, q)] += weight
        for dominant, weight in buckets.items():
            if weight >= n-p:
                result[q] = [k for k, (x, w) in enumerate(zip(values, weights))
                             if w and residue(x, q) != dominant]
    return result


def verify_continuations():
    rng, records, modes = Random(2026091409), [], Counter()
    for p in (5, 7, 11, 13, 17, 19, 23, 31, 43):
        for r in range(2, p):
            n = 3*p+r
            for _ in range(20):
                while True:
                    y, z = rng.randrange(-10**8, 10**8), rng.randrange(-10**8, 10**8)
                    if gcd(y, z) == gcd(y, n) == 1:
                        break
                a, b, c = core_values(p, r, y, z)
                first = exit_core(p, r, (a, b, c))
                i, j, s = first['type_counts']
                if s == 0:
                    m = first['new_value']
                    values, weights = (a, b, c, m), (p+1, p-1, r, p)
                    counts, mode = (1, p-1, 0, 0), 'congruent-original'
                else:
                    values, weights, counts, mode = successor_move(p, r, a, b, c, i)
                _, second = replay(values, weights, counts, p)
                modes[mode] += 1
                if modes[mode] <= 3:
                    records.append({'p': p, 'r': r, 'initial': [a, b, c],
                                    'first': first, 'second': second, 'mode': mode})
    # Small parameters deliberately exercise the all-collision exceptional case.
    for p in (5, 7, 11, 13, 17, 19, 23, 31):
        for r in range(2, p):
            for y in range(1, 8):
                if gcd(y, 3*p+r) != 1:
                    continue
                for z in range(-3, 4):
                    if gcd(y, z) != 1:
                        continue
                    a, b, c = core_values(p, r, y, z)
                    if (a-b) % p == 0:
                        continue
                    i = -(c-b)*pow(a-b, -1, p) % p
                    values, weights, counts, mode = successor_move(p, r, a, b, c, i)
                    _, second = replay(values, weights, counts, p)
                    modes[mode] += 1
                    if modes[mode] <= 3:
                        records.append({'p': p, 'r': r, 'initial': [a, b, c],
                                        'i': i, 'second': second, 'mode': mode})
    p, r, a, b, c, i = 7, 5, 4, 7, -21, 0
    values, weights, counts, mode = successor_move(p, r, a, b, c, i)
    assert values[-1] == 3 and mode == 'unit-gap-carrier'
    _, second = replay(values, weights, counts, p)
    assert second['mean'] == 0
    modes[mode] += 1
    records.append({'p': p, 'r': r, 'initial': [a, b, c],
                    'i': i, 'second': second, 'mode': mode})
    assert modes['unit-gap-carrier'] > 0
    print('core successor second integer step: PASS', sum(modes.values()), dict(modes))
    return records, dict(modes)


def verify_protection():
    checks = 0
    for p in (5, 7, 11, 13, 17, 19):
        for r in range(1, p):
            for y in range(1, 7):
                if gcd(y, 3*p+r) != 1:
                    continue
                for z in range(-2, 3):
                    if gcd(y, z) != 1:
                        continue
                    a, b, c = core_values(p, r, y, z)
                    if (a-b) % p == 0:
                        m = ((p-1)*a+b)//p
                        values, weights = (a, b, c, m), (p+1, p-1, r, p)
                        expected = {3: [2]} if r % 3 == 0 else {}
                    else:
                        i = -(c-b)*pow(a-b, -1, p) % p
                        m = (i*a+(p-1-i)*b+c)//p
                        assert gcd(a-m, 3*p+r) == gcd(3*(p-i)-2, 3*p+r)
                        values, weights = (a, b, c, m), (2*p-i, i+1, r-1, p)
                        expected = {q: ([1, 2] if r > 1 else [1])
                                    for q in factors(3*p+r)
                                    if (a-m) % q == 0 and i+r <= p}
                    assert danger_supports(values, weights) == expected
                    checks += 1
    print('successor common danger support: PASS', checks)
    return checks


def verify_r1_continuations():
    rng, checks = Random(2026091411), 0
    for p in (5, 7, 11, 13, 17, 19, 23, 31, 43):
        for _ in range(40):
            while True:
                y, z = rng.randrange(-10**7, 10**7), rng.randrange(-10**7, 10**7)
                if gcd(y, z) == gcd(y, 3*p+1) == 1:
                    break
            a, b, c = core_values(p, 1, y, z)
            first = exit_core(p, 1, (a, b, c))
            i, j, carrier = first['type_counts']
            m = first['new_value']
            if carrier == 0:
                values, weights = (a, b, c, m), (p+1, p-1, 1, p)
                counts = (1, p-1, 0, 0)
            else:
                values, weights = (a, b, c, m), (2*p-i, i+1, 0, p)
                if m == 0:
                    continue
                if (a-m) % p == 0:
                    counts = (1, 0, 0, p-1)
                elif i <= 1:
                    k = -(b-m)*pow(a-m, -1, p) % p
                    counts = (k, 1, 0, p-k-1)
                elif i <= p-2:
                    (k, s, ell), _, _ = one_light_move(p, 1, p-i, (a, m, b))
                    counts = (k, ell, 0, s)
                else:
                    triple_counts, _, _ = three_heavy_move(p, 1, (a, b, m), (1, 0, 0))
                    k, ell, s = triple_counts
                    counts = (k, ell, 0, s)
            replay(values, weights, counts, p)
            checks += 1
    print('r1 successor second integer step: PASS', checks)
    return checks


def count_choices(weights, p):
    """Compressed multiplicity choices, used only for short diagnostic policies."""
    if len(weights) == 1:
        if 0 <= p <= weights[0]:
            yield (p,)
        return
    for k in range(max(0, p-sum(weights[1:])), min(weights[0], p)+1):
        for rest in count_choices(weights[1:], p-k):
            yield (k,)+rest


def greedy_probe():
    # This is a bounded deterministic policy, not a branching word search.
    for p in (5, 7, 11, 13):
        for r in (1, 2):
            for y in range(1, 15):
                if gcd(y, 3*p+r) != 1:
                    continue
                for z in range(-3, 4):
                    if gcd(y, z) != 1:
                        continue
                    a, b, c = core_values(p, r, y, z)
                    state = Counter({a: 2*p, b: p, c: r})
                    path = []
                    for step in range(16):
                        if state.get(0, 0) >= p:
                            break
                        values = tuple(sorted(state))
                        weights = tuple(state[v] for v in values)
                        best = None
                        for counts in count_choices(weights, p):
                            total = sum(v*k for v, k in zip(values, counts))
                            if total % p:
                                continue
                            mean = total//p
                            loss = sum(k*(v-mean)**2 for v, k in zip(values, counts))
                            if not loss or not safe(values, weights, counts, mean):
                                continue
                            after = state.copy()
                            for v, k in zip(values, counts):
                                after[v] -= k
                            after[mean] += p
                            after = +after
                            score = (after[mean], loss, -len(after))
                            if best is None or score > best[0]:
                                best = (score, after, counts, mean)
                        if best is None:
                            report = {'p': p, 'r': r, 'initial': [a, b, c],
                                      'steps': path, 'frozen': sorted(state.items())}
                            print(json.dumps(report))
                            return report
                        _, state, counts, mean = best
                        path.append({'values': list(values), 'weights': list(weights),
                                     'counts': list(counts), 'mean': mean})
    print('No frozen endpoint in the bounded deterministic policy probe.')
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--probe', action='store_true')
    args = parser.parse_args()
    if args.probe:
        greedy_probe()
    else:
        records, modes = verify_continuations()
        r1_checks = verify_r1_continuations()
        protection = verify_protection()
        boundaries = verify_provenance_boundaries()
        fixed_anchor = verify_fixed_anchor_boundary()
        arithmetic = verify_arithmetic_stages()
        (ROOT/'provenance_dynamic_stages_records.json').write_text(json.dumps({
            'scope': 'Second core-successor steps and exact danger supports; recursive closure is not proved.',
            'records': records, 'modes': modes, 'protection_checks': protection,
            'r1_continuation_checks': r1_checks,
            'provenance_boundary': boundaries, 'fixed_anchor_checks': fixed_anchor,
            'arithmetic_stages': arithmetic}, indent=2)+'\n', encoding='utf-8')
        print('provenance and dynamic stages: PASS')
