"""Cache a public paper only after checking its content type and PDF header."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT=Path(__file__).parent/'core_gap_literature_20260914'


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('url')
    args=parser.parse_args()
    if not args.name.replace('_','').isalnum():
        raise ValueError('Use a simple document label.')
    ROOT.mkdir(exist_ok=True)
    result={'url':args.url,'label':args.name}
    try:
        request=urllib.request.Request(args.url,headers={'User-Agent':'AveragingMathematicsResearch/1.0'})
        with urllib.request.urlopen(request,timeout=25) as response:
            content=response.read(20_000_001)
            result.update({'final_url':response.url,'content_type':response.headers.get('Content-Type')})
        if len(content)>20_000_000:
            raise ValueError('Paper exceeded the20MB document limit.')
        result.update({'bytes':len(content),'sha256':sha256(content).hexdigest()})
        if content.startswith(b'%PDF-'):
            path=ROOT/(args.name+'.pdf')
            path.write_bytes(content)
            subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
            result['text']=str(path.with_suffix('.txt'))
        else:
            path=ROOT/(args.name+'.html')
            path.write_bytes(content)
            result['not_pdf']=True
    except Exception as exc:
        result['error']=str(exc)
    (ROOT/(args.name+'_source.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
