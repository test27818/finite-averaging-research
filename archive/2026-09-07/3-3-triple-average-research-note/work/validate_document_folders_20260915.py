"""Check the actual migrated tree, Markdown targets and registry references."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote
from run_verifications import load_manifest

ROOT=Path(__file__).resolve().parent.parent
RECORD=ROOT/'work/document_reorganization_20260915'
mapping=json.loads((RECORD/'path_map.json').read_text(encoding='utf-8'))
errors=[]
for old,new in mapping.items():
    if (ROOT/old).exists():errors.append('Old document still present: '+old)
    if not (ROOT/new).is_file():errors.append('Missing destination: '+new)
    if not (RECORD/'originals'/old).is_file():errors.append('Missing original snapshot: '+old)
count=0
preexisting_encoding=[]
for p in [ROOT/'README.md',ROOT/'HISTORY.md',*(ROOT/'outputs').rglob('*.md')]:
    text=p.read_text(encoding='utf-8')
    if '\ufffd' in text:
        backup=RECORD/'originals'/p.relative_to(ROOT)
        if backup.is_file() and backup.read_text(encoding='utf-8').count('\ufffd')==text.count('\ufffd'):
            preexisting_encoding.append(str(p.relative_to(ROOT)))
        else:
            errors.append('New replacement character: '+str(p.relative_to(ROOT)))
    for raw in re.findall(r'\[[^\]\n]*\]\(([^\)\n]+)\)',text):
        raw=raw.strip('<>')
        if re.match(r'(?i)(https?://|mailto:|app:|codex:|data:)',raw):continue
        part=unquote(raw.split('#')[0]).replace('\\','/')
        if not part:continue
        if part.startswith('/C:/'):part=part[1:]
        target=(Path(part) if re.match(r'^[A-Za-z]:/',part) else p.parent/part).resolve()
        count+=1
        if not target.exists():errors.append(str(p.relative_to(ROOT))+' -> '+raw)
m=load_manifest()
d=json.loads((ROOT/'outputs/prime_arity/proof_map.json').read_text(encoding='utf-8'))
registered={e['id'] for e in m['verifications']}
for node in d['nodes']:
    for path in node['documents']:
        if not (ROOT/path).is_file():errors.append('Map missing: '+path)
    for id in node['verification_ids']:
        if id not in registered:errors.append('Map unknown check: '+id)
actual={e['id'] for e in m['verifications'] if 'prime-proof' in e['profiles']}
if actual!=set(d['profile_verification_ids']):errors.append('Profile/map mismatch')
if hashlib.sha256((ROOT/d['theorem']['finite_certificate']).read_bytes()).hexdigest()!=d['theorem']['certificate_sha256']:errors.append('Certificate SHA mismatch')
result={'status':'PASS' if not errors else 'FAIL','moved_documents':len(mapping),
        'markdown_local_links_checked':count,'prime_profile_checks':len(actual),
        'remaining_root_documents':[p.name for p in (ROOT/'outputs').glob('*.md')],
        'preexisting_encoding_preserved':preexisting_encoding,
        'errors':errors,'scope':'All outputs/root Markdown link destinations, old/new paths, snapshot presence, full verification registry files and current proof-map IDs/hash. Not a mathematical proof or historical anchor audit.'}
(RECORD/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(bool(errors))
