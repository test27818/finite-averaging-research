"""Exclude fresh-context warmup as the explanation of tiny timing differences."""
from pathlib import Path
from fractions import Fraction
import json
from benchmark_arena import Harness,cases,verify

HERE=Path(__file__).resolve().parent


def main():
    selected=[r for r in cases() if r['suite']=='paired_small']
    with Harness() as harness:
        macros=harness.request({'action':'macros'})
        count=0
        for entry in macros['results']:
            size,zeros=entry['size'],entry['zeros']
            for j in range(size-1):
                raw=[0]*(size+zeros)
                raw[j]=1;raw[size-1]=-1
                verify(raw,entry['operations'])
                count+=1
        print('independent Fraction macro-basis replay: PASS',count,flush=True)
        warm=harness.request({'action':'suite','cases':[{'id':r['id'],'input':list(map(str,r['input']))} for r in selected]})
        assert warm['status']=='ok'
        raw_by_id={r['id']:r['input'] for r in selected}
        for r in warm['cases']:
            assert r['status']=='solved'
            verify(raw_by_id[r['id']],r['operations'])
        (HERE/'warm_small.json').write_text(json.dumps({'warmup_cases':3,'timing':'one persistent JS VM, three unmeasured warmups',
                                                     'cases':warm['cases']},indent=2)+'\n',encoding='utf-8')
        (HERE/'macro_basis_checks.json').write_text(json.dumps({'independent_basis_checks':count,
            'macros':macros['results']},indent=2)+'\n',encoding='utf-8')
        print('warm JS mean ms:',sum(r['reported_solve_ms'] for r in warm['cases'])/len(warm['cases']))


if __name__=='__main__':main()
