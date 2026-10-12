"""Exact checks, not a substitute for the all-prime proofs in the report.

The independent oracle visits the finite INTEGER energy DAG without a depth
cutoff. Its completeness for p < n <= 2p is a previously proved theorem.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
from random import Random
import json


def atom(state, selected):
    assert len(set(selected)) == len(selected)
    result = list(state)
    mean = sum((F(state[i]) for i in selected), F(0))/len(selected)
    for i in selected:
        result[i] = mean
    return tuple(result)


def core_distance(p, u, v):
    if not (u or v):
        return 0
    d = gcd(u, v)
    u, v = u//d, v//d
    count = 0
    while True:
        if u+v == 0:
            return count+1
        old_size = abs(u)+abs(v)
        if u and u % p == 0:
            u, v = -u//p, v-u//p
        elif v and v % p == 0:
            u, v = u-v//p, -v//p
        else:
            return None
        assert gcd(u, v) == 1
        assert abs(u)+abs(v) < old_size
        count += 1


def initial_distance(p, state):
    if not any(state):
        return 0
    best = None
    total = sum(state)
    assert total == 0 and len(state) == p+2
    for i, j in combinations(range(p+2), 2):
        selected_sum = total-state[i]-state[j]
        if selected_sum % p:
            continue
        a = selected_sum//p
        distance = core_distance(p, state[i]-a, state[j]-a)
        if distance is not None:
            value = distance+1
            best = value if best is None else min(best, value)
    return best


def independent_integer_oracle(p):
    choices = tuple(combinations(range(p+2), p))

    @lru_cache(None)
    def distance(state):
        assert sum(state) == 0
        if not any(state):
            return 0
        best = None
        successors = set()
        for selected in choices:
            values = [state[i] for i in selected]
            if min(values) == max(values) or sum(values) % p:
                continue
            mean = sum(values)//p
            new = list(state)
            for i in selected:
                new[i] = mean
            new = tuple(sorted(new))
            assert sum(x*x for x in new) < sum(x*x for x in state)
            successors.add(new)
        for new in successors:
            result = distance(new)
            if result is not None:
                value = result+1
                best = value if best is None else min(best, value)
        return best

    return distance


def compare_complete_algorithms():
    rng = Random(20260916)
    reports = []
    for p in (3, 5, 7, 11):
        oracle = independent_integer_oracle(p)
        initial_count = 0
        for state in combinations_with_replacement(range(-3, 4), p+2):
            if sum(state):
                continue
            assert initial_distance(p, state) == oracle(state), (p, state)
            initial_count += 1
        core_count = 0
        max_steps = 0
        for _ in range(80):
            a, b = rng.randrange(-3, 4), rng.randrange(-12, 13)
            c = -p*a-b
            state = tuple(sorted((a,)*p+(b, c)))
            result = core_distance(p, b-a, c-a)
            assert result == oracle(state), (p, state, result, oracle(state))
            if result is not None:
                max_steps = max(max_steps, result)
            core_count += 1
        reports.append({'p': p, 'initial_multisets': initial_count,
                        'core_samples': core_count, 'oracle_states': oracle.cache_info().currsize,
                        'maximum_core_distance_in_samples': max_steps})
    return reports


def complement_formula():
    rng = Random(516)
    count = 0
    for p in (3, 5, 7):
        for r in range(1, p+1):
            for _ in range(3):
                u = [F(rng.randrange(-10, 11)) for i in range(r)]
                a = -sum(u)/(p+r)
                state = (a,)*p+tuple(a+t for t in u)
                for mask in range(1 << r):
                    chosen = [i for i in range(r) if mask >> i & 1]
                    selected = list(range(p-len(chosen)))+[p+i for i in chosen]
                    literal = atom(state, selected)
                    new_a = a+sum((u[i] for i in chosen), F(0))/p
                    predicted = [(u[i] if i not in chosen else 0)-(new_a-a)
                                 for i in range(r)]
                    complement = [i for i in range(p+r) if i not in selected]
                    observed = [literal[i]-new_a for i in complement]
                    assert sorted(observed) == sorted(predicted)
                    assert all(literal[i] == new_a for i in selected)
                    assert sum(literal) == 0
                    count += 1
    return count


def explicit_paths_and_long_runs():
    atoms = 0
    inverse_checks = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        n = p+2
        state = (1-p,)*p+(p*p-p+1, -1)
        assert sum(state) == 0
        assert not any(state[i]+state[j] == 0 for i, j in combinations(range(n), 2))
        assert core_distance(p, p*p, p-2) == 3
        word = (list(range(p-1))+[p],
                [p-1]+list(range(p-1)),
                [p, p+1]+list(range(p-2)))
        for selected in word:
            state = atom(state, selected)
            atoms += 1
        assert not any(state)
        # Invert a prescribed D1 run; creates success paths of unbounded length.
        u, v = 1, -1
        for length in range(1, 151):
            u, v = -p*u, v-u
            assert gcd(u, v) == 1
            assert core_distance(p, u, v) == length+1
            inverse_checks += 1
    return {'literal_atoms': atoms, 'unbounded_length_formula_checks': inverse_checks}


def inverse_tree():
    checked = 0
    for p in (3, 5, 7, 11, 13):
        layer = [(1, -1)]
        seen = set()
        for depth in range(10):
            assert len(layer) == 2**depth
            for u, v in layer:
                assert gcd(u, v) == 1 and (v-u+2) % p == 0
                key = (u, v) if u > 0 else (-u, -v)
                assert key not in seen
                seen.add(key)
                assert core_distance(p, u, v) == depth+1
                checked += 1
            layer = [z for u, v in layer for z in ((-p*u, v-u), (u-v, -p*v))]
    return checked


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    results = {'complete_oracle_comparison': compare_complete_algorithms(),
               'complement_formula_literal_checks': complement_formula(),
               'paths': explicit_paths_and_long_runs(),
               'distinct_inverse_tree_directions': inverse_tree(),
               'scope': 'Finite exact checks supplement the written all-prime proof; no bit-polynomial claim for r >= 3.'}
    target = Path(__file__).with_name('subcritical_complement_dynamics_verification.json')
    target.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(json.dumps(results, indent=2))
