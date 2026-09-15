#!/usr/bin/env python3
"""Bounded reproducible migration evaluation (no UI dependencies).

Uses frozen pre-migration truth, never the upgraded truth as an independent oracle.
All current YES instances are constructed once and independently verified. Small
legacy BFS is timed separately; wall-clock results depend on the host.
"""
import json
from pathlib import Path
import platform
import time
import sys
from collections import Counter
import solver_v2 as V
import construct as C
from solver import judge, verify_sequence
from legacy_bfs import min_steps_sequence as bfs

ROOT=Path(__file__).resolve().parents[1]
CASES=[([38,-23,-14,16,-11,4,63,80,14,38],10),
       ([-81,-60,-95,-95,-20,-13,-87,-80,42,54],11)]


def main():
    report=dict(engine='projective-ida-v3',python=platform.python_version(),
                inputs='frozen before migration; all counts include repeated instances')
    t0=time.time(); old_t=new_t=0; count=0
    for l in (ROOT/'tests/fixtures/original_small.jsonl').read_text().splitlines():
        r=json.loads(l)
        if r['min_steps'] is None:continue
        ts=time.time();old,seq=bfs(r['a']);old_t+=time.time()-ts
        ts=time.time();new=V.solve(r['a'],deadline_s=5);new_t+=time.time()-ts
        assert old==r['min_steps']==new['min_steps'] and new['certified']
        assert verify_sequence(r['a'],new['sequence'])[0]
        count+=1
    report['frozen_small']=dict(agree=count,disagree=0,legacy_bfs_seconds=old_t,current_seconds=new_t)
    samples=json.loads((ROOT/'tests/fixtures/pre_migration_260.json').read_text())
    ts=time.time();certified=0
    for r in samples:
        new=V.solve(r['a'],deadline_s=5)
        assert new['sequence'] is not None and verify_sequence(r['a'],new['sequence'])[0]
        assert new['lb']<=r['min']<=new['ub']
        if new['certified']:
            assert new['min_steps']==r['min'];certified+=1
    report['frozen_random']=dict(total=len(samples),certified=certified,seconds=time.time()-ts,
        caveat='selected because the previous solver could certify them; not an unbiased scalability estimate')
    report['construction']={}
    for sp in ['small','dev','test','hard']:
        count=verified=0;times=[]
        for l in (ROOT/'data'/f'{sp}.jsonl').read_text().splitlines():
            r=json.loads(l);assert judge(r['a'])==(r['label']=='YES')
            if r['label']!='YES':continue
            count+=1;ts=time.time();c=C.construct(r['a'],deadline_s=5);times.append(time.time()-ts)
            if c['verified']:
                assert verify_sequence(r['a'],c['steps'])[0];verified+=1
        report['construction'][sp]=dict(total=count,verified=verified,seconds=sum(times),
                                        max_seconds=max(times))
    report['cases']=[]
    for a,minimum in CASES:
        r=V.solve(a,deadline_s=10)
        assert r['certified'] and r['min_steps']==minimum
        assert verify_sequence(a,r['sequence'])[0]
        report['cases'].append(dict(input=a,minimum=minimum,seconds=r['time'],
                                    expanded=r['states'],notes=r['notes']))
    report['seconds']=time.time()-t0
    path=ROOT/'results/migration_report.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    print('Report:',path)


if __name__=='__main__':main()
