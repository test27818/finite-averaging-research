"""Bounded four-factor cycle proposals, followed by exact checks.

This is a discovery tool: floating tolerances can miss solutions, so a
negative result is not a proof that a finite library has no cycles.
"""

import argparse
from time import perf_counter

import numpy as np

from compile_bn_integer_templates import compile_returns,primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order


def search(n,batches=8,batch_size=64):
    rows,_ = compile_returns(n,True,True,True)
    keys = sorted(rows,key=lambda x:(max(map(abs,x)),x))
    pairs = {}
    for i,a in enumerate(keys):
        for j,b in enumerate(keys):
            pairs.setdefault(primitive_matrix(mul(a,b)),(i,j))
    matrices = sorted(pairs,key=lambda x:(max(map(abs,x)),x))
    array = np.asarray(matrices,dtype=np.float64)
    array /= np.max(np.abs(array),axis=1)[:,None]
    transpose = array[:,[0,2,1,3]].T.copy()
    det = array[:,0]*array[:,3]-array[:,1]*array[:,2]
    found = []
    started = perf_counter()
    for offset in range(0,min(len(matrices),batches*batch_size),batch_size):
        current = array[offset:offset+batch_size]
        trace = current@transpose
        product_det = det[offset:offset+batch_size,None]*det[None,:]
        near = np.abs(trace) < 1e-12
        for k in (1,2,3):
            near |= np.abs(trace*trace-k*product_det) < 1e-14
        for i,j in zip(*np.nonzero(near)):
            a,b = matrices[offset+int(i)],matrices[int(j)]
            order = finite_order(mul(a,b))
            if order:
                word = pairs[a]+pairs[b]
                found.append((tuple(keys[i] for i in word),order))
        if found or offset % (16*batch_size) == 0 or offset+batch_size >= len(matrices):
            print('pair prefixes',min(offset+batch_size,len(matrices)),'of',len(matrices),
                  'exact cycles',len(found),'seconds',round(perf_counter()-started,3),flush=True)
        if found:
            print('SAMPLE',found[:3],flush=True)
            break
    return found


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=47)
    parser.add_argument('--batches',type=int,default=8)
    args = parser.parse_args()
    search(args.n,args.batches)
