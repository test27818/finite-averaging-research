"""Targeted extra-call inverse bridge with exact coefficient filtering.

The search is bounded by the extra call sizes. Missing targets are not
proofs of impossibility in larger libraries or at greater call depth.
"""

import argparse
from math import gcd
from time import perf_counter
from verify_twenty_five_arithmetic_group import finite_order

from compile_bn_integer_templates import (
    middle_states,selections,admissible_mean,contract,total,primitive_matrix,
)


TARGET = (-72,-5,-162,-9)


def finish(n,state,target):
    r = n-4
    capacities = tuple(c for _,_,c in state)
    if target is not None:a,b,c,d = target
    for size in range(r,r+3):
        for leftover in selections(capacities,n-size):
            sx,sy = total(state,leftover)
            if target is not None and sx*b != sy*a:
                continue
            matches = []
            if target is None:
                for index,((u,v,_),count) in enumerate(zip(state,leftover)):
                    if count:
                        raw = (-3*sx,-3*sy,r*sx-size*u,r*sy-size*v)
                        if (raw[0]*raw[3]-raw[1]*raw[2]) % n and finite_order(raw):
                            matches.append(index)
                if not matches:continue
            counts = tuple(cap-left for cap,left in zip(capacities,leftover))
            mean = admissible_mean(state,counts,size)
            if mean is None:continue
            (x,y),denominator = mean
            for index,((u,v,_),count) in enumerate(zip(state,leftover)):
                if not count or (target is None and index not in matches):continue
                second = (denominator*(sx-u)+(size-r)*x,
                          denominator*(sy-v)+(size-r)*y)
                raw = 3*x,3*y,*second
                if any(raw) and (target is None or primitive_matrix(raw) == target):
                    return dict(counts=counts,singleton=index,raw=raw,denominator=3*denominator)
    return None


def search(n=47,extra_sizes=(3,),target=TARGET,collect=False):
    source,prefixes,_ = middle_states(n,True,True,True)
    started = perf_counter()
    seen = set(prefixes)
    tested = 0
    found = {}
    for index,(state,prefix) in enumerate(prefixes.items(),1):
        capacities = tuple(c for _,_,c in state)
        for size in extra_sizes:
            for counts in selections(capacities,size):
                if sum(k>0 for k in counts)<2:continue
                mean = admissible_mean(state,counts,size)
                if mean is None:continue
                following,scale = contract(state,counts,*mean)
                if following in seen:continue
                seen.add(following)
                tested += 1
                final = finish(n,following,target)
                if final is not None:
                    certificate = dict(prefix,source=source,before_extra=state,
                                       extra=dict(counts=counts,scale=scale),
                                       before_final=following,
                                       final=dict(counts=final['counts'],singleton=final['singleton']),
                                       raw=final['raw'],denominator=final['denominator'])
                    matrix = primitive_matrix(final['raw'])
                    if matrix not in found:
                        found[matrix] = certificate
                        print('FOUND exact return',matrix,'extra',size,'states',tested,flush=True)
                    if not collect:
                        print('CERTIFICATE',repr(certificate),flush=True)
                        return certificate
        if index % 250 == 0:
            print('prefixes',index,'of',len(prefixes),'extra states',tested,
                  'seconds',round(perf_counter()-started,3),flush=True)
    if collect:
        print('COLLECTED returns',len(found),'sizes',extra_sizes,'states',tested,
              'seconds',round(perf_counter()-started,3),flush=True)
        return found
    print('BOUND: return target absent','sizes',extra_sizes,'states',tested,
          'seconds',round(perf_counter()-started,3),flush=True)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sizes',type=int,nargs='+',default=[3])
    parser.add_argument('--finite-order',action='store_true')
    parser.add_argument('--collect',action='store_true')
    args = parser.parse_args()
    search(extra_sizes=tuple(args.sizes),target=None if args.finite_order else TARGET,collect=args.collect)
