"""Targeted public bibliography queries; save URLs, errors, and raw results."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import sys
import requests

ROOT = Path(__file__).parent
QUERIES = [
    'clique gossiping',
    'perfect mixability',
    'ternary mixing',
    'integral points orbits semigroups',
    'integral points orbits rational functions',
    'S-unit orbits semigroup',
    'intersection orbits semigroups',
    'p-adic continued fractions quadratic',
    'Ruban continued fractions periodicity',
    'linear fractional semigroups',
    'rational points Cantor p-adic',
    'Pell equation matrix semigroup',
]

def query(item):
    idx, term = item
    try:
        response = requests.get('https://api.openalex.org/works', params={
            'filter': 'title.search:' + term, 'per-page': 6,
            'select': 'id,title,doi,publication_year,open_access,locations'}, timeout=35)
        response.raise_for_status()
        data = {'query': term, 'url': response.url,
                'results': response.json().get('results', [])}
    except Exception as exc:
        data = {'query': term, 'error': str(exc)}
    (ROOT / f'targeted_query_{idx:02d}.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    return idx, data

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    with ThreadPoolExecutor(max_workers=6) as pool:
        for idx, data in pool.map(query, enumerate(QUERIES)):
            print(idx, data['query'], data.get('error', ''))
            for work in data.get('results', []):
                pdfs = [loc.get('pdf_url') for loc in work.get('locations', [])
                        if loc.get('pdf_url')]
                print(' ', work['publication_year'], work['title'], work.get('doi'), pdfs[:2])
