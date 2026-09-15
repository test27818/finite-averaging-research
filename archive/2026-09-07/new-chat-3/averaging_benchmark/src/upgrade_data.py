#!/usr/bin/env python3
"""Enrich ground truth with the current solver; never downgrade existing truth.

Default writes to a SEPARATE --out directory. Existing labels, IDs, inputs and known
minima are checked, not silently replaced. Every chosen witness is independently
verified. All files and a SHA-256 manifest are staged before promotion with --in-place.
The default budgets are bounded; an incomplete search stores LB/UB, never a minimum.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import time
from solver import judge, verify_sequence
from solver_v2 import solve

ROOT = Path(__file__).resolve().parents[1]


def upgrade(path, out_path, deadline, budget):
    path, out_path = Path(path), Path(out_path)
    rows = [json.loads(l) for l in path.read_text().splitlines()]
    stats = dict(total=len(rows), mixable=0, min_certified=0, seq_verified=0,
                 bounds_only=0, new_minima=0)
    t0 = time.time()
    out = []
    for row in rows:
        a = row['a']
        if row['label'] != ('YES' if judge(a) else 'NO'):
            raise ValueError('label disagreement: '+row['id'])
        if row['label'] != 'YES':
            out.append(row)
            continue
        stats['mixable'] += 1
        r = solve(a, deadline_s=deadline, node_budget=budget)
        old_min, old_seq = row.get('min_steps'), row.get('sequence')
        if old_seq is not None and not verify_sequence(a,old_seq)[0]:
            raise ValueError('invalid old witness: '+row['id'])
        if old_min is not None:
            if old_seq is None or len(old_seq) != old_min:
                raise ValueError('old minimum lacks matching witness: '+row['id'])
            if r['lb'] > old_min or (r['ub'] is not None and r['ub'] < old_min):
                raise ValueError('old/new bounds conflict: '+row['id'])
            if r['certified'] and r['min_steps'] != old_min:
                raise ValueError('minima disagree: '+row['id'])
        rec = dict(row)
        if r['certified']:
            rec.update(min_steps=r['min_steps'], sequence=r['sequence'],
                       certified=True, lb=r['lb'], ub=r['ub'],
                       sequence_source='v3_ida_certified', min_steps_source='v3_ida_certified')
            if old_min is None:
                stats['new_minima'] += 1
        elif old_min is not None:
            # Preserve old proof and its matching witness even if this run times out.
            rec.update(certified=True, lb=old_min, ub=old_min,
                       min_steps_source=row.get('min_steps_source') or 'pre_migration_truth')
        else:
            options=[]
            if old_seq is not None:
                options.append((old_seq,row.get('sequence_source')))
            if r['sequence'] is not None:
                options.append((r['sequence'],'v3_construct_verified'))
            best = min(options,key=lambda x:len(x[0])) if options else (None,None)
            rec.update(min_steps=None, certified=False, lb=r['lb'],
                       sequence=best[0], sequence_source=best[1],
                       ub=len(best[0]) if best[0] is not None else None)
        if rec['sequence'] is not None:
            if not verify_sequence(a,rec['sequence'])[0]:
                raise ValueError('new witness failed verification: '+row['id'])
            if rec['ub'] != len(rec['sequence']):
                raise ValueError('upper bound/witness mismatch: '+row['id'])
            stats['seq_verified'] += 1
        stats['min_certified'] += rec['certified']
        stats['bounds_only'] += not rec['certified']
        out.append(rec)
    out_path.parent.mkdir(parents=True,exist_ok=True)
    out_path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in out))
    stats['seconds'] = round(time.time()-t0,3)
    print(path.name, stats, flush=True)
    return stats


def manifest(directory, seed, stats, budgets):
    files={}; dist={}
    for path in sorted(directory.glob('*.jsonl')):
        rows=[json.loads(l) for l in path.read_text().splitlines()]
        files[path.name]=dict(count=len(rows), sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        c=Counter(r['label'] for r in rows)
        dist[path.stem]=dict(YES=c['YES'],NO=c['NO'],total=len(rows))
    return dict(seed=seed,files=files,label_distribution=dist,
                engine='projective-ida-v3',upgrade=dict(budgets=budgets,stats=stats),
                note='Inputs/labels reproduce from seed. Resource-limited certification coverage may vary by hardware; checksums pin this release.')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ground',type=Path,default=ROOT/'data')
    ap.add_argument('--splits',nargs='+',default=['small','dev','test','hard'],choices=['small','dev','test','hard'])
    ap.add_argument('--deadline',type=float,default=2.0)
    ap.add_argument('--budget',type=int,default=1_000_000)
    ap.add_argument('--out',type=Path,default=ROOT/'data_upgraded')
    ap.add_argument('--in-place',action='store_true')
    args=ap.parse_args()
    if args.out.resolve()==args.ground.resolve() and not args.in_place:
        ap.error('Use --in-place explicitly to replace source data')
    if args.deadline<0 or args.budget<0:
        ap.error('budgets must be nonnegative')
    old_manifest=json.loads((args.ground/'manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix='avg-upgrade-',dir=ROOT) as tmp:
        stage=Path(tmp)
        for sp in ('small','dev','test','hard'):
            if (args.ground/f'{sp}.jsonl').exists():
                shutil.copy2(args.ground/f'{sp}.jsonl',stage/f'{sp}.jsonl')
        stats={sp:upgrade(args.ground/f'{sp}.jsonl',stage/f'{sp}.jsonl',args.deadline,args.budget)
               for sp in args.splits}
        data=manifest(stage,old_manifest.get('seed'),stats,dict(deadline_s=args.deadline,node_budget=args.budget))
        (stage/'manifest.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
        target=args.ground if args.in_place else args.out
        target.mkdir(parents=True,exist_ok=True)
        if args.in_place:
            backup=ROOT/('data_backup_'+time.strftime('%Y%m%d_%H%M%S'))
            shutil.copytree(args.ground,backup)
            print('Data backup:',backup)
        # Promotion only begins after the entire release passes validations.
        for path in stage.iterdir():
            shutil.copy2(path,target/path.name)
        print('Written:',target)


if __name__=='__main__':
    main()
