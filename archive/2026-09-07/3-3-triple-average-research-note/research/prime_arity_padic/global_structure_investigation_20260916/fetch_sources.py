"""Fetch identified open scholarly sources, retaining provenance and failures."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import requests

ROOT = Path(__file__).parent
SOURCES = [
    ('reachability_sl2_2016', 'https://drops.dagstuhl.de/storage/00lipics/lipics-vol058-mfcs2016/LIPIcs.MFCS.2016.84/LIPIcs.MFCS.2016.84.pdf'),
    ('low_dimensional_semigroups_2019', 'https://drops.dagstuhl.de/storage/00lipics/lipics-vol132-icalp2019/LIPIcs.ICALP.2019.44/LIPIcs.ICALP.2019.44.pdf'),
    ('parametric_presburger_2017', 'https://discreteanalysisjournal.com/article/1254.pdf'),
    ('presburger_quantifiers_2025', 'https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/LIPIcs.MFCS.2025.72/LIPIcs.MFCS.2025.72.pdf'),
    ('generalized_flatness_2021', 'https://link.springer.com/content/pdf/10.1007/s00229-021-01363-x.pdf'),
    ('barany_lattice_survey_2008', 'https://real.mtak.hu/57662/1/rsurv.pdf'),
    ('parametric_integer_1988', 'https://www.rairo-ro.org/articles/ro/pdf/1988/03/ro1988220302431.pdf'),
]

def fetch(item):
    name, url = item
    record = {'name': name, 'requested_url': url}
    try:
        response = requests.get(url, timeout=30)
        record.update(status=response.status_code, final_url=response.url,
                      content_type=response.headers.get('content-type'),
                      bytes=len(response.content), sha256=sha256(response.content).hexdigest())
        if response.status_code == 200 and response.content.startswith(b'%PDF'):
            pdf = ROOT / (name+'.pdf')
            pdf.write_bytes(response.content)
            subprocess.run(['pdftotext', '-layout', str(pdf), str(ROOT/(name+'.txt'))],
                           check=True, capture_output=True)
            record['pdf_verified'] = True
        else:
            record['pdf_verified'] = False
    except Exception as exc:
        record['error'] = str(exc)
    (ROOT/(name+'_source.json')).write_text(json.dumps(record, indent=2), encoding='utf-8')
    return record

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        for record in pool.map(fetch, SOURCES):
            print(json.dumps(record))
