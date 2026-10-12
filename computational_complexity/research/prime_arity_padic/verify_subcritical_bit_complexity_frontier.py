"""Exact checks for the written proofs, not a proof by bounded experimentation.

The counterexample oracle uses the full raw INTEGER DAG, with no depth cutoff,
no intermediate normalization, and no G pruning. Its completeness depends on
the previously proved subcritical integrality theorem.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd
from pathlib import Path
from random import Random
import json


def primitive_G(x):
    d = gcd(*x)
    if not d:
        return 0
    return gcd(*(v-x[0] for v in x))//d


def atom(x, selected):
    s = sum(x[i] for i in selected)
    p = len(selected)
    assert s % p == 0
    y = list(x)
    for i in selected:
        y[i] = s//p
    return tuple(y)


def singleton(p, a, u, v, c, which):
    x = (a,)*p+(a+u, a+v, c)
    delta = (u, v)[which]
    assert delta and delta % p == 0
    m = a+delta//p
    uu, vv = u-delta//p, v-delta//p
    if which == 0:
        uu = -delta//p
    else:
        vv = -delta//p
    y = atom(x, tuple(range(p-1))+(p+which,))
    expected = (m,)*p+(m+uu, m+vv, c)
    assert sorted(y) == sorted(expected)
    assert sum(y) == 0 and gcd(*y) == 1 and primitive_G(y) == 1
    assert sum(t*t for t in y) < sum(t*t for t in x)
    return m, uu, vv


def frontier(p, k):
    N = p**(2*k)
    x0 = (1,)*p+(1+N, 1-N, -p-2)
    assert sum(x0) == 0 and gcd(*x0) == 1 and primitive_G(x0) == 1
    states = {(1, N, -N)}
    atoms = 0
    for depth in range(k):
        nxt = set()
        for a, u, v in states:
            assert u > 0 > v and u % (p*p) == v % (p*p) == 0
            for which in (0, 1):
                m, uu, vv = singleton(p, a, u, v, -p-2, which)
                m, uu, vv = singleton(p, m, uu, vv, -p-2, which)
                atoms += 2
                if which == 0:
                    assert (uu, vv) == (u//(p*p), v-(p-1)*u//(p*p))
                    assert Fraction(-vv, uu) > p-1
                else:
                    assert (uu, vv) == (u-(p-1)*v//(p*p), v//(p*p))
                    assert Fraction(-vv, uu) < Fraction(1, p-1)
                assert uu > 0 > vv
                nxt.add((m, uu, vv))
        states = nxt
        assert len(states) == 2**(depth+1)
    physical = {tuple(sorted((a,)*p+(a+u, a+v, -p-2))) for a,u,v in states}
    assert len(physical) == 2**k
    for a,u,v in states:
        assert u % p and v % p
    return {'p':p, 'k':k, 'states_at_depth_2k':len(physical),
            'literal_atom_checks':atoms, 'N_bits':N.bit_length()}


def raw_oracle(p, n):
    choices = tuple(combinations(range(n), p))

    @lru_cache(None)
    def successors(x):
        out = set()
        for inds in choices:
            vals = [x[i] for i in inds]
            if min(vals) == max(vals) or sum(vals) % p:
                continue
            y = tuple(sorted(atom(x, inds)))
            assert sum(t*t for t in y) < sum(t*t for t in x)
            out.add(y)
        return tuple(sorted(out))

    @lru_cache(None)
    def distance(x):
        if not any(x):
            return 0
        ds = [distance(y) for y in successors(x)]
        ds = [d for d in ds if d is not None]
        return 1+min(ds) if ds else None

    return successors, distance


def counterexamples():
    succ, dist = raw_oracle(5, 8)
    reports = []
    for a,b,c,success_type in [(-4,21,-22,1),(4,-11,2,2)]:
        x = tuple(sorted((a,)*5+(b,b,c)))
        assert sum(x) == 0 and primitive_G(x) == 1
        es = []
        for count in (1,2):
            m = ((5-count)*a+count*b)//5
            y = tuple(sorted((m,)*5+(a,)*count+(b,)*(2-count)+(c,)))
            d = dist(y)
            assert (d is not None) == (count == success_type)
            assert primitive_G(y) == 1
            es.append({'selected_exceptions':count, 'raw_successor':y,
                       'distance':d,'energy_drop':sum(t*t for t in x)-sum(t*t for t in y)})
        assert set(succ(x)) == {tuple(e['raw_successor']) for e in es}
        assert dist(x) == 3
        if a == -4:
            assert [e['energy_drop'] for e in es] == [500,750]
        reports.append({'input':x,'distance':dist(x),'branches':es})
    z1 = tuple(sorted((2,)*5+(3,-2,-11)))
    z2 = tuple(sorted((1,)*5+(4,-11,2)))
    assert not succ(z1) and not succ(z2)
    return {'cases':reports,'raw_integer_oracle_states':dist.cache_info().currsize}


def gap_inequality():
    rng = Random(20261011)
    count = 0
    for p in (3,5,7,11):
        for r in range(p):
            n=p+r
            for _ in range(60):
                x=sorted(rng.randrange(-40,41) for _ in range(n))
                cut=max(range(n-1),key=lambda i:x[i+1]-x[i])
                gap=x[cut+1]-x[cut]
                if not gap:continue
                inds=tuple(sorted(rng.sample(range(n),p)))
                if not (inds[0]<=cut<inds[-1]):continue
                vals=[x[i] for i in inds]
                loss=sum(v*v for v in vals)-Fraction(sum(vals)**2,p)
                variance=sum(v*v for v in x)-Fraction(sum(x)**2,n)
                assert loss >= Fraction(gap*gap,2)
                assert loss >= variance/Fraction(2*n**3)
                assert min(cut+1,n-cut-1)<p
                count+=1
    return count


def main():
    result = {
        'scope':'Finite exact checks supplement the all-parameter written proofs; no P algorithm for general p+r is claimed.',
        'frontiers':[frontier(p,k) for p in (5,7,11,13) for k in range(1,13)],
        'counterexamples':counterexamples(),
        'gap_inequality_checks':gap_inequality(),
    }
    path=Path(__file__).with_name('subcritical_bit_complexity_frontier_verification.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'frontier_cases':len(result['frontiers']),
                      'literal_atom_checks':sum(z['literal_atom_checks'] for z in result['frontiers']),
                      'largest_frontier':max(z['states_at_depth_2k'] for z in result['frontiers']),
                      'raw_oracle_states':result['counterexamples']['raw_integer_oracle_states'],
                      'gap_checks':result['gap_inequality_checks'],
                      'record':str(path)},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
