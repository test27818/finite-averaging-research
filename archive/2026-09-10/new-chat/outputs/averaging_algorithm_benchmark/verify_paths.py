"""Verify p-average paths with exact rationals. Python standard library only.

Input coordinates are strings; operation indices are one-based original labels.
Run --self-check for saved reference paths, or --solutions solver_output.json.
"""

import argparse
from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
NUMBER = re.compile(r'-?\d+(?:/[1-9]\d*)?\Z')

if not __debug__:
    raise RuntimeError('Run without -O: self-check assertions are required.')


def rational(value):
    if type(value) is int:
        return Fraction(value)
    if isinstance(value, str) and NUMBER.fullmatch(value):
        return Fraction(value)
    raise ValueError('Coordinates must be integer or a/b strings; floats are forbidden.')


def verify_path(case, operations):
    if not isinstance(operations, list):
        raise ValueError('operations must be a list')
    p, n = case['p'], case['n']
    state = [rational(x) for x in case['input']]
    if type(p) is not int or type(n) is not int or len(state) != n or not 2 <= p <= n:
        raise ValueError('invalid case dimensions')
    total = sum(state)
    target = total/n
    initial_energy = sum((x-target)**2 for x in state)
    energy = initial_energy
    first_target = 0 if target in state else None
    maximum_denominator = max(x.denominator for x in state)
    maximum_numerator_bits = max(abs(x.numerator).bit_length() for x in state)
    nonintegral_steps = unchanged_steps = 0
    for step, group in enumerate(operations, 1):
        if not isinstance(group, list) or len(group) != p:
            raise ValueError('step %d: exactly p=%d indices required' % (step, p))
        if any(type(i) is not int or not 1 <= i <= n for i in group):
            raise ValueError('step %d: indices must be integers in [1,n]' % step)
        if len(set(group)) != p:
            raise ValueError('step %d: repeated position' % step)
        old = [state[i-1] for i in group]
        mean = sum(old)/p
        unchanged_steps += int(all(x == mean for x in old))
        nonintegral_steps += int(mean.denominator != 1)
        loss = sum((x-mean)**2 for x in old)
        energy -= loss
        for i in group:
            state[i-1] = mean
        if mean == target and first_target is None:
            first_target = step
        maximum_denominator = max(maximum_denominator, mean.denominator)
        maximum_numerator_bits = max(maximum_numerator_bits, abs(mean.numerator).bit_length())
    if sum(state) != total:
        raise ValueError('sum changed')
    if any(x != target for x in state):
        raise ValueError('path stops before every position reaches the original mean')
    if energy != 0:
        raise ValueError('inconsistent final energy')
    denominator = maximum_denominator
    exponent = 0
    while denominator % p == 0 and denominator > 1:
        denominator //= p
        exponent += 1
    return {'status': 'valid', 'steps': len(operations), 'target': str(target),
            'first_target_coordinate_step': first_target,
            'nonintegral_mean_steps': nonintegral_steps, 'unchanged_steps': unchanged_steps,
            'max_denominator': str(maximum_denominator),
            'max_denominator_bits': maximum_denominator.bit_length(),
            'max_p_denominator_exponent': exponent if denominator == 1 else None,
            'max_mean_numerator_bits': maximum_numerator_bits}


