"""Symbolic-count stages and labelled integer replay for arbitrary h.

Only critical Euclidean remainders are enumerated. A sieve, two possible
defects per h, quotient intervals and O(n+p) position updates avoid raw
position-subset or averaging-word search.
"""
from collections import Counter, deque
from math import gcd, isqrt
from pathlib import Path
import json

from verify_unit_witness_replenishment import core_parameters

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).resolve().parent


def primes_up_to(bound):
    sieve = bytearray(b'\x01')*(bound+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(bound)+1):
        if sieve[q]:
            start = q*q
            sieve[start:bound+1:q] = b'\x00'*(((bound-start)//q)+1)
    return [q for q in range(5, bound+1) if sieve[q]]


def critical_parameters(bound):
    for p in primes_up_to(bound):
        for h in range(2, isqrt((p-1)//2)+1):
            residue = p % h
            for d in (residue, residue+h):
                if not 1 <= d < 2*h-2:
                    continue
                s = (p-d)//h
                if s < 2*h:
                    continue
                assert p == h*s+d and gcd(h, d) == 1
                yield p, h, s, d


class Ledger:
    def __init__(self, p, values, weights):
        self.p = p
        self.raw = []
        self.positions = {}
        for value, count in zip(values, weights):
            start = len(self.raw)
            self.raw.extend([value]*count)
            self.positions.setdefault(value, deque()).extend(range(start, start+count))
        self.energy = sum(x*x for x in self.raw)
        self.trace = []
        assert sum(self.raw) == 0

    def average(self, selection):
        selection = [(value, count) for value, count in selection if count]
        assert all(count >= 0 for _, count in selection)
        assert sum(count for _, count in selection) == self.p
        total = sum(value*count for value, count in selection)
        assert total % self.p == 0
        mean = total//self.p
        loss = sum(count*(value-mean)**2 for value, count in selection)
        assert loss > 0
        group = []
        for value, count in selection:
            bucket = self.positions[value]
            assert len(bucket) >= count
            group.extend(bucket.popleft() for _ in range(count))
        assert len(group) == len(set(group)) == self.p
        for index in group:
            self.raw[index] = mean
        self.positions.setdefault(mean, deque()).extend(group)
        self.energy -= loss
        assert sum(self.raw) == 0
        assert sum(x*x for x in self.raw) == self.energy
        assert Counter(self.raw) == Counter({v: len(ids) for v, ids in self.positions.items() if ids})
        common = 0
        for x in self.raw:
            common = gcd(common, x-self.raw[0])
            if common == 1:
                break
        assert common == 1
        self.trace.append({'selection': selection, 'mean': mean,
                           'positions_1based': [i+1 for i in group],
                           'energy_drop': loss})
        return mean, set(group)

    def count(self, value):
        return len(self.positions.get(value, ()))


def upper_defect_counts(p, h, s, d):
    assert h < d < 2*h-2 and s >= 2*h and p == h*s+d
    f = d-h
    # Count order: A, B, old M, P. Q is produced in the first group.
    first = (p-2*d, 0, 2*f, 2*h)
    second = (p-h-2*f, f, 0, d)
    original = (2*p+2-h-d, h, d, p)
    assert all(k >= 0 for k in first+second)
    assert sum(first) == sum(second) == p
    assert all(x+y <= cap for x, y, cap in zip(first, second, original))
    assert first[2]+(s+1)*first[3]-s*first[1] == 2*p
    assert second[2]+(s+1)*second[3]-s*second[1] == p
    return first, second


def upper_continuation_counts(p, h, s, d):
    f, high, light_above = d-h, h+3*(d-h)+2, 2*h-d
    neutral = p-2*high-3*light_above
    assert neutral >= 0
    assert high+light_above <= p
    assert light_above <= p-3*h-f
    alpha = 4*h+2*d+4
    width = h+d
    odd = max(3, (p-alpha+width-1)//width)
    if odd % 2 == 0:
        odd += 1
    assert h*odd <= p-4*h and d*odd <= p-2*d-2
    assert 2*p-width*odd <= p+alpha
    k = (odd-1)//2
    assert width*(k+1) <= p
    return high, light_above, neutral, k


def continue_upper_output(ledger, p, h, s, d, a):
    high, light_above, neutral, k = upper_continuation_counts(p, h, s, d)
    b, old_m, old_p, old_q = a+s, a-1, a-s-1, a-2
    assert ledger.average(((a, high), (b, light_above), (old_p, light_above),
                           (old_q, high+light_above), (old_m, neutral)))[0] == old_m
    assert not ledger.count(a) and not ledger.count(b)
    assert Counter(ledger.raw) == Counter({
        old_m: p+4*h+2*d+4, old_q: p-2*d-2,
        old_p: p-4*h, a-(p*s+d): len(ledger.raw)-3*p-2})
    groups = []
    for j in (k, k+1):
        mean, labels = ledger.average(((old_m, p-(h+d)*j), (old_q, d*j), (old_p, h*j)))
        assert mean == old_m-j
        groups.append(labels)
    assert groups[0].isdisjoint(groups[1])
    assert ledger.count(old_m-k) >= p and ledger.count(old_m-k-1) >= p
    assert max(ledger.raw) <= old_m < a
    return k


def short_positive_remainder(e, t, d):
    assert e >= 2 and gcd(t, e) == 1
    inverse_gap = -pow(t, -1, e) % e
    rho = (e+2*inverse_gap-1)//(2*inverse_gap)
    if rho > d:
        return None
    j = e-inverse_gap*rho
    kappa = (j*t-rho)//e
    assert 1 <= j <= e//2 and 1 <= rho < e
    assert j*t == e*kappa+rho
    return j, kappa, rho, inverse_gap


def lower_defect_counts(p, h, s, d):
    e = h-d
    assert e >= 2 and s >= 2*h and p == h*s+d
    t = s+1
    j, kappa, rho, inverse_gap = short_positive_remainder(e, t, d)
    assert kappa >= 2*j and 0 <= rho <= d
    m1 = rho
    b1 = 0
    l1 = kappa*h-j
    a1 = p-l1-m1
    m2 = min(d-rho, e+rho)
    b2 = e+rho-m2
    l2 = (kappa-1)*h-j+b2
    a2 = p-l2-b2-m2
    first, second = (a1, b1, m1, l1), (a2, b2, m2, l2)
    original = (2*p+2-h-d, h, d, p)
    assert all(k >= 0 for k in first+second)
    assert sum(first) == sum(second) == p
    assert all(x+y <= cap for x, y, cap in zip(first, second, original))
    assert original[0]-a1 >= p and original[1]-b1 >= 1 and original[3]-l1 >= 1
    assert t*l1+m1-s*b1 == p*kappa
    assert t*l2+m2-s*b2 == p*(kappa-1)
    return first, second, kappa, rho, j, inverse_gap


def verify_short_remainder_criterion():
    checks = 0
    for e in range(2, 128):
        for t_mod in range(1, e):
            if gcd(t_mod, e) != 1:
                continue
            # The least positive residue in the first half-period is enough
            # to verify the threshold for every possible defect at once.
            least = min(j*t_mod % e for j in range(1, e//2+1))
            inverse_gap = -pow(t_mod, -1, e) % e
            assert least == (e+2*inverse_gap-1)//(2*inverse_gap)
            j = e-inverse_gap*least
            assert 1 <= j <= e//2 and j*t_mod % e == least
            checks += 1
    print('short positive remainder inverse criterion: PASS', checks)
    return checks


def direct_pair(p, r, h):
    inverse = pow(h, -1, p)
    for nb in range(h+1):
        nc = -nb*inverse % p
        na = p-nb-nc
        if 1 <= nc < r and 0 <= na <= p-h+1:
            return na, nb, nc
    return None


def verify_all():
    count_systems, physical, covered_old = Counter(), Counter(), Counter()
    records, unresolved, zero_checkpoints = [], [], 0
    for p, h, s, d in critical_parameters(1000):
        if d > h:
            kind = 'upper-defect'
            first, second = upper_defect_counts(p, h, s, d)
            upper_continuation_counts(p, h, s, d)
            kappa, rho, j, inverse_gap = 2, None, None, None
        elif h-d >= 2 and short_positive_remainder(h-d, s+1, d):
            kind = 'euclidean-lower-defect'
            first, second, kappa, rho, j, inverse_gap = lower_defect_counts(p, h, s, d)
        else:
            kind = None
        if kind:
            count_systems[kind] += 1
        for r, a, b, c in core_parameters(p, h, s):
            if a == 1 or a == s+1:
                zero_checkpoints += 1
                continue
            if kind is None:
                if d == 1:
                    covered_old['defect-one'] += 1
                elif h == 3 and d == 2:
                    covered_old['h3-defect2'] += 1
                elif direct_pair(p, r, h):
                    covered_old['direct-pair'] += 1
                else:
                    e = h-d
                    inverse_gap = -pow(s+1, -1, e) % e if e >= 2 else None
                    assert (d == h-1 and h >= 4) or (d >= 2 and 3*d < h and 2*d*inverse_gap < e)
                    unresolved.append({'p': p, 'r': r, 'h': h, 's': s, 'd': d,
                                       'e': e, 'rho': (s+1) % e if e else None,
                                       'negative_inverse': inverse_gap,
                                       'initial': [a, b, c]})
                continue
            m, carrier_mean = a-1, a-s-1
            ledger = Ledger(p, (a, b, c), (2*p, p, r))
            assert ledger.average(((a, h-1), (b, p-h), (c, 1)))[0] == m
            assert ledger.average(((a, d-1), (m, p-d), (c, 1)))[0] == carrier_mean
            values = (a, b, m, carrier_mean)
            q, group1 = ledger.average(tuple(zip(values, first)))
            target, group2 = ledger.average(tuple(zip(values, second)))
            assert group1.isdisjoint(group2)
            assert q == a-kappa and target == a-kappa+1
            assert ledger.count(q) >= p and ledger.count(target) >= p
            continuation_k = None
            if kind == 'upper-defect':
                continuation_k = continue_upper_output(ledger, p, h, s, d, a)
            physical[kind] += 1
            if sum(x['kind'] == kind for x in records) < 4:
                records.append({'kind': kind, 'p': p, 'r': r, 'h': h, 's': s, 'd': d,
                                'kappa': kappa, 'rho': rho, 'initial': [a, b, c],
                                'j': j, 'negative_inverse': inverse_gap,
                                'upper_output_continuation_k': continuation_k,
                                'trace': ledger.trace,
                                'output': sorted((v, len(ids)) for v, ids in ledger.positions.items() if ids)})
    assert physical['upper-defect'] and physical['euclidean-lower-defect']
    print('euclidean witness count systems: PASS', dict(count_systems))
    print('euclidean witness labelled disjoint transfers: PASS', dict(physical))
    print('upper-defect actual output continuations: PASS', physical['upper-defect'])
    print('remaining menu boundaries through p1000:', len(unresolved))
    print('previous menus and zero checkpoints:', dict(covered_old), zero_checkpoints)
    return {'scope': 'Two explicit local transfers, not recursive closure or a new threshold.',
            'count_systems': dict(count_systems), 'physical_counts': dict(physical),
            'previous_menus': dict(covered_old), 'zero_checkpoints': zero_checkpoints,
            'records': records, 'unresolved_by_current_menus': unresolved}


if __name__ == '__main__':
    criterion_checks = verify_short_remainder_criterion()
    result = verify_all()
    result['short_remainder_criterion_checks'] = criterion_checks
    (ROOT/'euclidean_witness_transfer_records.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('euclidean witness transfer: PASS')
