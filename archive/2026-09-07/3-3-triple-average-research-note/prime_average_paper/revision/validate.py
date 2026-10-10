"""Editorial validation, separate from the mathematical dependency audit."""
from pathlib import Path
from hashlib import sha256
import json
import re
import pymupdf

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
tex=(HERE/'prime_average_revised.tex').read_text(encoding='utf-8')
log=(HERE/'prime_average_revised.log').read_text(encoding='utf-8',errors='replace')
structure=json.loads((HERE/'structure_check.json').read_text(encoding='utf-8'))
errors=[]
for name in ('missing_references','unused_labels','duplicate_labels'):
    if structure[name]: errors.append(name)
if any(structure['forbidden_commands'].values()): errors.append('Conversion residues')
if re.search(r'^!|Missing character|undefined references|undefined on|multiply defined|Overfull',log,re.M):
    errors.append('Compilation or layout warning')
if re.search(r'定理\s*[AB]|引理\s*[AB]|第\s*[0-9]+\s*节|引理\s*[0-9]+',tex):
    errors.append('Hard-coded prose theorem/section reference')
with pymupdf.open(HERE/'prime_average_revised.pdf') as pdf:
    pages=len(pdf)
    if any('??' in p.get_text() for p in pdf):errors.append('Unresolved PDF reference')
old=json.loads((HERE.parent/'DELIVERY_CHECK.json').read_text(encoding='utf-8'))
for ext in ('tex','pdf'):
    if sha256((HERE.parent/('prime_average.'+ext)).read_bytes()).hexdigest()!=old[ext+'_sha256']:
        errors.append('Previous edition changed: '+ext)
baseline=json.loads((ROOT/'reader_edition_20260917/manifest.json').read_text(encoding='utf-8'))
for entry in baseline['files']:
    p=ROOT/entry['path']
    if not p.is_file() or sha256(p.read_bytes()).hexdigest()!=entry['sha256']:
        errors.append('Original changed: '+entry['path'])
report={'pdf_pages':pages,'structure':structure,
        'previous_edition_preserved':not any('Previous' in e for e in errors),
        'original_files_checked':len(baseline['files']),
        'finite_checks':json.loads((HERE/'finite_checks_result.json').read_text()),
        'formula_checks':json.loads((HERE/'revision_checks.json').read_text()),
        'tex_sha256':sha256((HERE/'prime_average_revised.tex').read_bytes()).hexdigest(),
        'scope':'Editorial checks and exact finite computations; not independent full proof certification.',
        'errors':errors}
(HERE/'VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
