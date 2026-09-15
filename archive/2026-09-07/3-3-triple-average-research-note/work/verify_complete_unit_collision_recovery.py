"""Complete the critical arithmetic branches of local unit-pair recovery.

The construction uses a modular inverse or at most 2h residue trials.
Every path is replayed with an O(n+p) original-position integer ledger.
This does not assert recursive closure of the output configurations.
"""
from collections import Counter
from math import gcd
from pathlib import Path
import json

from verify_unit_witness_replenishment import core_parameters
from verify_euclidean_witness_transfer import (
    Ledger, critical_parameters, direct_pair, lower_defect_counts,
    short_positive_remainder, upper_defect_counts,
)

ROOT = Path(__file__).resolve().parent
if not __debug__:
    raise RuntimeError('Assertions are required.')


def ceil_div(a, b):
    return (a+b-1)//b


def negative_inverse_carrier(p, h, s, d):
    e, t = h-d, s+1
    eta = -pow(t, -1, e) % e
    assert e >= 2 and 2*d*eta < e and 3*d < h
    inverse = (eta*p+h)//e
    assert inverse*t % p == 1
    stride = d*inverse
    limit = (p-d)//2
    assert 0 < stride <= limit
    carriers = ceil_div(p-d-limit, stride)
    count_p = p-d-stride*carriers
    assert 1 <= carriers < h and h < count_p <= limit
    first = (p-e-count_p-carriers, e, 0, count_p, carriers)
    second = (p-d-count_p-carriers, 0, 0, count_p+d, carriers)
    assert all(x >= 0 for x in first+second)
    assert sum(first) == sum(second) == p
    stock = (2*p+2-h-d, h, d, p)
    assert all(x+y <= cap for x, y, cap in zip(first[:4], second[:4], stock))
    return first, second, carriers, eta


