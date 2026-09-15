"""Bounded three-factor finite-cycle search using vectorized trace filters.

Floating point is used only to propose near-zero traces. Every returned
candidate is rechecked with exact integer finite-order classification.
This search is not a certificate that no cycle exists when it returns none.
"""

import argparse
from time import perf_counter

import numpy as np

from compile_bn_integer_templates import compile_returns
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order


def search(n,limit,prefixes=None):
    rows,_ = compile_returns(n,True,True,True)
    keys = sorted(rows,key=lambda m:(max(map(abs,m)),m))[:limit]
    candidates = np.array(keys,dtype=np.float64)
    norms = np.max(np.abs(candidates),axis=1)
    candidates /= norms[:,None]
    transpose = candidates[:,[0,2,1,3]].T.copy()
    determinants = candidates[:,0]*candidates[:,3]-candidates[:,1]*candidates[:,2]
    started = perf_counter()
    batches = 0
    found = []
    for i,a in enumerate(keys):
        products = [mul(a,b) for b in keys]
        pair = np.array(products,dtype=np.float64)
        pair /= np.max(np.abs(pair),axis=1)[:,None]
        traces = pair@transpose
        det_pair = pair[:,0]*pair[:,3]-pair[:,1]*pair[:,2]
        det_products = det_pair[:,None]*determinants[None,:]
        near = np.abs(traces) < 1e-11
        for order_value in (1,2,3):
            near |= np.abs(traces*traces-order_value*det_products) < 1e-13
        for j,k in zip(*np.nonzero(near)):
            exact = mul(products[int(j)],keys[int(k)])
            order = finite_order(exact)
            if order:
                result = (a,keys[int(j)],keys[int(k)],order)
                found.append(result)
                if prefixes is None:
                    print('FOUND',result,'seconds',round(perf_counter()-started,3),flush=True)
                    return result
        batches += 1
        if prefixes is not None and batches >= prefixes:
            break
        if batches % 100 == 0:
            print('prefix generators',batches,'of',len(keys),'seconds',round(perf_counter()-started,3),flush=True)
    if prefixes is not None:
        print('EXACT CYCLES',len(found),'from prefixes',batches,'seconds',round(perf_counter()-started,3),flush=True)
        return found
    print('NO CANDIDATE in floating proposal search',len(keys),'seconds',round(perf_counter()-started,3),flush=True)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=29)
    parser.add_argument('--limit',type=int,default=200)
    parser.add_argument('--prefixes',type=int)
    args = parser.parse_args()
    search(args.n,args.limit,args.prefixes)