def load_cases(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    cases = {}
    for case in data['cases']:
        if case['id'] in cases:
            raise ValueError('duplicate case id')
        cases[case['id']] = case
    return cases


def evaluate(cases, submitted, metadata):
    answers = submitted.get('solutions')
    if not isinstance(answers, list):
        raise ValueError('submission must contain a solutions list')
    seen, results = set(), []
    for answer in answers:
        case_id = answer.get('case_id')
        if case_id not in cases or case_id in seen:
            raise ValueError('unknown or repeated case_id: '+str(case_id))
        seen.add(case_id)
        expected = metadata.get(case_id, {}).get('expected_reachable')
        if answer.get('status') == 'not_found':
            result = {'status': 'not_found'}
        elif answer.get('status') == 'unreachable':
            result = {'status': 'known_negative_correct' if expected is False
                      else 'incorrect_or_unsupported_unreachability'}
        else:
            try:
                result = verify_path(cases[case_id], answer.get('operations'))
                if expected is False:
                    result['ground_truth_conflict'] = True
            except (ValueError, TypeError, KeyError) as exc:
                result = {'status': 'invalid', 'error': str(exc)}
        results.append({'case_id': case_id, **result})
    return {'counts': dict(Counter(r['status'] for r in results)), 'results': results,
            'not_submitted': sorted(set(cases)-seen)}


def check_rejections(cases, references):
    sample = next(x for x in references['solutions'] if x.get('operations'))
    case = cases[sample['case_id']]
    groups = sample['operations']
    bad = []
    duplicate = [list(x) for x in groups]
    duplicate[0][0] = duplicate[0][1]
    bad.append(duplicate)
    zero_index = [list(x) for x in groups]
    zero_index[0][0] = 0
    bad.append(zero_index)
    floating = [list(x) for x in groups]
    floating[0][0] = float(floating[0][0])
    bad.append(floating)
    bad.append([groups[0][:-1]]+groups[1:])
    bad.append([])
    for operations in bad:
        try:
            verify_path(case, operations)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid test unexpectedly accepted')
    try:
        rational(9007199254740992.0)
    except ValueError:
        pass
    else:
        raise AssertionError('floating coordinate accepted')
    assert rational('113667993707972565752') == 113667993707972565752
    return len(bad)+2


def check_input_invariants(cases, metadata):
    frozen = 0
    unique = set()
    for case_id, case in cases.items():
        values = [rational(x) for x in case['input']]
        p, n = case['p'], case['n']
        assert len(values) == n and all(x.denominator == 1 for x in values)
        values = list(map(int, values))
        key = p, tuple(sorted(values))
        assert key not in unique
        unique.add(key)
        meta = metadata[case_id]
        total = sum(values)
        centered = [n*x-total for x in values]
        common = gcd(*centered)
        g = None
        if common:
            centered = [x//common for x in centered]
            g = gcd(*(x-centered[0] for x in centered))
        assert g == meta['G']
        if 'fractions_required' in meta['tags']:
            counts = Counter(values)
            a, frequency = counts.most_common(1)[0]
            assert frequency >= p+2 and total == 0 and gcd(*values) == 1 and g == 1
            labels = [x-a for x in values if x != a]
            reached, mask = 1, (1 << p)-1
            for label in labels:
                label %= p
                new = ((reached << label) | (reached >> (p-label))) & mask
                assert not new & 1
                reached |= new
            frozen += 1
    return len(cases), frozen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', type=Path, default=ROOT/'cases.json')
    parser.add_argument('--solutions', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--self-check', action='store_true')
    args = parser.parse_args()
    cases = load_cases(args.cases)
    manifest = json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    metadata = {x['case_id']: x for x in manifest['case_metadata']}
    path = ROOT/'reference_solutions.json' if args.self_check else args.solutions
    if path is None:
        parser.error('provide --solutions or --self-check')
    references = json.loads(path.read_text(encoding='utf-8'))
    report = evaluate(cases, references, metadata)
    if args.self_check:
        report['input_invariants'] = check_input_invariants(cases, metadata)
        assert all(x['status'] in ('valid', 'known_negative_correct') for x in report['results']), report
        report['rejection_tests'] = check_rejections(cases, references)
        print('reference paths and known negative control: PASS', report['counts'])
        print('strict rational and invalid-path guards: PASS', report['rejection_tests'])
        print('unique input and frozen-state invariants: PASS', *report['input_invariants'])
    else:
        print(json.dumps({'counts': report['counts'],
                          'not_submitted_count': len(report['not_submitted'])}, ensure_ascii=False))
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    if any(x['status'] in ('invalid', 'incorrect_or_unsupported_unreachability')
           for x in report['results']):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
