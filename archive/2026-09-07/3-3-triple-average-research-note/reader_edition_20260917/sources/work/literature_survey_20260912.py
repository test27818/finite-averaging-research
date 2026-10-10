"""Read-only public scholarly/web retrieval with an auditable local cache."""

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

import requests

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).parent / 'literature_20260912'
ROOT.mkdir(exist_ok=True)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.links, self.skip, self.anchor = [], [], 0, None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'a':
            self.anchor = [attrs.get('href', ''), []]
        if tag in ('p', 'div', 'h1', 'h2', 'h3', 'li', 'br'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip-1)
        if tag == 'a' and self.anchor is not None:
            href, chunks = self.anchor
            self.links.append({'text': ' '.join(''.join(chunks).split()), 'url': href})
            self.anchor = None

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)
            if self.anchor is not None:
                self.anchor[1].append(data)


def fetch(url, params=None):
    key = hashlib.sha256((url+json.dumps(params, sort_keys=True)).encode()).hexdigest()[:16]
    path = ROOT / (key+'.json')
    if path.exists():
        record = json.loads(path.read_text(encoding='utf-8'))
    else:
        response = requests.get(url, params=params, timeout=35,
                                headers={'User-Agent': 'AcademicLiteratureReview/1.0'})
        record = {'url': response.url, 'status': response.status_code,
                  'retrieved': '2026-09-12', 'body': response.text}
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
    if record['status'] != 200:
        raise RuntimeError(f"HTTP {record['status']}: {record['body'][:350]}")
    return record


def abstract(index):
    if not index:
        return None
    positions = {i: word for word, places in index.items() for i in places}
    return ' '.join(positions[i] for i in sorted(positions))


def oa_item(item):
    return {'id': item['id'], 'title': item['title'], 'date': item.get('publication_date'),
            'doi': item.get('doi'), 'citations': item.get('cited_by_count'),
            'authors': [x['author']['display_name'] for x in item.get('authorships', [])],
            'abstract': abstract(item.get('abstract_inverted_index')),
            'locations': [{'url': x.get('landing_page_url'), 'pdf': x.get('pdf_url'),
                           'source': (x.get('source') or {}).get('display_name')}
                          for x in item.get('locations', [])],
            'reference_count': len(item.get('referenced_works') or [])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('oa', 'oa-filter', 'oa-id', 'crossref', 's2', 's2-search', 'bing', 'page'))
    parser.add_argument('query')
    parser.add_argument('--limit', type=int, default=15)
    parser.add_argument('--chars', type=int, default=18000)
    parser.add_argument('--exact', action='store_true')
    parser.add_argument('--since')
    parser.add_argument('--brief', action='store_true')
    args = parser.parse_args()
    if args.mode.startswith('oa'):
        fields = 'id,title,publication_date,doi,cited_by_count,authorships,abstract_inverted_index,locations,referenced_works'
        if args.mode == 'oa-id':
            record = fetch('https://api.openalex.org/works/'+args.query)
            result = oa_item(json.loads(record['body']))
        else:
            query = '"'+args.query+'"' if args.exact else args.query
            params = {'filter': ('title.search:'+query if args.mode == 'oa' else query),
                      'per-page': args.limit, 'select': fields}
            if args.since:
                params['filter'] += ',from_publication_date:'+args.since+',to_publication_date:2026-09-12'
            record = fetch('https://api.openalex.org/works', params)
            data = json.loads(record['body'])
            result = {'count': data['meta']['count'], 'results': [oa_item(x) for x in data['results']]}
    elif args.mode == 'crossref':
        params = {'query.bibliographic': args.query, 'rows': args.limit}
        if args.since:
            params['filter'] = 'from-pub-date:'+args.since+',until-pub-date:2026-09-12'
        record = fetch('https://api.crossref.org/works', params)
        data = json.loads(record['body'])['message']
        result = [{'title': x.get('title'), 'doi': x.get('DOI'), 'date': x.get('published'),
                   'venue': x.get('container-title'), 'citations': x.get('is-referenced-by-count'),
                   'abstract': x.get('abstract'), 'links': x.get('link')}
                  for x in data['items']]
    elif args.mode == 's2-search':
        record = fetch('https://api.semanticscholar.org/graph/v1/paper/search',
                       {'query': args.query, 'limit': args.limit,
                        'fields': 'title,authors,year,venue,externalIds,abstract,citationCount,openAccessPdf'})
        result = json.loads(record['body'])
    elif args.mode == 's2':
        record = fetch('https://api.semanticscholar.org/graph/v1/paper/'+args.query,
                       {'fields': 'title,authors,year,venue,externalIds,abstract,citationCount,openAccessPdf,citations.title,citations.year,citations.externalIds'})
        result = json.loads(record['body'])
    elif args.mode == 'bing':
        query = '"'+args.query+'"' if args.exact else args.query
        record = fetch('https://www.bing.com/search', {'q': query, 'format': 'rss', 'setlang': 'en', 'cc': 'us'})
        root = ET.fromstring(record['body'])
        result = [{tag: node.findtext(tag) for tag in ('title', 'link', 'description')}
                  for node in root.findall('.//item')]
    else:
        record = fetch(args.query)
        page = Page()
        page.feed(record['body'])
        result = {'text': '\n'.join(' '.join(x.split()) for x in ''.join(page.parts).splitlines() if x.strip()),
                  'links': page.links}
        Path(ROOT / (hashlib.sha256(args.query.encode()).hexdigest()[:16]+'.txt')).write_text(
            result['text'], encoding='utf-8')
    if args.brief:
        items = result if isinstance(result, list) else result.get('results', result.get('data', [result]))
        result = [{key: (str(value)[:750] if key == 'abstract' else value)
                   for key, value in item.items()
                   if key in ('id', 'title', 'date', 'year', 'doi', 'externalIds', 'citations', 'abstract')}
                  for item in items]
    print(json.dumps({'source': record['url'], 'result': result}, ensure_ascii=False, indent=2)[:args.chars])


if __name__ == '__main__':
    main()
