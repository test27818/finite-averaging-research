"""Cache public search pages and bibliographic leads, not theorem claims."""
import concurrent.futures as cf
from datetime import datetime, timezone
from hashlib import sha256
from html import unescape
import json,re,sys
from pathlib import Path
import requests

ROOT=Path(__file__).parent/'ht_literature_20260915'
QUERIES=[
 'multiplicative group modulo n generated integers square root composite modulus',
 'least character nonresidue composite modulus explicit bound',
 '"t^2+t+1" "generators"',
 '"n^2+n+1" "multiplicative" "group"',
 'Burgess small generators multiplicative group modulo composite integer',
 '"least" "nonresidue" "even character"',
 '"unit group" "small" "generators" Bach',
 '"smallest" "generating set" "modulo" integers',
 '"least character non-residue"',
 '"generators" "sqrt" "modulo n"',
 '"least nonresidue" "composite" Norton',
 '"Phi_3" "units" "generators"',
]
OA_QUERIES=[
 'small generators multiplicative group',
 'least character nonresidue',
 'least character non-residue',
 'least nonresidue composite modulus',
 'explicit Burgess bounds',
 'generating multiplicative group modulo',
 'smallest generators finite fields',
 'least prime in a coset',
 'least primitive root Burgess',
 'small integers generating unit group',
 'bounds explicit estimates elementary number theory Bach',
 'character sums composite moduli explicit',
 'Norton character non-residues',
 'least quadratic nonresidue square root',
 'least prime character nonresidues Pollack',
 'cyclotomic values small generators residue classes',
 'Burgess bounds imprimitive character',
 'generators residue class group unconditional',
 'explicit bounds subgroup least integer',
 'least non-residue arbitrary modulus',
]

def oaquery(i):
    ROOT.mkdir(exist_ok=True)
    phrase=OA_QUERIES[i];cache=ROOT/f'oa_{i:02}.json'
    if cache.exists():return json.loads(cache.read_text(encoding='utf-8'))
    result={'index':i,'query':phrase,'utc':datetime.now(timezone.utc).isoformat()}
    try:
        r=requests.get('https://api.openalex.org/works',params={'search':phrase,'per-page':12},timeout=(10,22))
        result.update(url=r.url,status=r.status_code);r.raise_for_status()
        data=r.json();result['count']=data['meta']['count']
        result['results']=[{k:x.get(k) for k in ('id','title','publication_year','doi','authorships','abstract_inverted_index','locations','referenced_works')} for x in data['results']]
    except Exception as e:result['error']=str(e)
    cache.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result

def clean(s):
    s=re.sub(r'<(script|style)\b[^>]*>.*?</\1>',' ',s,flags=re.S|re.I)
    return re.sub(r'\s+',' ',unescape(re.sub('<[^>]+>',' ',s))).strip()

def query(i):
    ROOT.mkdir(exist_ok=True)
    phrase=QUERIES[i]
    cache=ROOT/f'search_{i:02}.json'
    if cache.exists():return json.loads(cache.read_text(encoding='utf-8'))
    result={'index':i,'query':phrase,'utc':datetime.now(timezone.utc).isoformat()}
    try:
        r=requests.get('https://www.bing.com/search',params={'q':phrase,'count':8},headers={'User-Agent':'Mozilla/5.0'},timeout=(10,30))
        result.update(url=r.url,status=r.status_code)
        r.raise_for_status();raw=r.text
        (ROOT/f'search_{i:02}.html').write_text(raw,encoding='utf-8')
        items=[]
        for block in re.findall(r'<li\b[^>]*class="b_algo"[^>]*>(.*?)</li>',raw,re.S):
            h=re.search(r'<h2[^>]*>(.*?)</h2>',block,re.S)
            links=re.findall(r'<a\b[^>]*href="([^"]+)"',h[1] if h else block)
            items.append({'title':clean(h[1]) if h else '', 'links':links, 'text':clean(block)})
        result['results']=items
        if not items:result['page_text']=clean(raw)[:22000]
    except Exception as e:result['error']=str(e)
    cache.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    mode=sys.argv[1] if len(sys.argv)>1 and sys.argv[1]=='oa' else 'web'
    args=sys.argv[2:] if mode=='oa' else sys.argv[1:]
    start=int(args[0]) if args else 0
    end=int(args[1]) if len(args)>1 else len(OA_QUERIES if mode=='oa' else QUERIES)
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for v in ex.map(oaquery if mode=='oa' else query,range(start,end)):
            brief={k:v.get(k) for k in ('index','query','count','error')}
            brief['results']=[{k:x.get(k) for k in ('title','publication_year','doi')} for x in v.get('results',[])]
            print(json.dumps(brief if mode=='oa' else v,ensure_ascii=False),flush=True)
