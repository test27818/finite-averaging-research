"""Exact finite audits; uniform p-adic and all-r statements are proved in the note."""
from fractions import Fraction as F
from itertools import combinations,product
from math import gcd
from pathlib import Path
from random import Random
import json
from verify_subcritical_complement_dynamics import core_distance,initial_distance,atom

def primitive(values):
    g=gcd(*values)
    return tuple(x//g for x in values) if g else tuple(values)

def gap(state):return gcd(*(x-state[0] for x in state))

def normdir(z,m,p):
    u,v=z
    if v%p:return (u*pow(v,-1,m)%m,1)
    assert u%p
    return (1,v*pow(u,-1,m)%m)

def branch(i,z,p):
    u,v=z
    return (-p*u,v-u) if i==0 else (u-v,-p*v)

def local_trees():
    rows=[];words=0
    for p in (3,5,7,11,13):
        layer=[(1,-1)]
        for length in range(8):
            seen=set()
            for z in layer:
                assert gcd(*z)==1 and sum(z)%(p+2)==0
                assert core_distance(p,*z)==length+1
                seen.add(z if z[0]>0 else tuple(-x for x in z))
            assert len(seen)==2**length
            words+=len(layer)
            layer=[branch(i,z,p) for z in layer for i in (0,1)]
        for m in range(1,6):
            mod=p**m;seed=normdir((1,-1),mod,p);seen={seed};queue=[seed]
            while queue:
                z=queue.pop()
                for i in (0,1):
                    y=normdir(branch(i,z,p),mod,p)
                    if y not in seen:seen.add(y);queue.append(y)
            assert len(seen)==2**(m+1)-1
            boundary={(0,1),(1,0)}
            for _ in range(m-1):boundary={normdir(branch(i,z,p),mod,p) for z in boundary for i in (0,1)}
            assert len(boundary)==2**m and boundary<=seen
            rows.append({'p':p,'precision':m,'marked_closure_classes':len(seen),
                         'boundary_classes':len(boundary),'full_projective_classes':(p+1)*p**(m-1)})
    return {'positive_words':words,'finite_precision_counts':rows}

def complement_g_and_moves():
    rng=Random(27172026);gc=mc=0
    for p in (3,5,7,11):
        for r in range(1,p+1):
            n=p+r
            for _ in range(14):
                u=primitive([rng.randrange(-20,21) for i in range(r)])
                if not any(u):continue
                s=sum(u);raw=(-s,)*p+tuple(n*x-s for x in u);state=primitive(raw)
                assert gap(state)==n//gcd(n,s)
                allowed=gap(state)
                while allowed%p==0:allowed//=p
                assert (allowed==1)==(s%n==0 if r<p else s%2==0)
                gc+=1
                # Compare subset formula to actual original-position rational averaging.
                a=-F(s,n);physical=(a,)*p+tuple(a+x for x in u)
                for _ in range(4):
                    subset=[i for i in range(r) if rng.randrange(2)]
                    inds=list(range(p-len(subset)))+[p+i for i in subset]
                    y=atom(physical,inds);anew=a+F(sum(u[i] for i in subset),p)
                    leftover=[i for i in range(n) if i not in inds]
                    predicted=[(0 if i in subset else u[i])-F(sum(u[j] for j in subset),p) for i in range(r)]
                    assert sorted(y[i]-anew for i in leftover)==sorted(predicted)
                    mc+=1
    return {'primitive_complement_G_checks':gc,'literal_subset_update_checks':mc}

def indistinguishable_families():
    total=types=0
    for p in (3,5,7,11,13):
        for r in range(2,p+1):
            n=p+r
            for M in (1,2,5,9,14,101):
                a=p*n*M
                good=(0,)*p+(1,)*(r-1)+(-(r-1),)
                bad=(a,)*p+(1,)*(r-1)+(-p*a-(r-1),)
                assert sum(good)==sum(bad)==0 and gcd(*bad)==gcd(*good)==1
                assert gap(good)==gap(bad)==1 and all((x-y)%M==0 for x,y in zip(good,bad))
                # Exhaust every value type of the first p-subset, not every labelled choice.
                moves=[]
                for ones in range(r):
                    for special in (0,1):
                        bg=p-ones-special
                        if bg<0:continue
                        sm=bg*a+ones+special*bad[-1]
                        if sm%p==0:moves.append((ones,special))
                assert set(moves)=={(0,0),(r-1,1)}
                after=(-r*a//p,)*p+(a,)*r
                assert gap(primitive(after))==(n if r<p else 2)
                selected=list(range(p,p+r))+list(range(p-r))
                assert not any(atom(good,selected))
                if r==2:assert initial_distance(p,bad) is None
                total+=1;types+=2*r
    return {'all_r_family_instances':total,'first_move_value_types_exhausted':types,
            'scope':'Nonexistence uses the existing no-new-denominator theorem plus the two written value-type cases.'}

def input_and_norm_formulas():
    rng=Random(723);inputs=norms=0
    for p in (3,5,7,11):
        n=p+2
        for _ in range(12):
            state=[F(rng.randrange(-9,10),rng.randrange(1,5)) for i in range(n)];S=sum(state)
            for i,j in combinations(range(n),2):
                a=(S-state[i]-state[j])/p
                U=(p+1)*state[i]+state[j]-S;V=state[i]+(p+1)*state[j]-S
                assert (U,V)==(p*(state[i]-a),p*(state[j]-a));inputs+=1
        def q(u,v):return u*u+(p*p-2)*u*v+v*v
        C=(F(1-p*p,p),F(-1,p),F(1,p),F(-1,p))
        for u,v in product(range(-5,6),repeat=2):
            x=C[0]*u+C[1]*v;y=C[2]*u+C[3]*v
            assert q(x,y)==q(u,v);norms+=1
    return {'arbitrary_rational_first_step_pairs':inputs,'inverse_quotient_norm_identities':norms}


def torus_four_punctures():
    """Exact identities in Q[s]/(s^2-(p^2-4)), without requiring squarefree delta.

    Does not test or prove the external ESS finiteness theorem.
    """
    states=branches=unit_equations=trace_conics=0
    rows=[]
    for p in (3,5,7,11,13,17,19):
        delta=p*p-4
        one=(F(1),F(0));minus_one=(F(-1),F(0))
        def add(x,y):return x[0]+y[0],x[1]+y[1]
        def neg(x):return -x[0],-x[1]
        def mul(x,y):return x[0]*y[0]+delta*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
        def norm(x):return x[0]*x[0]-delta*x[1]*x[1]
        def inv(x):
            n=norm(x);assert n
            return x[0]/n,-x[1]/n
        def divide(x,y):return mul(x,inv(y))
        def lift(u,v):
            ss=u+v;dd=u-v;den=delta*dd*dd-p*p*ss*ss
            assert den
            return F(delta*dd*dd+p*p*ss*ss,den),F(2*p*ss*dd,den)
        a=(F(p-1),F(0))
        def twist(x):return divide(neg(add(mul(a,x),one)),add(x,a))
        epsilon=(F(p,2),F(1,2))
        assert norm(epsilon)==1 and lift(1,-1)==one and lift(1,1)==minus_one
        assert twist((F(-1,p-1),F(0)))==(F(0),F(0))
        assert add((F(-(p-1)),F(0)),a)==(F(0),F(0))
        for u,v in product(range(-10,11),repeat=2):
            if gcd(u,v)!=1:continue
            alpha=lift(u,v)
            assert norm(alpha)==1 and twist(twist(alpha))==alpha
            assert twist(inv(alpha))==inv(twist(alpha))
            assert delta*(u-v)**2-p*p*(u+v)**2==-4*(u*u+(p*p-2)*u*v+v*v)
            states+=1
            X=2*alpha[0];Y=2*mul(inv(epsilon),alpha)[0]
            assert X*X+Y*Y-p*X*Y+delta==0
            assert (F(X,2),F(p*X-2*Y,2*delta))==alpha
            trace_conics+=1
            for sign,uv in ((1,(-p*u,v-u)),(-1,(u-v,-p*v))):
                gamma=mul(epsilon if sign==1 else inv(epsilon),alpha)
                assert lift(*uv)==twist(gamma)
                AA=add(mul(a,gamma),one);BB=add(gamma,a)
                assert add(mul(a,BB),neg(AA))==(F(p*(p-2)),F(0))
                assert add(AA,neg(mul(a,gamma)))==one
                assert norm(twist(gamma))==1
                # Original rational t chart and direct core formula.
                if u!=v and uv[0]!=uv[1]:
                    t=F(u+v,u-v)
                    predicted=(p*t+sign*(p+2))/(sign*p*t+p-2)
                    assert predicted==F(uv[0]+uv[1],uv[0]-uv[1])
                branches+=1;unit_equations+=1
        rows.append({'p':p,'positions':p+2,'delta':delta,
                     'extra_punctures':[str(F(-1,p-1)),str(-(p-1))],
                     'normalized_fourth_puncture':(p-1)**2})
    return {'rational_norm_one_states':states,'branch_conjugacies':branches,
            'trace_conics':trace_conics,'unit_equation_identities':unit_equations,
            'parameters':rows,
            'scope':'Exact finite identity checks; all-p conjugacy and fixed-S integrality '
                    'are proved in section 8. ESS only controls fixed-S adjacent endpoints, '
                    'not the entire positive semigroup orbit.'}

def p_plus_three_surface():
    replays=charts=kernels=0
    for p in (3,5,7,11,13):
        for u,v,w in product(range(-3,4),repeat=3):
            if not (u or v or w):continue
            center=-F(u+v+w,p+3)
            state=(center,)*p+(center+u,center+v,center+w)
            for count in (1,2,3):
                selected=list(range(p-count))+list(range(p,p+count))
                actual=atom(state,selected)
                chosen_sum=sum((u,v,w)[:count])
                new_center=center+F(chosen_sum,p)
                prediction=tuple((-F(chosen_sum,p) if i<count else
                                  F((u,v,w)[i])-F(chosen_sum,p)) for i in range(3))
                left=[i for i in range(p+3) if i not in selected]
                assert sorted(actual[i]-new_center for i in left)==sorted(prediction)
                assert all(actual[i]==new_center for i in selected)
                if count==1:
                    assert tuple(p*x for x in prediction)==(-u,p*v-u,p*w-u)
                elif count==2:
                    assert tuple(p*x for x in prediction)==(-u-v,-u-v,p*w-u-v)
                    assert (not any(prediction))==(u+v==0 and w==0)
                    kernels+=1
                else:
                    assert (not any(prediction))==(u+v+w==0)
                replays+=1
            if u*v*w*(p*v-u)*(p*w-u):
                s,t=F(p*v,u),F(p*w,u)
                assert s not in (0,1) and t not in (0,1)
                assert F(p*v-u,-u)==1-s and F(p*w-u,-u)==1-t
                assert (F(1),s/p,t/p)==(F(1),F(v,u),F(w,u))
                charts+=1
    return {'primes':[3,5,7,11,13],'literal_rank_3_2_1_replays':replays,
            'pair_projection_kernel_checks':kernels,'two_punctured_line_product_charts':charts,
            'scope':'Projective-plane and five-line-complement identities only. Fixed-S '
                    'finiteness follows from ESS; it is not full p+3 reachability.'}


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required')
    report={'p_plus_two_trees':local_trees(),'all_r_complement':complement_g_and_moves(),
            'fixed_congruence_obstruction':indistinguishable_families(),'input_and_arithmetic':input_and_norm_formulas(),
            'torus_four_punctures':torus_four_punctures(),
            'p_plus_three_surface':p_plus_three_surface(),
            'status':'Exact finite checks passed; general quantifiers are in the companion note.',
            'not_claimed':'No static gcd criterion for all p+2; no bit-polynomial algorithm for arbitrary p+r, r>=3.'}
    path=Path(__file__).with_name('subcritical_prime_uniform_structure_verification.json')
    path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,indent=2))
