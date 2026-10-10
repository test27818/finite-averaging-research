from pathlib import Path
import re, json, shutil

ROOT = Path(r'C:\Users\19226\Documents\Codex\2026-09-07\3-3-triple-average-research-note')
REV = ROOT / 'prime_average_paper/revision'
OUT = Path(r'C:\Users\19226\Documents\Codex\2026-09-24\c-users-19226-documents-codex-2026\outputs\prime_average_lecture')
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'chapters').mkdir(exist_ok=True)
(OUT/'data').mkdir(exist_ok=True)

def read(name):
    return (REV/name).read_text(encoding='utf-8-sig')

def between(s, a, b=None):
    i=s.index(a)
    return s[i:s.index(b,i)] if b else s[i:]

def start(label, typ='lemma'):
    return '\\begin{'+typ+'}\\label{'+label+'}'

def body(name):
    s=read(name).replace('\\appendix\n','')
    return s[s.index('\n')+1:]

arith=body('03_arithmetic.tex')
control=body('07_controllers.tex')
lower=body('appendix_lower.tex')
upper=body('appendix_upper.tex')
small=body('appendix_small.tex')
descent=body('04_descent.tex')
full=read('prime_average_revised.tex')
cert=between(full, '\\section{有限证书及复核规范}', '\\begin{thebibliography}')
cert=cert[cert.index('\n')+1:]
rootcert=between(cert,'\\begin{proposition}[根计数证书]','\\begin{proposition}[碰撞分类证书]')
collisioncert=between(cert,'\\begin{proposition}[碰撞分类证书]','\\begin{proposition}[二十二元有限轨道证书]')
sevencert=between(cert,'\\begin{proposition}[二十二元有限轨道证书]','\\begin{proposition}[十元二次覆盖证书]')
tencert=between(cert,'\\begin{proposition}[十元二次覆盖证书]')
tencert=tencert.split('有限消元及轨道程序作为补充材料')[0]

chapters=[
('01_problem','问题、例子与主定理','sec:main',body('01_problem.tex')),
('02_obstruction','共同余数障碍与锐下界','sec:obstruction',body('02_obstruction.tex')),
('03_descent_tools','整数下降的准备','sec:descent',descent[:descent.index(start('lem:background'))]),
('04_descent_complete','整数下降如何覆盖所有状态','ch:descent-finish',between(descent,start('lem:background'))),
('05_zero_tail','三个等大块与含零收尾','sec:blocks',body('05_blocks.tex')),
('06_compression','从一般配置到三块核心','sec:compression',body('06_compression.tex')+'\n'+upper[:upper.index(start('lem:count-interface'))]),
('07_returns','平均词、返回矩阵与局部化','sec:arithmetic',arith[:arith.index('\\begin{theorem}[Morris')]),
('08_congruence','从剪切到精确同余输送','ch:congruence',between(arith,'\\begin{theorem}[Morris',start('lem:content'))),
('09_terminal','有限余数如何决定精确终端','sec:controllers',between(arith,start('lem:content'))+'\n'+control[:control.index(start('prop:odd','proposition'))]),
('10_odd','奇数下半带：一组共同反射','ch:odd',between(control,start('prop:odd','proposition'),start('prop:r2','proposition'))),
('11_two','两个剩余位置：按输入选择返回','ch:two',between(control,start('prop:r2','proposition'),start('prop:even','proposition'))+'\n'+lower[:lower.index(start('lem:binary-depth'))]),
('12_even','偶数内部与上边界','app:lower',between(control,start('prop:even','proposition'),start('prop:upper','proposition'))+'\n'+between(lower,start('lem:binary-depth'))),
('13_counting','上半带：计数表怎样产生剪切','app:upper',between(upper,start('lem:count-interface'),start('lem:upper-supply'))),
('14_upper','上半带：全部参数的具体选择','ch:upper',between(control,start('prop:upper','proposition'))+'\n'+between(upper,start('lem:upper-supply'))),
('15_wide','宽维数中剩余情形的补齐','sec:wide',body('08_wide.tex')),
('16_three','三平均：最小奇素数的完整证明','ch:three',small[:small.index(start('lem:collision-small'))]+'\n'+tencert),
('17_five_seven','五平均与七平均的必要基例','app:small',between(small,start('lem:collision-small'))+'\n'+collisioncert+'\n'+sevencert),
('18_completion','合并全部范围，完成定理','sec:completion',body('09_completion.tex')),
]

