"""Package the hand-written continuation and preserve curated research evidence."""
from pathlib import Path
import ast
import hashlib
import json
import re
import shutil
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = HERE / 'general_k_average_lecture'
OUT.mkdir(exist_ok=True)
(OUT / 'chapters').mkdir(exist_ok=True)
sources = json.loads((HERE / 'sources.json').read_text(encoding='utf-8'))
catalog = json.loads((ROOT / 'work/verification_manifest.json').read_text(encoding='utf-8'))
source_paths = {s['file'] for s in sources}
verifications = [v for v in catalog['verifications']
                 if set(v.get('documents', [])) & source_paths]

def esc(s):
    return s.replace('\\', r'\textbackslash{}').replace('_', r'\_').replace('&', r'\&').replace('%', r'\%').replace('#', r'\#')

def direct_files(text, parent):
    paths = set()
    # Literal repository paths and normal markdown links, limited to evidence formats.
    for value in re.findall(r'(?:work|research|outputs)/[A-Za-z0-9_./-]+\.(?:py|json|txt|md|pdf)', text):
        p = ROOT / value
        if p.is_file(): paths.add(p.resolve())
    for value in re.findall(r'\]\(([^)]+)\)', text):
        value = unquote(value.split('#')[0])
        if '://' in value: continue
        p = (parent / value).resolve()
        if p.is_file() and p.suffix in {'.py', '.json', '.txt', '.pdf'}: paths.add(p)
    return paths

# Preserve all research articles in the general-arity directory; only two navigations
# are outside the curated thirty entries.
selected = {(ROOT / s['file']).resolve() for s in sources}
selected.update(p.resolve() for p in (ROOT/'outputs/general_arity').rglob('*.md'))
evidence = set()
for s in sources:
    p = ROOT / s['file']
    evidence.update(direct_files(p.read_text(encoding='utf-8'), p.parent))
for v in verifications:
    for name in v.get('scripts', []):
        if (ROOT/name).is_file(): evidence.add((ROOT/name).resolve())
    for dependency in v.get('dependencies', []):
        evidence.update(direct_files(dependency, ROOT))

# Small-unit certificates and source-access records are explicitly part of this package.
for name in ['work/ht_literature_20260915/ht_through999_certificate.json',
             'work/two_three_square_multiple_small_units.json']:
    if (ROOT/name).is_file(): evidence.add((ROOT/name).resolve())
for p in (ROOT/'work/ht_literature_20260915').iterdir():
    if p.is_file() and (p.name.endswith('_source.json') or p.name in {
            'pollack_hudson.pdf','pollack_hudson.txt',
            'martin_pollack2013_author.pdf','martin_pollack2013_author.txt',
            'cubefree2025_author.pdf','cubefree2025_author.txt'}):
        evidence.add(p.resolve())

# Follow local Python imports and file literals. This is a convenience snapshot,
# not a claim that every historical runner is independently relocatable.
queue = list(evidence)
seen = set()
while queue:
    p = queue.pop()
    if p in seen: continue
    seen.add(p)
    if p.suffix != '.py': continue
    try:
        body = p.read_text(encoding='utf-8-sig')
        tree = ast.parse(body)
    except (UnicodeError, SyntaxError): continue
    more = direct_files(body, p.parent)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import): modules = [x.name for x in node.names]
        elif isinstance(node, ast.ImportFrom): modules = [node.module or '']
        else: modules = []
        for module in modules:
            rel = module.replace('.', '/') + '.py'
            for base in [p.parent, ROOT, ROOT/'work', ROOT/'research/prime_arity_padic']:
                q = base/rel
                if q.is_file(): more.add(q.resolve())
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            literal = node.value
            if len(literal)<230 and '\n' not in literal and literal.endswith(('.json','.py')):
                for base in [p.parent,ROOT,ROOT/'work']:
                    q = base/literal
                    if q.is_file(): more.add(q.resolve())
    for q in more - evidence:
        if q.is_relative_to(ROOT):
            evidence.add(q)
            queue.append(q)

