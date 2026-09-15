"""Exact multiplicity arithmetic for the unit-gap core branch.

The replenishment menu solves two linear equations before checking capacity.
No position subsets or averaging-word tree are enumerated.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

from verify_provenance_dynamic_stages import apply_types

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).resolve().parent


def ceil_div(a, b):
    return -((-a)//b)


def replenishment(p, h, s):
    alpha, t = h*(s-1)+2, s+1
    assert h >= 1 and s >= 1 and h*s < p
    for ell in range(h+1):
        lower = max(ceil_div(ell, s), ceil_div(h*s-ell, t), 0)
        upper = min((alpha+ell)//s, (p-ell)//t)
        if lower <= upper:
            v = lower
            k, u, zeros = s*v-ell, v+ell, p-t*v-ell
            assert k+t*ell-s*u == 0
            assert k+ell+u+zeros == p
            assert 0 <= k <= alpha and 0 <= zeros <= p-h*s
            return k, ell, u, zeros
    return None


def criterion(p, h, s):
    if 2*h >= s+1:
        return True
    return p-h*s >= h+max(0, h-2)


def is_prime(n):
    return n >= 2 and all(n % q for q in range(2, int(n**0.5)+1))


def verify_capacity():
    systems, successes, failures = 0, 0, 0
    for p in range(2, 301):
        for h in range(1, p):
            for s in range(1, (p-1)//h+1):
                answer = replenishment(p, h, s)
                assert (answer is not None) == criterion(p, h, s), (p, h, s, answer)
                systems += 1
                successes += answer is not None
                failures += answer is None
                if answer is None:
                    defect = p-h*s
                    assert h >= 2 and s+1 > 2*h and defect < 2*h-2
                    assert 2*h*h <= h*s < p
    print('unit witness exact capacity criterion: PASS', systems, successes, failures)
    return systems, successes, failures


def core_parameters(p, h, s):
    total = 3*p*(s+1)-(3*h-1)*s
    low = ceil_div(total, 4*p-1)
    high = total//(3*p+1)
    for v in range(max(1, low), high+1):
        if total % v:
            continue
        n = total//v
        r = n-3*p
        a = p*(s+1-v)-h*s
        assert 1 <= r < p and a >= 1
        assert 3*a+s == r*v and r >= 2
        yield r, a, a+s, -p*v


def verify_physical_stages():
    records, exceptional, completed, capacity_obstructions, terminal = [], [], 0, 0, 0
    for p in (q for q in range(5, 102) if is_prime(q)):
        for h in range(1, p):
            for s in range(1, (p-1)//h+1):
                for r, a, b, c in core_parameters(p, h, s):
                    assert gcd(a-b, a-c) == 1
                    if a == 1 or a == s+1:
                        terminal += 1
                        continue
                    solution = replenishment(p, h, s)
                    if solution is None:
                        capacity_obstructions += 1
                        direct = None
                        for nc in range(1, r):
                            nb = -h*nc % p
                            na = p-nb-nc
                            if nb <= h and 0 <= na <= p-h+1:
                                direct = (na, nb, nc)
                                assert (na*a+nb*b+nc*c) % p == 0
                                break
                        exceptional.append({'p': p, 'r': r, 'h': h, 's': s,
                                            'defect': p-h*s, 'initial': [a, b, c],
                                            'direct_preserved_unit_pair': direct})
                        continue
                    raw = [F(a)]*(2*p)+[F(b)]*p+[F(c)]*r
                    raw, first = apply_types(raw, ((a, h-1), (b, p-h), (c, 1)), p)
                    assert first['mean'] == str(a-1)
                    raw, second = apply_types(raw, ((a, p-1-h*s), (a-1, h*s), (c, 1)), p)
                    assert second['mean'] == str(a-s-1)
                    k, ell, u, zeros = solution
                    raw, third = apply_types(raw, ((a, k), (b, ell),
                                                   (a-s-1, u), (a-1, zeros)), p)
                    assert third['mean'] == str(a-1)
                    assert raw.count(a) >= p and raw.count(a-1) >= p
                    completed += 1
                    if len(records) < 12:
                        records.append({'p': p, 'r': r, 'h': h, 's': s,
                                        'initial': [a, b, c],
                                        'trace': [first, second, third],
                                        'final': [[str(x), count] for x, count in sorted(Counter(raw).items())]})
    print('unit witness original-position replenishment stages: PASS',
          completed, capacity_obstructions, terminal)
    return records, exceptional, [completed, capacity_obstructions, terminal]


def target_groups(values, weights, p, target, caps=None):
    """Eliminate the two largest type counts using length and exact sum."""
    caps = list(weights if caps is None else caps)
    pivot = sorted(range(len(values)), key=lambda i: caps[i], reverse=True)[:2]
    a, b = pivot
    others = [i for i in range(len(values)) if i not in pivot]
    counts = [0]*len(values)
    def visit(depth, used, total):
        if depth == len(others):
            rest = p-used
            numerator = p*target-total-rest*values[b]
            delta = values[a]-values[b]
            if numerator % delta:
                return
            ka = numerator//delta
            kb = rest-ka
            if 0 <= ka <= caps[a] and 0 <= kb <= caps[b]:
                counts[a], counts[b] = ka, kb
                yield tuple(counts)
            return
        idx = others[depth]
        for k in range(min(caps[idx], p-used)+1):
            counts[idx] = k
            yield from visit(depth+1, used+k, total+k*values[idx])
    yield from visit(0, 0, 0)


def verify_actual_one_step_obstruction():
    p, r, h, s = 29, 8, 2, 14
    a, b, c, m = 30, 44, -377, 29
    raw = [F(a)]*(2*p)+[F(b)]*p+[F(c)]*r
    raw, first = apply_types(raw, ((a, h-1), (b, p-h), (c, 1)), p)
    assert Counter(raw) == Counter({F(a): 57, F(b): 2, F(c): 7, F(m): 29})
    values, weights = (a, b, c, m), (57, 2, 7, 29)
    assert not list(target_groups(values, weights, p, 0))
    # New adjacent pairs require a new value next to a currently p-heavy value.
    new_pair_groups = []
    for old in (a, m):
        caps = list(weights)
        caps[values.index(old)] -= p
        for target in (old-1, old+1):
            for counts in target_groups(values, weights, p, target, caps):
                if sum(k > 0 for k in counts) > 1:
                    new_pair_groups.append((old, target, counts))
    assert not new_pair_groups
    # Keeping both old heavy values bounds A usage and forbids M usage.
    preserved_pair_candidates = []
    for nb in range(3):
        for nc in range(8):
            na = p-nb-nc
            if 0 <= na <= 28 and (na*a+nb*b+nc*c) % p == 0:
                preserved_pair_candidates.append((na, nb, nc, 0))
    assert not preserved_pair_candidates
    assert replenishment(p, h, s) is None
    raw, second = apply_types(raw, ((a, p-1-h*s), (m, h*s), (c, 1)), p)
    assert Counter(raw) == Counter({F(a): 57, F(b): 2, F(c): 6, F(m): 1, F(15): 29})
    # Outside the new 15-block, differences from 30 are 14^2 and (-1)^7 mod29.
    assert all((14*l-k) % 29 for l in range(3) for k in range(8) if l+k)
    print('actual core unit-heavy one-step obstruction: PASS', p, 3*p+r)
    return {'p': p, 'r': r, 'initial': [a, b, c], 'first': first, 'second': second,
            'blocked_targets': [0, 28, 29, 30, 31],
            'second_state': [[str(v), n] for v, n in sorted(Counter(raw).items())]}


def verify_uniform_unit_pair_obstruction():
    checks, records = 0, []
    for p in (2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 19, 29, 43):
        for r in sorted({1, p//2, p-1, 2*p+1}):
            q = 6*p+1
            c = -3*p-(p+r-1)*q
            values, weights = (1, 2, q, c), (p, p, p+r-1, 1)
            assert sum(v*w for v, w in zip(values, weights)) == 0
            assert (-3*p-r*q) % p != 0
            assert not list(target_groups(values, weights, p, 0))
            for old in (1, 2, q):
                caps = list(weights)
                caps[values.index(old)] -= p
                for target in (old-1, old+1):
                    assert not [counts for counts in target_groups(values, weights, p, target, caps)
                                if sum(k > 0 for k in counts) > 1]
            checks += 1
            if len(records) < 3:
                records.append({'p': p, 'r': r, 'values': values, 'weights': weights})
    print('uniform one-step adjacent-heavy obstruction: PASS', checks)
    return records


def verify_extended_stages(exceptional):
    records, kinds, unresolved = [], Counter(), []
    for entry in exceptional:
        p, r, h, s, d = (entry[key] for key in ('p', 'r', 'h', 's', 'defect'))
        a, b, c = entry['initial']
        m, middle = a-1, a-s-1
        raw = [F(a)]*(2*p)+[F(b)]*p+[F(c)]*r
        raw, first = apply_types(raw, ((a, h-1), (b, p-h), (c, 1)), p)
        trace = [first]
        if d == 1:
            assert r >= h+1 and p-h-3 >= 0
            q = a-(p-1)
            selections = [((m, p-1), (c, 1)),
                          ((a, 1), (middle, p-h), (c, h-1)),
                          ((a, p-h-3), (b, h), (q, 2), (m, 1))]
            kind = 'defect-one-three-step'
        elif h == 3 and d == 2:
            assert r >= 3 and p-9 >= 0
            q = a-2*s+1
            selections = [((a, 1), (m, p-2), (c, 1)),
                          ((a, 5), (middle, p-6), (c, 1)),
                          ((a, p-9), (b, 3), (middle, 2), (q, 2), (m, 2))]
            kind = 'three-types-defect-two'
        elif entry['direct_preserved_unit_pair']:
            ka, kb, kc = entry['direct_preserved_unit_pair']
            selections = [((a, ka), (b, kb), (c, kc))]
            kind = 'direct-preserved-pair'
        else:
            unresolved.append(entry)
            continue
        for selection in selections:
            raw, step = apply_types(raw, selection, p)
            assert all(x.denominator == 1 for x in raw)
            trace.append(step)
        assert raw.count(a) >= p and raw.count(m) >= p
        kinds[kind] += 1
        records.append({**entry, 'kind': kind, 'trace': trace})
    # This is completeness only for the documented finite parameter range.
    assert not unresolved
    print('extended unit witness stages through p101: PASS', dict(kinds))
    return records, dict(kinds)


def verify_29_zero_trigger():
    p = 29
    raw = [F(30)]*58+[F(44)]*29+[F(-377)]*8
    selections = [((30, 1), (44, 27), (-377, 1)),
                  ((29, 28), (-377, 1)),
                  ((30, 1), (15, 27), (-377, 1)),
                  ((30, 9), (44, 1), (29, 1), (-377, 1), (2, 17))]
    trace = []
    for selection in selections:
        raw, step = apply_types(raw, selection, p)
        trace.append(step)
    assert raw.count(0) >= 29
    print('p29 n95 four-step zero trigger: PASS')
    return trace


if __name__ == '__main__':
    capacity = verify_capacity()
    records, exceptional, physical_counts = verify_physical_stages()
    obstruction = verify_actual_one_step_obstruction()
    uniform = verify_uniform_unit_pair_obstruction()
    extended, extended_counts = verify_extended_stages(exceptional)
    zero_29 = verify_29_zero_trigger()
    (ROOT/'unit_witness_replenishment_records.json').write_text(json.dumps({
        'scope': 'Exact two- and three-atom local replenishment stages, not a recursive invariant or a new threshold.',
        'capacity_counts': capacity, 'physical_counts': physical_counts,
        'records': records, 'exceptional_parameters': exceptional,
        'obstruction': obstruction, 'uniform_obstruction': uniform,
        'extended_stages': extended, 'extended_counts': extended_counts,
        'p29_zero_trigger': zero_29}, indent=2)+'\n', encoding='utf-8')
    print('unit witness replenishment and boundary: PASS')
