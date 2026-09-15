"""Parallel extra-atom search with trace filtering before lattice checks."""
import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from math import gcd
from time import perf_counter
from compile_bn_integer_templates import (
    middle_states,selections,admissible_mean,contract,total,solved_size,primitive_matrix)
from verify_bn_integer_templates import replay,physical_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order


def periodic_product(flank,matrix):
    a,b,c,d = flank
    x,y,z,w = matrix
    trace = a*x+b*z+c*y+d*w
    det = (a*d-b*c)*(x*w-y*z)
    if not det:
        return False
    if trace == 0:
        return True
    if det <= 0 or trace*trace not in (det,2*det,3*det,4*det):
        return False
    return bool(finite_order(mul(flank,matrix)))


def batch(task):
    n,source,items,*options = task
    prefilter = options[0] if options else True
    flank = options[1] if len(options)>1 else (1,0,0,1)
    all_orders = options[2] if len(options)>2 else False
    collect_all = options[3] if len(options)>3 else False
    fa,fb,fc,fd = flank
    r = n-4
    hits = {}
    checked = 0
    seen = set()
    for state,prefix in items:
        caps = tuple(c for x,y,c in state)
        for chosen in selections(caps,3):
            if sum(k>0 for k in chosen)<2:
                continue
            mean = admissible_mean(state,chosen,3)
            target,scale = contract(state,chosen,*mean)
            if target in seen:
                continue
            seen.add(target)
            capacities = tuple(c for x,y,c in target)
            for size in range(r,r+3):
                if not solved_size(size):
                    continue
                for leftover in selections(capacities,n-size):
                    sx,sy = total(target,leftover)
                    # Mean=(-sx,-sy)/size since the complete state is zero-sum.
                    # trace=3*x + sy-b +(size-r)*y = 0 determines b.
                    required = (r*fb-3*fa)*sx+(r*fd-3*fc)*sy
                    candidates = [i for i,((a,b,c),count) in enumerate(zip(target,leftover))
                                  if count and (collect_all or not prefilter or
                                      (periodic_product(flank,(-3*sx,-3*sy,r*sx-size*a,r*sy-size*b))
                                       if all_orders else size*(fb*a+fd*b) == required))]
                    if not candidates:
                        continue
                    checked += 1
                    counts = tuple(c-k for c,k in zip(capacities,leftover))
                    finalmean = admissible_mean(target,counts,size)
                    if finalmean is None:
                        continue
                    (x,y),den = finalmean
                    for index in candidates:
                        a,b,_ = target[index]
                        raw = (3*x,3*y,den*(sx-a)+(size-r)*x,
                               den*(sy-b)+(size-r)*y)
                        accepted = (periodic_product(flank,raw) if all_orders else
                                    fa*raw[0]+fb*raw[2]+fc*raw[1]+fd*raw[3] == 0)
                        if not accepted and not collect_all:
                            assert not prefilter
                            continue
                        det = raw[0]*raw[3]-raw[1]*raw[2]
                        if not det:
                            continue
                        key = primitive_matrix(raw)
                        if gcd(key[0]*key[3]-key[1]*key[2],n) != 1:
                            continue
                        row = dict(prefix,source=source,before_extra=state,
                                   extra=dict(counts=chosen,scale=scale),before_final=target,
                                   final=dict(counts=counts,singleton=index),
                                   raw=raw,denominator=3*den)
                        hits.setdefault(key,row)
    return hits,len(seen),checked


def search(n,jobs,flank=(1,0,0,1),all_orders=False,collect_all=False):
    start = perf_counter()
    source,prefixes,_ = middle_states(n,True,True,True)
    items = list(prefixes.items())
    tasks = [(n,source,items[i:i+64],True,flank,all_orders,collect_all) for i in range(0,len(items),64)]
    print("prefixes",len(items),"batches",len(tasks),"jobs",jobs,flush=True)
    hits = {}
    states = tests = 0
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        for result,count,checked in pool.map(batch,tasks):
            hits.update(result)
            states += count
            tests += checked
    for key,row in hits.items():
        replay(n,row)
        a,b,c,d = physical_matrix(row)
        if collect_all:
            assert a*d-b*c
        elif all_orders:
            assert periodic_product(flank,key)
        else:
            assert flank[0]*a+flank[1]*c+flank[2]*b+flank[3]*d == 0 and a*d-b*c
    suffix = "involutions" if flank == (1,0,0,1) else "seed_products"
    if all_orders:
        suffix += "_all_orders"
    if collect_all:
        suffix = "full_returns"
    out = Path(__file__).with_name(f"b{n}_extra_atom_{suffix}.json")
    out.write_text(json.dumps(dict(n=n,flank=flank,hits=[dict(matrix=k,row=v) for k,v in sorted(hits.items())]),
                              indent=2)+"\n",encoding="utf-8")
    print("unique involutions",len(hits),"batch-local states",states,"lattice checks",tests,
          "seconds",round(perf_counter()-start,3),flush=True)
    if not collect_all:
        print("keys",sorted(hits),flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n",type=int,default=59)
    parser.add_argument("--jobs",type=int,default=4)
    parser.add_argument("--flank",type=int,nargs=4,default=(1,0,0,1))
    parser.add_argument("--all-orders",action="store_true")
    parser.add_argument("--collect-all",action="store_true")
    args = parser.parse_args()
    search(args.n,args.jobs,tuple(args.flank),args.all_orders,args.collect_all)
