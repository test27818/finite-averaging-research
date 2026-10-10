"""Cached, parallel metadata survey; outputs are leads, not theorem claims."""

from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import sys
import requests

from literature_survey_20260912 import oa_item

ROOT = Path(__file__).parent / 'literature_strategy_20260912'
ROOT.mkdir(exist_ok=True)
QUERIES = [
    'bounded elementary generation',
    'elementary congruence subgroups',
    'Mennicke symbols',
    'Euclidean rings S integers',
    'division chains',
    'continued fractions congruence subgroups',
    'continued fractions restrictions',
    'Jacobian function Jacobsthal',
    'idempotent chains',
    'stochastic matrices factorization',
    'orthogonal projections finite convergence',
    'matrix mortality nonnegative',
    'synchronizing weighted automata',
    'finite time clique gossip',
    'finite time consensus rational',
    'perfect mixability',
    'restricted sumsets sequences',
    'zero sum subsequences same length',
    'subsequence sums multiplicity',
    'zero sum hypergraph',
    'control Lyapunov discrete switching',
    'path complete Lyapunov',
    'continued fractions S arithmetic',
    'strong approximation semigroups',
    'congruence constrained matroid',
    'quadratic forms reduction indefinite',
    'Markov bases bounded fibers',
    'finite convergence paracontractions',
    'even continued fractions',
    'odd continued fractions',
    'Jacobsthal function',
    'elementary generation SL2 congruence',
    'relative SL2',
    'Euclidean algorithm rings integers',
    'stabilizability switched linear systems',
    'S arithmetic groups generation',
    'mixability graphs',
    'Clique Gossiping',
    'zero sum nondispersive',
    'Markov subbases',
    'positive margins Markov bases',
    'restricted continued fractions',
    'Bruhat Tits tree elementary',
    'bounded generation SL2',
]


def query(index):
    phrase = QUERIES[index]
    path = ROOT / ('query_%02d.json' % index)
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    try:
        response = requests.get(
            'https://api.openalex.org/works',
            params={'filter': 'title.search:'+phrase, 'per-page': 7,
                    'select': 'id,title,publication_date,doi,cited_by_count,authorships,abstract_inverted_index,locations,referenced_works'},
            headers={'User-Agent': 'AveragingMathematicsLiteratureReview/1.0'},
            timeout=25)
        response.raise_for_status()
        data = response.json()
        result = {'index': index, 'query': phrase, 'url': response.url,
                  'count': data['meta']['count'],
                  'results': [oa_item(x) for x in data['results']]}
    except Exception as exc:
        result = {'index': index, 'query': phrase, 'error': str(exc)}
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    stop = int(sys.argv[2]) if len(sys.argv) > 2 else len(QUERIES)
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        for future in as_completed([executor.submit(query, i) for i in range(start, stop)]):
            results.append(future.result())
    for result in sorted(results, key=lambda x: x['index']):
        brief = {'index': result['index'], 'query': result['query'],
                 'count': result.get('count'), 'error': result.get('error'),
                 'results': [{k: x[k] for k in ('id', 'title', 'date', 'doi')}
                             for x in result.get('results', [])]}
        print(json.dumps(brief, ensure_ascii=False), flush=True)
