"""Symmetrized necessary equations for arbitrary-prime collision mass.

Every actual solution can be averaged within residue classes, preserving total
mass. Thus compression is valid for the mass test without assuming equal
actual values inside a class. This file is exploratory, not a threshold proof.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import gcd, lcm


def equations(p, alpha, beta, residues, frequencies):
    width = len(residues)
    for j, residue in enumerate(residues):
        if residue in (0,1):
            yield tuple(int(i == j) for i in range(width)), p if residue == 0 else 1-p
    for counts in product(*(range(f+1) for f in frequencies)):
        size = sum(counts)
        if not 1 <= size <= p:
            continue
        remainder = sum(r*k for r,k in zip(residues,counts)) % p
        i = -remainder % p
        if i <= min(alpha,p-size):
            if p-size-i <= beta:
                yield (0,)*width, 1
                return
            yield counts, p-i
        j = (remainder-size) % p
        if j <= min(beta,p-size):
            yield counts, size+j-p


def echelon(rows, width):
    pivots = {}
    for coefficients,rhs in rows:
        row = tuple(coefficients)+(rhs,)
        for j,pivot in sorted(pivots.items()):
            if row[j]:
                a,b = pivot[j],row[j]
                row = tuple(a*x-b*y for x,y in zip(row,pivot))
                common = gcd(*row)
                if common:
                    row = tuple(x//common for x in row)
        j = next((j for j in range(width) if row[j]),None)
        if j is None:
            if row[-1]:
                return None
        else:
            if row[j] < 0:
                row = tuple(-x for x in row)
            pivots[j] = row
    return pivots


def functional(pivots, coefficients):
    row,constant = list(map(F,coefficients)),F(0)
    for j,pivot in sorted(pivots.items()):
        if row[j]:
            factor = row[j]/pivot[j]
            row = [x-factor*y for x,y in zip(row,pivot[:-1])]
            constant += factor*pivot[-1]
    return None if any(row) else constant


def scalar_solution(pivots,width):
    if len(pivots) != width:
        return None
    result = [F(0)]*width
    for j,row in sorted(pivots.items(),reverse=True):
        result[j] = (F(row[-1])-sum(row[k]*result[k] for k in range(j+1,width)))/row[j]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--p',type=int,default=7)
    parser.add_argument('--extra',type=int,default=2)
    parser.add_argument('--min-extra',type=int,default=0)
    parser.add_argument('--dump',action='store_true')
    args = parser.parse_args()
    p=args.p
    stats,denominators,massranges,exceptions = Counter(),{}, {}, []
    for extra in range(args.min_extra,args.extra+1):
        denominators[extra]=set()
        massranges[extra]=[]
        for alpha in range(p-2):
            for beta in range(min(alpha,p-3-alpha)+1):
                length=p+extra-alpha-beta
                for seq in combinations_with_replacement(range(p),length):
                    f=Counter(seq)
                    if max(f.values())>=p or f[0]>1 or f[1]>1:
                        continue
                    residues,frequencies=list(f),list(f.values())
                    pivots=echelon(equations(p,alpha,beta,residues,frequencies),len(residues))
                    stats['systems']+=1
                    if pivots is None:
                        continue
                    stats['consistent']+=1
                    mass=functional(pivots,frequencies)
                    if mass is None:
                        stats['undetermined-mass']+=1
                        exceptions.append((extra,alpha,beta,dict(f),'free-mass'))
                        continue
                    mass+=p+alpha
                    denominators[extra].add(mass.denominator)
                    massranges[extra].append(mass)
                    if (3*p+extra) % mass.denominator:
                        stats['denominator-not-dividing-size']+=1
                        if len(exceptions)<12:
                            exceptions.append((extra,alpha,beta,dict(f),str(mass)))
                    values=scalar_solution(pivots,len(residues))
                    if values is not None:
                        if any(x.denominator%p==0 or x.numerator*pow(x.denominator,-1,p)%p!=r for x,r in zip(values,residues)):
                            stats['wrong-residue']+=1
                        if args.dump and extra:
                            print('template',extra,alpha,beta,dict(f),tuple(map(str,values)),str(mass),flush=True)
                    stats['consistent-extra-'+str(extra)]+=1
        print('finished extra',extra,'systems',stats['systems'],flush=True)
    print('p',p,'stats',dict(stats))
    print('mass denominators',{k:sorted(v) for k,v in denominators.items()})
    print('mass ranges',{k:(str(min(v)),str(max(v)),len(v)) if v else None for k,v in massranges.items()})
    print('exceptions',exceptions)


if __name__=='__main__':
    main()
