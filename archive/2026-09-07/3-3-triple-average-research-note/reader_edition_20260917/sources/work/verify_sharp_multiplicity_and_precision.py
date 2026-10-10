"""Exact safety obstructions, capped multiplicity and precision necessity.

All adversarial families have three or four types. Counts, residue buckets
and a small witness-cover dynamic program replace position-subset searches.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_core_exit_and_potential_scope import factors
from verify_provenance_dynamic_stages import apply_types, count_choices, primitive_g
from verify_euclidean_witness_transfer import primes_up_to

ROOT = Path(__file__).resolve().parent
if not __debug__:
    raise RuntimeError('Assertions are required.')


def capped_mass(weights, p):
    return sum(min(w, p-1) for w in weights)


def witness_cover(values, weights, p):
    n = sum(weights)
    supports = []
    for q in factors(n):
        if q == p:
            continue
        sizes = Counter()
        for value, weight in zip(values, weights):
            sizes[value % q] += weight
        assert len(sizes) > 1
        main = next((r for r, size in sizes.items() if size >= n-p), None)
        if main is not None:
            supports.append((q, tuple(i for i, value in enumerate(values) if value % q != main)))
    full = (1 << len(supports))-1
    best = {0: ()}
    for i in range(len(values)):
        mask = sum(1 << j for j, (_, support) in enumerate(supports) if i in support)
        for current, chosen in tuple(best.items()):
            after = current | mask
            candidate = chosen+(i,)
            if after not in best or len(candidate) < len(best[after]):
                best[after] = candidate
    return best[full], supports


def integer_menus(values, weights, p):
    for counts in count_choices(weights, p):
        total = sum(x*k for x, k in zip(values, counts))
        if total % p == 0 and sum(k > 0 for k in counts) > 1:
            yield counts, total//p


def verify_deadlocks():
    records, cases, precision = [], 0, 0
    for p in primes_up_to(200):
        for multiplier in (3, 4, p+3):
            heavy = multiplier*(p-1)
            n = heavy+p
            c = 1-p*(heavy+1)
            values, weights = (p, 1, c), (heavy, p-1, 1)
            assert sum(v*w for v, w in zip(values, weights)) == 0
            assert gcd(p-1, c-1) == 1 and gcd(p, heavy) == 1
            choices = list(integer_menus(values, weights, p))
            assert choices == [((0, p-1, 1), -heavy)]
            forbidden = [F(p)]*heavy+[F(-heavy)]*p
            assert primitive_g(forbidden)[0] == n
            assert all(p % q for q in factors(n))
            protected, supports = witness_cover(values, weights, p)
            assert len(protected) == 1 and all(s == (1, 2) for _, s in supports)
            assert capped_mass(weights, p) == 2*p-1
            raw = [F(v) for v, w in zip(values, weights) for _ in range(w)]
            escaped, step = apply_types(raw, ((p, p-1), (1, 1)), p)
            assert escaped[step['group_1based'][0]-1] == F(p*p-p+1, p)
            assert max(x.denominator for x in escaped) == p
            counts = Counter(escaped)
            assert counts[F(p)] >= p and counts[F(p*p-p+1, p)] >= p
            if multiplier == 4:
                dangerous_prime_count = len(factors(n))
                assert n == 5*p-4 and n >= 4*p-2+dangerous_prime_count
                precision += 1
            if len(records) < 6:
                records.append({'p': p, 'n': n, 'values': values, 'weights': weights,
                                'only_nonconstant_integer_step': choices[0],
                                'forbidden_output_G': n, 'fractional_escape': step})
            cases += 1
    print('sharp near-heavy safety deadlocks: PASS', cases)
    print('one-extra-digit optimality interface: PASS', precision)
    return records, cases, precision


def verify_frozen_sharpness():
    cases = 0
    for p in (3, 5, 7, 11, 13, 17, 23, 31):
        for multiple in (2, 3, 5):
            n = multiple*p+1
            values = (1, 2, 2-(multiple+1)*p)
            weights = ((multiple-1)*p+2, p-2, 1)
            assert sum(weights) == n and sum(v*w for v, w in zip(values, weights)) == 0
            assert gcd(*(x-values[0] for x in values)) == 1
            assert not list(integer_menus(values, weights, p))
            assert capped_mass(weights, p) == 2*p-2
            assert sorted(weights, reverse=True)[1] == p-2
            cases += 1
    print('integer frozen second-multiplicity sharpness: PASS', cases)
    return cases


def verify_capped_mass_selection():
    rng, tested, guarded = Random(2026091417), 0, 0
    for p in (3, 5, 7, 11):
        for _ in range(50):
            while True:
                n = 3*p+rng.randrange(1, p)
                wa = rng.randrange(1, n-3)
                wb = rng.randrange(1, n-wa-2)
                wc = n-wa-wb-1
                a, b, c = (rng.randrange(-30, 31) for _ in range(3))
                values = (a, b, c, -wa*a-wb*b-wc*c)
                weights = (wa, wb, wc, 1)
                if len(set(values)) == 4 and gcd(*(x-values[0] for x in values)) == 1:
                    break
            protected, supports = witness_cover(values, weights, p)
            score = capped_mass(weights, p)
            if score < 2*p-1+len(protected):
                continue
            capacities = tuple(min(w-int(i in protected), p-1) for i, w in enumerate(weights))
            assert sum(capacities) >= 2*p-1
            candidate = next(integer_menus(values, capacities, p), None)
            assert candidate is not None
            counts, mean = candidate
            raw = [F(v) for v, w in zip(values, weights) for _ in range(w)]
            after, _ = apply_types(raw, tuple(zip(values, counts)), p)
            assert all(x.denominator == 1 for x in after)
            assert all(len({int(x) % q for x in after}) > 1 for q in factors(n))
            assert not any(all(weights[i] == counts[i] for i in support) for _, support in supports)
            tested += 1
            guarded += bool(protected)
    assert guarded
    print('capped mass protected integer selection: PASS', tested, guarded)
    return tested, guarded


def verify_precision_policy_boundary():
    records = []
    parameters = (5, 7, 11, 13, 17, 23, 31, 43)
    for p in parameters:
        raw = [F(1)]*(3*p-3)+[F(2-p)]*3+[F(-1), F(-2)]
        trapped, bad_trace = raw[:], []
        for _ in range(3):
            trapped, step = apply_types(trapped, ((1, p-1), (2-p, 1)), p)
            assert step['mean'] == str(F(1, p))
            bad_trace.append(step)
        assert Counter(trapped) == Counter({F(1, p): 3*p, F(-1): 1, F(-2): 1})
        scaled = (1, -p, -2*p)
        assert not list(integer_menus(scaled, (3*p, 1, 1), p))
        assert primitive_g(trapped)[0] == 1
        good, first = apply_types(raw, ((2-p, 2), (-1, 1), (1, p-3)), p)
        assert first['mean'] == '-1'
        good, second = apply_types(good, ((-2, 1), (1, (p+1)//2), (-1, (p-3)//2)), p)
        assert second['mean'] == '0' and good.count(0) >= p
        if len(records) < 3:
            records.append({'p': p, 'n': len(raw), 'trapping_fractional_prefix': bad_trace,
                            'integer_zero_trigger': [first, second]})
    print('safe fixed-precision policy obstruction and alternative: PASS', len(parameters))
    return records


if __name__ == '__main__':
    deadlocks, cases, precision = verify_deadlocks()
    frozen = verify_frozen_sharpness()
    mass = verify_capped_mass_selection()
    policies = verify_precision_policy_boundary()
    (ROOT/'sharp_multiplicity_precision_records.json').write_text(json.dumps({
        'scope': 'Sharp one-step safety and precision bounds; no new all-input threshold.',
        'deadlock_count': cases, 'precision_instances': precision,
        'frozen_count': frozen, 'capped_mass_checks': mass,
        'deadlocks': deadlocks, 'policy_boundaries': policies}, indent=2)+'\n', encoding='utf-8')
    print('sharp multiplicity and precision: PASS')
