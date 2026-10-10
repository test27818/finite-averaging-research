"""Finite exact checks for fixed-D counting and periodic return statements."""
from fractions import Fraction as Q
from itertools import product
from math import gcd,isqrt
from pathlib import Path
import json
from verify_five_padic_fractal import A,B,I,mul
from verify_five_torus_denominators import q5
from verify_subcritical_complement_dynamics import core_distance


def mv(M,z):return (M[0]*z[0]+M[1]*z[1],M[2]*z[0]+M[3]*z[1])


def spectral_checks():
    mixed=0;recurrences=0;pure=0
    # Characteristic polynomial of Sym²(M): x³-(tr²-det)x²+det(tr²-det)x-det³.
    for length in range(1,9):
        for word in product((0,1),repeat=length):
            M=I
            for i in word:M=mul(M,(A,B)[i])
            tr=M[0]+M[3];d=M[0]*M[3]-M[1]*M[2]
            assert tr%3==1 and d==(-3)**length
            if len(set(word))==2:
                disc=tr*tr-4*d
                assert disc<0 or isqrt(disc)**2!=disc
                assert 1-tr+d and 1+tr+d
                mixed+=1
            else:pure+=1
            for seed in ((1,-1),(9,1),(11,24)):
                seq=[];z=seed
                for n in range(9):
                    seq.append(q5(*z));z=mv(M,z)
                r=tr*tr-d
                for n in range(3,len(seq)):
                    assert seq[n]==r*seq[n-1]-d*r*seq[n-2]+d**3*seq[n-3]
                    recurrences+=1
    return {'mixed_words':mixed,'pure_words':pure,'symmetric_square_recurrence_checks':recurrences}


def pell_fibonacci():
    fib=[0,1]
    for _ in range(4*300+2):fib.append(fib[-1]+fib[-2])
    u,v=1,-1;checked=excluded=0
    for k in range(1,301):
        u,v=-7*u-v,u
        assert q5(u,v)==-5
        a=(-1)**(k+1)*fib[4*k]//3
        b=(-1)**k*fib[4*k+1]
        c=(-1)**(k+1)*fib[4*k-1]
        assert 3*a+b+c==0 and (b-a,c-a)==(u,v)
        assert (b-c)**2-45*a*a==4
        checked+=1
        if k%3==0 or (k!=1 and k%27==1) or k%27==26:
            assert core_distance(3,u,v) is None
            excluded+=1
    return {'fibonacci_pell_instances':checked,'proved_residue_family_checks':excluded}


def pure_branch_formula():
    checks=0
    for u,v in ((1,-1),(9,1),(11,24),(139,261)):
        for n in range(25):
            r=(-3)**n;t=Q(4*v-u,4)
            x=r*u;y=v+Q(r-1,4)*u
            assert q5(x,y)==Q(45,16)*r*r*u*u+Q(15,2)*r*u*t+t*t
            checks+=1
    return checks


def residue_bound():
    count=0
    for L in range(1,10001):
        modulus=1;m=0
        while modulus<L:modulus*=3;m+=1
        allowed=2**(m+1)-1
        # Exact premises of allowed < 4 L**log_3(2), without floating logs.
        assert L<=modulus and allowed<2**(m+1)
        assert (m==0 and L==1) or (m>=1 and 3**(m-1)<L)
        count+=1
    return count


if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions required.')
    result={'positive_word_spectral_checks':spectral_checks(),'D1_pell_family':pell_fibonacci(),
            'pure_branch_identity_checks':pure_branch_formula(),'interval_bound_checks':residue_bound(),
            'scope':'Periodic-return finiteness and effective sparsity proved generally; D1 full classification remains open.'}
    Path(__file__).with_name('five_fixed_D_returns_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
