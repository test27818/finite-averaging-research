"""Independent finite checks of the cluster escape lemma and exact solver.

The exponential lower bound and the no-instance family are proved in the note.
Numerical state counts below are only implementation/instance checks.
"""
from collections import Counter
from fractions import Fraction
from math import gcd
from random import Random
from pathlib import Path
import json
from fixed_p_plus_three_solver import Solver,SearchLimit,canonical,escape_filter
from verify_subcritical_uniform_np_hard import integer_oracle,primitive


def group_checks():
    rows=[]
    for p in (5,7,23,31):
        H=set();x=1
        while x not in H:H.add(x);x=2*x%p
        union=H|{3*x%p for x in H}
        rows.append({'p':p,'H':sorted(H),'H_union_3H':sorted(union)})
    H=set(rows[-1]['H_union_3H'])
    assert 22 not in H and 22 not in {(-x)%31 for x in H}
    return rows


def local_leading_checks():
    rng=Random(102111);atoms=0;rejects=0
    for p in (5,7,11,23,31):
        for _ in range(140):
            a=rng.choice([x for x in range(-8,9) if x and x%p])
            q=rng.choice([x for x in range(-8,9) if x and x%p])
            L=rng.randrange(1,10);P=p**L
            current=a;pair=[P*q,P*q]
            c=-(p+2)*a-2*P*q
            doubles=0
            for t in range(1,L+1):
                assert all((v-a)%p==0 for v in [current,current+pair[0],current+pair[1]])
                assert ((p-1)*a+c)%p==(-3*a)%p!=0
                mask=rng.randrange(1,4)
                chosen=[j for j in range(2) if mask>>j&1]
                s=sum(pair[j] for j in chosen)
                assert s%p==0
                shift=s//p
                pair=[-shift if j in chosen else pair[j]-shift for j in range(2)]
                current+=shift
                assert current!=a or t<L # final leading coefficient must be nonzero
                doubles+=len(chosen)==2
                numerator=(current-a)//q
                assert (current-a)%q==0
                if t==1:
                    assert numerator//p**(L-1) in (1,2)
                else:
                    assert (p-1)*p**(L-2)<=numerator<=2*p**(L-1)
                atoms+=1
            lead=(current-a)*pow(q,-1,p)%p
            assert lead==((-1)**(L-1)*pow(2,doubles,p))%p
            assert all((current+v-a)%p==0 for v in pair)
            if escape_filter(p,a,P*q):
                assert all((c-a-(j+1)*(current-a))%p for j in range(2))
                if (c-a-3*(current-a))%p==0:
                    assert current!=0
                rejects+=1
    return {'literal_local_atoms':atoms,'filtered_random_paths':rejects}


def independent_comparison():
    rng=Random(101124);stats=Counter()
    for p in (5,7,11,23,31):
        n=p+3;edges,oracle=integer_oracle(p,n)
        solvers=[Solver(p,False),Solver(p,True)]
        for _ in range(350):
            a=rng.randrange(-8,9)
            u=[rng.randrange(-35,36) for _ in range(2)]
            u.append(-n*a-sum(u))
            expected=oracle(primitive((a,)*p+tuple(a+v for v in u)))
            for solver in solvers:assert solver.solve_core(tuple(u))==expected
            stats['cores']+=1
        for L in (1,2,3):
            for a in range(-4,5):
                if not a or a%p==0:continue
                for q in (-3,-1,1,3):
                    u=p**L*q;v=-n*a-2*u
                    if gcd(u,v)!=1:continue
                    expected=oracle(primitive((a,)*p+(a+u,a+u,a+v)))
                    for solver in solvers:assert solver.solve_core((u,u,v))==expected
                    if escape_filter(p,a,u):
                        assert expected is None
                        stats['verified_filter_rejections']+=1
                    stats['cluster_cases']+=1
        if p<=11:
            for _ in range(80):
                x=[rng.randrange(-3,4) for _ in range(n-1)];x.append(-sum(x))
                expected=oracle(primitive(tuple(x)))
                assert solvers[1].solve_input(x)==expected
                transformed=[Fraction(-7,13)*v+Fraction(4,17) for v in x]
                assert solvers[1].solve_input(transformed)==expected
                stats['full_inputs']+=1;stats['affine_rational_checks']+=1
        stats['oracle_states']+=oracle.cache_info().currsize
    # An explicit instance passing the necessary escape test but still no.
    assert not escape_filter(5,3,-5)
    assert Solver(5).solve_core((-5,-5,-14)) is None
    return dict(stats)


