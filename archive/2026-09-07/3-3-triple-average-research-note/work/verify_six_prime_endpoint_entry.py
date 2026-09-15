"""Five forbidden order classes imply six-prime physical endpoint entry.

Large inputs stay in exact multiplicity form. This checks original-position
capacities without allocating hundreds of thousands of equal coordinates.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm, prod
from pathlib import Path
import json

from verify_four_prime_entry_and_band import (
    order, residue, factors, endpoint_entry, forced_input, choose_exponent)

ROOT = Path(__file__).parent

if not __debug__:
    raise RuntimeError('Assertions required.')


def check_five_classes():
    core = (3, 5, 7, 13, 17, 241)
    prime_sets = list(combinations(core, 5))+[
        (3, 5, 17, 257, 65537), (3, 7, 13, 17, 31),
        (5, 7, 17, 31, 127), (3, 5, 7, 641, 6700417)]
    checked = 0
    for primes in prime_sets:
        periods = [order(2, q) for q in primes]
        period = lcm(*periods)
        full = (1 << period)-1
        masks = [[sum(1 << k for k in range(b, period, d)) for b in range(d)]
                 for d in periods]
        for choice in product(*masks):
            union = 0
            for mask in choice:
                union |= mask
            assert union != full
            checked += 1
    periods = tuple(order(2, q) for q in core)
    assert periods == (2, 4, 3, 12, 8, 24)
    forbidden = (0, 1, 2, 7, 7, 3)
    assert all(any(k % d == b for d, b in zip(periods, forbidden)) for k in range(24))
    # Classical Riesel arithmetic validates these as actual powers of2.
    assert all((509203*pow(2, b, q)-1) % q == 0 for q, b in zip(core, forbidden))
    print('five-prime arbitrary forbidden classes: PASS', checked)
    print('six forbidden classes exactly cover all exponents: PASS 24')


def merge_compressed(p, initial):
    n, primes = 2*p+1, tuple(factors(2*p+1))
    assert len(primes) <= 6
    assert sum(initial.values()) == n and sum(v*f for v, f in initial.items()) == 0
    assert gcd(*initial) == gcd(*(v-next(iter(initial)) for v in initial)) == 1
    assert initial[1] >= p
    a, singles = F(1), Counter({F(v): f for v, f in initial.items()})
    singles[a] -= p
    singles += Counter()
    periods = [order(2, q) for q in primes]
    sizes, phases, atom_count = [], [], 1  # First p copies of1 form the initial block.

    def support(value):
        return {q for q in primes if residue(value-a, q)}

    while True:
        target = max(singles, key=lambda value: len(support(value)))
        before = support(target)
        sizes.append(len(before))
        assert not phases or len(before) > phases[-1]['before_support']
        if len(before) == len(primes):
            break
        chosen = max((v for v in singles if v != target),
                     key=lambda value: len(support(value)-before))
        assert support(chosen)-before
        assert len(support(chosen)) <= len(primes)-1 <= 5
        k, expected = choose_exponent(p, primes, a, chosen, target, periods)
        assert 0 < k < lcm(*periods)
        original_a, original_carrier = a, chosen
        carrier = chosen
        for _ in range(k):
            old_a = a
            a = ((p-1)*a+carrier)/p
            assert singles[carrier] >= 1
            singles[carrier] -= 1
            if not singles[carrier]:
                del singles[carrier]
            singles[old_a] += 1
            carrier = old_a
            assert sum(singles.values()) == p+1
            assert p*a+sum(value*f for value, f in singles.items()) == 0
        assert singles[target] and support(target) == expected and before < expected
        phases.append({'block_before': str(original_a), 'carrier_before': str(original_carrier),
                       'untouched_target': str(target), 'power': k,
                       'before_support': len(before), 'after_support': len(expected)})
        atom_count += k
    b = (sum(value*f for value, f in singles.items())-target)/p
    assert target == -p*(a+b)
    assert all(residue(a-b, q) for q in primes)
    atom_count += 1
    assert len(phases) <= len(primes)-1
    return {'p': p, 'n': n, 'prime_factors': list(primes),
            'input_multiplicities': [[str(v), f] for v, f in initial.items()],
            'support_sizes': sizes, 'phases': phases,
            'atomic_steps_including_initial_and_final_blocks': atom_count,
            'final_block_values_and_singleton': list(map(str, (a, b, target)))}


def forced_counts(n):
    p, primes = n//2, tuple(factors(n))
    modulus = prod(primes)
    counts = Counter({1: n})
    for q in primes:
        unit = modulus//q*pow(modulus//q, -1, q) % modulus
        counts[1] -= 2
        counts[1+unit] += 1
        counts[1-unit] += 1
    counts[1] -= 1
    counts[1-n] += 1
    assert counts[1] >= p
    return counts


def check_entries():
    records = []
    for n in (15015, 135135, 255255, 435435, 285212655):
        records.append(merge_compressed(n//2, forced_counts(n)))
        assert records[-1]['support_sizes'] == list(range(1, len(factors(n))+1))
    # The historical K4/CRT counterexample to every DIRECT (p,p,1) partition.
    k4 = Counter({1: 435429, 2641: 1, 8295: 1, 82447: 1, 342056: 1,
                  435436: 1, -1306304: 1})
    records.append(merge_compressed(217717, k4))
    # A moderate five-factor input is also replayed on individual positions.
    n = 15015
    literal = endpoint_entry(forced_input(n), n//2, list(range(n//2)), prime_limit=6)
    assert literal['support_sizes'][-1] == 5
    print('six-prime exact multiplicity entries and direct-partition trap: PASS',
          len(records), max(x['atomic_steps_including_initial_and_final_blocks'] for x in records))
    print('five-prime independently labelled entry: PASS',
          n, len(literal['operations']))
    (ROOT/'six_prime_endpoint_entry_results.json').write_text(json.dumps({
        'scope': 'Entry only; no new all-level core-group claim.',
        'compressed_entries': records, 'literal_entry': literal}, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    check_five_classes()
    check_entries()
    print('six-prime endpoint entry: PASS')
