"""Parallel finite seed survey; exact integer screening before physical replay."""
import argparse
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from math import lcm
from time import perf_counter
from compile_bn_integer_templates import compile_returns,primitive_matrix
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order
from verify_bn_integer_templates import replay


def inspect(p):
    start = perf_counter()
    rows,_ = compile_returns(p,True,True,True)
    keys = sorted(rows)
    pairs = []
    determinants = [a*d-b*c for a,b,c,d in keys]
    for i,a in enumerate(keys):
        aa,ab,ac,ad = a
        for j in range(i,len(keys)):
            b = keys[j]
            ba,bb,bc,bd = b
            trace = aa*ba+ab*bc+ac*bb+ad*bd
            det = determinants[i]*determinants[j]
            if trace == 0:
                order = 2
            elif det > 0 and trace*trace in (det,2*det,3*det):
                order = {1:3,2:4,3:6}[trace*trace//det]
            elif det > 0 and trace*trace == 4*det:
                order = finite_order(mul(a,b))
            else:
                order = None
            if order:
                pairs.append((a,b,order))
    targets = []
    for k in (1,3,5,7,9):
        t = F(1,3**k)
        m = p-4
        matrix = (1-t,t,-(m*(1-t)+1)/3,-m*t/3)
        den = lcm(*(x.denominator for x in matrix))
        key = primitive_matrix(tuple(int(x*den) for x in matrix))
        if key in rows:
            targets.append((k,key))
    hits = {m for a,b,_ in pairs for m in (a,b)} | {m for _,m in targets}
    for m in hits:
        replay(p,rows[m])
    return dict(p=p,templates=len(rows),pair_checks=len(keys)*(len(keys)+1)//2,
                pairs=pairs,odd_returns=targets,replayed=len(hits),
                seconds=round(perf_counter()-start,3))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes",type=int,nargs="+",default=[53,59,71,83])
    parser.add_argument("--jobs",type=int,default=4)
    args = parser.parse_args()
    with ProcessPoolExecutor(max_workers=min(args.jobs,len(args.primes))) as pool:
        for result in pool.map(inspect,args.primes):
            print(result,flush=True)
    print("Finite current-library survey; missing candidates do not prove impossibility.")
