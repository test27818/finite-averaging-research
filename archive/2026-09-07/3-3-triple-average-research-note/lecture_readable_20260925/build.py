"""Assemble a pedagogical rewrite while preserving every formal source block.

No Markdown conversion or automatic guesses about mathematical notation.
Handwritten explanations live in drafts/. The delivered chapters are native,
fully expanded LaTeX and can be edited or compiled independently.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,re,shutil

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'original/prime_average_lecture'
OUT=HERE/'prime_average_lecture_readable'
BLOCKS=json.loads((HERE/'proof_blocks.json').read_text(encoding='utf-8'))
INDEX=json.loads((HERE/'proof_index.json').read_text(encoding='utf-8'))
used=[]; table_records=[]; changes=[]


def put(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text,encoding='utf-8',newline='\n')


def proof(match):
    key=match[1]; used.append(key)
    body=BLOCKS[key]['text']
    if 'n=4p+s,quad1' in body:
        body=body.replace('n=4p+s,quad1',r'n=4p+s,\quad1')
        changes.append({'block':key,'kind':'typesetting typo','before':'n=4p+s,quad1','after':r'n=4p+s,\quad1'})
    return body


def tables(match):
    filename=match[1]
    source=(SOURCE/'chapters'/filename).read_text(encoding='utf-8')
    found=re.findall(r'\\begingroup\\small\s*\\begin\{longtable\}[\s\S]*?\\endgroup',source)
    assert found,filename
    table_records.extend({'source':filename,'sha256':sha256(x.encode()).hexdigest()} for x in found)
    return '\n\n'.join(found)


def build():
    (OUT/'chapters').mkdir(parents=True,exist_ok=True)
    chapters=[]
    for name in INDEX:
        draft=HERE/'drafts'/name
        text=draft.read_text(encoding='utf-8')
        text=re.sub(r'\\InsertProof\{([^}]+)\}',proof,text)
        text=re.sub(r'\\InsertTables\{([^}]+)\}',tables,text)
        put(OUT/'chapters'/name,text)
        chapters.append(text)
    assert Counter(used)==Counter(BLOCKS.keys()), (set(BLOCKS)-set(used),set(used)-set(BLOCKS))
    old_preamble=(SOURCE/'preamble.tex').read_text(encoding='utf-8')
    old_preamble=old_preamble.replace('bookmarksnumbered=true','bookmarks=false')
    old_preamble=old_preamble.replace('素数平均：有限可达性与最优阈值','素数平均：从例子到完整证明')
    # xcolor is loaded before hyperref to define the link colours explicitly.
    old_preamble=old_preamble.replace('\\usepackage{xcolor}\n','')
    old_preamble=old_preamble.replace('\\usepackage[unicode,','\\usepackage{xcolor}\n\\usepackage[unicode,')
    put(OUT/'preamble.tex',old_preamble)
    preface=(HERE/'drafts/preface.tex').read_text(encoding='utf-8')
    put(OUT/'preface.tex',preface)
    refs=(SOURCE/'references.tex').read_text(encoding='utf-8').replace(r'\end{document}','')
    put(OUT/'references.tex',refs)
    main=(SOURCE/'prime_average_lecture.tex').read_text(encoding='utf-8')
    main=main.replace('有限可达性与最优阈值','从例子到完整证明')
    main=main.replace('从整数下降到二维同余输送','面向数学本科生的逐步讲解')
    main=main.replace('中文讲义\\quad 2026年9月','通俗展开版\\quad 2026年9月')
    put(OUT/'prime_average_lecture.tex',main)
    flat=main.replace(r'\input{preamble}',old_preamble).replace(r'\input{preface}',preface).replace(r'\input{references}',refs)
    for name,content in zip(INDEX,chapters):
        flat=flat.replace(r'\input{chapters/'+Path(name).stem+'}',content)
    put(OUT/'prime_average_lecture_single.tex',flat)
    for file in (SOURCE/'data').iterdir():
        if file.is_file():
            (OUT/'data').mkdir(exist_ok=True)
            shutil.copyfile(file,OUT/'data'/file.name)
    source_all='\n'.join(p.read_text(encoding='utf-8') for p in (SOURCE/'chapters').glob('*.tex'))
    labels=re.findall(r'\\label\{([^}]+)\}',flat)
    references=re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}',flat)
    source_labels=set(re.findall(r'\\label\{([^}]+)\}',source_all))
    report={'original_formal_blocks':len(BLOCKS),'included_formal_blocks':len(used),
            'original_tables':source_all.count(r'\begin{longtable}'),
            'included_tables':sum(t.count(r'\begin{longtable}') for t in chapters),
            'copied_table_groups':table_records,
            'missing_original_labels':sorted(source_labels-set(labels)),
            'unresolved_references':sorted(set(references)-set(labels)),
            'duplicate_labels':sorted(k for k,v in Counter(labels).items() if v>1),
            'explicit_typesetting_changes':changes,
            'claim':'Formal statements and attached proofs preserved verbatim except listed typesetting correction; explanatory prose rewritten.',
            'blocks':[{'key':k,'source':BLOCKS[k]['file'],'sha256':sha256(BLOCKS[k]['text'].encode()).hexdigest()} for k in used]}
    put(OUT/'preservation_manifest.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    mapping=['# 逐讲对应与完整性说明','',
             '新版保留原18讲及计数附录的顺序，重写全部讲解过渡，增加具体算例和术语解释。正式命题及相邻证明逐项保留；这里的完整性核对不等于独立数学审稿。','',
             '| 文件 | 保留的正式块 |','|---|---|']
    mapping += ['| '+name+' | '+', '.join(keys)+' |' for name,keys in INDEX.items()]
    mapping += ['', '完整数表、参考文献及data中的原程序与数据一并保留。原文宽维数公式中裸写的quad改为LaTeX间距命令；没有据此修改数学结论。',
                '', '补充的归一化、错误平均、矩阵剪切、内容分支、CRT及容量数值例子由check_examples.py精确核对。']
    put(OUT/'内容对应.md','\n'.join(mapping)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('blocks','copied_table_groups')},ensure_ascii=False,indent=2))
    if report['missing_original_labels'] or report['unresolved_references'] or report['duplicate_labels']:
        raise SystemExit(1)


if __name__=='__main__':build()
