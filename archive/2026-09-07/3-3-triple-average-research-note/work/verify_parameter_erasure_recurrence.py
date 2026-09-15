"""Five-atom parameter erasure and an exact nonterminating recurrence.

Groups are fixed by original-position labels. The recurrence changes only
the mathematical normalization; the physical ledger uses averaging alone.
No averaging-word search is performed.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger
from verify_provenance_dynamic_stages import primitive_g
from verify_unit_witness_replenishment import target_groups

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).resolve().parent


def plan(p, r, a_ids, m_ids, other_ids, outside_a, split=None, retained_preference=None):
    assert len(a_ids) == len(m_ids) == p and len(other_ids) == p+r
    assert r <= outside_a <= p
    outside_m = p+r-outside_a
    a_out, m_out = a_ids[:outside_a], m_ids[:outside_m]
    active = a_ids[outside_a:]+m_ids[outside_m:]+other_ids
    assert len(active) == len(set(active)) == 2*p
    u_ids, v_ids = (active[:p], active[p:]) if split is None else split
    assert set(u_ids+v_ids) == set(active) and len(u_ids) == len(v_ids) == p
    half = (p-1)//2
    first_anchor, second_anchor = a_out[-1], m_out[-1]
    a_left, m_left = a_out[:-1], m_out[:-1]
    u_new = u_ids[:half]+v_ids[:half]+[first_anchor]
    v_new = u_ids[half:p-1]+v_ids[half:p-1]+[second_anchor]
    retain_a = retained_preference == 'A' or (retained_preference is None and outside_a == p)
    if not retain_a:
        assert outside_a < p
        fill_a, fill_m = a_left, m_left[:p-1-outside_a]
        remaining = m_left[p-1-outside_a:]
        retained_value = 'M'
    else:
        assert outside_a >= r+1
        fill_a, fill_m = a_left[:outside_a-r-1], m_left
        remaining = a_left[outside_a-r-1:]
        retained_value = 'A'
    third = [u_ids[-1], v_ids[-1]]+fill_a+fill_m
    word = [u_ids, v_ids, u_new, v_new, third]
    assert all(len(group) == len(set(group)) == p for group in word)
    assert len(remaining) == r
    assert len(set(u_new+v_new+third+remaining)) == 3*p+r
    return word, (u_new, v_new, third, remaining), retained_value


def run_word(ledger, word, require_nonzero=False):
    means, losses = [], []
    for group in word:
        before = sum(x*x for x in ledger.state)
        ledger.average(group)
        after = sum(x*x for x in ledger.state)
        assert after <= before
        assert sum(ledger.state) == 0
        assert primitive_g(ledger.state)[0] == 1
        if require_nonzero:
            assert after < before and all(ledger.state)
        means.append(ledger.state[group[0]])
        losses.append(before-after)
    assert sum(losses) > 0
    return means, losses


def verify_erasure():
    rng, cases, one_digit, two_digits = Random(2026091420), 0, 0, 0
    examples = []
    for p in (3, 5, 7, 11, 13, 17, 23):
        for r in range(1, p):
            for k in sorted({r, p, (p+r)//2}):
                a = rng.randrange(2, 10000)
                m = a-1
                other = [rng.randrange(-10000, 10000) for _ in range(p+r-1)]
                other.append(-p*(a+m)-sum(other))
                raw = [a]*p+[m]*p+other
                ids = list(range(3*p+r))
                word, blocks, retained = plan(p, r, ids[:p], ids[p:2*p], ids[2*p:], k)
                ledger = Ledger(raw, p)
                means, _ = run_word(ledger, word)
                scalar = -F((p+r)*m+k, p)
                u = (F((p-1)//2)*scalar+a)/p
                v = u-F(1, p)
                outside = a if retained == 'A' else m
                w = -u-v-F(r*outside, p)
                for block, expected in zip(blocks, (u, v, w, F(outside))):
                    assert all(ledger.state[i] == expected for i in block)
                assert u-v == F(1, p)
                denominator = lcm(*(x.denominator for x in ledger.state))
                expected_depth = p if scalar.denominator == 1 else p*p
                assert denominator == expected_depth
                one_digit += denominator == p
                two_digits += denominator == p*p
                ledger.independent_replay(raw)
                cases += 1
                if len(examples) < 4:
                    examples.append({'p': p, 'r': r, 'A': a, 'outside_A': k,
                                     'means': list(map(str, means)), 'denominator': denominator,
                                     'word_1based': [[i+1 for i in group] for group in word]})
    print('five-atom parameter erasure: PASS', cases, one_digit, two_digits)
    return examples, [cases, one_digit, two_digits]


def verify_source_kernel():
    checks = 0
    for p in (3, 5, 7, 11):
        for r in sorted({1, p-1}):
            n = 3*p+r
            ids = list(range(n))
            for k in sorted({r, p}):
                word, _, _ = plan(p, r, ids[:p], ids[p:2*p], ids[2*p:], k)
                # Each basis column moves two arbitrary light entries in
                # opposite directions while fixing both repeated sources.
                for position in range(2*p, n-1):
                    basis = [F(0)]*n
                    basis[position], basis[-1] = F(1), F(-1)
                    ledger = Ledger(basis, p)
                    for group in word:
                        ledger.average(group)
                    assert not any(ledger.state)
                    checks += 1
    print('all light-source directions annihilated: PASS', checks)
    return checks


def verify_recurrent_policy():
    records, cycles = [], 0
    for p in (5, 7, 11, 13, 19, 31):
        half = (p-1)//2
        coefficient = p*(half-1)+half
        a, carrier = 4*p*coefficient-(half-1), 4*p*p-1
        assert a > p*p*(p-2)
        z = carrier+1-2*a
        raw = [a]*p+[a-1]*p+[z]*p+[-p*carrier]
        ledger = Ledger(raw, p)
        ids = list(range(3*p+1))
        a_ids, m_ids, z_ids, c_ids = ids[:p], ids[p:2*p], ids[2*p:3*p], ids[3*p:]
        scale, trace = F(1), []
        initial_a = a
        for cycle in range(20):
            assert 1 <= carrier <= 2*a-2
            rho = p*a-coefficient*carrier
            assert abs(rho) <= half*(p-1)
            assert not list(target_groups((a, a-1, z, -p*carrier), (p, p, p, 1), p, 0))
            quotient = (a+p-1)//p
            outside_a = p*quotient-a+1
            active_positive = a_ids[outside_a:]+m_ids[p+1-outside_a:]
            assert len(active_positive) == p-1
            split = (active_positive+[z_ids[0]], z_ids[1:]+c_ids)
            preference = 'A' if outside_a >= 2 and cycle % 2 else None
            word, blocks, retained = plan(p, 1, a_ids, m_ids, z_ids+c_ids, outside_a, split, preference)
            means, losses = run_word(ledger, word, require_nonzero=True)
            new_a = (half-1)*(a-1)+half*quotient
            new_carrier = a if retained == 'A' else a-1
            assert new_a > a and 2*new_a < p*a
            next_scale = -scale/p
            new_z = new_carrier+1-2*new_a
            u_ids, v_ids, third_ids, leftover = blocks
            a_ids, m_ids, z_ids, c_ids = v_ids, u_ids, third_ids, leftover
            expected = (new_a, new_a-1, new_z, -p*new_carrier)
            for block, value in zip((a_ids, m_ids, z_ids, c_ids), expected):
                assert all(ledger.state[i] == next_scale*value for i in block)
            assert lcm(*(x.denominator for x in ledger.state)) == p**(cycle+1)
            assert max(abs(x) for x in ledger.state) < F(2*p*initial_a, 2**(cycle+1))
            if cycle < 3:
                trace.append({'A': a, 'E': carrier, 'next_A': new_a, 'next_E': new_carrier,
                              'normalization': str(next_scale), 'means': list(map(str, means)),
                              'word_1based': [[i+1 for i in group] for group in word]})
            a, carrier, z, scale = new_a, new_carrier, new_z, next_scale
            cycles += 1
        ledger.independent_replay(raw)
        records.append({'p': p, 'initial_A': initial_a, 'cycles': 20,
                        'final_A': a, 'physical_denominator': str(p**20), 'first_cycles': trace})
    print('closed nonterminating recurrence: PASS', cycles)
    return records, cycles


def verify_zero_subset_coefficient():
    checks = 0
    for p in (5, 7, 11, 13, 19, 31, 43, 67):
        half = (p-1)//2
        coefficient = p*(half-1)+half
        for c in range(p+1):
            for singleton in (0, 1):
                if c+singleton > p:
                    continue
                leading = coefficient*(p-3*c-singleton)+p*(c-p*singleton)
                assert leading != 0
                checks += 1
        assert p*(half*(p-1)+coefficient) == p*p*(p-2)
    print('checkpoint zero-subset exclusion coefficients: PASS', checks)
    return checks


def verify_ternary_contraction():
    cases, total_cycles, records = 0, 0, []
    p = 3
    for initial_a in (2, 3, 4, 10, 28, 100, 1000, 3**12+17):
        a = initial_a
        other = [-a, 2*a+7, -3*a-1, -4*a-3]
        raw = [a]*p+[a-1]*p+other
        assert sum(raw) == 0
        ledger = Ledger(raw, p)
        a_ids, m_ids, other_ids = list(range(p)), list(range(p, 2*p)), list(range(2*p, 10))
        scale, cycles = F(1), 0
        while a > 1:
            quotient = (a+2)//3
            k = 3*quotient-a+1
            word, blocks, _ = plan(p, 1, a_ids, m_ids, other_ids, k)
            run_word(ledger, word)
            next_scale = -scale/3
            u_ids, v_ids, third, leftover = blocks
            assert all(ledger.state[i] == next_scale*quotient for i in v_ids)
            assert all(ledger.state[i] == next_scale*(quotient-1) for i in u_ids)
            assert all((x/next_scale).denominator == 1 for x in ledger.state)
            assert quotient < a
            a_ids, m_ids, other_ids = v_ids, u_ids, third+leftover
            a, scale = quotient, next_scale
            cycles += 1
        expected = 0
        while 3**expected < initial_a:
            expected += 1
        assert cycles == expected and ledger.state.count(0) >= 3
        ledger.independent_replay(raw)
        records.append({'initial_A': initial_a, 'cycles': cycles, 'averages': 5*cycles})
        cases += 1
        total_cycles += cycles
    print('ternary unit-pair contraction to zero trigger: PASS', cases, total_cycles)
    return records


def verify_recovery_output_integration():
    p, r, a = 983, 50, 3899
    m = a-1
    # This is the exact multiset produced by the earlier five-atom recovery.
    raw = [a]*p+[m]*p+[3935]*146+[3447]*840+[-236903]*47
    assert len(raw) == 3*p+r and sum(raw) == 0
    outside_a = (-r*m) % p or p
    assert outside_a == 717 and r <= outside_a <= p
    ids = list(range(len(raw)))
    word, blocks, retained = plan(p, r, ids[:p], ids[p:2*p], ids[2*p:], outside_a)
    ledger = Ledger(raw, p)
    means, _ = run_word(ledger, word)
    assert retained == 'M'
    expected = (F(-2007728, p), F(-2007729, p), F(3820557, p), F(m))
    for block, value in zip(blocks, expected):
        assert all(ledger.state[index] == value for index in block)
    ledger.independent_replay(raw)
    print('actual unit-recovery output parameter erasure: PASS', p, 3*p+r)
    return {'p': p, 'r': r, 'A': a, 'outside_A': outside_a,
            'output_values': list(map(str, expected)), 'means': list(map(str, means))}


if __name__ == '__main__':
    examples, erasure = verify_erasure()
    source_checks = verify_source_kernel()
    recurrence, cycles = verify_recurrent_policy()
    zero_checks = verify_zero_subset_coefficient()
    ternary = verify_ternary_contraction()
    integration = verify_recovery_output_integration()
    (ROOT/'parameter_erasure_recurrence_records.json').write_text(json.dumps({
        'scope': 'A uniform physical rank reduction and a failed closed policy, not a terminating solver.',
        'erasure_counts': erasure, 'source_kernel_checks': source_checks,
        'recurrence_cycles': cycles, 'zero_coefficient_checks': zero_checks,
        'examples': examples, 'recurrence': recurrence,
        'ternary_contraction': ternary, 'recovery_output_integration': integration}, indent=2)+'\n', encoding='utf-8')
    print('parameter erasure and recurrence boundary: PASS')