selected.update(p for p in evidence if p.is_relative_to(ROOT))
manifest = []
for p in sorted(selected):
    rel = p.relative_to(ROOT).as_posix()
    target = OUT/'sources'/rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p,target)
    manifest.append({'path':rel,'bytes':p.stat().st_size,
                     'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                     'role':'curated-source' if rel in source_paths else 'supporting-snapshot'})
(OUT/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'sources/verification_entries.json').write_text(json.dumps({
    'scope':'Original verification entries matched by the thirty curated documents; not rerun by assembly.',
    'verifications':verifications},ensure_ascii=False,indent=2),encoding='utf-8')

source_appendix = [r'\appendix',r'\chapter{原证明、计算证据与本篇的对应}',
    '本附录以稳定来源编号连接讲义与原研究。压缩包的 sources 目录保持原项目相对路径；来源散列见 SOURCE\_MANIFEST.json。正文按教学顺序重写，原始计数表、推导及历史实验仍保留在对应原文中。',
    '技术原稿中的“未解”或“下一步”可能属于历史阶段；本篇第十四讲按后续定理更新其覆盖范围。核验记录列出原核验的证据等级，本轮没有把所有历史程序重新运行一遍。',
    '原验证器的命令应在原项目根目录执行。证据快照便于检查与追溯，少数历史程序仍可能依赖原工作区；本篇PDF和LaTeX编译不依赖它们。']
md = ['# 任意k平均：讲义与原研究对照','',
      '本包覆盖 outputs/general_arity 的全部25篇技术稿及两个导航文件，另收入5项跨目录来源。章节不重复展开素数篇已经讲解的工具。','',
      '|来源|讲义位置|原文件与用途|','|---|---|---|']
for s in sources:
    rel=s['file']
    title=(ROOT/rel).read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()
    source_appendix.extend([
        '\\section{'+s['id']+'：'+esc(title)+'}\\label{source:'+s['id']+'}',
        esc(s['use'])+'。对应本篇第'+esc(s['chapter'])+'讲。',
        '\\par\\smallskip{\\small 原路径：\\nolinkurl{'+rel+'}}\\par'])
    matches=[v for v in verifications if rel in v.get('documents',[])]
    if matches:
        for v in matches:
            source_appendix.append('核验登记：{\\small\\nolinkurl{'+v['id']+'}}。原证据等级：{\\small\\nolinkurl{'+v.get('evidence_level','未标注')+'}}。')
    else:
        source_appendix.append('本文件没有单独匹配的核验登记；其书面推导或依赖结果须在原文中核对，不能据此虚构独立程序。')
    md.append(f"|{s['id']}|第{s['chapter']}讲|[{title}](sources/{rel})；{s['use']}|")
md += ['', '## 原核验入口', '', '以下命令用于原项目根目录。证据范围保留在 sources/verification_entries.json 中。', '']
for v in verifications:
    commands=[' '.join(c.get('argv',[])) for c in v.get('commands',[])]
    md += [f"### {v['id']}", '', f"等级：{v.get('evidence_level','未标注')}", '',
           v.get('evidence_scope',''), '', '不证明：'+v.get('does_not_establish','原登记未单列'), '']
    md += ['`'+c+'`' for c in commands]+['']
(OUT/'READING_MAP.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
(OUT/'chapters/sources.tex').write_text('\n\n'.join(source_appendix)+'\n',encoding='utf-8')

parts=[]
for p in sorted((HERE/'drafts').glob('*.tex')):
    # This only repairs an explicit handful of missing slashes in the hand draft.
    # Mathematical markup is hand-authored; no markdown conversion occurs.
    body=p.read_text(encoding='utf-8')
    body=re.sub(r'(?<![A-Za-z\\])(qquad|quad)\b',r'\\\1',body)
    if body!=p.read_text(encoding='utf-8'): p.write_text(body,encoding='utf-8')
    if p.name in {'preamble.tex','preface.tex','references.tex'}:
        shutil.copyfile(p,OUT/p.name)
    else:
        shutil.copyfile(p,OUT/'chapters'/p.name)
        parts.append('chapters/'+p.name)
order=['preamble.tex','preface.tex']+parts+['chapters/sources.tex','references.tex']
(OUT/'general_k_average_lecture.tex').write_text('\n'.join('\\input{'+x+'}' for x in order)+'\n',encoding='utf-8')
(OUT/'general_k_average_lecture_single.tex').write_text('\n\n'.join((OUT/x).read_text(encoding='utf-8') for x in order),encoding='utf-8')

compiler=(ROOT/'lecture_readable_20260925/prime_average_lecture_readable/compile.py').read_text(encoding='utf-8')
compiler=compiler.replace("main='prime_average_lecture'","main='general_k_average_lecture'").replace('prime-average-readable-','general-k-lecture-')
(OUT/'compile.py').write_text(compiler,encoding='utf-8')
(OUT/'README.md').write_text('''# 任意元数平均：合数带来的新结构与尚未完成的证明

这是素数平均通俗讲义的续篇，面向数学本科生。14讲按“现象—困难—构造—证明—尚缺内容”展开。

先读 `general_k_average_lecture.pdf`。可编辑源码分两种：

- `general_k_average_lecture.tex` 与 `chapters/`：按讲分文件。
- `general_k_average_lecture_single.tex`：内容完全一致的单文件版本。

需要素数篇已经讲解的中心化、G障碍、CRT、见证、宏、同余子群与贝祖输送。本篇只解释它们在合数处新增的条件和技术，不另抄一遍素数证明。

## 读什么

1—5讲：临界尺度、自动G、固定网络、因子转译、一般线性上界。
6—10讲：小合数模型、平方控制器、全输入入口、小单位群与GRH、二和三的奇次幂。
11—14讲：较大素数奇次幂的部分进展、端点与区间、复制和刚性障碍、当前覆盖及未解任务。

GRH专指Dirichlet L函数的广义黎曼假设。完整合数阈值没有被证明。具体小参数的无条件证书、全参数的条件性定理及只供应部分返回的结果分别标明。

## 来源与证据

`READING_MAP.md` 给30项来源与原核验登记的对应。`sources/` 保存相关原稿、选定脚本、数据和文献访问记录，保持原项目相对路径。`SOURCE_MANIFEST.json` 逐文件记录SHA256，可核对快照完整性。

本轮是编辑综合与新增例子核对，不是对全部既有论文和程序的重新独立审查。原核验命令默认在原项目根目录运行；来源快照不承诺每个历史程序脱离原工作区仍能运行。主讲义及其编译完全独立于历史程序。

`verify_lecture.py` 只核对本篇新增例子、表格算术、若干矩阵公式及打包完整性；它不把有限测试提升为全参数证明。结果见 `EDITORIAL_CHECKS.json`。

## 编译

安装XeLaTeX和中文字体，在本目录运行 `python compile.py`。本版使用Windows常见字体Times New Roman、SimSun、SimHei、KaiTi和Microsoft YaHei；其他系统可在preamble.tex换成已安装字体。单文件版本也可直接用XeLaTeX编译。

原项目证明、知识库、历史文件均保持不变。编辑日期：2026年9月25日。
''',encoding='utf-8')
print(json.dumps({'sources':len(sources),'source_snapshots':len(manifest),
                  'matched_verifications':len(verifications),
                  'snapshot_bytes':sum(x['bytes'] for x in manifest),
                  'chapters':len(parts)},ensure_ascii=False))
