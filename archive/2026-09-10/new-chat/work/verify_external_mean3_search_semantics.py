"""Focused search-semantics review; no large enumeration or deep search."""

from collections import deque
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import json
import sys

from verify_external_mean3_review import load_readonly, SOURCE, OUT

sys.dont_write_bytecode = True


def physical_shape(values):
    lower = min(values)
    differences = [F(x)-lower for x in values]
    denominator = lcm(*(x.denominator for x in differences))
    content = gcd(*(int(x*denominator) for x in differences))
    if not content:
        return None
    step = F(content, denominator)
    return [int(x/step) for x in differences]


def replay_normalized_moves(raw, moves):
    state = list(map(F, raw))
    target = sum(state)/len(state)
    records = []
    for normalized in moves:
        shape = physical_shape(state)
        assert shape is not None
        group = []
        for value in normalized:
            index = next(i for i, x in enumerate(shape) if x == value and i not in group)
            group.append(index)
        selected = [state[i] for i in group]
        mean = sum(selected)/3
        for i in group:
            state[i] = mean
        assert sum(state) == len(raw)*target
        records.append({'normalized_values': list(normalized),
                        'original_positions_1based': [i+1 for i in group],
                        'physical_values': list(map(str, selected)),
                        'mean': str(mean), 'state': list(map(str, state))})
    assert state == [target]*len(raw)
    return records


def independent_closed_component(raw):
    initial = tuple(sorted(physical_shape(list(map(F, raw)))))
    frontier = deque([initial])
    seen, edges = {initial}, {}
    while frontier:
        current = frontier.popleft()
        successors = set()
        for indices in combinations(range(len(current)), 3):
            selected = [current[i] for i in indices]
            if len(set(selected)) == 1:
                continue
            result = list(map(F, current))
            mean = sum(result[i] for i in indices)/3
            for i in indices:
                result[i] = mean
            shape = physical_shape(result)
            assert shape is not None
            next_state = tuple(sorted(shape))
            successors.add(next_state)
            if next_state not in seen:
                seen.add(next_state)
                frontier.append(next_state)
        edges[current] = sorted(successors)
        assert len(seen) <= 20
    assert all(t in seen for values in edges.values() for t in values)
    return [{'state': list(s), 'all_nonconstant_successors': [list(t) for t in ts]}
            for s, ts in sorted(edges.items())]


def main():
    lib = load_readonly('review_numerical_kmean', 'kmean.py')
    fast = load_readonly('review_numerical_fast', 'kmean_fast.py')
    ida = load_readonly('review_numerical_idas', 'idas.py')
    raw = [0]*5+[1, 13]
    shown = [(0, 0, 13), (0, 0, 3), (1, 1, 13), (0, 5, 13),
             (4, 5, 12), (0, 5, 7), (0, 0, 3), (0, 0, 3)]
    records = replay_normalized_moves(raw, shown)
    # The literal interpretation fails at move2: the current values contain no3.
    assert records[0]['mean'] == '13/3'
    assert '3' not in records[0]['state']
    assert records[-1]['state'] == ['2']*7
    max_denominator = max(F(x).denominator for record in records for x in record['state'])
    assert max_denominator == 3
    print('displayed eight-step path physically reconstructed: PASS', len(records), max_denominator)

    witness = [0]*3+[1]*3+[2]*3
    no_path, reason = ida.solve(witness, k=3, max_depth=1, time_cap=1)
    assert no_path is None and 'exhausted to depth 1' in reason
    assert lib.decide_bfs(witness, k=3, max_depth=1)[0] is None
    path, solved = lib.solve(witness, k=3, max_depth=3, time_cap=2)
    assert path is not None and len(path) == 3
    reconstructed = replay_normalized_moves(witness, [values for state, values in path])
    # Execute the actual wrapper with its original import dependencies.
    sys.path.insert(0, str(SOURCE))
    wrapper = load_readonly('review_numerical_exp4', 'exp4.py')
    output = StringIO()
    with redirect_stdout(output):
        wrapper.run(3, 9, 2, 1, 1)
    wrapper_text = output.getvalue()
    assert 'MC-true-unsolvable=' in wrapper_text
    assert 'MC-true-unsolvable=0' not in wrapper_text
    print('old depth-limited wrapper false-negative label demonstrated: PASS')

    component = independent_closed_component([0, 1, 3, 4])
    assert lib.decide_bfs([0, 1, 3, 4], max_depth=6)[0] is False
    assert fast.decide([0, 1, 3, 4], k=3, cap=1000) is False
    assert fast.decide(witness, k=3, cap=10000) is True
    cache_path = fast.find_solution(witness, k=3)
    assert len(cache_path) == 1 and len(set(cache_path[0])) > 1
    print('closed-component negative proof and cached-positive certificate gap: PASS', len(component))

    # Test exact transition semantics on a small range, independent of search.
    transition_checks = 0
    for state in ((0, 1, 3, 4), (0, 0, 1, 2, 6), (0, 1, 2, 3, 5, 7)):
        canonical = fast.canon(state)
        expected = set()
        for group in combinations(range(len(canonical)), 3):
            values = list(map(F, canonical))
            if len({values[i] for i in group}) == 1:
                continue
            mean = sum(values[i] for i in group)/3
            for i in group:
                values[i] = mean
            shape = physical_shape(values)
            if shape is not None:
                direct = tuple(sorted(shape))
                reflection = tuple(sorted(max(shape)-x for x in shape))
                expected.add(min(direct, reflection))
            else:
                # These cases are selected to avoid all-constant outputs.
                raise AssertionError('Unexpected terminal')
        assert fast.successors(canonical, k=3) == expected
        transition_checks += len(expected)
    print('fast ternary transition against literal Fraction averages: PASS', transition_checks)

    (OUT/'external_mean3_search_semantics_checks.json').write_text(json.dumps({
        'scope': 'Selected exact tests of the current ternary search implementation; no all-input or precision theorem.',
        'displayed_path_reconstructed': records,
        'maximum_path_denominator': max_denominator,
        'depth_failure_on_solvable_input': {'input': witness, 'result': reason,
                                            'three_step_witness': reconstructed},
        'old_wrapper_output': wrapper_text,
        'closed_n4_component': component,
        'cached_positive_path': [list(x) for x in cache_path],
        'ternary_transition_checks': transition_checks}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('external small-n numerical-method audit: PASS')


if __name__ == '__main__':
    main()
