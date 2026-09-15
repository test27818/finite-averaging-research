"""Fetch a bounded list of identified papers and retain source metadata."""

from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import requests

ROOT = Path(__file__).parent / 'literature_strategy_20260912'
ROOT.mkdir(exist_ok=True)
PAPERS = [
    ('morgan_rapinchuk_sury_2018',
     'https://msp.org/ant/2018/12-8/ant-v12-n8-p04-s.pdf'),
    ('control_language_2018',
     'https://hal.science/hal-01677493/document'),
    ('polyhedral_path_2019',
     'https://pureadmin.qub.ac.uk/ws/files/184256484/CDC19_1494_FI.pdf'),
    ('chevalley_uniform_2024',
     'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EAF86BAC28D0B0EA18BCA21EDB2B826D/S0008414X24000713a.pdf/div-class-title-uniform-bounded-elementary-generation-of-chevalley-groups-div.pdf'),
]


def download(item):
    name, url = item
    path = ROOT / (name+'.pdf')
    try:
        if not path.exists():
            response = requests.get(url, timeout=35)
            response.raise_for_status()
            if not response.content.startswith(b'%PDF'):
                raise ValueError('response is not PDF: '+response.text[:80])
            path.write_bytes(response.content)
        digest = sha256(path.read_bytes()).hexdigest()
        text = path.with_suffix('.txt')
        subprocess.run(['pdftotext', '-layout', str(path), str(text)], check=True,
                       capture_output=True)
        result = {'name': name, 'url': url, 'bytes': path.stat().st_size,
                  'sha256': digest, 'text_chars': len(text.read_text(encoding='utf-8'))}
    except Exception as exc:
        result = {'name': name, 'url': url, 'error': str(exc)}
    (ROOT / (name+'_source.json')).write_text(json.dumps(result, indent=2), encoding='utf-8')
    return result


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    with ThreadPoolExecutor(max_workers=4) as executor:
        for result in executor.map(download, PAPERS):
            print(json.dumps(result, ensure_ascii=False), flush=True)
