"""Remeasure previous methods serially, after the web benchmark has stopped."""
from pathlib import Path
from time import perf_counter
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work'))
from triple_average_optimal_search import solve
from analyze_double_triple_sequence_length import solve_policy


def main():
    result=[]
    data=json.loads((HERE/'comparison_single.json').read_text(encoding='utf-8'))
    # Warm up imports and code once outside the measured corpus.
    solve([0,1,2,3,4,5,6,7,8,9,10],seconds=0)
    for case in data['cases']:
        if case['suite']=='scale':continue
        raw=case['input']
        begin=perf_counter()
        if case['suite']=='paired_small':
            output=solve(raw,seconds=0)
            seconds=perf_counter()-begin
            chosen={'status':output['status'],'steps':output['steps'],
                    'solver_ms':output['solveSeconds']*1000,'outer_ms':seconds*1000,
                    'method':'existing Python portfolio with no IDA optimization'}
        else:
            from verify_composite_arity_transfer import primitive_center
            state=primitive_center(raw)
            output=solve_policy(state,'maximal-drop')
            seconds=perf_counter()-begin
            chosen={**output,'solver_ms':output['solve_seconds']*1000,'outer_ms':seconds*1000,
                    'method':'existing Python maximal-drop constructive strategy'}
        result.append({'id':case['id'],'baseline':chosen})
        print(case['id'],chosen['status'],chosen['steps'],round(chosen['solver_ms'],3),flush=True)
        (HERE/'baseline_current.json').write_text(json.dumps({'timing':'same computer,serial run; different implementation languages',
            'cases':result},indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':main()
