"""Read-only public literature queries; retain exact metadata and failures."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import json

HERE=Path(__file__).resolve().parent
QUERIES=[
    'p-adic continued fractions rational termination Browkin Ruban',
    'finiteness rational p-adic continued fractions',
    'p-adic precision lattices Caruso Roe Vaccon',
    'finite time consensus clique gossiping averaging',
    'reachability rational two dimensional matrix semigroups',
    'Euclidean algorithm S integers division chains elementary matrices',
]

def query(item):
    i,term=item
    url='https://api.openalex.org/works?'+urlencode({
        'search':term,'per-page':6,
        'select':'id,doi,title,publication_year,authorships,primary_location,open_access,abstract_inverted_index'})
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:
            payload=json.load(r)
        rows=[]
        for x in payload.get('results',[]):
            inv=x.get('abstract_inverted_index') or {}
            positions={k:word for word,ks in inv.items() for k in ks}
            abstract=' '.join(positions[k] for k in sorted(positions))
            rows.append({'title':x['title'],'year':x['publication_year'],'doi':x.get('doi'),
                         'authors':[a['author']['display_name'] for a in x.get('authorships',[])],
                         'location':x.get('primary_location'),'open_access':x.get('open_access'),
                         'abstract':abstract,'openalex':x['id']})
        result={'query':term,'url':url,'status':'metadata_read','results':rows}
    except Exception as e:
        result={'query':term,'url':url,'status':'error','error':str(e)}
    (HERE/f'query_{i:02d}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=6) as pool:
        for result in pool.map(query,enumerate(QUERIES)):
            print(json.dumps({'query':result['query'],'status':result['status'],
                              'error':result.get('error'),
                              'results':[{k:r[k] for k in ['title','year','doi','authors','abstract']}
                                         for r in result.get('results',[])]},ensure_ascii=False))
