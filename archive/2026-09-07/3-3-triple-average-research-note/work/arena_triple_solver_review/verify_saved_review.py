"""Fast independent verification of saved Arena review artifacts.

Does not run web searches, browser code, long beam searches or retime benchmarks.
Checks source provenance, all reported successful paths, macro bases and the
scale-invariance counterexample with Python Fraction.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
from statistics import mean

HERE=Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE/name).read_text(encoding='utf-8'))


def replay(raw,ops):
    a=list(map(Fraction,raw))
    target=sum(a)/len(a)
    for atom in ops:
        assert len(atom)==len(set(atom))==3
        assert all(type(i) is int and 1<=i<=len(a) for i in atom)
        value=sum(a[i-1] for i in atom)/3
        for i in atom:a[i-1]=value
    assert a==[target]*len(a)


def main():
    source=read('provenance.json')
    assert sha256((HERE/'frame1.html').read_bytes()).hexdigest()==source['html_sha256']
    assert sha256((HERE/'arena_solver.js').read_bytes()).hexdigest()==source['algorithm_sha256']
    cases=read('comparison_single.json')['cases']
    raw_by_id={r['id']:r['input'] for r in cases}
    solved=0
    for r in cases:
        if r['arena']['status']=='solved':
            replay(r['input'],r['arena']['operations']);solved+=1
    assert len(cases)==52 and solved==37
    warm=read('warm_small.json')['cases']
    for r in warm:
        assert r['status']=='solved'
        replay(raw_by_id[r['id']],r['operations'])
    assert len(warm)==24
    macro_count=0
    for macro in read('macro_basis_checks.json')['macros']:
        for j in range(macro['size']-1):
            raw=[0]*(macro['size']+macro['zeros'])
            raw[j]=1;raw[macro['size']-1]=-1
            replay(raw,macro['operations']);macro_count+=1
    assert macro_count==33
    structure=read('structure_checks.json')
    scaling=structure['scaled_search']
    assert [r['status'] for r in scaling]==['solved','solved','not_found']
    for r in scaling:
        replay(list(map(int,r['input'])),scaling[0]['operations'])
    assert scaling[2]['calls']['nonfinite_views']>0 and scaling[2]['calls']['candidates']==0
    baseline={r['id']:r['baseline'] for r in read('baseline_current.json')['cases']}
    assert len(baseline)==48 and all(r['status']=='solved' for r in baseline.values())
    small=[r for r in cases if r['suite']=='paired_small']
    improvements=Counter('shorter' if r['arena']['steps']<baseline[r['id']]['steps'] else
                         'longer' if r['arena']['steps']>baseline[r['id']]['steps'] else 'same'
                         for r in small)
    assert improvements=={'same':22,'shorter':1,'longer':1}
    groups=[]
    for name,predicate in [('small',lambda r:r['suite']=='paired_small'),
                           ('8bit',lambda r:r['suite']=='height' and r['bits']==8),
                           ('16bit',lambda r:r['suite']=='height' and r['bits']==16),
                           ('32bit',lambda r:r['suite']=='height' and r['bits']==32),
                           ('64_128bit',lambda r:r['suite']=='large')]:
        rows=[r for r in cases if predicate(r)]
        ok=[r for r in rows if r['arena']['status']=='solved']
        groups.append({'group':name,'cases':len(rows),'web_success':len(ok),
            'baseline_success':sum(baseline[r['id']]['status']=='solved' for r in rows),
            'web_mean_ms':mean(r['arena']['reported_solve_ms'] for r in rows),
            'baseline_mean_ms':mean(baseline[r['id']]['solver_ms'] for r in rows),
            'web_steps_success_mean':mean(r['arena']['steps'] for r in ok) if ok else None,
            'baseline_steps_all_mean':mean(baseline[r['id']]['steps'] for r in rows),
            'baseline_steps_on_web_success_mean':mean(baseline[r['id']]['steps'] for r in ok) if ok else None})
    summary={'scope':'finite same-input comparison; mixed JS/Python implementations; timings are saved observations',
        'groups':groups,'small_warm_web_mean_ms':mean(r['reported_solve_ms'] for r in warm),
        'small_step_comparison':dict(improvements),'compared_cases':48,'web_solved_compared':33,
        'baseline_solved_compared':48,'extra_scaled_demo_cases':4,
        'exact_macros_basis_count':macro_count,'numeric_scale_bug_confirmed':True}
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print('Arena captured algorithm provenance: PASS')
    print('Arena saved independent solution replays: PASS',solved,len(warm),macro_count)
    print('Arena same-input success and step comparison: PASS 48 33 48 22 1 1')
    print('Arena scaled-input heuristic counterexample: PASS')
    print('Arena triple solver review artifacts: PASS')


if __name__=='__main__':main()
