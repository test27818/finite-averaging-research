from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,re,zipfile,shutil
import pymupdf

HERE=Path(__file__).resolve().parent
OUT=HERE/'prime_average_lecture_readable'
SOURCE=HERE/'original/prime_average_lecture'
original=json.loads((HERE/'source.json').read_text(encoding='utf-8'))
manifest=json.loads((OUT/'preservation_manifest.json').read_text(encoding='utf-8'))
blocks=json.loads((HERE/'proof_blocks.json').read_text(encoding='utf-8'))
all_chapters='\n'.join(p.read_text(encoding='utf-8') for p in sorted((OUT/'chapters').glob('*.tex')))
errors=[]
for key,block in blocks.items():
    expected=block['text'].replace('n=4p+s,quad1',r'n=4p+s,\quad1')
    if all_chapters.count(expected)!=1:errors.append('Formal block missing/changed/duplicated: '+key)
for item in manifest['copied_table_groups']:
    source=(SOURCE/'chapters'/item['source']).read_text(encoding='utf-8')
    tables=re.findall(r'\\begingroup\\small\s*\\begin\{longtable\}[\s\S]*?\\endgroup',source)
    matching=[t for t in tables if sha256(t.encode()).hexdigest()==item['sha256']]
    if len(matching)!=1 or all_chapters.count(matching[0])!=1:errors.append('Changed table: '+item['source'])
for file in (SOURCE/'data').iterdir():
    if file.is_file() and file.read_bytes()!=(OUT/'data'/file.name).read_bytes():errors.append('Changed original data: '+file.name)
if sha256(Path(original['archive']).read_bytes()).hexdigest()!=original['sha256']:
    errors.append('Original ZIP changed')
log=(OUT/'compilation.log').read_text(encoding='utf-8',errors='replace')
if re.search(r'^!|Overfull|Missing character|undefined references|undefined on|multiply defined',log,re.M):
    errors.append('Compilation/reference/layout issue')
flat=(OUT/'prime_average_lecture_single.tex').read_text(encoding='utf-8')
if re.search(r'\\(?:input|include)\{',flat):errors.append('Single-file source still has an include')
labels=re.findall(r'\\label\{([^}]+)\}',flat)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',flat)
if set(refs)-set(labels):errors.append('Undefined source reference')
if len(labels)!=len(set(labels)):errors.append('Duplicate source label')
with pymupdf.open(OUT/'prime_average_lecture.pdf') as doc:
    pages=len(doc)
    if any('??' in p.get_text() for p in doc):errors.append('Unresolved PDF reference')
    text_chars=sum(len(p.get_text()) for p in doc)
with pymupdf.open(SOURCE/'prime_average_lecture.pdf') as doc:old_pages=len(doc)
shutil.copyfile(SOURCE/'来源说明.md',OUT/'原讲义来源说明.md')
report={'pages':pages,'original_pages':old_pages,'formal_blocks_preserved':len(blocks),
        'long_tables_preserved':len(manifest['copied_table_groups']),
        'reference_labels':len(labels),'reference_occurrences':len(refs),
        'original_zip_unchanged':True,'original_data_byte_identical':True,
        'teaching_examples':json.loads((OUT/'example_checks.json').read_text()),
        'scope':'Source preservation, new exact numerical examples, typesetting and references; not independent proof certification.',
        'pdf_sha256':sha256((OUT/'prime_average_lecture.pdf').read_bytes()).hexdigest(),
        'errors':errors}
(OUT/'VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
archive_path=HERE/'prime_average_lecture_readable.zip'
excluded={'compilation_error.log','compilation.log','contents.toc','labels.aux'}
with zipfile.ZipFile(archive_path,'w',compression=zipfile.ZIP_DEFLATED) as archive:
    for file in sorted(OUT.rglob('*')):
        if file.is_file() and file.name not in excluded and '__pycache__' not in file.parts:
            archive.write(file,Path(OUT.name)/file.relative_to(OUT))
with zipfile.ZipFile(archive_path) as archive:
    assert archive.testzip() is None
    assert archive.read(OUT.name+'/prime_average_lecture.pdf')==(OUT/'prime_average_lecture.pdf').read_bytes()
print('Created and checked '+str(archive_path))
