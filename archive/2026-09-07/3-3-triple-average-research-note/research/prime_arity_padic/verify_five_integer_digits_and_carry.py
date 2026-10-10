"""Exact diagnostics for the written theorems; finite checks do not prove nonregularity.

Only the standard library is required. This writes its own result record, never
the result records belonging to the earlier oracles imported below.
"""

from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
import json

from verify_subcritical_complement_dynamics import (
    core_distance,
    independent_integer_oracle,
)


def eta(a, b):
    assert gcd(a, b) == 1
    return int((a-b) % 2 != 0)


def next_pair(a, b):
    assert b > 0 and gcd(a, b) == 1 and b % 3 and a % 3
    epsilon = 1 if a*pow(b, -1, 3) % 3 == 1 else -1
    q = (a-epsilon*b)//3
    content = gcd(q, 4)
    aa, bb = -q//content, (4*b+15*epsilon*q)//content
    assert bb != 0 and gcd(aa, bb) == 1
    assert content == 2**(1+eta(aa, bb)-eta(a, b))
    old = F(a, b)
    assert F(aa, bb) == (old-epsilon)/(3-15*epsilon*old)
    if bb < 0:
        aa, bb = -aa, -bb
    return aa, bb, content


def h_distance(h):
    if h is None:
        return None
    a, b = h.numerator, h.denominator
    if b % 3 == 0 or b % 5 == 0:
        return None
    start_eta = eta(a, b)
    total_content = 1
    count = 0
    while a:
        if a % 3 == 0:
            return None
        a, b, content = next_pair(a, b)
        count += 1
        total_content *= content
        assert total_content == 2**(count+eta(a, b)-start_eta)
        # This is a diagnostic guard, not a proof or a search cutoff returning false.
        assert count < 10000
    return count+1


def from_pair(u, v):
    if u == v == 0:
        return 0
    if u == v:
        return None
    return h_distance(F(u+v, 5*(u-v)))


def input_distance(values):
    if len(set(values)) == 1:
        return 0
    total = sum(values)
    choices = []
    for i, j in combinations(range(5), 2):
        u = 4*values[i]+values[j]-total
        v = values[i]+4*values[j]-total
        d = from_pair(u, v)
        if d is not None:
            choices.append(1+d)
    return min(choices, default=None)


def balanced_prefix(x, length):
    result = []
    for _ in range(length):
        residue = x.numerator*pow(x.denominator, -1, 3) % 3
        epsilon = -1 if residue == 2 else residue
        result.append(epsilon)
        x = (x-epsilon)/3
    return result


def multiplicative_order_3(d):
    if d == 1:
        return 1
    assert gcd(d, 3) == 1
    value, length = 3 % d, 1
    while value != 1:
        value = 3*value % d
        length += 1
        assert length <= d
    return length


def run():
    comparisons = 0
    for u in range(-180, 181):
        for v in range(-180, 181):
            assert from_pair(u, v) == core_distance(3, u, v), (u, v)
            comparisons += 1

    content_checks = 0
    for a in range(-120, 121):
        for b in range(1, 101):
            if gcd(a, b) != 1 or not (a % 3 and b % 3):
                continue
            aa, bb, content = next_pair(a, b)
            epsilon = 1 if a*pow(b, -1, 3) % 3 == 1 else -1
            q = (a-epsilon*b)//3
            assert gcd(q, 4*b+15*epsilon*q) == content
            content_checks += 1

    reverse_nodes = 0
    layer = [(0, 1)]
    for length in range(13):
        for a, b in layer:
            content = gcd(a, b)
            assert content == 2**(length+eta(a//content, b//content)-1)
            assert h_distance(F(a, b)) == length+1
            reverse_nodes += 1
        layer = [(3*a+sign*b, 15*sign*a+b)
                 for a, b in layer for sign in (-1, 1)]

    # This oracle explores the complete finite integer energy DAG, without depth cutoff.
    oracle = independent_integer_oracle(3)
    input_checks = 0
    for values in combinations_with_replacement(range(4), 5):
        total = sum(values)
        centered = tuple(5*x-total for x in values)
        common = gcd(*centered)
        if common:
            centered = tuple(x//common for x in centered)
        assert input_distance(values) == oracle(centered), values
        input_checks += 1

    bridges = []
    for k in range(2, 7):
        power = (-3)**k
        u, v = (9*power+75)//4, (21*power-5)//4
        assert gcd(u, v) == 1
        t = F(u, v)
        assert 0 < t < 1 and t.denominator % 3
        assert core_distance(3, u, v) == k+5
        assert t.denominator == abs(21*power-5)//4
        m = multiplicative_order_3(t.denominator)
        denom = 3**m-1
        numerator = t.numerator*(denom//t.denominator)
        assert 0 < numerator < denom and F(numerator, denom) == t
        assert core_distance(3, numerator, denom) == k+5
        # Full bridge equality modulo 3^m, without converting the huge integer to text.
        modulus = 3**m
        assert (numerator+t.numerator*pow(t.denominator, -1, modulus)) % modulus == 0
        bridges.append({'k': k, 'slope': str(t), 'denominator': t.denominator,
                        'bridge_digit_length': m, 'shortest_core_steps': k+5})

    examples = []
    for h in (F(1, 7), F(-2), F(-1, 2), F(3)):
        a, b = h.numerator, h.denominator
        values = (0, 0, 0, 5*a+b, 5*a-b)
        d = h_distance(h)
        assert input_distance(values) == d
        examples.append({'h': str(h), 'balanced_digits_low_first': balanced_prefix(h, 8),
                         'instance': values, 'minimum_steps': d})

    return {'status': 'PASS', 'core_box': [-180, 180],
            'core_comparisons_with_prior_exact_recursion': comparisons,
            'content_identity_checks': content_checks,
            'all_reverse_words_through_depth': 12, 'reverse_nodes': reverse_nodes,
            'independent_integer_DAG_input_checks': input_checks,
            'independent_DAG_states': oracle.cache_info().currsize,
            'isolated_repunit_bridges': bridges, 'digit_examples': examples,
            'scope': 'Exact finite diagnostics only. The written nonregularity proof uses '
                     'unbounded isolated denominators and regular-language closure, not these samples. '
                     'No all-input static gcd criterion or primitive-promise nonregularity is claimed.'}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    result = run()
    Path(__file__).with_name('five_integer_digits_and_carry_verification.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
