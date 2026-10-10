"""Snapshot audit and same-input comparisons; external algorithm is unmodified.

Node executes only inspected computational functions in a VM worker. Timing
excludes loading and rendering; Python Fraction independently checks all words.
One case at a time avoids parallel timing contention. Hard timeouts are unknown.
"""

import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'work'))


def read(name):
    return json.loads((ROOT/'work'/name).read_text(encoding='utf-8'))


def verify(raw,ops):
    values=list(map(Fraction,raw))
    target=sum(values)/len(values)
    for atom in ops:
        assert len(atom)==len(set(atom))==3
        assert all(type(i) is int and 1<=i<=len(raw) for i in atom)
        mean=sum(values[i-1] for i in atom)/3
        for i in atom:
            values[i-1]=mean
    assert values==[target]*len(values)


class Harness:
    def __enter__(self):
        self.process=subprocess.Popen(['node',str(HERE/'run_arena.cjs')],stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8')
        return self

    def request(self,request):
        self.process.stdin.write(json.dumps(request)+'\n');self.process.stdin.flush()
        text=self.process.stdout.readline()
        if not text: raise RuntimeError(self.process.stderr.read())
        return json.loads(text)

    def __exit__(self,*args):
        self.process.stdin.close()
        try:self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:self.process.kill();self.process.wait()
        self.process.stdout.close();self.process.stderr.close()


def cases():
    out=[]
    for i,r in enumerate(read('pair_triple_same_input_benchmark.json')['records']):
        out.append({'id':f'paired-{i}','suite':'paired_small','input':r['input'],
                    'previous':r['ternary'],'previous_invariant_steps':r['ternary_invariant_steps']})
    for i,r in enumerate(read('double_triple_length_benchmark.json')['records']):
        out.append({'id':f'height-{i}','suite':'height','input':r['raw'],
                    'bits':r['sample_bits'],'previous':r['maximal-drop']})
    for i,r in enumerate(read('double_triple_length_large_benchmark.json')['records']):
        if r['sample']==0:
            out.append({'id':f'large-{i}','suite':'large','input':r['raw'],
                        'bits':r['sample_bits'],'previous':r['maximal-drop']})
    example=[0,1,2,3,4,5,6]
    out.append({'id':'example','suite':'scale','input':example})
    for digits in (30,100,310):
        out.append({'id':f'example-scale-{digits}','suite':'scale',
                    'input':[x*10**digits for x in example]})
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--ids',nargs='*')
    parser.add_argument('--batch',action='store_true')
    parser.add_argument('--output',default='results.json')
    args=parser.parse_args()
    selected=cases()
    if args.ids:selected=[r for r in selected if r['id'] in args.ids]
    results=[]
    output=HERE/args.output
    with Harness() as harness:
        for case in selected:
            request={'input':list(map(str,case['input'])),'hard_ms':16000}
            if args.batch:
                request['budget']={'width':140,'depth':45,'maxNodes':14000,'timeMs':1500,'moveCap':42}
            arena=harness.request(request)
            if arena['status']=='solved':
                verify(case['input'],arena['operations'])
                arena['independent_verified']=True
            result={**case,'arena':arena}
            results.append(result)
            output.write_text(json.dumps({'source':'snapshot provenance.json','mode':'batch' if args.batch else 'single',
                'timing':'Node worker solver functions; excludes load/render; original budget plus external16s safeguard',
                'cases':results},indent=2)+'\n',encoding='utf-8')
            print(case['id'],'n',len(case['input']),'old steps',case.get('previous',{}).get('steps'),
                  'arena',arena['status'],'steps',arena.get('steps'),'ms',round(arena.get('reported_solve_ms',arena.get('outer_ms',0)),2),
                  'method',arena.get('method',''),flush=True)


if __name__=='__main__':main()
