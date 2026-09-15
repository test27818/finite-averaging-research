#!/usr/bin/env python3
"""Current algorithm baseline. Reads ONLY a/id, never label/min_steps/sequence.

python3 baselines/current.py data/test.jsonl results/current_test.jsonl --seconds 2
Output combines judge/min_steps/construct fields; evaluator can score each task.
For min_steps use --task min_steps to put certified minimum in answer; unknown=null.
"""
import argparse
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from solver_v2 import solve


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('ground',type=Path)
    ap.add_argument('output',type=Path)
    ap.add_argument('--task',choices=['judge','construct','min_steps'],default='construct')
    ap.add_argument('--seconds',type=float,default=2)
    ap.add_argument('--opt-ms',type=float,default=0)
    args=ap.parse_args()
    out=[]
    for line in args.ground.read_text().splitlines():
        row=json.loads(line)
        # No oracle truth is passed to solve().
        r=solve(row['a'],deadline_s=args.seconds,
                optimize_ms=None if args.task=='min_steps' else args.opt_ms)
        out.append(dict(id=row['id'], answer=r['min_steps'] if args.task=='min_steps'
                        else ('YES' if r['ok'] else 'NO'), steps=r['sequence'],
                        certified=r['certified'],lb=r['lb'],ub=r['ub'],status=r['status']))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(''.join(json.dumps(r)+'\n' for r in out))
    print('wrote',len(out),'predictions to',args.output)


if __name__=='__main__':
    main()
