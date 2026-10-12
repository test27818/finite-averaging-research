"""Validate the publication snapshot; this does not certify mathematics."""
import ast
import hashlib
import importlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parent
manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
errors = []
counts = {'hashes': 0, 'python_parsed': 0, 'json_parsed': 0, 'python_imported': 0}
for item in manifest['files']:
    path = root / item['path']
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != item['sha256']:
        errors.append('SHA-256 mismatch: ' + item['path'])
    if hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() != item['git_blob_sha1']:
        errors.append('Git blob mismatch: ' + item['path'])
    counts['hashes'] += 1
    if path.suffix == '.py':
        ast.parse(data.decode('utf-8'))
        counts['python_parsed'] += 1
    if path.suffix == '.json':
        json.loads(data)
        counts['json_parsed'] += 1

research = root / 'research/prime_arity_padic'
sys.path.insert(0, str(research))
for path in sorted(research.glob('*.py')):
    importlib.import_module(path.stem)
    counts['python_imported'] += 1

expected = {x['path'] for x in manifest['files']} | set(manifest['excluded_self_records'])
actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
errors += ['Unlisted file: ' + x for x in sorted(actual - expected)]
errors += ['Missing file: ' + x for x in sorted(expected - actual) if x != 'publication_check.json']
result = {'status': 'PASS' if not errors else 'FAIL', **counts, 'errors': errors,
          'scope': 'Snapshot hashes, parseability and imports; not proof certification.'}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
