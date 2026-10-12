"""Exact p+3 solver with proved forced-run compression; no P claim.

The optional finite-field and real-range filter is a necessary escape condition. Budget
exhaustion raises SearchLimit and is never interpreted as a negative answer.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd,lcm,isqrt
from verify_fixed_p_block_norm_descent import reduce_double_core,valuation
from five_eight_first_escape import FirstEscape

class SearchLimit(RuntimeError):pass

def canonical(u):
    d=gcd(*u)
    if not d:return (0,)*len(u)
    a=tuple(sorted(x//d for x in u))
    b=tuple(sorted(-x for x in a))
    return min(a,b)

def local_zero_in_range(p,a,q,e):
    """Necessary real/arithmetic condition for the local common value to be zero."""
    if a%q:return False
    target=-a//q
    if e==1:return target in (1,2)
    scale=p**(e-2)
    return (p-1)*scale<=target<=2*p*scale


def escape_filter(p,a,u):
    """True certifies no solution; False is inconclusive, not acceptance."""
    assert u and u%p==0 and a%p
    e=valuation(u,p);q=u//p**e
    beta=(-3*a*pow(q,-1,p))%p
    powers=set();v=1
    for _ in range(e+1):
        if v in powers:break
        powers.add(v);v=2*v%p
    sign=1 if e%2 else -1
    # Using all three exceptions traps the state in two nonzero blocks unless
    # the current local common value is exactly zero. Its normalized numerator
    # lies in [(p-1)*p**(e-2), 2*p**(e-1)] for e>=2, or {1,2} for e=1.
    factors=(1,2,3) if local_zero_in_range(p,a,q,e) else (1,2)
    allowed={sign*k*v%p for k in factors for v in powers}
    return beta not in allowed

class Solver:
    def __init__(self,p,filter_escape=True,max_states=None,filter_first_escape=False):
        if p<5 or any(p%d==0 for d in range(2,isqrt(p)+1)):
            raise ValueError('p must be a prime at least 5')
        self.p=p;self.n=p+3;self.filter_escape=filter_escape
        self.filter_first_escape=filter_first_escape and p==5
        self.max_states=max_states;self.stats=Counter()
        self.children=lru_cache(None)(self._children)
        self.contract=lru_cache(None)(self._contract)
        self.distance=lru_cache(None)(self._distance)
        self.first_escape_possible=lru_cache(None)(self._first_escape_possible)

    def _first_escape_possible(self,u):
        a=-sum(u)//8
        inside=[x for x in u if x%5==0]
        outside=next(x for x in u if x%5)
        query=FirstEscape()
        result=query.decide((a,a+inside[0],a+inside[1],a+outside))
        self.stats['first_escape_queries']+=1
        self.stats['first_escape_nodes']+=query.stats['visited_nodes']
        return result['possible']

    def _children(self,u):
        p,n=self.p,self.n;out=set()
        for mask in range(1,7):
            s=sum(u[i] for i in range(3) if mask>>i&1)
            if s%p:continue
            q=s//p
            y=canonical(tuple(-q if mask>>i&1 else u[i]-q for i in range(3)))
            if sum(y)%n or y==u:continue
            assert n*sum(v*v for v in y)-sum(y)**2<n*sum(v*v for v in u)-sum(u)**2
            out.add(y)
        return tuple(sorted(out))

    def _contract(self,u):
        p,n=self.p,self.n;offset=0
        while True:
            if not any(u):return ('yes',offset,u)
            if sum(u)%n:return ('no',0,u)
            if not sum(u):return ('yes',offset+1,u)
            if self.filter_first_escape and sum(x%5==0 for x in u)==2:
                if not self.first_escape_possible(u):
                    self.stats['first_escape_rejections']+=1
                    return ('no',0,u)
            dup=None
            if u[0]==u[1]:dup,other=u[0],u[2]
            elif u[1]==u[2]:dup,other=u[1],u[0]
            if dup is not None:
                a=-(2*dup+other)//n
                if self.filter_escape and dup%p==0 and escape_filter(p,a,dup):
                    self.stats['escape_rejections']+=1
                    return ('no',0,u)
                reduced=reduce_double_core(p,dup,other)
                if reduced['status']=='yes':return('yes',offset+reduced['distance'],u)
                if reduced['status']=='no':return('no',0,u)
                offset+=reduced['forced']
                self.stats['batched_atoms']+=reduced['forced']
                b,c=reduced['pair'];u=canonical((b,b,c))
            ys=self.children(u)
            if not ys:return('no',0,u)
            if any(not sum(y) for y in ys):return('yes',offset+2,u)
            if len(ys)>1:return('branch',offset,u)
            u=ys[0];offset+=1;self.stats['forced_atoms']+=1

    def _distance(self,u):
        self.stats['queries']+=1
        if self.max_states is not None and self.stats['queries']>self.max_states:
            raise SearchLimit(dict(self.stats))
        tag,offset,v=self.contract(u)
        if tag=='yes':return offset
        if tag=='no':return None
        if v!=u:
            d=self.distance(v)
            return None if d is None else offset+d
        self.stats['branch_nodes']+=1
        answers=[self.distance(y) for y in self.children(u)]
        answers=[d for d in answers if d is not None]
        return None if not answers else 1+min(answers)

    def solve_core(self,u):
        if len(u)!=3:raise ValueError('a p+3 core must have three differences')
        return self.distance(canonical(u))

    def solve_input(self,values):
        n,p=self.n,self.p
        assert len(values)==n
        values=[Fraction(x) for x in values]
        mean=sum(values)/n
        centered=[x-mean for x in values]
        D=lcm(*(x.denominator for x in centered))
        x=[int(v*D) for v in centered];d=gcd(*x)
        if not d:return 0
        x=tuple(sorted(v//d for v in x))
        if gcd(*(v-x[0] for v in x))!=1:return None
        counts=Counter(x)
        heavy=next((a for a,c in counts.items() if c>=p),None)
        if heavy is not None:
            rest=list(x)
            for _ in range(p):rest.remove(heavy)
            return self.solve_core(tuple(v-heavy for v in rest))
        answers=[]
        for inds in combinations(range(n),3):
            s=sum(x[i] for i in inds)
            if s%p:continue
            a=-s//p
            d=self.solve_core(tuple(x[i]-a for i in inds))
            if d is not None:answers.append(1+d)
        return min(answers) if answers else None

if __name__=='__main__':
    import json
    for L in range(1,10):
        p=31;a=3;P=p**L
        u=(P,P,-(p+3)*a-2*P)
        rows=[]
        for use in (False,True):
            solver=Solver(p,use,max_states=300000)
            try:
                ans=solver.solve_core(u)
                assert ans is None
                rows.append({'filter':use,'distance':ans,'stats':dict(solver.stats)})
            except SearchLimit:
                rows.append({'filter':use,'resource_limit':True,'stats':dict(solver.stats)})
        print(json.dumps({'L':L,'height_bits':P.bit_length(),'runs':rows}),flush=True)
