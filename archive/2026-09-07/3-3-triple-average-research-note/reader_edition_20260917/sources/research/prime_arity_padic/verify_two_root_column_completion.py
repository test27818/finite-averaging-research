"""Two evaluated root directions + norm cycle; no shallow-group lift or orbit search."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from random import Random
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/"work"))
from check_large_symmetric_carrier_certificate import check_pair,check_row
from verify_upper_band_unrestricted_completion import zy
from verify_uniform_odd_middle_cores import mm,invq,residue,bezout
from verify_even_odd_half_core import mod_power
from verify_terminal_fan import terminal,primitive_preparation
from verify_square_zero_compiler import check_frozen_files,check_local_links
ID=(1,0,0,1)
E21=(0,0,1,0)
if not __debug__:raise RuntimeError("Assertions required")


def det(A):return A[0]*A[3]-A[1]*A[2]
def red(A,m):return tuple(residue(x,m) for x in A)
def act(A,w,m):
    a,b,c,d=red(A,m)
    return ((a*w[0]+b*w[1])%m,(c*w[0]+d*w[1])%m)
def scale(t,A):return tuple(t*x for x in A)
def powq(A,k):
    if k<0:return powq(invq(A),-k)
    out=ID
    while k:
        if k&1:out=mm(out,A)
        k//=2
        if k:A=mm(A,A)
    return out
def oddpart(n):
    while n%2==0:n//=2
    return n
def crt2(a,m,b,n):
    assert gcd(m,n)==1
    if n==1:return a%m
    return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)


def root_supply(p,s,pairs):
    n=3*p+s
    roots=[];delta=0
    for pair in pairs:
        alpha,H,f,g=check_pair(p,s,pair)
        delta=gcd(delta,H)
        J,_=check_row(p,s,pair[0])
        roots.append((alpha,scale(F(1,p*p),zy(J,p))))
    if (p,s)==(11,3):
        # This row is part of the retained auxiliary13 proof, not the direction field.
        row=(3,2,6,0,4,1,6)
        J,_=check_row(p,s,row)
        roots.append((1,scale(F(1,p*p),zy(J,p))))
        delta=2
    S=(1,0,n,-1)
    d=0;coeff=[]
    for alpha,J in roots:
        new,x,y=bezout(d,alpha)
        coeff=[x*c for c in coeff]+[y]
        d=new
    assert d==1
    V=ID
    for coefficient,(alpha,J) in zip(coeff,roots):
        V=mm(powq(mm(S,J),coefficient),V)
    assert red(V,n)==(1,residue(F(-1,p*p),n),0,1)
    return delta,V,coeff


def choose_direction(p,s,pairs,old_direction=None):
    delta,V,coeff=root_supply(p,s,pairs)
    if (3*p+s)%4!=2:
        if (3*p+s)%2==0:assert residue(V[0]+V[3],4)==2
        return delta,V,"root-derived",coeff
    # Conservative fallback: retain this finite trace condition in the 2 mod4 branch.
    assert old_direction is not None
    matrices=[scale(F(1,p*p),zy(check_row(p,s,row)[0],p)) for row in old_direction]
    V=mm(*matrices)
    assert residue(V[0]+V[3],4)==2
    return delta,V,"retained-direction",None


def compile_column(p,s,delta,V,z,y,eps):
    n=3*p+s;h=delta*n;Q=h*h;m=oddpart(n);two=h//m
    assert y%n==eps*p*p%n and z%n==eps%n
    assert gcd(eps,n)==1 and (delta==1 if n%2 else delta in (2,4))
    current=(z%Q,y%Q)
    D=det(V)
    B=None;entry_power=0
    if n%2==0:
        assert residue(V[0]+V[3],4)==2
        B=scale(pow(residue(D,Q),-n//2,Q),mod_power(V,n,Q))
        B=red(B,Q)
        assert red(B,2*n)==(1,n,0,1)
        for bit in range(delta.bit_length()-1):
            precision=n*(1<<bit)
            if ((current[0]-eps)//precision)%2:
                entry_power+=1<<bit
                current=act(mod_power(B,1<<bit,Q),current,Q)
            assert (current[0]-eps)%(2*precision)==0
    assert (current[0]-eps)%h==0
    j=((eps*p*p-current[1])//n)*pow(eps,-1,delta)%delta if delta>1 else 0
    goal=(eps,eps*(p*p-n*j))
    assert all((current[i]-goal[i])%h==0 for i in range(2))
    X=mm(mm(V,E21),invq(V))
    q=lcm(*(F(x).denominator for x in X))
    assert gcd(q,h)==1
    # Evaluate two roots at the target column: determinant = 2 eps^2/p^2 modulo odd m.
    vx=act(scale(q,X),goal,m) if m>1 else (0,0)
    a0=(0,residue(q*goal[0],m)) if m>1 else (0,0)
    determinant=(-vx[0]*a0[1])%m if m>1 else 0
    assert m==1 or gcd(determinant,m)==1
    rhs=((goal[0]-current[0])//h %m,(goal[1]-current[1])//h %m) if m>1 else (0,0)
    r1=rhs[0]*pow(vx[0],-1,m)%m if m>1 else 0
    r0=(rhs[1]-r1*vx[1])*pow(a0[1],-1,m)%m if m>1 else 0
    # Make both root corrections invisible modulo the complete binary square.
    r0=crt2(r0,m,0,two)
    r1=crt2(r1,m,0,two)
    for root,param in ((E21,r0),(X,r1)):
        T=tuple(ID[i]+h*q*param*root[i] for i in range(4))
        assert det(T)==1
        current=act(T,current,Q)
    assert all((current[i]-goal[i])%(m*m)==0 for i in range(2))
    dyadic_power=last=0
    if two>1:
        # C is identity mod m^2 and starts with h E12 in the binary component.
        C=mod_power(B,delta*m,Q)
        assert red(C,m*m)==red(ID,m*m)
        assert red(C,2*two)==(1,two,0,1)
        precision=two
        bit=0
        while precision<two*two:
            if ((current[0]-goal[0])//precision)%2:
                dyadic_power+=1<<bit
                current=act(mod_power(C,1<<bit,Q),current,Q)
            assert (current[0]-goal[0])%(2*precision)==0
            precision*=2;bit+=1
        assert current[0]==goal[0]%Q
        diff=((goal[1]-current[1])//h)%two
        last=crt2(diff*pow(residue(current[0],two),-1,two)%two,two,0,m)
        current=act((1,0,h*last,1),current,Q)
    assert current==tuple(x%Q for x in goal)
    return {"terminal_j":j,"entry_norm_power":entry_power,
            "odd_root_parameters":[h*q*r0,h*q*r1],
            "dyadic_norm_power":dyadic_power,"last_lower_parameter":h*last,
            "deep_level":Q}


def all_cases():
    cases=json.loads((ROOT/"work/large_symmetric_carrier_shallow_certificate.json").read_text())["cases"]
    rng=Random(3192026)
    types={};counts=atoms=0;examples=[]
    for case in cases:
        p,s=case["p"],case["s"];n=3*p+s
        fallback=case["direction"] if n%4==2 else None
        delta,V,kind,coeff=choose_direction(p,s,case["root_pairs"],fallback)
        assert delta in (1,2,4)
        types[kind]=types.get(kind,0)+1
        for j in range(delta):_,a=terminal(p,s,j);atoms+=a
        h=delta*n;Q=h*h
        safe=[i for i in range(1,p+1) if gcd(i,n)==1]
        for _ in range(12):
            eps=rng.choice(safe)
            z=eps+n*rng.randrange(-4*h,4*h)
            y=eps*p*p+n*rng.randrange(-4*h,4*h)
            result=compile_column(p,s,delta,V,z,y,eps);counts+=1
            if (p,s) in ((11,3),(13,3),(13,4)) and len(examples)<8:
                examples.append({"p":p,"s":s,"kind":kind,"bezout":coeff,**result})
    assert types=={"retained-direction":46,"root-derived":116}
    return types,counts,atoms,examples


def large_cases():
    from verify_carrier_interval_reduction import family
    rng=Random(8316);count=0;derived=0
    for p in (83,97,101,307,997):
        for s in range(1,10):
            a=s//3+1
            pairs=[family(p,s,alpha,p//(3*alpha)-j)[:2] for alpha in (a,a+1) for j in (1,0)]
            fallback=None
            if (3*p+s)%4==2:
                # The old trace selection remains only in this branch.
                first=pairs[0]
                second=pairs[2]
                for x in first:
                    for y in second:
                        A=scale(F(1,p*p),zy(check_row(p,s,x)[0],p))
                        B=scale(F(1,p*p),zy(check_row(p,s,y)[0],p))
                        if residue(sum((mm(A,B)[0],mm(A,B)[3])),4)==2:
                            fallback=(x,y);break
                    if fallback:break
                assert fallback
            delta,V,kind,coeff=choose_direction(p,s,pairs,fallback)
            derived+=kind=="root-derived"
            n=3*p+s;h=delta*n
            for _ in range(6):
                z=1+n*rng.randrange(h);y=p*p+n*rng.randrange(h)
                compile_column(p,s,delta,V,z,y,1);count+=1
    return count,derived


def general_algebra():
    count=0
    for m in (3,5,9,15,25,45):
        for a in (0,1,2):
            n=(2**a)*m
            for delta in ((1,) if a==0 else (2,4)):
                h=delta*n
                for tau in (0,1,3):
                    # Correct mod n upper unipotent; choose trace=2 exactly.
                    V=(1+n*tau,-F(1,49),0,1-n*tau)
                    if gcd(det(V).numerator,n)!=1:continue
                    if gcd(7,n)!=1:continue
                    compile_column(7,n-21,delta,V,1+3*n,49-2*n,1)
                    count+=1
    return count


def main():
    t=perf_counter()
    types,count,atoms,examples=all_cases()
    large,derived=large_cases()
    abstract=general_algebra()
    preps=sum(primitive_preparation(q,r,u) for q,r in ((8,3),(36,5),(42,13),(136,19)) for u in (-5,0,9))
    report={"status":"PASS","finite_cases":162,"direction_sources":types,
        "independent_direction_fields_not_used":116,
        "retained_direction_fields":46,"finite_transports":count,
        "large_formula_transports":large,"large_root_derived_cases":derived,
        "algebraic_parameter_checks":abstract,"terminal_atoms":atoms,
        "primitive_preparation_checks":preps,
        "shallow_congruence_lifting_used":False,"binary_unit_fields_used":False,
        "auxiliary13_retained":True,"special97_retained":False,
        "examples":examples,"unchanged_frozen_files":check_frozen_files(),
        "local_links_checked":check_local_links(),
        "seconds":round(perf_counter()-t,3),
        "scope":"Exact finite checks support the general written column-lifting theorem; old root supply and exact deep kernel remain assumptions. No search for averaging words or finite group orbits."}
    (HERE/"two_root_column_completion_verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="examples"},indent=2))


if __name__=="__main__":main()
