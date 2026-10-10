"""Exact certificates for bounded-run norm separation; no unbounded search."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def q5(z):
    u,v=z
    return u*u+7*u*v+v*v


def normalized(kind,t,z):
    u,v=z
    return (u,(1-t)*u/4+t*v) if kind==0 else (t*u+(1-t)*v/4,v)


def block(kind,a,z):
    u,v=z
    x=(-3)**a
    b=(x-1)//4
    return (x*u,b*u+v) if kind==0 else (u+b*v,x*v)


def evaluate(parameters):
    z=(F(1),F(-1))
    for j,t in reversed(list(enumerate(parameters))):
        z=normalized(j%2,t,z)
    return z


def grid_certificate(r,m):
    grid=[F(0)]+[F(1,(-3)**a) for a in range(1,m+1)]
    minimum=None
    checked=0
    for pars in product(grid,repeat=r):
        value=abs(q5(evaluate(pars)))
        assert value>0
        if minimum is None or value<minimum:minimum=value
        checked+=1
    error=F(23*r,3**(m+1))
    delta=minimum-error
    assert delta>0
    # Exact all-length cutoff for D=1, since delta*9**L <=5 is necessary.
    length_bound=-1
    while delta*9**(length_bound+1)<=5:length_bound+=1
    hits=[];words=0
    for exponents in product(range(1,length_bound+1),repeat=r):
        if sum(exponents)>length_bound:continue
        z=(1,-1)
        for j,a in reversed(list(enumerate(exponents))):
            z=block(j%2,a,z)
        pars=[F(1,(-3)**a) for a in exponents]
        scale=(-3)**sum(exponents)
        assert evaluate(pars)==tuple(F(x,scale) for x in z)
        assert abs(q5(z))>=delta*9**sum(exponents)
        if abs(q5(z))==5:hits.append({'exponents':exponents,'pair':z})
        words+=1
    return {'runs':r,'grid_cutoff':m,'grid_points':checked,
            'grid_minimum':str(minimum),'tail_error':str(error),
            'positive_lower_bound':str(delta),'D1_maximum_word_length':length_bound,
            'all_words_through_proved_bound_one_orientation':words,
            'D1_hits_one_orientation':hits}


def fixed_network_check():
    # Independent exact check of the literature counterexample, all 9 columns.
    rows=[[F(i==j) for j in range(9)] for i in range(9)]
    selections=((1,2,3,4,5,6),(1,2,3,7,8,9),
                (1,2,3,7,4,5),(1,2,3,6,8,9))
    for chosen in selections:
        indices=[i-1 for i in chosen]
        mean=[sum(rows[i][j] for i in indices)/6 for j in range(9)]
        for i in indices:rows[i]=mean[:]
    assert all(x==F(1,9) for row in rows for x in row)
    return {'steps':4,'entries_checked':81,'result':'J9/9',
            'scope':'Contradicts the m|n necessity in arXiv:1706.02540v1; final journal version not audited.'}


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    result={'bounded_run_certificates':[grid_certificate(r,m) for r,m in ((1,1),(2,8),(3,13))],
            'clique_paper_crosscheck':fixed_network_check(),
            'scope':'All word lengths covered for at most 3 runs; arbitrary run count and full D1 classification remain open.'}
    path=Path(__file__).with_name('five_bounded_runs_verification.json')
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