TITLES={
'lem:affine':'归一化与操作序列相容','lem:obstruction':'非平均素数处的共同余数障碍',
'lem:fraction':'小维数中首次分数化不可挽回','prop:lower':'位于2p的反例',
'lem:safety':'由未选位置保证安全','lem:initialize':'建立两个不同重值',
'lem:background':'有充足背景副本时的续步','lem:heavy':'三个及更多重值的续步',
'lem:two-heavy':'两个重值共享富余副本','lem:integer-range':'整数下降覆盖的维数范围',
'prop:threep':'3p个位置的独立解法','lem:zero-base':'含零的2p+1元配置','lem:zero-tail':'从一个零和组到全部归零',
'lem:short-choice':'短区间中的同时避让','lem:concentrate':'把同余见证集中到一个差分',
'lem:two-block-entry':'保留见证的双块入口','prop:entry':'一般输入的三块归约',
'lem:shape-change':'用两次平均改换块重数','lem:localize':'可逆倍率扩展剪切参数',
'lem:deep':'两条根生成一个确定的同余层','lem:transverse':'横向返回与换基的分母损失',
'lem:fiber':'相同剩余类中的精确输送','lem:inverse':'获得深同余群以后的正向逆',
'lem:content':'本原化的全部有限分支','cor:finite-group':'有限正向对应的群化',
'lem:local-cycle':'局部平移的逐层提升','lem:small-units':'小数字生成模n单位群',
'thm:terminal':'三块核心的共同终端定理','prop:odd':'奇数余量的全部合法核心',
'prop:r2':'余量为2的核心','prop:even':'偶数余量的其余核心',
'prop:upper':'上半带的充分性','lem:two-carrier':'两次CRT将尺度送到正负1',
'lem:binary-depth':'降低二进深度','lem:even-core':'偶数内部的完整构造',
'lem:upper-boundary':'余量为p−1的重叠反射','lem:count-interface':'由库存表计算返回矩阵',
'cor:resource':'相邻输出表的充分条件','lem:upper-supply':'大素数的三组计数公式',
'lem:upper-small':'偏移至少10时的小素数','lem:small-supply':'九个低偏移的有限补充',
'prop:wide':'所有n至少4p的配置','lem:triple-large':'三平均的全部n至少11',
'lem:eight':'三平均八元的欧几里得下降','lem:ten':'三平均十元的二次势能下降',
'lem:collision-small':'五平均和七平均的碰撞分类','lem:seven22':'七平均二十二元的方向与尺度',
'thm:prime':'素数平均的充要条件','cor:threshold':'最优最终阈值',
}

from lecture_texts import INTRO, BEFORE, AFTER, REPLACEMENTS, PREFACE, PREAMBLE
import lecture_more
import lecture_last
import lecture_restore
for ident,title,label,s in chapters:
    if ident in REPLACEMENTS:
        for old,new in REPLACEMENTS[ident]:
            if old not in s:
                raise ValueError(('missing editorial anchor',ident,old[:90]))
            s=s.replace(old,new,1)
    for anchor, addition in BEFORE.get(ident,[]):
        if anchor not in s: raise ValueError(('before',ident,anchor))
        s=s.replace(anchor,addition+'\n'+anchor,1)
    for anchor, addition in AFTER.get(ident,[]):
        if anchor not in s: raise ValueError(('after',ident,anchor))
        s=s.replace(anchor,anchor+'\n'+addition,1)
    for key, value in TITLES.items():
        s=re.sub(r'(\\begin\{(?:lemma|theorem|proposition|corollary)\})(\\label\{'+re.escape(key)+r'\})',lambda m:m[1]+'['+value+']'+m[2],s)
    # Repair inherited literal spacing commands introduced in the earlier assembler.
    s=re.sub(r'(?<![A-Za-z\\])qquad\b',r'\\qquad',s)
    s=re.sub(r'(?<![A-Za-z\\])quad\b',r'\\quad',s)
    s=s.replace('附录\\ref{app:lower}','第\\ref{app:lower}讲').replace('附录\\ref{app:upper}','第\\ref{app:upper}讲').replace('附录\\ref{app:small}','第\\ref{app:small}讲')
    s=re.sub(r'第(\\ref\{sec:[^}]+\})节',r'第\1讲',s)
    s=s.replace('本文','本讲义').replace('本节设','本讲设')
    # Explicit paragraph breaks after proof steps keep the original argument readable.
    text='\\chapter{'+title+'}\\label{'+label+'}\n'+INTRO.get(ident,'')+'\n'+s
    (OUT/'chapters'/f'{ident}.tex').write_text(text,encoding='utf-8')

