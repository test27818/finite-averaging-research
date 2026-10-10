"""Render all twelve exact quadratic covers as inspectable article data."""
from pathlib import Path
from collections import defaultdict
import json
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT/'work'))
import verify_ten_descent_cover as ten
from verify_seven_descent_cover import exact_uncovered_set, display_root

grouped, coverage = ten.verify()
representatives = {}
for pair, scale in ten.residue_classes():
    representatives.setdefault((scale, ten.signature(pair)), pair)
lines = [r'\section{十元三平均的十二个精确二次覆盖}\label{sec:ten-cover}',
         r'以下给出下降覆盖的全部二次多项式，而不是仅报告程序通过。对表列局部代表 $(X,Y)$，输入尺度及各宏的约分因子按十元构造中的规则决定。表中 $i:(a,b,c)$ 表示第 $i$ 个宏的严格下降条件 $a+bt+ct^2>0$，其中 $t=Y/X$。每行全部开区间均被覆盖，列出的只是未严格覆盖的孤立实点；无穷方向另列。局部相容性通过同一模 $96$ 签名检查，唯一相容例外为 $X=0$，此时已有零坐标，九元网络收尾。',
         r'\small\begin{longtable}{r r l p{83mm} p{24mm}}',
         r'\toprule 类&个数&代表&$i:(a,b,c)$&未严格覆盖\\\midrule\endhead']
report = []
for index, ((scale, signature), count) in enumerate(grouped.items(), 1):
    data=[]
    for i,(matrix,(divisor,outscale)) in enumerate(zip(ten.SELECTED,signature),1):
        if outscale is not None:
            data.append((i,ten.descent_polynomial(matrix,scale,divisor,outscale)))
    intervals,points,inf=exact_uncovered_set([c for _,c in data])
    assert not intervals
    labels=[str(display_root(point)) for point in points]
    if not inf: labels.append('infinity')
    poly='; '.join(str(i)+':('+','.join(map(str,c))+')' for i,c in data)
    exceptional=', '.join(labels).replace('infinity', r'$\infty$') or r'$\varnothing$'
    rep=representatives[(scale,signature)]
    lines.append(f'{index}&{count}&$({rep[0]},{rep[1]})$&{poly}&{exceptional}\\\\')
    report.append({'index':index,'count':count,'representative':rep,'scale':scale,
                   'polynomials':data,'uncovered_real_points':labels})
lines += [r'\bottomrule\end{longtable}\normalsize',
          r'每个多项式至多二次。核验一行只须将其全部实根排序，在每个相邻根区间取一个有理数检查符号，再逐根检查等号。根可以写为有理数或有理数加有理倍的平方根；比较根时先分离符号再平方，因而全程不需要浮点容差。二次项系数给无穷方向的符号。由于表列完整的系数及例外集，这一有限证明可独立重做。']
(HERE/'ten_cover.tex').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(HERE/'ten_cover_result.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'classes':sum(grouped.values()),'signatures':len(grouped),
                  'uncovered_points':[r['uncovered_real_points'] for r in report]},indent=2))