def overlapped_negative_unit(p, h, s):
    d, t = h-1, s+1
    assert h >= 4 and s >= 2*h and p == h*t-1
    modulus = h*h-2
    keep_a = (h*h-h-2)//2
    p_cap = (h*h-2*h+2)//2
    b_cap = h//2
    top = p_cap+d*b_cap
    start = ceil_div(modulus*keep_a, p)
    end = modulus//2-1
    trials = modulus-top
    assert gcd(p, modulus) == 1 and end-start+1 >= trials >= 1
    chosen = None
    for index in range(start, start+trials):
        residue = -index*p % modulus
        if residue <= top:
            b_count = min(b_cap, residue//d)
            p_count = residue-d*b_count
            q_count = (index*p+residue)//modulus
            a_count = p-q_count-p_count-b_count
            chosen = (a_count, b_count, p_count, q_count, index, residue)
            break
    assert chosen is not None
    a_count, b_count, p_count, q_count, index, residue = chosen
    trade = 2*h-2
    assert 0 <= p_count <= p_cap and 0 <= b_count <= b_cap
    assert keep_a <= q_count <= (p-1)//2
    assert trade <= a_count <= p-keep_a
    overlap = (h*d-1, p-h*d, 1)  # A, P, C
    first = (a_count, b_count, 0, p_count, q_count)  # A, B, M, P, Q
    second = (a_count-trade, b_count, d, p_count+h-2, q_count+1)
    stock = (2*p+4-h-h*h, h, d, h*d, p)
    assert all(x >= 0 for x in first+second+overlap)
    assert sum(overlap) == sum(first) == sum(second) == p
    assert all(x+y <= cap for x, y, cap in zip(first, second, stock))
    gap_q = 2*t-h
    loss1 = t*p_count+gap_q*q_count-s*b_count
    assert loss1 > 0 and loss1 % p == 0
    loss2 = t*(p_count+h-2)+gap_q*(q_count+1)+d-s*b_count
    assert loss2-loss1 == p
    return overlap, first, second, {
        'modulus': modulus, 'start': start, 'end': end, 'max_trials': trials,
        'chosen_index': index, 'chosen_residue': residue, 'gap_q': gap_q,
        'first_mean_loss': loss1//p,
    }


def verify_all():
    systems, branches = Counter(), Counter()
    records = []
    old_keys = set()
    resolved_keys = set()
    no_disjoint_examples = []
    for p, h, s, d in critical_parameters(1000):
        e = h-d
        data = None
        if d > h:
            kind = 'upper-defect'
            first, second = upper_defect_counts(p, h, s, d)
        elif e >= 2 and short_positive_remainder(e, s+1, d):
            kind = 'short-positive-remainder'
            first, second, _, _, _, _ = lower_defect_counts(p, h, s, d)
        elif e >= 2:
            kind = 'negative-inverse-carrier'
            first, second, needed_carriers, eta = negative_inverse_carrier(p, h, s, d)
        elif h >= 4:
            kind = 'overlapped-negative-unit'
            overlap, first, second, data = overlapped_negative_unit(p, h, s)
        elif h == 2:
            kind = 'h2-defect1'
        else:
            assert h == 3 and d == 2
            kind = 'h3-defect2'
        systems[kind] += 1
        for r, a, b, c in core_parameters(p, h, s):
            assert a >= p+d and r >= 3*h+2
            key = p, r, h, s, d
            previously_covered = (
                d > h or
                (e >= 2 and short_positive_remainder(e, s+1, d)) or
                d == 1 or (h == 3 and d == 2) or direct_pair(p, r, h)
            )
            if not previously_covered:
                old_keys.add(key)
            m, old_p = a-1, a-s-1
            ledger = Ledger(p, (a, b, c), (2*p, p, r))
            assert ledger.average(((a, h-1), (b, p-h), (c, 1)))[0] == m
            assert ledger.average(((a, d-1), (m, p-d), (c, 1)))[0] == old_p
            if kind in ('upper-defect', 'short-positive-remainder'):
                values = (a, b, m, old_p)
                left, labels1 = ledger.average(tuple(zip(values, first)))
                right, labels2 = ledger.average(tuple(zip(values, second)))
                assert labels1.isdisjoint(labels2)
                pair = left, right
            elif kind == 'negative-inverse-carrier':
                assert 2*needed_carriers <= r-2
                values = (a, b, m, old_p, c)
                left, labels1 = ledger.average(tuple(zip(values, first)))
                right, labels2 = ledger.average(tuple(zip(values, second)))
                assert labels1.isdisjoint(labels2)
                pair = left, right
            elif kind == 'overlapped-negative-unit':
                if h*d*r < p:
                    no_disjoint_examples.append({'p': p, 'r': r, 'h': h, 's': s, 'budget': h*d*r})
                q, overlap_labels = ledger.average(((a, overlap[0]), (old_p, overlap[1]), (c, 1)))
                assert q == a-(2*(s+1)-h)
                values = (a, b, m, old_p, q)
                left, labels1 = ledger.average(tuple(zip(values, first)))
                right, labels2 = ledger.average(tuple(zip(values, second)))
                assert labels1.isdisjoint(labels2)
                assert overlap_labels & labels1 and overlap_labels & labels2
                pair = left, right
            elif kind == 'h2-defect1':
                q = a-(p-1)
                assert ledger.average(((a, 1), (old_p, p-h), (c, h-1)))[0] == q
                assert ledger.average(((a, p-h-3), (b, h), (q, 2), (m, 1)))[0] == m
                pair = a, m
            else:
                q = a-2*s+1
                assert ledger.average(((a, 5), (old_p, p-6), (c, 1)))[0] == q
                assert ledger.average(((a, p-9), (b, 3), (old_p, 2), (q, 2), (m, 2)))[0] == m
                pair = a, m
            assert abs(pair[0]-pair[1]) == 1
            assert all(ledger.count(value) >= p for value in pair)
            assert 0 < min(pair) and max(pair) <= a
            assert len(ledger.trace) <= 5
            if key in old_keys:
                resolved_keys.add(key)
            branches[kind] += 1
            if sum(item['branch'] == kind for item in records) < 2 or key in old_keys:
                records.append({'branch': kind, 'p': p, 'r': r, 'h': h, 's': s, 'd': d,
                                'initial': [a, b, c], 'pair': pair, 'geometry': data,
                                'trace': ledger.trace, 'previously_uncovered': key in old_keys})
    assert resolved_keys == old_keys
    assert any(x['p'] == 983 and x['r'] == 50 and x['budget'] == 600 for x in no_disjoint_examples)
    print('uniform critical recovery count systems: PASS', dict(systems))
    print('uniform critical original-position recoveries: PASS', sum(branches.values()), dict(branches))
    print('previous critical menu gaps recovered: PASS', len(resolved_keys))
    print('verified shortage of disjoint integer groups: PASS', len(no_disjoint_examples))
    return {'scope': 'Uniform local recovery after the prescribed carrier step; recursive output closure remains open.',
            'count_systems': dict(systems), 'physical_branches': dict(branches),
            'previous_menu_gaps_recovered': len(resolved_keys), 'records': records,
            'no_disjoint_group_examples': no_disjoint_examples}


if __name__ == '__main__':
    result = verify_all()
    (ROOT/'complete_unit_collision_recovery_records.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('complete local unit-collision recovery: PASS')