rootcert=re.sub(r'(?<![A-Za-z\\])qquad\b',r'\\qquad',rootcert)
rootcert=re.sub(r'(?<![A-Za-z\\])quad\b',r'\\quad',rootcert)
(OUT/'chapters/19_tables.tex').write_text('\\chapter{上半带的完整根计数表}\\label{app:certificates}\n'+r'''
本附录给出第\ref{ch:upper}讲所用的全部剩余计数。每行是一对真实返回的选择方案，
并非对一般有理输入逐项搜索。阅读时先掌握第\ref{app:upper}讲的库存公式，
再将任意一行代入，即可读出它代表的平均操作。相同的 $(p,s)$ 下可能有两对或三对表；
必须合用该参数下的全部表，以取得所需最大公因子。
为方便查找，按 $p$、$s$ 递增排列。这个附录是证明数据的一部分；
读者首次阅读时只需跟随正文的一个算例理解用法，随后可以返回查阅具体参数。
'''+'\n'+rootcert,encoding='utf-8')
(OUT/'preface.tex').write_text(PREFACE,encoding='utf-8')
(OUT/'preamble.tex').write_text(PREAMBLE,encoding='utf-8')
(OUT/'references.tex').write_text(read('references.tex').replace('\\begin{thebibliography}{9}', '\\begin{thebibliography}{9}\n\\addcontentsline{toc}{chapter}{参考文献}'),encoding='utf-8')
main=r'''\documentclass[11pt,a4paper,oneside,openany]{book}
\input{preamble}
\begin{document}
\frontmatter
\begin{titlepage}
\centering
\vspace*{25mm}
{\sffamily\Large 数学讲义\par}
\vspace{15mm}
{\Huge\bfseries 素数平均\par}
\vspace{7mm}
{\LARGE 有限可达性与最优阈值\par}
\vspace{16mm}
{\large 从整数下降到二维同余输送\par}
\vfill
\begin{minipage}{.79\textwidth}
\large
对奇素数 $p$，当 $n\ge 2p+1$ 时，\par
有限次 $p$ 元平均可达全等\par
\hfill 当且仅当\quad $G$ 是 $p$ 的幂。
\end{minipage}
\vfill
{\large 中文讲义\quad 2026年9月\par}
\end{titlepage}
\input{preface}
\tableofcontents
\mainmatter
'''
for ident,_,_,_ in chapters: main+='\\input{chapters/'+ident+'}\n'
main+='\\appendix\n\\input{chapters/19_tables}\n\\backmatter\n\\input{references}\n\\end{document}\n'
(OUT/'prime_average_lecture.tex').write_text(main,encoding='utf-8')
for name in ['root_certificate.json','finite_checks_result.json']:
    shutil.copyfile(REV/name,OUT/'data'/name)
shutil.copyfile(REV/'finite_checks.py',OUT/'data/finite_checks.py')
# Supporting finite data are inherited, not recomputed in this editorial task.
print(json.dumps({'chapters':len(chapters),'output':str(OUT),'tex_characters':sum(len(p.read_text(encoding='utf-8')) for p in OUT.rglob('*.tex'))},ensure_ascii=False))
