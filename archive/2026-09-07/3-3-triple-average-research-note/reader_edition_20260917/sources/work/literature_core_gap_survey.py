"""Targeted public bibliographic queries; cache metadata, not theorem claims."""

import argparse
import json
from pathlib import Path
import urllib.parse
import urllib.request
import sys

ROOT=Path(__file__).parent/'core_gap_literature_20260914'
QUERIES=[
    'odd odd continued fractions',
    'continued fractions congruence restrictions',
    'Farey subgraphs continued fractions',
    'N continued fractions rational numbers',
    'Euclidean algorithm division chains number rings',
    'Cooke Weinberger division chains',
    'local global principle Zaremba conjecture',
    'paired Jacobsthal function',
    'Jacobsthal function reduced residues gaps',
    'congruence subgroup continued fraction algorithms',
    'generalized continued fractions even numerators',
    'recurrent control Lyapunov switching',
    'Euclidean minima localized integers',
    'Farey graph congruence subgroups connectivity',
    'continued fractions restricted denominators rational approximation',
    'covering systems multiplicative orders',
]
TITLE_FILTERS={
    8:'Jacobsthal',9:'continued fractions',10:'continued fractions',
    11:'recurrent control Lyapunov',12:'Euclidean',13:'Farey',
    14:'continued fractions',15:'covering',
}


def query(index):
    phrase=QUERIES[index]
    path=ROOT/('query_%02d.json'%index)
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    params={'search':phrase,'per-page':'7',
            'select':'id,title,publication_date,doi,authorships,abstract_inverted_index,primary_location,open_access'}
    if index in TITLE_FILTERS:
        params['filter']='title.search:'+TITLE_FILTERS[index]
    url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
    result={'query':phrase,'url':url}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'AveragingMathematicsResearch/1.0'})
        with urllib.request.urlopen(request,timeout=18) as response:
            data=json.load(response)
        result['count']=data['meta']['count']
        result['results']=data['results']
    except Exception as exc:
        result['error']=str(exc)
    ROOT.mkdir(exist_ok=True)
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser()
    parser.add_argument('index',type=int)
    index=parser.parse_args().index
    data=query(index)
    brief={'index':index,'query':data['query'],'count':data.get('count'),'error':data.get('error'),
           'results':[{'title':x['title'],'doi':x['doi'],'date':x['publication_date'],
                       'url':(x.get('primary_location') or {}).get('landing_page_url'),
                       'pdf':(x.get('primary_location') or {}).get('pdf_url')}
                      for x in data.get('results',[])]}
    print(json.dumps(brief,ensure_ascii=False))
