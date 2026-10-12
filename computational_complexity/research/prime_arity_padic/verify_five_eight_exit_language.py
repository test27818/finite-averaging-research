"""Independent literal replay and finite checks of the exit-language theorem.

No successful-tail or full-P claim is inferred from family membership.
The infinite cardinality, earliest-time and decoder bounds are proved in the note.
"""
from collections import Counter, deque
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json

from five_eight_exit_language import source, encode, decode, encode_pair, decode_pair, physical_word
from five_eight_exit_language import (singleton_source, encode_singleton_pair, decode_singleton_pair,
                                      encode_singletons, decode_singletons)
from verify_subcritical_uniform_np_hard import integer_oracle, primitive


def literal_step(state, letter):
    """Perform an actual selected five-position average, without rescaling."""
    a, b, c, d = state
    values = (a,) * 5 + (b, c, d)
    if letter == 'S1':
        selected, retained = (0, 1, 2, 3, 5), (4, 6, 7)
    elif letter == 'S2':
        selected, retained = (0, 1, 2, 3, 6), (5, 4, 7)
    elif letter == 'E0':
        selected, retained = (0, 1, 2, 3, 7), (4, 5, 6)
    else:
        raise ValueError(letter)
    total = sum(values[i] for i in selected)
    assert total % 5 == 0 and len({values[i] for i in selected}) > 1
    result = (total // 5,) + tuple(values[i] for i in retained)
    raw = (result[0],) * 5 + result[1:]
    assert sum(raw) == 0 and gcd(*raw) == 1
    assert gcd(*(v - raw[0] for v in raw)) == 1
    assert sum(v * v for v in raw) < sum(v * v for v in values)
    return result


def replay(word):
    k = len(word)
    initial = source(k)
    state = (initial[0],) + initial[5:]
    d = state[3]
    letters = physical_word(word)
    for i, letter in enumerate(letters):
        assert (letter == 'E0') == (i == len(letters) - 1)
        state = literal_step(state, letter)
        if letter != 'E0':
            assert state[3] == d
    raw = tuple(sorted((state[0],) * 5 + state[1:]))
    assert raw == encode(word)
    return raw, len(letters)


def oracle_witness(state, edges, distance):
    """Recover and literally replay a shortest unscaled physical witness."""
    current = tuple(sorted(state))
    path = [current]
    while any(current):
        core = primitive(current)
        target = next(y for y in edges(core)
                      if distance(y) is not None and distance(y) == distance(core) - 1)
        from itertools import combinations
        for selected in combinations(range(8), 5):
            total = sum(current[i] for i in selected)
            if total % 5:
                continue
            indices = set(selected)
            raw = tuple(sorted(total // 5 if i in indices else current[i] for i in range(8)))
            if raw != current and primitive(raw) == target:
                assert sum(raw) == 0
                assert sum(v * v for v in raw) < sum(v * v for v in current)
                current = raw
                path.append(current)
                break
        else:
            raise AssertionError('oracle edge could not be physically replayed')
    return path


def main():
    levels = []
    atoms = 0
    for k in range(9):
        endpoints = set()
        for word in product((1, 2), repeat=k):
            endpoint, count = replay(word)
            atoms += count
            assert decode(endpoint, k) == word
            assert decode(reversed(endpoint)) == word
            assert decode(endpoint, k + 1) is None
            endpoints.add(endpoint)
        assert len(endpoints) == 2 ** k
        levels.append({'k': k, 'distinct_earliest_endpoints': len(endpoints),
                       'prefix_length': 2 * k + 2})

    singleton_levels = []
    singleton_atoms = 0
    for length in range(1, 14):
        endpoints = set()
        for tail in product((1, 2), repeat=length - 1):
            word = (1,) + tail  # Exchange of the two exception labels is quotiented.
            raw_initial = singleton_source(length)
            state = (raw_initial[0],) + raw_initial[5:]
            for letter in tuple('S' + str(b) for b in word) + ('E0',):
                state = literal_step(state, letter)
                singleton_atoms += 1
                if letter != 'E0':
                    assert state[3] == raw_initial[-1]
            raw = tuple(sorted((state[0],) * 5 + state[1:]))
            assert raw == encode_singletons(word)
            assert decode_singletons(raw, length) == word
            assert decode_singletons(raw, length + 1) is None
            assert encode_singletons(tuple(3 - b for b in word)) == raw
            endpoints.add(raw)
        assert len(endpoints) == 2 ** (length - 1)
        singleton_levels.append({'length': length, 'distinct_earliest_endpoints': len(endpoints),
                                 'prefix_length': length + 1})

    general_pair_checks = []
    pair_height = 150
    for p in (3, 5, 7, 9, 11, 15, 31):
        orbit = {(1, 1): ()}
        queue = deque([(1, 1)])
        while queue:
            u, v = queue.popleft()
            for b, child in ((1, (-u, p * v - u)), (2, (p * u - v, -v))):
                if max(map(abs, child)) > pair_height:
                    continue
                assert child not in orbit
                orbit[child] = orbit[(u, v)] + (b,)
                queue.append(child)
        for u in range(-pair_height, pair_height + 1):
            for v in range(-pair_height, pair_height + 1):
                assert decode_singleton_pair(u, v, p) == orbit.get((u, v)), (p, u, v)
        general_pair_checks.append({'p': p, 'candidates': (2 * pair_height + 1) ** 2,
                                    'orbit_members': len(orbit)})
    long_run = (1,) * 1000 + (2,) * 700 + (1, 2) * 150
    long_pair = encode_singleton_pair(long_run)
    assert decode_singleton_pair(*long_pair) == long_run

    # Exhaustive bounded pair-language comparison. Both forward generators
    # strictly increase max(x,y), so no orbit point within the box is omitted.
    height = 500
    reachable = {(1, 4): ()}
    queue = deque([(1, 4)])
    while queue:
        x, y = queue.popleft()
        for b, child in ((1, (x, 4 * x + 25 * y)), (2, (25 * x + 4 * y, y))):
            if max(child) > height:
                continue
            assert child not in reachable
            reachable[child] = reachable[(x, y)] + (b,)
            queue.append(child)
    for x in range(1, height + 1):
        for y in range(1, height + 1):
            assert decode_pair(x, y) == reachable.get((x, y))

    rng = Random(20261011)
    large = []
    for k in (100, 1000):
        word = tuple(rng.choice((1, 2)) for _ in range(k))
        endpoint, count = replay(word)
        atoms += count
        assert decode(endpoint, k) == word
        large.append({'k': k, 'encoded_exits': f'2^{k}',
                      'endpoint_height_bits': max(abs(v) for v in endpoint).bit_length(),
                      'decoded_letters': len(word), 'literal_atoms': count})

    # Independent full graph proves both semantic boundaries on small inputs.
    edges, distance = integer_oracle(5, 8)
    mixed = []
    for word in ((1,), (2,)):
        state = encode(word)
        d = distance(primitive(state))
        row = {'word': word, 'endpoint': state, 'full_distance': d}
        if d is not None:
            row['unscaled_success_path'] = oracle_witness(state, edges, distance)
            assert len(row['unscaled_success_path']) == d + 1
        mixed.append(row)
    assert [row['full_distance'] for row in mixed] == [None, 6]
    k = 2
    family_distances = [distance(primitive(encode(w))) for w in product((1, 2), repeat=k)]
    assert all(d is None for d in family_distances)
    source_distance = distance(primitive(source(k)))
    assert source_distance == 15
    incomplete = {'k': k, 'source': source(k), 'source_distance': source_distance,
                  'all_four_family_exits_unsolvable': True,
                  'unscaled_success_path': oracle_witness(source(k), edges, distance)}
    assert len(incomplete['unscaled_success_path']) == 16

    # Even the entire singleton-then-E0 family can omit all successful exits.
    length = 8
    all_singleton_distances = [distance(primitive(encode_singletons((1,) + tail)))
                              for tail in product((1, 2), repeat=length - 1)]
    assert all(d is None for d in all_singleton_distances)
    raw_source = singleton_source(length)
    assert distance(primitive(raw_source)) == 15
    singleton_incomplete = {'length': length, 'source': raw_source,
                            'source_distance': 15, 'rejected_family_exits': 128,
                            'unscaled_success_path': oracle_witness(raw_source, edges, distance)}
    assert len(singleton_incomplete['unscaled_success_path']) == 16

    record = {'scope': 'Earliest G=1 outside-exit family, not full consensus decision.',
              'levels': levels, 'total_literal_atoms': atoms,
              'singleton_levels': singleton_levels, 'singleton_literal_atoms': singleton_atoms,
              'general_pair_checks': general_pair_checks,
              'long_singleton_word_length': len(long_run),
              'long_singleton_pair_bits': max(abs(x) for x in long_pair).bit_length(),
              'bounded_pair_candidates': height * height,
              'bounded_pair_members': len(reachable), 'large': large,
              'mixed_outcomes': mixed, 'family_not_complete': incomplete,
              'singleton_family_not_complete': singleton_incomplete,
              'independent_full_oracle_states': distance.cache_info().currsize}
    destination = Path(__file__).with_name('five_eight_exit_language_verification.json')
    destination.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in record.items() if k not in (
        'levels', 'singleton_levels', 'mixed_outcomes', 'family_not_complete', 'singleton_family_not_complete')},
                     ensure_ascii=False, indent=2))
    print('Macro levels 0..8, singleton lengths 1..13, and complete counterexample DAGs passed.')


if __name__ == '__main__':
    main()
