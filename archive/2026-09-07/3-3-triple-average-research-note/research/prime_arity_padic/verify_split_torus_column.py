"""Finish all nine offsets using root-derived translations and the existing split torus."""
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
from verify_carrier_interval_reduction import family
from verify_uniform_odd_middle_cores import mm,invq,residue,bezout
from verify_even_odd_half_core import mod_power
from verify_four_prime_entry_and_band import Ledger
from verify_two_root_column_completion import root_supply as old_supply,red,act,scale,det,oddpart,crt2,powq
from verify_upper_band_unrestricted_completion import zy
from verify_terminal_fan import terminal
from verify_square_zero_compiler import check_frozen_files,check_local_links
ID=(1,0,0,1)
E=(0,0,1,0)
if not __debug__:raise RuntimeError("Assertions required")


def root_supply(p,s,pairs):
    if (p,s)!=(11,3):return old_supply(p,s,pairs)
    # Use the alpha=3 reflection already needed for the retained auxiliary13 repair.
    # Its scalar is -11, a base-ring unit; the alternative alpha=1 row adds107.
    rows=[pairs[0][0],(4,1,6,2,7,1,1)]
    alphas=[row[0]-row[1] for row in rows]
    d,x,y=bezout(*alphas);assert d==1
    S=(1,0,36,-1);V=ID
    for coefficient,row in zip((x,y),rows):
        J,_=check_row(p,s,row)
        T=mm(S,scale(F(1,p*p),zy(J,p)))
        V=mm(powq(T,coefficient),V)
    return 2,V,[x,y]


def digit(p,n):
    for q in (3,5,11,13):
        if q<=p and gcd(q,n)==1:return q
    # One progression suffices by the written inclusion-exclusion bound.
    for q in range(3,p+1,8):
        if gcd(q,n)==1:return q
    raise AssertionError(("small dyadic digit missing",p,n))


