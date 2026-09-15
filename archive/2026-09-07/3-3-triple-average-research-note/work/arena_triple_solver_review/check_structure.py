"""Meaningful exact macro and heuristic-limit checks on the unmodified snapshot."""
from pathlib import Path
from fractions import Fraction
from math import gcd
import json
from benchmark_arena import Harness,read,verify

HERE=Path(__file__).resolve().parent


def main():
    raw=read('double_triple_length_benchmark.json')['records'][2]['raw']
    large=read('double_triple_length_large_benchmark.json')['records'][0]['raw']
    result={}
    with Harness() as harness:
        result['macro_bases']=harness.request({'action':'macros'})
        assert result['macro_bases']['status']=='ok'
        result['scaled_search']=[]
        for exponent in (0,30,310):
            xs=[x*10**exponent for x in raw]
            solved=harness.request({'input':list(map(str,xs)),'diagnostics':True,'hard_ms':16000})
            if solved['status']=='solved':verify(xs,solved['operations'])
            result['scaled_search'].append({'decimal_scale_exponent':exponent,'input':list(map(str,xs)),**solved})
            print('scaled search',exponent,solved['status'],solved.get('steps'),solved.get('calls'),flush=True)
        base=result['scaled_search'][0]
        if base['status']=='solved':
            for exponent in (30,310):verify([x*10**exponent for x in raw],base['operations'])
            result['base_path_replays_on_all_scales']=True
        result['tiny_budget']=harness.request({'input':list(map(str,large)),'diagnostics':True,
            'budget':{'width':400,'depth':70,'maxNodes':10,'timeMs':1,'moveCap':60},'hard_ms':16000})
        print('tiny budget',result['tiny_budget']['status'],result['tiny_budget'].get('reported_solve_ms'),
            result['tiny_budget'].get('calls'),flush=True)
        # Independent input-classification guard samples include huge integer strings.
        result['known_classes']=[]
        for xs,expected in [([1]*10+[-10],'impossible'),([7]*11,'solved'),([1,2,3],'solved'),
                            ([1,2],'impossible'),([1,2,3,4],'unsupported')]:
            got=harness.request({'input':list(map(str,xs))})
            assert got['status']==expected,(xs,got)
            if got['status']=='solved':verify(xs,got['operations'])
            result['known_classes'].append({'input':xs,'status':got['status'],'G':got.get('G')})
    (HERE/'structure_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('exact macro bases and classification checks: PASS',flush=True)


if __name__=='__main__':main()
