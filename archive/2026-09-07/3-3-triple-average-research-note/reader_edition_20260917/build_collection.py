"""Build an additive, byte-preserving research reading edition.

All generated writes stay inside this edition directory. The source workspace
is read-only. Markdown anthologies retain complete bodies with local links
redirected into a full, unchanged source snapshot.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import quote, unquote

EDITION = Path(__file__).resolve().parent
ROOT = EDITION.parent
SOURCES = EDITION / 'sources'
MANIFEST = EDITION / 'manifest.json'
LABELS = {
    'proved-source': '原证明已完成（沿用登记，非本次重审）',
    'proved-local': '本地已给证明，未独立重审',
    'partial': '部分结果，须保留范围', 'open': '开放问题',
    'synthesis': '解释／综述，非新证明', 'historical': '历史路线',
    'corrected': '已修正／撤回过强表述',
}
VOLUMES = {
    '01_foundations': ('基础：符号、G、格与公共接口', '01_problem_and_obstruction.md'),
    '02_binary_triple': ('二平均与三平均完整证明', '02_binary_and_triple.md'),
    '03_prime': ('一般素数平均：基线、区间与独立简化', '03_prime_proof.md'),
    '04_geometry': ('端点与算术几何：宏、同余群、尖点和范数', '04_endpoint_geometry.md'),
    '05_subcritical': ('阈值以下：五元、六元与一般补集动力学', '05_subcritical.md'),
    '06_composite': ('合数平均、临界尺度与GRH', '06_composite.md'),
    '07_algorithms': ('算法、求解器、复杂度与核验', '07_algorithms_and_evidence.md'),
    '08_literature': ('外部文献、阅读记录与适用范围', '08_history_and_sources.md'),
    '09_history': ('历史推导、失败路线与审计', '08_history_and_sources.md'),
    '10_archives': ('工作材料、历次快照及旧目录完整附卷', '08_history_and_sources.md'),
}
PRIORITY = {
    '01_foundations': ['G-OBSTRUCTION', 'GEOMETRY-ALL-N', 'STABILIZATION', 'EXTERNAL-ARITH'],
    '02_binary_triple': ['TRIPLE-ALL', 'TRIPLE-BASES', 'SEVEN-STRUCTURE'],
    '03_prime': ['PRIME-TOTAL', 'PRIME-MOVE-MERGE', 'PRIME-COMMON-SHAPE',
                 'PRIME-2P2', 'PRIME-EVEN-INTERIOR', 'PRIME-3PM1', 'PRIME-3P',
                 'PRIME-NATURAL-UNIFICATION', 'PRIME-ODD-PENCIL', 'PRIME-FINITE-TERMINAL'],
    '04_geometry': ['PRIME-ENDPOINT-GEOMETRY', 'SEVEN-GEOMETRY', 'PRIME-ADELIC',
                    'PRIME-FIBER', 'PRIME-GEOMETRY'],
    '05_subcritical': ['SUBCRITICAL-COMPLETE', 'SIX-EXPLICIT', 'FIVE-SUMMARY',
                       'FIVE-NORMAL-FORM', 'FIVE-NORM-SLICE', 'FIVE-FRACTAL',
                       'FIVE-DIGITS', 'FIVE-TORUS', 'FIVE-DENOMINATORS',
                       'FIVE-UNITS-GROUP', 'FIVE-SPARSITY', 'FIVE-BOUNDED-RUNS',
                       'FIVE-HECKE', 'FIVE-TEMPLATE-ESCAPE', 'FIVE-ESCAPE-OPEN'],
    '06_composite': ['COMPOSITE-DEFINITIONS', 'COMPOSITE-FRONTIER'],
    '07_algorithms': ['ALG-LENGTH', 'ALG-WEB'],
}


def digest(data):
    return sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def put(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


def link(label, path, base=EDITION):
    url = quote(os.path.relpath(path, base).replace('\\', '/'), safe='/._-')
    return f'[{label.replace("|", "/").replace("]", ")")}]({url})'


def workspace_files():
    found = []
    for folder, dirs, files in os.walk(ROOT, followlinks=False):
        folder = Path(folder)
        dirs[:] = sorted(d for d in dirs if folder/d != EDITION)
        for name in sorted(files):
            found.append(folder/name)
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())


def category(path, claims):
    if path.startswith(('work/', 'knowledge/')) or path.count('/') == 0:
        return '10_archives'
    if '/literature' in path or '/investigation' in path or '/audits/' in path:
        return '08_literature' if '/audits/' not in path else '09_history'
    if '/history/' in path or path.startswith('outputs/history/'):
        return '09_history'
    if Path(path).name == 'README.md':
        return '10_archives'
    ids = {c['id'] for c in claims}
    if ids & {'G-OBSTRUCTION', 'GEOMETRY-ALL-N', 'STABILIZATION', 'EXTERNAL-ARITH'}:
        return '01_foundations'
    if path == 'outputs/prime_arity/arithmetic_toolkit.md' or ids & {
            'PRIME-ENDPOINT-GEOMETRY', 'SEVEN-GEOMETRY', 'PRIME-ADELIC',
            'PRIME-FIBER', 'PRIME-GEOMETRY'} or path == 'outputs/prime_arity/geometry.md':
        return '04_geometry'
    if any(c['topic'] == 'subcritical' for c in claims):
        return '05_subcritical'
    if path.startswith('outputs/general_arity/'):
        return '06_composite'
    if path.startswith('outputs/algorithms/'):
        return '07_algorithms'
    if path.startswith('outputs/triple_average/'):
        return '02_binary_triple'
    if path.startswith('outputs/prime_arity/'):
        return '03_prime'
    if any(c['topic'] == 'interfaces' for c in claims):
        return '09_history'
    if any(c['topic'] == 'prime' for c in claims):
        return '03_prime'
    return '09_history'


def redirect_links(body, source, source_paths, unresolved):
    """Redirect balanced Markdown destinations, reference definitions and HTML attrs.

    Fenced code stays literal. Ambiguous inline-code spans are left untouched.
    Missing inherited targets are reported rather than guessed or removed.
    """
    def target(raw):
        raw = raw.strip()
        if not raw or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', raw):
            return raw
        name, sep, fragment = raw.partition('#')
        if '?' in name:
            return raw
        resolved = (ROOT/source).parent / unquote(name).replace('\\', '/') if name else ROOT/source
        try:
            rel = resolved.resolve().relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            unresolved.add((source, raw, '原引用位于工作区外'))
            return raw
        if rel not in source_paths and not (ROOT/rel).is_dir():
            unresolved.add((source, raw, '原文已有的目标不存在'))
            return raw
        url = '../sources/' + quote(rel, safe='/._-')
        return url + (sep+fragment if sep else '')

    def destination(content):
        if content.startswith('<') and '>' in content:
            stop = content.index('>')
            return '<'+target(content[1:stop])+'>'+content[stop+1:]
        match = re.match(r'([^\s]+)(.*)', content, re.S)
        return target(match[1])+match[2] if match else content

    output = []
    fence = None
    for line in body.splitlines(keepends=True):
        token = re.match(r'^\s*(`{3,}|~{3,})', line)
        if token:
            if fence is None:
                fence = token[1]
            elif token[1][0] == fence[0] and len(token[1]) >= len(fence):
                fence = None
            output.append(line)
            continue
        if fence is not None:
            output.append(line)
            continue
        i, chunks = 0, []
        while True:
            match = re.search(r'!?\[[^\]\n]*\]\(', line[i:])
            if not match:
                chunks.append(line[i:])
                break
            start, opening = i+match.start(), i+match.end()
            # A link-looking string inside an inline code span is source text.
            if line[:start].count('`') % 2:
                chunks.append(line[i:opening]); i = opening; continue
            end, depth = opening, 1
            while end < len(line) and depth:
                if line[end] == '\\':
                    end += 2; continue
                if line[end] == '(':
                    depth += 1
                elif line[end] == ')':
                    depth -= 1
                end += 1
            if depth:
                chunks.append(line[i:]); break
            chunks.append(line[i:opening])
            chunks.append(destination(line[opening:end-1])+')')
            i = end
        line = ''.join(chunks)
        reference = re.match(r'^(\s*\[[^\]]+\]:\s*)(.+?)(\r?\n)?$', line)
        if reference:
            line = reference[1]+destination(reference[2])+(reference[3] or '')
        line = re.sub(r'\b(href|src)=("|\')(.*?)\2',
                      lambda m: m[1]+'='+m[2]+target(m[3])+m[2], line)
        output.append(line)
    return ''.join(output)


def build():
    if MANIFEST.exists() or SOURCES.exists():
        raise SystemExit('Snapshot exists; use --check. Build a new edition for later revisions.')
    files = workspace_files()
    cat = read_json(ROOT/'knowledge/catalog.json')
    legacy = read_json(ROOT/'work/verification_manifest.json')
    bydoc, olddoc = defaultdict(list), defaultdict(list)
    for claim in cat['claims']:
        for doc in claim['documents']:
            bydoc[doc].append(claim)
    for item in legacy['verifications']:
        for doc in item.get('documents', []):
            olddoc[doc].append(item)
    entries = []
    for file in files:
        rel = file.relative_to(ROOT).as_posix()
        data = file.read_bytes()
        copy = SOURCES/rel
        copy.parent.mkdir(parents=True, exist_ok=True)
        copy.write_bytes(data)
        entries.append({'path': rel, 'size': len(data), 'sha256': digest(data)})
    source_paths = {e['path'] for e in entries}
    docs = []
    for entry in entries:
        rel = entry['path']
        if Path(rel).suffix.lower() != '.md':
            continue
        data = (SOURCES/rel).read_bytes()
        try:
            body = data.decode('utf-8-sig')
            encoding = 'utf-8-sig'
        except UnicodeDecodeError:
            body = data.decode('gb18030')
            encoding = 'gb18030'
        title = next((line.lstrip('# ').strip() for line in body.splitlines()
                      if line.startswith('#')), Path(rel).stem)
        docs.append({'path': rel, 'id': 'doc-'+digest(rel.encode())[:12],
                     'title': title, 'category': category(rel, bydoc[rel]),
                     'claim_ids': [c['id'] for c in bydoc[rel]],
                     'verification_ids': [v['id'] for v in olddoc[rel]],
                     'encoding': encoding, '_body': body})
    # Curated primary order first; registered prerequisite order then remaining appendices.
    claim_rank = {}
    visiting = set()
    def visit(cid):
        if cid in claim_rank or cid in visiting:
            return
        visiting.add(cid)
        c = next(c for c in cat['claims'] if c['id'] == cid)
        for dep in c.get('depends_on', []):
            visit(dep)
        claim_rank[cid] = len(claim_rank)
    for c in cat['claims']:
        visit(c['id'])
    def order(doc):
        priority = PRIORITY.get(doc['category'], [])
        primary = min((priority.index(c) for c in doc['claim_ids'] if c in priority), default=999)
        rank = min((claim_rank[c] for c in doc['claim_ids']), default=9999)
        return primary, rank, doc['path']
    docs.sort(key=lambda d: (d['category'], order(d)))
    unresolved, volume_records = set(), []
    for group, (name, chapter) in VOLUMES.items():
        members = [d for d in docs if d['category'] == group]
        parts, part, size = [], [], 0
        for doc in members:
            if part and size+len(doc['_body']) > 85000:
                parts.append(part); part, size = [], 0
            part.append(doc); size += len(doc['_body'])
        if part:
            parts.append(part)
        for number, items in enumerate(parts, 1):
            path = EDITION/'volumes'/f'{group}_{number:02d}.md'
            head = [f'# {name} · 第{number}分册', '',
                    link('返回总目录', EDITION/'CONTENTS.md', path.parent)+' · '+
                    link('本卷连贯导读', EDITION/'chapters'/chapter, path.parent), '',
                    '> 本册完整收录原文；篇前状态为本次登记快照。历史语句不因汇编而成为当前结论。', '',
                    '## 本册篇目', '']
            head += [f'- [{d["title"]}](#{d["id"]})' for d in items]
            sections = ['\n'.join(head)+'\n']
            for doc in items:
                rel, did = doc['path'], doc['id']
                doc['volume'] = path.relative_to(EDITION).as_posix()
                annotation = ['\n---\n', f'<a id="{did}"></a>', '',
                              f'## 原文导签：{doc["title"]}', '',
                              f'来源：`{rel}` · '+link('逐字节原样副本', SOURCES/rel, path.parent), '']
                if bydoc[rel]:
                    for c in bydoc[rel]:
                        annotation += [f'**{c["id"]} · {LABELS[c["status"]]}**', '',
                                       c['scope'], '', '**边界：** '+c['boundary'], '']
                        if c.get('updates'):
                            annotation += ['**具体替代范围：** '+'；'.join(
                                u['id']+'：'+u['scope'] for u in c['updates']), '']
                        annotation += [link('完整前提与核验', EDITION/'EVIDENCE.md', path.parent)+
                                       f'（搜索 `{c["id"]}`）', '']
                else:
                    annotation += ['本篇没有单独的当前结论卡；保留其原声明，不自动判定为过时或已证。', '']
                if olddoc[rel]:
                    annotation += ['旧核验ID：'+', '.join('`'+v['id']+'`' for v in olddoc[rel]), '']
                if group in ('09_history', '10_archives'):
                    annotation += ['**历史阅读提示：** 此处为历史／工作／导航材料。原有未解表述与计数须对照当前结论卡，正文不删改。', '']
                transformed = redirect_links(doc['_body'], rel, source_paths, unresolved)
                doc['rendered_body_sha256'] = digest(transformed.encode())
                sections += ['\n'.join(annotation), f'<!-- BEGIN SOURCE {did} -->\n',
                             transformed, f'\n<!-- END SOURCE {did} -->\n']
            put(path, ''.join(sections))
            volume_records.append({'path': path.relative_to(EDITION).as_posix(),
                                   'title': f'{name} · {number}', 'documents': [d['id'] for d in items]})
    guide = ['# 有限平均问题：连续阅读导读', '',
             '[入口](README.md) · [完整正文分卷](CONTENTS.md) · [证据索引](EVIDENCE.md)', '',
             '本导读重新组织论证主线；所有技术原文在配套分卷全文保留。状态为整理时快照，不构成独立数学审核。', '']
    for path in sorted((EDITION/'chapters').glob('*.md')):
        guide += ['---', '', path.read_text(encoding='utf-8'), '']
    put(EDITION/'GUIDE.md', '\n'.join(guide))
    index = ['# 分卷目录', '', '[先读连贯导读](GUIDE.md) · [逐篇索引](DOCUMENT_INDEX.md)', '',
             '每篇正文主收录一次。跨卷的证明依赖通过原文链接、篇前导签和证据索引保留。', '']
    for group, (title, chapter) in VOLUMES.items():
        index += ['## '+title, '', link('主题导读', EDITION/'chapters'/chapter), '']
        for volume in volume_records:
            if Path(volume['path']).name.startswith(group+'_'):
                index += ['- '+link(volume['title'], EDITION/volume['path'])+
                          f'（{len(volume["documents"])}篇）']
        index.append('')
    put(EDITION/'CONTENTS.md', '\n'.join(index))
    lines = ['# 全部原文逐篇索引', '',
             '完整性范围包括根目录、outputs、research、knowledge和work中的全部Markdown。', '',
             '| 原文 | 主收录位置 | 原样副本 | 登记ID |', '|---|---|---|---|']
    for d in sorted(docs, key=lambda d: d['path']):
        vol = quote(d['volume'], safe='/._-')+'#'+d['id']
        ids = ', '.join(d['claim_ids']) or '未单独登记'
        lines.append(f'| `{d["path"]}` | [{d["title"].replace("|", "/")}]({vol}) | '+
                     link('原样', SOURCES/d['path'])+f' | {ids} |')
    put(EDITION/'DOCUMENT_INDEX.md', '\n'.join(lines)+'\n')
    file_lines = ['# 全部文件保留清单', '', '未排除任何原文件类型；每项字节散列见manifest.json。', '',
                  '| 原路径 | 字节数 | 副本 |', '|---|---:|---|']
    file_lines += [f'| `{e["path"]}` | {e["size"]} | '+link('打开', SOURCES/e['path'])+' |'
                   for e in entries]
    put(EDITION/'FILE_INDEX.md', '\n'.join(file_lines)+'\n')
    write_evidence(cat, legacy, docs)
    for d in docs:
        d.pop('_body')
    manifest = {'built_at_utc': datetime.now(timezone.utc).isoformat(),
                'source_root': str(ROOT), 'source_catalog_updated': cat.get('updated'),
                'scope': 'Every pre-existing workspace file, excluding only this edition directory.',
                'files': entries, 'documents': docs, 'volumes': volume_records,
                'claim_ids': [c['id'] for c in cat['claims']],
                'verification_ids': [v['id'] for v in legacy['verifications']],
                'inherited_link_issues': [dict(zip(('source', 'target', 'reason'), row))
                                         for row in sorted(unresolved)]}
    manifest['edition_files'] = [
        {'path': p.relative_to(EDITION).as_posix(), 'sha256': digest(p.read_bytes())}
        for p in sorted(EDITION.rglob('*')) if p.is_file() and SOURCES not in p.parents
        and p.name not in ('manifest.json', 'AUDIT.md')]
    put(MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    check(True)


def write_evidence(cat, legacy, docs):
    bypath = {d['path']: d for d in docs}
    lines = ['# 结论、证明与核验对照', '',
             '以下是原登记的完整结构化字段的可读副本；保留量词、条件和未证明内容。不是新的独立审核。', '',
             '## 当前结论ID目录', '']
    lines += [f'- [{c["id"]} · {c["title"]}](#claim-{c["id"].lower()})' for c in cat['claims']]
    for c in cat['claims']:
        lines += ['', f'<a id="claim-{c["id"].lower()}"></a>', '', f'## {c["id"]} · {c["title"]}', '',
                  '**状态：** '+LABELS[c['status']], '', '**范围：** '+c['scope'], '',
                  '**边界：** '+c['boundary'], '', '### 原文与主收录', '']
        for source in c['documents']:
            doc = bypath.get(source)
            dest = f'[{doc["title"]}]({doc["volume"]}#{doc["id"]})' if doc else source
            lines += ['- '+dest+' · '+link('原样副本', SOURCES/source)]
        lines += ['', '### 登记的全部字段', '', '```json',
                  json.dumps(c, ensure_ascii=False, indent=2), '```', '']
        for item in c.get('local_checks', []):
            for source in [item['argv'][1]]+item.get('records', []):
                lines += ['- '+link(source, SOURCES/source)]
        for source in c.get('source_records', []):
            lines += ['- '+link(source, SOURCES/source)]
    lines += ['', '# 原185项核验登记', '',
              '数量来自快照实际记录。下列完整字段保留原命令、证据级别、证书、限制与参数；不自动执行。', '']
    for item in legacy['verifications']:
        lines += [f'<a id="verify-{item["id"]}"></a>', '', '## '+item['id'], '',
                  item.get('claim', ''), '', '```json', json.dumps(item, ensure_ascii=False, indent=2), '```', '']
        for source in item.get('documents', [])+item.get('scripts', []):
            lines += ['- '+link(source, SOURCES/source)]
    put(EDITION/'EVIDENCE.md', '\n'.join(lines)+'\n')


def check(originals=False):
    manifest = read_json(MANIFEST)
    errors = []
    expected = {e['path'] for e in manifest['files']}
    actual = {p.relative_to(SOURCES).as_posix() for p in SOURCES.rglob('*') if p.is_file()}
    if actual != expected:
        errors.append('Snapshot inventory differs: '+str(sorted(actual ^ expected)[:12]))
    for entry in manifest['files']:
        copy = SOURCES/entry['path']
        if not copy.is_file() or digest(copy.read_bytes()) != entry['sha256']:
            errors.append('Snapshot hash: '+entry['path'])
        if originals:
            source = ROOT/entry['path']
            if not source.is_file() or digest(source.read_bytes()) != entry['sha256']:
                errors.append('Original changed: '+entry['path'])
    if originals:
        current = {p.relative_to(ROOT).as_posix() for p in workspace_files()}
        if current != expected:
            errors.append('Original inventory changed: '+str(sorted(current ^ expected)[:12]))
    md_paths = {p for p in expected if Path(p).suffix.lower() == '.md'}
    docs = manifest['documents']
    if len(docs) != len(md_paths) or {d['path'] for d in docs} != md_paths:
        errors.append('Markdown full coverage mismatch')
    volumes = {v['path']: (EDITION/v['path']).read_text(encoding='utf-8')
               for v in manifest['volumes']}
    for doc in docs:
        text = volumes[doc['volume']]
        begin, end = f'<!-- BEGIN SOURCE {doc["id"]} -->\n', f'\n<!-- END SOURCE {doc["id"]} -->'
        if text.count(begin) != 1 or text.count(end) != 1:
            errors.append('Missing/duplicate anthology body: '+doc['path']); continue
        body = text.split(begin, 1)[1].split(end, 1)[0]
        original = (SOURCES/doc['path']).read_bytes().decode(doc['encoding'])
        transformed = redirect_links(original, doc['path'], expected, set())
        # read_text normalizes CRLF; compare semantic source text after that normalization.
        if body != transformed.replace('\r\n', '\n').replace('\r', '\n'):
            errors.append('Anthology body mismatch: '+doc['path'])
        if digest(transformed.encode()) != doc['rendered_body_sha256']:
            errors.append('Rendered source hash mismatch: '+doc['path'])
    evidence = (EDITION/'EVIDENCE.md').read_text(encoding='utf-8')
    for cid in manifest['claim_ids']:
        if f'<a id="claim-{cid.lower()}"></a>' not in evidence:
            errors.append('Missing claim: '+cid)
    for vid in manifest['verification_ids']:
        if f'<a id="verify-{vid}"></a>' not in evidence:
            errors.append('Missing verification: '+vid)
    for e in manifest['edition_files']:
        file = EDITION/e['path']
        if not file.is_file() or digest(file.read_bytes()) != e['sha256']:
            errors.append('Edition file changed: '+e['path'])
    index_links = 0
    for name in ('README.md', 'CONTENTS.md', 'DOCUMENT_INDEX.md', 'FILE_INDEX.md', 'EVIDENCE.md'):
        text = (EDITION/name).read_text(encoding='utf-8')
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for dest in re.findall(r'\]\(([^)]+)\)', text):
            if dest.startswith('#') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', dest):
                continue
            index_links += 1
            if not (EDITION/unquote(dest.split('#')[0])).exists():
                errors.append('Index link missing: '+name+' -> '+dest)
    stats = {'files': len(expected), 'bytes': sum(e['size'] for e in manifest['files']),
             'markdown_full_bodies': len(docs), 'volume_parts': len(volumes),
             'claims': len(manifest['claim_ids']), 'legacy_verifications': len(manifest['verification_ids']),
             'originals_checked': originals, 'index_links_checked': index_links,
             'inherited_link_issues': len(manifest['inherited_link_issues']),
             'errors': errors}
    if originals:
        write_audit(manifest, stats)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


def write_audit(manifest, stats):
    lines = ['# 整理完整性与原文件保护报告', '',
             '实际构建时间（UTC）：'+manifest['built_at_utc'], '',
             '底稿登记日期：'+str(manifest['source_catalog_updated']), '',
             '## 结果', '', '```json', json.dumps(stats, ensure_ascii=False, indent=2), '```', '',
             '以上检查核对文件字节、全文收录、证据登记及原文件未修改，不认证数学证明。', '',
             '## 保留方法', '',
             '全部原文件逐字节复制，未排除缓存、历史快照、旧证书或重复材料。原路径层级完整保留。', '',
             'Markdown汇编保留全部原文，篇前增加状态导签；仅将存在的本地链接重定向到副本。'
             '完整性检查重新生成链接变换后逐篇比较正文。原始字节另以SHA256核对。', '',
             '全部当前结论卡与旧核验的完整字段收录于EVIDENCE，不仅摘取结论句。', '',
             '## 继承的本地链接问题', '',
             '以下是扫描原文所得的疑似缺失目标或工作区外路径，可能含数学记号误识别，数量不等于确证断链数。没有删除原引用、猜测替代证明或修改原文。'
             '这不包括全部裸文本路径、数学交叉引用、网址可用性或Markdown锚点语义审查。', '',
             '| 来源 | 原目标 | 情况 |', '|---|---|---|']
    for issue in manifest['inherited_link_issues']:
        lines.append('| '+link(issue['source'], SOURCES/issue['source'])+' | `'+
                     issue['target'].replace('|', '/')+'` | '+issue['reason']+' |')
    put(EDITION/'AUDIT.md', '\n'.join(lines)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--build', action='store_true')
    mode.add_argument('--check', action='store_true')
    parser.add_argument('--check-originals', action='store_true')
    args = parser.parse_args()
    if args.build:
        build()
    else:
        check(args.check_originals)