def prefix_frontier(k):
    p=31;n=34;a0=3;L=2*k+2;P=p**L;c=-99-2*P
    total=(p+2)*a0+2*P
    # First legal singleton splits the two equal exceptional values.
    pairs={((p-1)*(P//p),-P//p)}
    atoms=1
    checker=Solver(p,False)
    for level in range(k):
        nxt=set()
        for u,v in pairs:
            for which in (0,1):
                w=[u,v]
                for _ in range(2):
                    base=(total-sum(w))//(p+2)
                    assert (total-sum(w))%(p+2)==0
                    assert w[which]%p==0 and w[which]
                    q=w[which]//p
                    w=[-q if j==which else w[j]-q for j in range(2)]
                    base+=q
                    full=(base,)*p+(base+w[0],base+w[1],c)
                    assert sum(full)==0 and gcd(*full)==1
                    assert gcd(*(x-full[0] for x in full))==1
                    core=canonical((w[0],w[1],c-base))
                    assert len(set(core))==3
                    tag,offset,returned=checker.contract(core)
                    assert tag=='branch' and offset==0 and returned==core
                    assert len(checker.children(core))>=2
                    atoms+=1
                assert w[0]>0>w[1]
                nxt.add(tuple(w))
        pairs=nxt
        assert len(pairs)==2**(level+1)
    cores=set()
    for u,v in pairs:
        base=(total-u-v)//(p+2)
        cores.add(canonical((u,v,c-base)))
    assert len(cores)==2**k
    return {'L':L,'k':k,'boundary_nodes':len(cores),'checked_prefix_atoms':atoms,
            'source_height_bits':(99+2*P).bit_length()}


def no_family_counts():
    rows=[]
    for L in range(1,10):
        p=31;P=p**L;u=(P,P,-102-2*P)
        row={'L':L,'height_bits':(99+2*P).bit_length(),'without_escape':None,'with_escape':None}
        for enabled,key in ((False,'without_escape'),(True,'with_escape')):
            solver=Solver(p,enabled,max_states=100000)
            assert solver.solve_core(u) is None
            row[key]=dict(solver.stats)
        assert row['with_escape']['queries']==1
        rows.append(row)
    # Large height: test the symbolic filter, not an exponential graph search.
    for L in (100,1000,10000):
        assert escape_filter(31,3,31**L)
    return rows


def resource_semantics():
    try:
        Solver(31,False,max_states=0).solve_core((31,31,-164))
    except SearchLimit:
        return 'resource limit raises SearchLimit; no false negative returned'
    raise AssertionError('expected explicit resource exception')


def main():
    result={'scope':'Exact finite checks. The multiplicative-coset escape obstruction and exponential lower bound for the previous compression are proved in the note. The solver still has no polynomial worst-case bound.',
            'groups':group_checks(),'leading_coefficients':local_leading_checks(),
            'oracle_comparison':independent_comparison(),
            'exponential_prefixes':[prefix_frontier(k) for k in range(1,10)],
            'no_family_counts':no_family_counts(),'resource_semantics':resource_semantics()}
    path=Path(__file__).with_name('fixed_p_cluster_escape_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'leading_coefficients':result['leading_coefficients'],
                      'oracle_comparison':result['oracle_comparison'],
                      'largest_prefix':result['exponential_prefixes'][-1],
                      'largest_benchmark':result['no_family_counts'][-1],
                      'resource_semantics':result['resource_semantics'],'record':str(path)},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
