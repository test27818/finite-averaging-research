"""Budgeted rational paths for deterministically selected frozen candidates.

Reuses the existing value-pattern beam selector with q=7 and its independent
labelled Fraction verifier. No failure is interpreted as nonreachability.
"""

from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path
from time import perf_counter

from explore_five_average_n11 import search, verify_operations

ROOT = Path(__file__).parent
OPTIONS = {'q': 7, 'seconds': 8, 'max_nodes': 3000, 'width': 96,
           'max_depth': 24, 'mode': 'beam'}


def worker(item):
    metadata, raw = item
    result = search(raw, **OPTIONS)
    if result['status'] == 'solved':
        verify_operations(raw, result['operations'], 7)
    result['selection'] = metadata
    return result


if __name__ == '__main__':
    data = json.loads((ROOT/'endpoint_reverse_structured_inputs.json').read_text(encoding='utf-8'))
    tasks = []
    for record in data['records']:
        if record['p'] != 7:
            continue
        unproved = [x for x in record['candidates'] if x['three_step_zero_path'] is None][:2]
        for index, candidate in enumerate(unproved):
            tasks.append(({'lift_bound': record['lift_bound'], 'first_unproved_index': index},
                          [candidate['background']]*candidate['frequency']+candidate['light']))
    started = perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(worker, tasks))
    for result in results:
        print(json.dumps({key: result[key] for key in
              ('selection', 'status', 'steps', 'expanded', 'generated', 'reason')}), flush=True)
    report = {'settings': OPTIONS, 'workers': 4, 'wall_seconds': perf_counter()-started,
              'selection': 'First two outside-horizon p7 inputs per lift scale from the saved sample.',
              'warning': 'Resource limits and beam omissions mean unknown, never nonreachability.',
              'results': results}
    (ROOT/'endpoint_reverse_candidate_paths.json').write_text(
        json.dumps(report, indent=2)+'\n', encoding='utf-8')
