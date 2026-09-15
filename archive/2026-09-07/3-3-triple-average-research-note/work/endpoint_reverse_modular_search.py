"""Exact finite-quotient audit and bounded search on structured frozen inputs.

Reverse modular search uses multiplicity vectors, not labelled state vectors.
Frozen-input horizon two is reduced analytically to two disjoint p-blocks.
"""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter
import argparse
import json

from verify_endpoint_reverse_diagnostic import Ledger, zero_free

ROOT = Path(__file__).parent


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for head in range(total+1):
        for tail in compositions(total-head, parts-1):
            yield (head,)+tail


def modular_audit(p, n, modulus):
    started = perf_counter()
    assert gcd(p, modulus) == 1
    states = {c for c in compositions(n, modulus)
              if sum(i*k for i, k in enumerate(c)) % modulus == 0}
    patterns = [[] for _ in range(modulus)]
    inverse = pow(p, -1, modulus)
    for c in compositions(p, modulus):
        mean = sum(i*k for i, k in enumerate(c))*inverse % modulus
        patterns[mean].append(c)
    zero = (n,)+(0,)*(modulus-1)
    queue, reached, transitions = deque([zero]), {zero}, 0
    while queue:
        target = queue.popleft()
        for mean, multiplicity in enumerate(target):
            if multiplicity < p:
                continue
            remainder = list(target)
            remainder[mean] -= p
            for old_group in patterns[mean]:
                before = tuple(a+b for a, b in zip(remainder, old_group))
                assert before in states
                transitions += 1
                if before not in reached:
                    reached.add(before)
                    queue.append(before)
    missing = states-reached
    common_nonzero = set()
    for state in states:
        support = [i for i, k in enumerate(state) if k]
        ideal = gcd(modulus, *(x-support[0] for x in support))
        if support[0] % ideal:
            common_nonzero.add(state)
    unexplained = missing-common_nonzero
    assert not common_nonzero-reached.intersection(common_nonzero)-missing
    assert not reached.intersection(common_nonzero)
    return {'p': p, 'n': n, 'modulus': modulus, 'zero_sum_histograms': len(states),
            'reachable_to_zero': len(reached), 'known_common_residue_obstructions': len(common_nonzero),
            'unreachable_histograms': len(missing), 'unexplained_obstructions': len(unexplained),
            'unexplained_examples': [list(x) for x in sorted(unexplained)[:12]],
            'reverse_edges_checked': transitions, 'seconds': perf_counter()-started}


def disjoint_two_step_escape(p, light):
    n, f = 2*p+1, 2*p+1-len(light)
    values = [1]*f+list(light)
    assert sum(values) == 0 and f >= p+2
    for singleton in [0]+list(range(f, n)):
        background = [i for i in range(f) if i != singleton]
        exceptions = [i for i in range(f, n) if i != singleton]
        c = values[singleton]
        sums, sizes = [0]*(1 << len(exceptions)), [0]*(1 << len(exceptions))
        for mask in range(1 << len(exceptions)):
            if mask:
                bit = mask & -mask
                previous = mask-bit
                sums[mask] = sums[previous]+values[exceptions[bit.bit_length()-1]]
                sizes[mask] = sizes[previous]+1
            count = sizes[mask]
            if count > p or p-count > len(background):
                continue
            first_sum = sums[mask]+p-count
            second_sum = -c-first_sum
            difference = first_sum-second_sum
            if not difference:
                continue
            for use_carrier in (0, 1):
                numerator = -(p-use_carrier)*second_sum-use_carrier*p*c
                if numerator % difference:
                    continue
                k = numerator//difference
                if not 0 <= k <= p-use_carrier:
                    continue
                first = [exceptions[j] for j in range(len(exceptions)) if mask >> j & 1]
                first += background[:p-count]
                chosen = set(first+[singleton])
                second = [i for i in range(n) if i not in chosen]
                zero_group = first[:k]+second[:p-use_carrier-k]
                if use_carrier:
                    zero_group.append(singleton)
                ledger = Ledger(values, p)
                ledger.average_indices(first)
                ledger.average_indices(second)
                ledger.average_indices(zero_group)
                assert all(ledger.state[i] == 0 for i in zero_group)
                ledger.finish_from_zero()
                return [list(group) for group in ledger.groups]
    return None


def structured_search():
    rng, records = Random(2026091218), []
    for p in (7, 19, 37):
        for lift_bound in (2, 64, 10**6, 2**64):
            successes, candidates = [], []
            attempts = 0
            while len(candidates) < 48:
                attempts += 1
                length = rng.randrange(3, min(p-1, 6)+1)
                cuts = sorted(rng.sample(range(1, p-1), length-1))
                residue_parts = [b-a for a, b in zip([0]+cuts, cuts+[p-1])]
                lifts = [rng.randint(-lift_bound, lift_bound) for _ in range(length-1)]
                lifts.append(-3-sum(lifts))
                light = [1+r+p*z for r, z in zip(residue_parts, lifts)]
                if gcd(*(x-1 for x in light)) != 1:
                    continue
                assert zero_free([x-1 for x in light], p)
                path = disjoint_two_step_escape(p, light)
                candidates.append({'background': 1, 'frequency': 2*p+1-length,
                                   'light': light, 'three_step_zero_path': path})
                if path is not None:
                    successes.append(len(path))
            records.append({'p': p, 'n': 2*p+1, 'lift_bound': str(lift_bound),
                            'accepted': len(candidates), 'generation_attempts': attempts,
                            'two_preparation_steps_certified': len(successes),
                            'outside_two_preparation_horizon': len(candidates)-len(successes),
                            'candidates': candidates})
    return {'sampling': 'Structured frozen inputs: positive residue composition of p-1; '
                        'first L-1 lifts uniform in [-B,B], final lift enforces sum=-3; G=1 filter.',
            'warning': 'Outside the two-step preparation horizon means unknown, not unreachable.',
            'records': records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modulus', type=int)
    parser.add_argument('--n', type=int, default=15)
    parser.add_argument('--p', type=int, default=7)
    parser.add_argument('--structured', action='store_true')
    args = parser.parse_args()
    if args.structured:
        report = structured_search()
        path = ROOT / 'endpoint_reverse_structured_inputs.json'
        for r in report['records']:
            print(json.dumps({k: v for k, v in r.items() if k != 'candidates'}), flush=True)
    else:
        report = modular_audit(args.p, args.n, args.modulus)
        path = ROOT / ('endpoint_reverse_mod%d_n%d_p%d.json' %
                       (args.modulus, args.n, args.p))
        print(json.dumps(report), flush=True)
    path.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
