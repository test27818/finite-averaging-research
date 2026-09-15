#!/usr/bin/env python3
"""Convert browser JSON export to benchmark construct predictions.

Matches the ORIGINAL ORDER of input to a/id (not sorted input). Repeats may map to
multiple benchmark IDs. Independently validates operations; ignores browser's claims
of optimality. No operation schedule can by itself certify a minimum.
"""
import argparse
import json
from pathlib import Path
from solver import verify_sequence


def convert(export, ground):
    records = export if isinstance(export,list) else export.get('cases',[export])
    by_input={}
    for row in ground:
        by_input.setdefault(tuple(row['a']),[]).append(row['id'])
    out={}
    for r in records:
        if not isinstance(r,dict) or not isinstance(r.get('input'),list):
            raise ValueError('expected input array in browser export')
        values=[]
        for x in r['input']:
            if type(x) not in (str,int) or (type(x) is int and abs(x)>2**53-1):
                raise ValueError('browser integers must be strings or safe JSON integers')
            text=str(x)
            if not text.lstrip('+-').isdigit() or text.count('+')+text.count('-')>1:
                raise ValueError('invalid integer')
            values.append(int(text))
        values=tuple(values)
        if values not in by_input:
            raise ValueError('export input does not match ground truth in original order')
        steps=r.get('operations')
        if not isinstance(steps,list) or not verify_sequence(values,steps)[0]:
            raise ValueError('invalid/incomplete operation certificate')
        for id in by_input[values]:
            if id not in out or len(steps)<len(out[id]['steps']):
                out[id]=dict(id=id,steps=steps)
    return list(out.values())


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('export',type=Path)
    ap.add_argument('--ground',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    rows=[json.loads(l) for l in args.ground.read_text().splitlines()]
    preds=convert(json.loads(args.export.read_text(encoding='utf-8-sig')),rows)
    args.out.write_text(''.join(json.dumps(r)+'\n' for r in preds))
    print('verified and converted',len(preds),'certificates')


if __name__=='__main__':
    main()
