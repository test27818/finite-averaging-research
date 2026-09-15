"""Fetch identified public mathematical sources and record provenance."""
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from hashlib import sha256
import json,subprocess,sys
from pathlib import Path
import requests

ROOT=Path(__file__).parent/'ht_literature_20260915'
SOURCES=[
 ('pollack_prime_nonres','https://www.ams.org/proc/2017-145-07/S0002-9939-2016-13432-1/S0002-9939-2016-13432-1.pdf'),
 ('norton1972','https://www.ams.org/tran/1972-167-00/S0002-9947-1972-0296034-8/S0002-9947-1972-0296034-8.pdf'),
 ('bach1990','https://www.ams.org/mcom/1990-55-191/S0025-5718-1990-1023756-8/S0025-5718-1990-1023756-8.pdf'),
 ('jain_khale_liu2021','https://arxiv.org/pdf/2010.09530'),
 ('cubefree2025','https://arxiv.org/pdf/2511.17778'),
 ('pollack_home','https://pollack.uga.edu/'),
 ('martin_pollack2012','https://arxiv.org/pdf/1112.1175'),
]

def fetch(item):
    name,url=item;meta=ROOT/(name+'_source.json')
    if meta.exists():return json.loads(meta.read_text(encoding='utf-8'))
    result={'name':name,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
    try:
        r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=(10,25))
        result.update(status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type'));r.raise_for_status()
        raw=r.content
        if len(raw)>25_000_000:raise ValueError('Source exceeds25MB')
        result.update(bytes=len(raw),sha256=sha256(raw).hexdigest())
        if raw.startswith(b'%PDF-'):
            path=ROOT/(name+'.pdf');path.write_bytes(raw)
            out=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],capture_output=True,text=True)
            result['text']=str(path.with_suffix('.txt'));result['conversion_status']=out.returncode
        else:
            (ROOT/(name+'.html')).write_text(r.text,encoding='utf-8');result['not_pdf']=True
    except Exception as e:result['error']=str(e)
    meta.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');ROOT.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        for future in as_completed([ex.submit(fetch,item) for item in SOURCES]):print(json.dumps(future.result(),ensure_ascii=False),flush=True)
