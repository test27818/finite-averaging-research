"""Exact reverse-endpoint audit: labelled certificates and frozen integer forms.

Bounded search failures never imply rational nonreachability. All pattern
enumerations use value multiplicities; zero-free tests use modular bitsets.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd
import json
from pathlib import Path

P = 7
REPORT = Path(__file__).with_name('exact_seven_average_n15_bounded_b5.json')
CERTIFICATES = Path(__file__).with_name('endpoint_reverse_escape_certificates.json')


def value_patterns(values, amount=P):
    counts, chosen = Counter(values), []
    distinct = tuple(sorted(counts))
    capacity = [0]*(len(distinct)+1)
    for i in range(len(distinct)-1, -1, -1):
        capacity[i] = capacity[i+1]+counts[distinct[i]]
    def visit(i, left):
        if not left:
            yield tuple(chosen)
            return
        if i == len(distinct) or capacity[i] < left:
            return
        x = distinct[i]
        for k in range(max(0, left-capacity[i+1]), min(counts[x], left)+1):
            chosen.extend([x]*k)
            yield from visit(i+1, left-k)
            if k:
                del chosen[-k:]
    yield from visit(0, amount)


def zero_value_subset(values, amount=P):
    return next((m for m in value_patterns(values, amount) if sum(m) == 0), None)


def apply_values(values, move, p=P):
    counts = Counter(values)
    counts.subtract(move)
    assert len(move) == p and min(counts.values()) >= 0
    return tuple(counts.elements())+(sum(map(F, move))/p,)*p


def canonical(values):
    return min(tuple(sorted(values)), tuple(sorted(-x for x in values)))


def zero_free(labels, p):
    reached, mask = 1, (1 << p)-1
    for label in labels:
        label %= p
        new = ((reached << label) | (reached >> (p-label))) & mask
        if new & 1:
            return False
        reached |= new
    return True


class Ledger:
    def __init__(self, values, p):
        self.p, self.state, self.groups = p, list(map(F, values)), []

    def average_indices(self, indices):
        indices = tuple(indices)
        assert len(indices) == len(set(indices)) == self.p
        assert all(0 <= i < len(self.state) for i in indices)
        old = sum(x*x for x in self.state)
        mean = sum(self.state[i] for i in indices)/self.p
        for i in indices:
            self.state[i] = mean
        assert sum(self.state) == 0 and sum(x*x for x in self.state) <= old
        self.groups.append(indices)

    def average_values(self, move):
        available, indices = {}, []
        for i, value in enumerate(self.state):
            available.setdefault(value, []).append(i)
        for value in move:
            assert available.get(value)
            indices.append(available[value].pop())
        self.average_indices(indices)

    def finish_from_zero(self):
        if not any(self.state):
            return
        keep = self.state.index(F(0))
        rest = [i for i in range(len(self.state)) if i != keep]
        assert len(rest) == 2*self.p
        self.average_indices(rest[:self.p])
        self.average_indices(rest[self.p:])
        if not any(self.state):
            return
        for count in ((self.p-1)//2, (self.p-1)//2, 1):
            positive = [i for i, x in enumerate(self.state) if x > 0]
            negative = [i for i, x in enumerate(self.state) if x < 0]
            zeros = [i for i, x in enumerate(self.state) if not x]
            assert len(positive) >= count and len(negative) >= count
            assert self.state[positive[0]] == -self.state[negative[0]]
            self.average_indices(positive[:count]+negative[:count]+zeros[:self.p-2*count])
        assert not any(self.state)


def first_escape(values):
    for move in value_patterns(values):
        if len(set(move)) == 1:
            continue
        after = apply_values(values, move)
        for move2 in value_patterns(after):
            if len(set(move2)) == 1:
                continue
            witness = zero_value_subset(apply_values(after, move2))
            if witness is not None:
                return move, move2, witness
    raise AssertionError('No bounded escape: not a nonreachability proof.')


def verify_frozen_classification(unknown):
    observed, bound = set(), 5
    for background in range(1, bound+1):
        others = [x for x in range(-bound, bound+1) if x != background]
        for frequency in range(P+2, 2*P+1):
            size = 2*P+1-frequency
            for light in combinations_with_replacement(others, size):
                if frequency*background+sum(light):
                    continue
                values = (background,)*frequency+light
                if gcd(*values) != 1 or gcd(*(x-background for x in light)) != 1:
                    continue
                if zero_free([x-background for x in light], P):
                    observed.add(canonical(values))
    assert observed == set(unknown)
    print('n15 bounded frozen-state structural classification: PASS', len(observed))


def verify_uniform_family():
    checked = paths = 0
    for p in range(5, 150):
        if any(p % d == 0 for d in range(2, int(p**.5)+1)):
            continue
        values = (1,)*(2*p-2)+(2-p, 3-p, -3)
        assert len(values) == 2*p+1 and sum(values) == 0
        assert gcd(*values) == gcd(*(x-1 for x in values)) == 1
        assert zero_free((1, 2, p-4), p)
        checked += 1
        if p % 3 == 2:
            ledger = Ledger(values, p)
            ledger.average_values((2-p,)+(1,)*(p-1))
            ledger.average_values((3-p, -3)+(1,)*(p-2))
            k = (p-2)//3
            ledger.average_values((F(1, p),)*k+(F(-2, p),)*(p-1-k)+(1,))
            assert 0 in ledger.state
            ledger.finish_from_zero()
            paths += 1
    print('uniform integer-frozen family and rational escapes: PASS', checked, paths)


def verify_depth_formula():
    checked = 0
    for p in (3, 5, 7, 11, 13, 17):
        for order in (1, 2, 3):
            value = F(1, p**order)
            for overlap in range(1, p):
                mean = (overlap*value+sum(range(p-overlap)))/p
                assert mean.denominator == p**(order+1)
                checked += 1
    print('partial minimal-layer overlap increases denominator depth: PASS', checked)


def main():
    report = json.loads(REPORT.read_text(encoding='utf-8'))['reports'][0]
    assert report['states'] == 35714 and report['certified'] == 35707
    unknown = [tuple(x) for x in report['unknown_states']]
    assert len(unknown) == len(set(unknown)) == 7
    first_count, certificates = 0, []
    for values in unknown:
        moves = [m for m in value_patterns(values) if len(set(m)) > 1]
        assert all(sum(m) % P for m in moves)
        assert 0 not in values
        for move in moves:
            after = apply_values(values, move)
            assert 0 not in after and zero_value_subset(after) is None
            first_count += 1
        escape = first_escape(values)
        ledger = Ledger(values, P)
        for move in escape:
            ledger.average_values(move)
        assert not set(ledger.groups[0]).intersection(ledger.groups[1])
        assert 0 in ledger.state
        ledger.finish_from_zero()
        replay = list(map(F, values))
        for group in ledger.groups:
            assert len(group) == len(set(group)) == P
            mean = sum(replay[i] for i in group)/P
            for i in group:
                replay[i] = mean
        assert not any(replay)
        certificates.append({'p': P, 'input': list(values),
                             'groups': [list(g) for g in ledger.groups],
                             'first_three_value_groups': [[str(x) for x in m] for m in escape]})
    CERTIFICATES.write_text(json.dumps({'scope': 'Seven explicit inputs only.',
        'certificates': certificates}, indent=2)+'\n', encoding='utf-8')
    print('n15 bounded integer-trap states: PASS', len(unknown))
    print('n15 exhaustive first rational layers avoid zero triggers: PASS', first_count)
    print('n15 independently replayed rational complete paths: PASS',
          len(certificates), max(len(c['groups']) for c in certificates))
    verify_frozen_classification(unknown)
    verify_uniform_family()
    verify_depth_formula()
    print('endpoint reverse diagnostic: PASS')


if __name__ == '__main__':
    main()
