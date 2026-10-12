"""Polynomial reduction of five-average/eight-position decision to clusters.

First reduce to two equal exception residues, then to two differences divisible
by 5 and one unit. decide_input remains an exact finite solver, not a P claim:
it delegates these cluster cores to the existing exhaustive, compressed solver.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd,lcm
from fixed_p_plus_three_solver import Solver,canonical
from verify_fixed_p_block_norm_descent import reduce_double_core


def energy_numerator(u):
    return 8*sum(v*v for v in u)-sum(u)**2


def sector(u):
    """Call on a nonzero primitive triple."""
    q=energy_numerator(u)%5
    if q==0:return 'equal'
    return 'distinct' if q in (1,4) else 'collision'


def image(u,mask):
    selected_sum=sum(u[i] for i in range(3) if mask>>i&1)
    if selected_sum%5:return None
    shift=selected_sum//5
    raw=tuple(-shift if mask>>i&1 else u[i]-shift for i in range(3))
    v=canonical(raw)
    if sum(v)%8 or v==u:return None
    return v


def reduce_core(values):
    """Return immediate yes/no, or an OR of collision-sector instances.

    None in the immediate field means that the target instances remain to be
    decided; it is neither a yes answer nor a negative certificate.
    """
    if len(values)!=3:raise ValueError('three integer differences required')
    u=canonical(tuple(values))
    targets=set();stats=Counter()
    while True:
        if sum(u)%8:return {'immediate':False,'targets':(),'stats':dict(stats)}
        if not sum(u):return {'immediate':True,'targets':(),'stats':dict(stats)}
        current=sector(u)
        stats[current+'_visits']+=1
        if current=='equal':
            break
        if current=='collision':
            targets.add(u)
            break
        zeros=[i for i in range(3) if u[i]%5==0]
        assert len(zeros)<=1
        for mask in (3,5,6):
            # With one zero and two opposite units, the pair can survive only
            # if its sum is divisible by 25; otherwise its image is an equal
            # residue trap. Keeping image() below also checks the G condition.
            if zeros and not (mask>>zeros[0]&1):
                if sum(u[i] for i in range(3) if mask>>i&1)%25:continue
            v=image(u,mask)
            if v is None:continue
            stats['pair_candidates']+=1
            if not sum(v):
                return {'immediate':True,'targets':(),'stats':dict(stats)}
            kind=sector(v)
            assert kind in ('collision','equal')
            if kind=='collision':targets.add(v)
        if not zeros:break
        i=zeros[0]
        if u[i]==0:break # the only singleton is an identity
        v=image(u,1<<i)
        assert v is not None and sector(v)=='distinct'
        assert energy_numerator(v)<energy_numerator(u)
        u=v;stats['singleton_steps']+=1
    return {'immediate':None if targets else False,
            'targets':tuple(sorted(targets)),'stats':dict(stats)}


def reduce_input(values):
    if len(values)!=8:raise ValueError('exactly eight rational numbers required')
    xs=[Fraction(x) for x in values]
    mean=sum(xs)/8
    centered=[x-mean for x in xs]
    den=lcm(*(x.denominator for x in centered))
    x=tuple(int(v*den) for v in centered)
    g=gcd(*x)
    if not g:return {'immediate':True,'targets':(),'stats':{}}
    x=tuple(sorted(v//g for v in x))
    if gcd(*(v-x[0] for v in x))!=1:
        return {'immediate':False,'targets':(),'stats':{'g_rejection':1}}
    targets=set();stats=Counter()
    counts=Counter(x)
    heavy=next((a for a,c in counts.items() if c>=5),None)
    cores=[]
    if heavy is not None:
        rest=list(x)
        for _ in range(5):rest.remove(heavy)
        cores.append(tuple(v-heavy for v in rest))
    else:
        for keep in combinations(range(8),3):
            total=sum(x[i] for i in keep)
            if total%5:continue
            avg=-total//5
            cores.append(tuple(x[i]-avg for i in keep))
    stats['first_step_cores']=len(cores)
    for u in cores:
        result=reduce_core(u);stats.update(result['stats'])
        if result['immediate'] is True:
            return {'immediate':True,'targets':(),'stats':dict(stats)}
        targets.update(result['targets'])
    return {'immediate':None if targets else False,
            'targets':tuple(sorted(targets)),'stats':dict(stats)}


def collision_to_cluster(values):
    """Reduce a collision core to at most two seven-position cluster cores."""
    u=canonical(tuple(values));stats=Counter()
    assert sum(u)%8==0 and sector(u)=='collision'
    while True:
        if not sum(u):return {'immediate':True,'targets':(),'stats':dict(stats)}
        zeros=[i for i in range(3) if u[i]%5==0]
        if len(zeros)==2:
            return {'immediate':None,'targets':(u,),'stats':dict(stats)}
        if len(set(u))==2:
            d=u[1] # in a sorted triple, the middle value is the repeated one
            v=next(x for x in u if x!=d)
            result=reduce_double_core(5,d,v)
            stats['duplicate_forced_steps']+=result.get('forced',result.get('distance',0))
            if result['status'] in ('yes','no'):
                return {'immediate':result['status']=='yes','targets':(),'stats':dict(stats)}
            d,v=result['pair'];target=canonical((d,d,v))
            assert sum(x%5==0 for x in target)==2
            return {'immediate':None,'targets':(target,),'stats':dict(stats)}
        if len(zeros)==1:
            i=zeros[0]
            if not u[i]:
                return {'immediate':False,'targets':(),'stats':dict(stats)}
            v=image(u,1<<i)
            assert v is not None and sector(v)=='collision'
            u=v;stats['collision_singleton_steps']+=1
            continue
        assert not zeros
        # No singleton is possible. At most two pair operations are legal;
        # each creates an actual duplicate, whose forced reduction is known.
        targets=set()
        for mask in (3,5,6):
            v=image(u,mask)
            if v is None or sector(v)=='equal':continue
            assert len(set(v))==2
            result=collision_to_cluster(v)
            stats.update(result['stats']);stats['collision_pair_exits']+=1
            if result['immediate'] is True:
                return {'immediate':True,'targets':(),'stats':dict(stats)}
            targets.update(result['targets'])
        assert len(targets)<=2
        return {'immediate':None if targets else False,
                'targets':tuple(sorted(targets)),'stats':dict(stats)}


def cluster_reduction(result):
    if result['immediate'] is not None:return result
    stats=Counter(result['stats']);targets=set()
    for u in result['targets']:
        narrowed=collision_to_cluster(u);stats.update(narrowed['stats'])
        if narrowed['immediate'] is True:
            return {'immediate':True,'targets':(),'stats':dict(stats)}
        targets.update(narrowed['targets'])
    return {'immediate':None if targets else False,
            'targets':tuple(sorted(targets)),'stats':dict(stats)}


def reduce_core_to_clusters(values):
    return cluster_reduction(reduce_core(values))


def reduce_input_to_clusters(values):
    return cluster_reduction(reduce_input(values))


def decide_input(values,max_states=None):
    """Complete decision via the unresolved-sector oracle, with honest limits."""
    reduced=reduce_input_to_clusters(values)
    if reduced['immediate'] is not None:return reduced['immediate'],reduced['stats']
    oracle=Solver(5,max_states=max_states)
    for u in reduced['targets']:
        assert sum(x%5==0 for x in u)==2
        if oracle.solve_core(u) is not None:
            return True,{'reduction':reduced['stats'],'oracle':dict(oracle.stats)}
    return False,{'reduction':reduced['stats'],'oracle':dict(oracle.stats)}
