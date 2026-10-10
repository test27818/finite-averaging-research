"""Four-prime endpoint witness merging and intermediate triple-block returns.

Exponent choices use modular powers only, never averaging-word enumeration.
All displayed sample paths are independently replayed on original positions.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm, prod
from pathlib import Path
from random import Random
import json

from verify_carrier_energy_and_pair_reduction import safe_flatten
from verify_composite_endpoint_transfer import (
    exact_decomposition, factors, signature, mm, inverse, GENERATORS)

if not __debug__:
    raise RuntimeError('Assertions required.')

ROOT = Path(__file__).parent


def order(value, ell):
    value %= ell
    assert value
    result = ell-1
    for q in factors(result):
        while result % q == 0 and pow(value, result//q, ell) == 1:
            result //= q
    return result


def residue(value, ell):
    value = F(value)
    return value.numerator*pow(value.denominator, -1, ell) % ell


def primitive(values):
    common = gcd(*values)
    return [x//common for x in values] if common else list(values)


def is_legal(values, primes):
    return all(len({residue(x, ell) for x in values}) > 1 for ell in primes)


class Ledger:
    def __init__(self, raw, p):
        self.state, self.p, self.word = list(map(F, raw)), p, []

    def average(self, positions):
        positions = list(positions)
        assert len(positions) == len(set(positions)) == self.p
        old_sum = sum(self.state)
        mean = sum(self.state[i] for i in positions)/self.p
        for i in positions:
            self.state[i] = mean
        assert sum(self.state) == old_sum
        self.word.append(positions)

    def swap(self, block, single):
        newblock, newsingle = block[:-1]+[single], block[-1]
        self.average(newblock)
        return newblock, newsingle

    def independent_replay(self, raw):
        values = list(map(F, raw))
        for group in self.word:
            assert len(group) == len(set(group)) == self.p
            mean = sum(values[i] for i in group)/self.p
            for i in group:
                values[i] = mean
        assert values == self.state


def choose_exponent(p, primes, a, carrier, target, periods):
    """The target is untouched. Return a positive power covering support union."""
    local = [(ell, residue(a, ell), residue(carrier, ell), residue(target, ell))
             for ell in primes]
    union = {ell for ell, aa, cc, tt in local if aa != cc or aa != tt}
    state = [(ell, aa, cc, tt) for ell, aa, cc, tt in local]
    period = lcm(*periods)
    for k in range(period):
        if all(ell not in union or aa != tt for ell, aa, cc, tt in state):
            return k, union
        state = [(ell, ((p-1)*aa+cc)*pow(p, -1, ell) % ell, aa, tt)
                 for ell, aa, cc, tt in state]
    raise AssertionError(('Exponent coverage failed', p, primes, local))


def first_block(raw, p, primes):
    protected = set()
    for ell in primes:
        j = next(j for j in range(1, len(raw)) if (raw[j]-raw[0]) % ell)
        protected.update((0, j))
    assert len(raw)-len(protected) >= p
    return [i for i in range(len(raw)) if i not in protected][:p]


def endpoint_entry(raw, p, first=None, prime_limit=4):
    n, primes = len(raw), tuple(factors(len(raw)))
    assert n == 2*p+1 and p % 2 and 1 <= prime_limit <= 6 and len(primes) <= prime_limit
    assert sum(raw) == 0 and gcd(*raw) == 1 and is_legal(raw, primes)
    ledger = Ledger(raw, p)
    block = first[:] if first is not None else first_block(raw, p, primes)
    ledger.average(block)
    singles = [i for i in range(n) if i not in block]
    assert is_legal(ledger.state, primes)
    def support(single):
        a = ledger.state[block[0]]
        return {ell for ell in primes if residue(ledger.state[single]-a, ell)}
    target = max(singles, key=lambda i: len(support(i)))
    sizes, powers = [len(support(target))], []
    periods = [order(2, ell) for ell in primes]
    while len(support(target)) < len(primes):
        complete = next((i for i in singles if len(support(i)) == len(primes)), None)
        if complete is not None:
            target = complete
            sizes.append(len(primes))
            break
        previous = support(target)
        selected = max((i for i in singles if i != target),
                       key=lambda i: len(support(i)-previous))
        assert support(selected)-previous
        k, expected = choose_exponent(p, primes, ledger.state[block[0]],
                                      ledger.state[selected], ledger.state[target], periods)
        assert k > 0
        role = singles.index(selected)
        for _ in range(k):
            block, singles[role] = ledger.swap(block, singles[role])
        assert support(target) == expected and previous < expected
        assert is_legal(ledger.state, primes)
        sizes.append(len(expected))
        powers.append(k)
    second = [i for i in singles if i != target]
    ledger.average(second)
    a, b, c = (ledger.state[block[0]], ledger.state[second[0]], ledger.state[target])
    assert c == -p*(a+b) and all(residue(a-b, ell) for ell in primes)
    assert all(ledger.state[i] == a for i in block)
    assert all(ledger.state[i] == b for i in second)
    assert len(powers) <= len(primes)-1
    assert len(ledger.word) <= 2+(len(primes)-1)*(lcm(*periods)-1)
    ledger.independent_replay(raw)
    return {'p': p, 'n': n, 'input': list(raw), 'prime_factors': list(primes),
            'periods': periods, 'support_sizes': sizes, 'exchange_powers': powers,
            'operations': [[i+1 for i in group] for group in ledger.word],
            'final_parameters': [str(a), str(b), str(c)]}


def verify_exponent_covering():
    sets = ((3, 5, 7), (3, 5, 7, 11), (3, 5, 7, 13),
            (3, 5, 17, 257), (7, 13, 17, 31), (3, 5, 641, 6700417))
    checked = 0
    for primes in sets:
        orders = [order(2, ell) for ell in primes]
        period = lcm(*orders)
        full = (1 << period)-1
        forbidden = [[sum(1 << k for k in range(j, period, d)) for j in range(d)]
                     for d in orders]
        for masks in product(*forbidden):
            covered = 0
            for mask in masks:
                covered |= mask
            assert covered != full
            checked += 1
    # Seven distinct primes can yield a complete covering of exponent classes.
    primes = (3, 5, 17, 257, 65537, 641, 6700417)
    orders = tuple(order(2, ell) for ell in primes)
    assert orders == (2, 4, 8, 16, 32, 64, 64)
    forbidden = (0, 1, 3, 7, 15, 31, 63)
    assert all(any(k % d == b for d, b in zip(orders, forbidden)) for k in range(64))
    print('four-prime arbitrary forbidden-exponent classes: PASS', checked)
    print('seven-prime exponent-cover boundary retained: PASS')


def forced_input(n):
    p, primes = n//2, tuple(factors(n))
    modulus = prod(primes)
    singles = []
    for ell in primes:
        unit = modulus//ell * pow(modulus//ell, -1, ell) % modulus
        singles.extend((1+unit, 1-unit))
    singles += [1]*(p+1-len(singles))
    singles[-1] -= n
    raw = [1]*p+singles
    assert sum(raw) == 0 and gcd(*raw) == 1 and 0 not in raw
    return raw


def verify_entries():
    rng, records = Random(2026091219), []
    levels = (15, 27, 39, 75, 195, 231, 255, 315, 399, 435, 455, 1071, 1155)
    forced = 0
    for n in levels:
        p = n//2
        for _ in range(4):
            while True:
                raw = [rng.randrange(-(1 << 72), 1 << 72) for _ in range(n-1)]
                raw.append(-sum(raw))
                raw = primitive(raw)
                if is_legal(raw, factors(n)):
                    break
            records.append(endpoint_entry(raw, p))
        if len(factors(n)) >= 2:
            result = endpoint_entry(forced_input(n), p, list(range(p)))
            assert result['support_sizes'] == list(range(1, len(factors(n))+1))
            records.append(result)
            forced += 1
    (ROOT/'four_prime_endpoint_entry_records.json').write_text(
        json.dumps({'scope': 'General theorem in document; these are labelled entry replays.',
                    'records': records}, indent=2)+'\n', encoding='utf-8')
    print('four-prime endpoint labelled entries and forced merges: PASS', len(records), forced,
          max(len(x['operations']) for x in records))


def verify_existing_core_certificates():
    required = {195, 231, 255, 315, 399, 435, 455, 1155}
    data = json.loads((ROOT/'composite_endpoint_pivot_certificates.json').read_text(encoding='utf-8'))
    checked, seen = 0, set()
    for case in data['cases']:
        n, p = case['level'], case['arity']
        if n not in required:
            continue
        seen.add(n)
        primepowers = [(ell, ell**e) for ell, e in factors(n).items()]
        reps = [tuple(r) for r in case['representatives']]
        assert all(r[0]*r[3]-r[1]*r[2] == 1 for r in reps)
        labels = [signature(r[2], r[3], primepowers) for r in reps]
        assert reps[0] == (1, 0, 0, 1)
        assert len(set(labels)) == len(reps) == prod(m+m//ell for ell, m in primepowers)
        assert {(e['source'], e['generator']) for e in case['edges']} == {
            (i, j) for i in range(len(reps)) for j in range(3)}
        assert len(case['edges']) == 3*len(reps)
        for e in case['edges']:
            r, g, following = reps[e['source']], GENERATORS[e['generator']], reps[e['target']]
            candidate = mm(r, g)
            assert signature(candidate[2], candidate[3], primepowers) == labels[e['target']]
            matrix = mm(candidate, inverse(following))
            assert matrix[2] % n == 0
            # Decode exact proof data using its actual schema.
            mode = e['mode']
            t = F(e['shear'])
            exact_decomposition(matrix, mode, t, n, p)
            checked += 1
    assert seen == required
    print('previous core certificates now joined to full entry: PASS', len(seen), checked)


def carrier_period(p, ell):
    return ell if (p+1) % ell == 0 else order(-pow(p, -1, ell), ell)


def band_reduce(raw, p, r):
    n, primes = len(raw), tuple(factors(len(raw)))
    periods = [carrier_period(p, ell) for ell in primes]
    assert n == 2*p+r and 1 <= r < p and r >= len(primes)
    assert sum((F(1, d) for d in periods), F(0)) < 1
    _, blocks, singles = safe_flatten(raw, p, 2, ledger=True)
    ledger = Ledger(raw, p)
    for group in blocks:
        ledger.average(group)
    a_block, b_block = blocks
    b_index = b_block[0]
    def support(i):
        return {ell for ell in primes if residue(ledger.state[i]-ledger.state[a_block[0]], ell)}
    powers, sizes = [], [len(support(b_index))]
    while len(support(b_index)) < len(primes):
        previous = support(b_index)
        chosen = max(singles, key=lambda i: len(support(i)-previous))
        assert support(chosen)-previous
        k, expected = choose_exponent(p, primes, ledger.state[a_block[0]],
                                      ledger.state[chosen], ledger.state[b_index], periods)
        role = singles.index(chosen)
        for _ in range(k):
            a_block, singles[role] = ledger.swap(a_block, singles[role])
        assert support(b_index) == expected and previous < expected
        powers.append(k)
        sizes.append(len(expected))
    old_a, b = ledger.state[a_block[0]], ledger.state[b_index]
    group = a_block[:p-r]+singles
    retained = a_block[p-r:]
    ledger.average(group)
    assert ledger.state[group[0]] == -b-F(r, p)*old_a
    assert all(ledger.state[i] == old_a for i in retained) and len(retained) == r
    assert is_legal(ledger.state, primes)
    ledger.independent_replay(raw)
    return len(ledger.word)


def verify_band_reductions():
    rng, total, maximum, dimensions = Random(2026091220), 0, 0, set()
    for p in (5, 7, 11, 13, 17, 19, 23, 31, 43):
        for r in range(1, p):
            n, primes = 2*p+r, tuple(factors(2*p+r))
            if r < len(primes):
                continue
            periods = [carrier_period(p, ell) for ell in primes]
            if sum((F(1, d) for d in periods), F(0)) >= 1:
                continue
            for _ in range(3):
                while True:
                    raw = [rng.randrange(-1000, 1001) for _ in range(n-1)]
                    raw.append(-sum(raw))
                    raw = primitive(raw)
                    if is_legal(raw, primes):
                        break
                maximum = max(maximum, band_reduce(raw, p, r))
                total += 1
                dimensions.add((p, n))
    print('band full-input reductions under period-density criterion: PASS',
          len(dimensions), total, maximum)


def triple_return(ledger, groups, p, r, s):
    aa, bb, cc = groups
    i = (p-s)//2
    assert 0 <= i <= p-r
    first = aa[:i]+bb[:i]+cc[:s]
    second = aa[i:p-r]+bb[i:]+cc[s:]
    retained = aa[p-r:]
    ledger.average(first)
    ledger.average(second)
    return first, second, retained


def verify_all_r_involutions():
    checked = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 31):
        for r in range(1, p):
            n, primes = 2*p+r, tuple(factors(2*p+r))
            for s in range(max(1, 2*r-p), r+1):
                if s % 2 == 0:
                    continue
                for x, z in ((1, 0), (0, 1), (3, -5)):
                    if r % 2:
                        a, b, c = x, r*z-x, -p*z
                    else:
                        t = r//2
                        a, b, c = t*z+x, t*z-x, -p*z
                    raw = [a]*p+[b]*p+[c]*r
                    ledger = Ledger(raw, p)
                    groups = list(range(p)), list(range(p, 2*p)), list(range(2*p, n))
                    groups = triple_return(ledger, groups, p, r, s)
                    k = F(p*r-n*s, 2*p*r)
                    expected = k*(a+b), -F(r, p)*a-k*(a+b), F(a)
                    assert [ledger.state[g[0]] for g in groups] == list(expected)
                    assert all(all(ledger.state[i] == v for i in g) for g, v in zip(groups, expected))
                    if is_legal(raw, primes):
                        assert is_legal(ledger.state, primes)
                    groups = triple_return(ledger, groups, p, r, s)
                    scale = F(n*s-p*r, 2*p*p)
                    assert scale
                    assert [ledger.state[g[0]] for g in groups] == [scale*a, scale*b, scale*c]
                    ledger.independent_replay(raw)
                    checked += 1
    print('all-r actual four-atom scalar periods and local safety: PASS', checked)


if __name__ == '__main__':
    verify_exponent_covering()
    verify_entries()
    verify_existing_core_certificates()
    verify_band_reductions()
    verify_all_r_involutions()
    print('four-prime entry and intermediate-band structures: PASS')
