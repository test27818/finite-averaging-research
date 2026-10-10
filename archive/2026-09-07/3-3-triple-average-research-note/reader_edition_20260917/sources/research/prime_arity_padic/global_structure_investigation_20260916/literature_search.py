"""Read-only public bibliography search; records both successes and failures."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import sys
import requests

ROOT = Path(__file__).parent
QUERIES = [
    'planar flatness theorem lattice free convex sets lattice width',
    'parametric integer programming two variables continued fractions integer hull',
    'Graver basis bounded fibers augmentation integer programming',
    'Markov bases bounded contingency tables structural zeros',
    'rational subset reachability SL2 Z vector reachability',
    'matrix semigroup reachability rational projective line',
    'Hecke operators cusps Gamma0 U p double cosets',
    'finite time consensus clique gossiping exact averaging',
    'integer decomposition property transportation polytopes additional constraints',
    'flatness theorem integer programming certificates infeasibility',
]
TITLE_QUERIES = [
    'flatness', 'parametric integer programming', 'Graver',
    'Markov bases bounded', 'vector reachability', 'matrix semigroup reachability',
    'finite-time consensus', 'clique gossiping', 'lattice-free sets',
    'integer hull two-dimensional', 'rational subsets', 'Presburger arithmetic',
]

def query(item):
    index, term = item
    url = 'https://api.openalex.org/works'
    params = {'filter': 'title.search:'+term, 'per-page': 5,
              'select': 'id,title,doi,publication_year,open_access,locations'}
    try:
        response = requests.get(url, params=params, timeout=25)
        response.raise_for_status()
        data = response.json()
        payload = {'query': term, 'url': response.url,
                   'results': data.get('results', [])}
    except Exception as exc:
        payload = {'query': term, 'error': str(exc)}
    (ROOT / f'query_{index:02d}.json').write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return index, payload

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(query, enumerate(TITLE_QUERIES, start=10)))
    for index, payload in sorted(results):
        print(index, payload['query'])
        if 'error' in payload:
            print(' ERROR', payload['error'])
        for work in payload.get('results', []):
            pdfs = [loc.get('pdf_url') for loc in work.get('locations', [])
                    if loc.get('pdf_url')]
            print(' ', work['publication_year'], work['title'], work.get('doi'), pdfs[:2])