def dyadic_unit_word(q,target,M):
    """Represent target mod 2^L as sign*q^e by deterministic bit lifting."""
    assert M>=8 and M&(M-1)==0 and q%8 in (3,5) and target%2
    selected=None
    for sign in (1,-1):
        for parity in (0,1):
            if sign*pow(q,parity,8)%8==target%8:selected=(sign,parity)
    assert selected is not None
    sign,e=selected
    current=sign*pow(q,e,M)%M
    generator=pow(q,2,M)
    precision=8;step=2
    while precision<M:
        assert (current-target)%precision==0
        if ((target-current)//precision)%2:
            current=current*generator%M;e+=step
        assert (current-target)%(2*precision)==0
        generator=generator*generator%M
        precision*=2;step*=2
    assert current==target%M
    return sign,e


def column(p,s,delta,V,z,y,eps):
    n=3*p+s;h=delta*n;Q=h*h;m=oddpart(n);two=h//m;M=two*two
    # Work with residues of R-elements, including nonintegral primitive representatives.
    z,y,eps=(residue(x,Q) for x in (z,y,eps))
    assert z%n==eps%n and y%n==eps*p*p%n and gcd(eps,n)==1
    assert red(V,n)==(1,residue(F(-1,p*p),n),0,1)
    w=(z%Q,y%Q)
    qdigit=None;sign=1;exponent=0;k=0
    if n%2==0:
        assert delta in (2,4) and two>=4
        qdigit=digit(p,n)
        target=w[0]*pow(eps,-1,M)%M
        sign,exponent=dyadic_unit_word(qdigit,target,M)
        half=n//2
        D=(F(1,qdigit),0,half*(F(1,qdigit)-1),1)
        minus=(-1,0,-n,1)
        T=mod_power(red(D,Q),exponent,Q)
        if sign==-1:T=mm(red(minus,Q),T)
        w=act(T,w,Q)
        assert w[0]%M==eps%M
        assert w[1]%n==eps*p*p%n
        # An explicit power-of-two exponent makes V the identity in the binary quotient.
        order=M
        assert red(mod_power(V,order,M),M)==ID
        if m>1:
            k=order*(p*p*(w[0]-eps)*pow(w[1],-1,m)*pow(order,-1,m)%m)
            w=act(mod_power(V,k,Q),w,Q)
        assert w[0]%M==eps%M and (w[0]-eps)%m==0
    else:assert delta==1
    j=((eps*p*p-w[1])//n)*pow(eps,-1,delta)%delta if delta>1 else 0
    goal=(eps,eps*(p*p-n*j))
    assert all((w[i]-goal[i])%h==0 for i in range(2))
    X=mm(mm(V,E),invq(V))
    denominator=lcm(*(F(a).denominator for a in X))
    assert gcd(denominator,h)==1
    if m>1:
        right=((goal[0]-w[0])//h%m,(goal[1]-w[1])//h%m)
        c0=act(scale(denominator,E),goal,m)
        c1=act(scale(denominator,X),goal,m)
        assert gcd(c0[1]*c1[0],m)==1
        u1=right[0]*pow(c1[0],-1,m)%m
        u0=(right[1]-u1*c1[1])*pow(c0[1],-1,m)%m
        u0=crt2(u0,m,0,two);u1=crt2(u1,m,0,two)
        for root,u in ((E,u0),(X,u1)):
            A=tuple(ID[i]+h*denominator*u*root[i] for i in range(4))
            assert det(A)==1
            w=act(A,w,Q)
    else:u0=u1=0
    assert all((w[i]-goal[i])%(m*m)==0 for i in range(2))
    last=0
    if two>1:
        assert w[0]%M==eps%M
        last=crt2(((goal[1]-w[1])//h)*pow(w[0],-1,two)%two,two,0,m)
        w=act((1,0,h*last,1),w,Q)
    assert w==tuple(x%Q for x in goal)
    return {"terminal_j":j,"small_digit":qdigit,"digit_sign":sign,
            "digit_exponent":exponent,"odd_translation_exponent":k,
            "odd_root_parameters":[h*denominator*u0,h*denominator*u1],
            "last_lower_parameter":h*last,"deep_level":Q}


def base_ring_support(p,s,pairs):
    n=3*p+s;D=p
    for pair in pairs:
        a,H,f,g=check_pair(p,s,pair)
        D*=abs(f*g)//gcd(f,g)**2
    for a in range(2,p+1):
        if gcd(a,n)==1:D*=a
    if (p,s)==(11,3):D*=37
    return D


def supported(value,D):
    value=abs(int(value))
    assert value
    while gcd(value,D)>1:value//=gcd(value,D)
    return value==1


def torus_literal(p,s,q):
    n=3*p+s;r=p+s
    for a,z in ((1,0),(0,1)):
        raw=[F(a)]*p+[F(r*z-a)]*p+[F(-p*z)]*r
        led=Ledger(raw,p)
        plus=(p+q)//2;minus=(p-q)//2
        x=list(range(plus))+list(range(p,p+minus))
        y=list(range(plus,p))+list(range(p+minus,2*p))
        led.average(x);led.average(y)
        expected_a=F(q,p)*a+F(r*(p-q),2*p)*z
        expected_b=r*z-expected_a
        assert all(led.state[i]==expected_a for i in x)
        assert all(led.state[i]==expected_b for i in y)
        assert all(led.state[i]==-p*z for i in range(2*p,n))
    return 4


def negative_control():
    V=(F(19,121),F(-1,121),F(-34,121),F(-15,121))
    assert residue(V[0]+V[3],4)==0
    return column(11,1,4,V,1+34*17,121-34*9,1)


def rational_column_checks():
    count=0
    cases=json.loads((ROOT/"work/large_symmetric_carrier_shallow_certificate.json").read_text())["cases"]
    for p,s in ((11,1),(11,3),(13,3),(13,4),(19,7)):
        case=next(c for c in cases if c["p"]==p and c["s"]==s)
        delta,V,coeff=root_supply(p,s,case["root_pairs"])
        n=3*p+s
        for sign in (-1,1):
            eps=F(sign,p)
            for a,b in ((-7,3),(5,-11),(0,9)):
                z=eps+F(n*a,p*p)
                y=eps*p*p+F(n*b,p*p)
                column(p,s,delta,V,z,y,eps)
                count+=1
    return count


def small_digit_bound_checks():
    count=0;fallbacks=0
    for p in range(11,1001):
        for n in range(2*p+2,4*p,2):
            q=digit(p,n)
            assert q<=p and q%8 in (3,5) and gcd(q,n)==1
            count+=1;fallbacks+=q not in (3,5,11,13)
    # Cases blocking all four initial digits; no primality of p needed.
    for n in (4290,30030,510510,9699690):
        p=n//4+1
        if p%2==0:p+=1
        q=digit(p,n)
        assert q<=p and gcd(q,n)==1 and q%8 in (3,5)
        fallbacks+=1;count+=1
    return count,fallbacks


def main():
    started=perf_counter()
    # Deliberately retain only p,s,root_pairs; direction/binary_unit cannot be consulted.
    raw=json.loads((ROOT/"work/large_symmetric_carrier_shallow_certificate.json").read_text())["cases"]
    cases=[{k:c[k] for k in ("p","s","root_pairs")} for c in raw]
    rng=Random(20260917)
    transports=atoms=bad_traces=0
    examples=[]
    for case in cases:
        p,s=case["p"],case["s"];n=3*p+s
        delta,V,coeff=root_supply(p,s,case["root_pairs"])
        D=base_ring_support(p,s,case["root_pairs"])
        assert gcd(D,n)==1
        for a in (*V,*invq(V)):
            assert supported(F(a).denominator,D)
        dd=F(det(V))
        assert supported(dd.numerator,D) and supported(dd.denominator,D)
        if n%2==0:
            bad_traces+=residue(V[0]+V[3],4)!=2
            atoms+=torus_literal(p,s,digit(p,n))
        for j in range(delta):_,num=terminal(p,s,j);atoms+=num
        h=delta*n
        for _ in range(16):
            eps=rng.choice([a for a in range(1,p+1) if gcd(a,n)==1])
            result=column(p,s,delta,V,eps+n*rng.randrange(-h,h),eps*p*p+n*rng.randrange(-h,h),eps)
            transports+=1
            if (p,s) in ((11,1),(13,3)) and len(examples)<6:
                examples.append({"p":p,"s":s,"root_bezout":coeff,**result})
    large=0
    for p in (83,97,101,307,997):
        for s in range(1,10):
            a=s//3+1
            pairs=[family(p,s,alpha,p//(3*alpha)-j)[:2] for alpha in (a,a+1) for j in (1,0)]
            delta,V,coeff=root_supply(p,s,pairs)
            n=3*p+s;h=delta*n
            for _ in range(8):
                column(p,s,delta,V,1+n*rng.randrange(h),p*p+n*rng.randrange(h),1);large+=1
    digits,fallback=small_digit_bound_checks()
    control=negative_control()
    rational=rational_column_checks()
    report={"status":"PASS","finite_cases":len(cases),"independent_direction_fields_used":0,
        "binary_unit_fields_used":0,"old_direction_conditions_replaced":162,
        "bad_trace_cases_now_completed":bad_traces,"finite_transports":transports,
        "large_formula_transports":large,"literal_torus_and_terminal_atoms":atoms,
        "nonintegral_R_column_checks":rational,
        "small_digit_instances":digits,"noninitial_digit_cases":fallback,
        "shallow_group_lifting_used":False,"smith_primitive_preparation_used":False,
        "auxiliary13_retained":True,"examples":examples,"negative_control":control,
        "unchanged_frozen_files":check_frozen_files(),"seconds":round(perf_counter()-started,3),
        "local_links_checked":check_local_links(),
        "scope":"Exact finite support and transport checks. The all-parameter theorem is in the companion proof. Old root supplies, base units, exact deep kernel and auxiliary13 remain. No averaging-word or large-group orbit search."}
    (HERE/"split_torus_column_verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k not in ("examples","negative_control")},indent=2))


if __name__=="__main__":main()
