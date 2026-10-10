"""Exact finite audit of unit exponent isometry and the written p-adic group proof."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from pathlib import Path
import json
from verify_five_torus_twist import EPS, ONE, lift, mul, inv, valuation
from verify_five_torus_denominators import power, from_alpha, q5
from verify_five_padic_fractal import A, B, I, mul as matmul
from verify_subcritical_complement_dynamics import core_distance


def matinv(M):
    d=M[0]*M[3]-M[1]*M[2]
    return tuple(Q(x,d) for x in (M[3],-M[1],-M[2],M[0]))


def signed_power(k):
    return power(EPS,k) if k>=0 else power(inv(EPS),-k)


def local_allowed(m):
    modulus=3**m
    seen={0};todo=[0]
    while todo:
        h=todo.pop()
        for sign in (1,-1):
            y=(3*h+sign)*pow(1+15*sign*h,-1,modulus)%modulus
            if y not in seen:seen.add(y);todo.append(y)
    return seen


def units():
    permutations=[];isometries=0
    for seed in (Q(0),Q(1),Q(1,4),Q(-5,23)):
        alpha0=lift(seed)
        for m in range(1,6):
            modulus=3**m;allowed=local_allowed(m);image=set();count=0
            for k in range(modulus):
                h,_=from_alpha(mul(alpha0,power(EPS,4*k)))
                assert h.denominator%3
                residue=h.numerator*pow(h.denominator,-1,modulus)%modulus
                image.add(residue);count+=residue in allowed
            assert len(image)==modulus and count==2**(m+1)-1
            permutations.append({'seed':str(seed),'m':m,'bijection_size':len(image),'allowed_classes':count})
        for k in range(-20,21):
            for l in range(k+1,21):
                h1,_=from_alpha(mul(alpha0,signed_power(4*k)))
                h2,_=from_alpha(mul(alpha0,signed_power(4*l)))
                assert valuation(h1-h2,3)==valuation(k-l,3)
                isometries+=1
    return {'exact_isometry_pairs':isometries,'finite_exponent_bijections':permutations}


def group():
    C=matmul(A,matinv(B));D=matmul(matmul(C,C),matmul(C,C))
    E=matmul(matmul(A,D),matinv(A));F=matmul(matmul(B,D),matinv(B));EF=matmul(E,F)
    assert C==(-3,1,-1,0) and D==(55,-21,21,-8)
    assert E==(34,63,7,13) and F==(34,-7,-63,13)
    conjugates=(D,matmul(matmul(E,D),matinv(E)),matmul(matmul(EF,D),matinv(EF)))
    rows=[]
    for M in conjugates:
        assert M[0]*M[3]-M[1]*M[2]==1
        v=tuple(int((x-y)/3)%3 for x,y in zip(M,I))
        assert (v[0]+v[3])%3==0
        rows.append((v[0],v[1],v[2]))
    assert rows==[(0,2,1),(1,2,2),(1,1,1)]
    a,b,c=rows
    det=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    assert det%3==1
    layer_checks=0
    for M in conjugates:
        K=M
        for depth in range(1,8):
            modulus=3**(depth+1)
            v=tuple(int((x-y)/(3**depth))%3 for x,y in zip(K,I))
            target=tuple(int((x-y)/3)%3 for x,y in zip(M,I))
            assert v==target
            K=matmul(matmul(K,K),K)
            layer_checks+=1
    finite=[]
    for k in range(1,4):
        modulus=3**k;seen={I};todo=[I]
        while todo:
            M=todo.pop()
            for N in (D,E,F):
                result=tuple(int(x)%modulus for x in matmul(M,N))
                if result not in seen:seen.add(result);todo.append(result)
        assert len(seen)==24*3**(3*(k-1))
        finite.append({'k':k,'generated_SL2_size':len(seen)})
    P=(Q(2),Q(0),Q(1,2),Q(1,2))
    assert P[0]*P[3]-P[1]*P[2]==1
    assert matmul(matmul(matinv(P),A),P)==(-3,0,0,1)
    return {'kernel_basis_determinant_mod3':det%3,'kernel_power_layer_checks':layer_checks,'finite_SL2_images':finite}


def bounded_denominator_diagnostic():
    layer={(1,-1)};counts={}
    for depth in range(19):
        for u,v in layer:
            D=abs(q5(u,v))//5
            if D<=100:counts[D]=counts.get(D,0)+1
        if depth<18:
            layer={z for u,v in layer for z in ((-3*u,v-u),(u-v,-3*v))}
    return {'max_reverse_word_depth':18,'counts_D_at_most_100':dict(sorted(counts.items())),
            'scope':'Finite depth only; absence is not an impossibility certificate.'}


def unit_denominator_one_diagnostic():
    u,v=1,-1
    hits=[]
    for k in range(10001):
        if k:
            u,v=-7*u-v,u
        assert u*u+7*u*v+v*v==-5
        distance=core_distance(3,u,v)
        if distance is not None:
            hits.append({'k':k,'minimal_steps':distance})
    assert hits==[{'k':0,'minimal_steps':1},{'k':1,'minimal_steps':3}]
    return {'positive_exponent_limit':10000,'hits':hits,
            'largest_height_bits':max(abs(u),abs(v)).bit_length(),
            'scope':'Conjecture diagnostic only; no exclusion beyond this exponent bound.'}


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required.')
    result={'unit_exponents':units(),'group_closure_formulas':group(),
            'fixed_denominator_diagnostic':bounded_denominator_diagnostic(),
            'D1_unit_exponent_diagnostic':unit_denominator_one_diagnostic(),
            'scope':'All-depth group closure and density proved in prose; fixed-D finiteness remains open.'}
    Path(__file__).with_name('five_unit_exponents_and_group_verification.json').write_text(
        json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
