"""Check the article packaging without claiming an independent proof review."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
tex = (HERE/'prime_average.tex').read_text(encoding='utf-8')
log = (HERE/'prime_average.log').read_text(encoding='utf-8', errors='replace')
labels = re.findall(r'\\label\{([^}]+)\}', tex)
references = re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}', tex)
cites = re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', tex)
bibliography = set(re.findall(r'\\bibitem\{([^}]+)\}', tex))
errors = []
if len(labels) != len(set(labels)):
    errors.append('Duplicate LaTeX labels')
if set(references) - set(labels):
    errors.append('Missing labels: '+str(sorted(set(references)-set(labels))))
if set(cites) - bibliography:
    errors.append('Missing citations')
if re.search(r'^!|Missing character|undefined references|undefined on', log, re.M):
    errors.append('LaTeX errors, missing glyphs or unresolved references')
if '待补文内引用' in tex or json.loads((HERE/'unresolved_references.json').read_text(encoding='utf-8')):
    errors.append('Unresolved selected-source links')
if re.search(r'\\(?:input|include|includegraphics)\{', tex):
    errors.append('TeX depends on an external content file')
with pymupdf.open(HERE/'prime_average.pdf') as pdf:
    pages = len(pdf)
    missing_markers = sum(page.get_text().count('??') for page in pdf)
    if missing_markers:
        errors.append('Unresolved-reference markers in PDF')
sources = json.loads((HERE/'source_map.json').read_text(encoding='utf-8'))
for source in sources:
    if sha256((ROOT/source['path']).read_bytes()).hexdigest() != source['sha256']:
        errors.append('Source changed: '+source['path'])
original_manifest = ROOT/'reader_edition_20260917/manifest.json'
original_count = None
if original_manifest.exists():
    originals = json.loads(original_manifest.read_text(encoding='utf-8'))['files']
    original_count = len(originals)
    for source in originals:
        path = ROOT/source['path']
        if not path.is_file() or sha256(path.read_bytes()).hexdigest() != source['sha256']:
            errors.append('Original workspace file changed: '+source['path'])
report = {
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'pdf_pages': pages, 'latex_labels': len(labels), 'bibliographic_entries': len(bibliography),
    'construction_sources': len(sources), 'original_files_compared': original_count,
    'standalone_tex': not re.search(r'\\(?:input|include|includegraphics)\{', tex),
    'certificate_check': json.loads((HERE/'certificate_check.json').read_text(encoding='utf-8')),
    'finite_checks': json.loads((HERE/'finite_checks_result.json').read_text(encoding='utf-8')),
    'tex_sha256': sha256((HERE/'prime_average.tex').read_bytes()).hexdigest(),
    'pdf_sha256': sha256((HERE/'prime_average.pdf').read_bytes()).hexdigest(),
    'scope': 'Editorial integrity, exact finite checks and compilation; not an independent full mathematical review.',
    'errors': errors,
}
(HERE/'DELIVERY_CHECK.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
if errors:
    raise SystemExit(1)
