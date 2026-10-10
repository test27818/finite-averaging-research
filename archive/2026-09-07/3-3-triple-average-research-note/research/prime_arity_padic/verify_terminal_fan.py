"""Terminal-family transport removes extra dyadic units; no orbit/word search."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from random import Random
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/"work"))
from check_large_symmetric_carrier_certificate import check_pair
from verify_transverse_root_lifting import V_of
from verify_uniform_odd_middle_cores import mm,invq,residue
from verify_even_odd_half_core import mod_power
from verify_four_prime_entry_and_band import Ledger
from verify_square_zero_compiler import check_frozen_files,check_local_links
ID=(1,0,0,1)
if not __debug__:raise RuntimeError("Assertions required")


def det(A):return A[0]*A[3]-A[1]*A[2]
def red(A,m):return tuple(residue(x,m) for x in A)
def act(A,w,m):
    a,b,c,d=red(A,m)
    return ((a*w[0]+b*w[1])%m,(c*w[0]+d*w[1])%m)


def terminal(p,s,j):
    n=3*p+s;r=p+s
    z=1;y=p*p-n*j
    k=p-1-2*j;i=j+1
    assert min(i,j,k)>=0 and i+j+k==p and k<=r
    assert gcd(y,n)==gcd(z,y)==1
    a=y-p*z
    state=[F(a)]*p+[F(r*z-a)]*p+[F(-p*z)]*r
    selected=list(range(i))+list(range(p,p+j))+list(range(2*p,2*p+k))
    assert len(selected)==p and sum(state[x] for x in selected)==0
    ledger=Ledger(state,p);ledger.average(selected)
    assert all(ledger.state[x]==0 for x in selected)
    return (z,y),1


def transport(p,s,delta,V,z,y,eps):
    """Columns already normalized modulo n. Correct modulo Q without new units."""
    n=3*p+s;c=2*delta;Q=c*n;h=delta*n
    assert n%2==0 and delta in (2,4)
    assert y%n==(eps*p*p)%n and gcd(y,n)==gcd(eps,n)==1
    assert red(V,n)==(1,residue(F(-1,p*p),n),0,1)
    assert residue(V[0]+V[3],4)==2
    assert residue(det(V),2)==1
    assert z%n==eps%n
    # Normalize the first coordinate modulo Q; combine the planned bits into one power.
    current=(z%Q,y%Q)
    B=tuple(x*pow(residue(det(V),Q),-n//2,Q)%Q for x in mod_power(V,n,Q))
    assert red(B,2*n)==(1,n,0,1)
    advance=0
    assert (current[0]-eps)%n==0
    for bit in range(c.bit_length()-1):
        precision=n*(1<<bit)
        if ((current[0]-eps)//precision)%2:
            advance+=1<<bit
            current=act(mod_power(B,1<<bit,Q),current,Q)
        assert (current[0]-eps)%(2*precision)==0
    assert current[0]==eps%Q
    assert act(mod_power(B,advance,Q),(z,y),Q)==current
    # Choose one of delta terminals, then correct only its last scale bit.
    j=((eps*p*p-current[1])//n)*pow(eps,-1,delta)%delta
    desired=(eps,eps*(p*p-n*j))
    lower_toggle=((desired[1]-current[1])//h)*pow(eps,-1,2)%2
    if lower_toggle:current=act((1,0,h,1),current,Q)
    assert current==tuple(x%Q for x in desired)
    return {"normalized_cycle_power":advance,"lower_toggle":lower_toggle,"terminal_j":j}


def bezout(a,b):
    x0,x1,y0,y1=1,0,0,1
    while b:
        q=a//b;a,b=b,a-q*b;x0,x1=x1,x0-q*x1;y0,y1=y1,y0-q*y1
    if a<0:return -a,-x0,-y0
    return a,x0,y0


def primitive_preparation(Q,r,seed):
    """Exact Smith-chart preparation and a literal principal-congruence matrix."""
    assert gcd(Q,r)==1
    U=lambda x:(1,x,0,1)
    L=lambda x:(1,0,x,1)
    left=mm(U(seed+1),L(seed-2))
    right=mm(L(seed+3),U(2-seed))
    A=mm(mm(left,(F(1,r),0,0,F(r))),right)
    v=(seed,seed+1)
    assert gcd(*v)==1 and det(A)==1
    rv=(right[0]*v[0]+right[1]*v[1],right[2]*v[0]+right[3]*v[1])
    targets=(rv[0]*pow(r,-1,Q)%Q,rv[1]%Q)
    h1=targets[0]+Q*((1-targets[0])*pow(Q,-1,r)%r)
    if h1==0:h1=Q*r
    h2=targets[1]+Q*((1-targets[1])*pow(Q,-1,r)%r)
    # For primes dividing h1 outside Qr, choose a nonzero h2 residue.
    remain=abs(h1);primes=[];d=2
    while d*d<=remain:
        if remain%d==0:
            primes.append(d)
            while remain%d==0:remain//=d
        d+=1
    if remain>1:primes.append(remain)
    modulus=1;k=0
    for ell in primes:
        if Q*r%ell==0:continue
        target=1 if h2%ell==0 else 0
        k+=modulus*((target-k)*pow(modulus,-1,ell)%ell)
        modulus*=ell
    h2+=Q*r*k
    assert gcd(h1,h2)==gcd(h1,r)==gcd(h2,r)==1
    pre=(r*h1,h2)
    ri=invq(right)
    w=(ri[0]*pre[0]+ri[1]*pre[1],ri[2]*pre[0]+ri[3]*pre[1])
    assert all(F(x).denominator==1 for x in w)
    w=tuple(int(x) for x in w)
    out=(A[0]*w[0]+A[1]*w[1],A[2]*w[0]+A[3]*w[1])
    assert all(F(x).denominator==1 for x in out)
    assert gcd(*w)==gcd(*(int(x) for x in out))==1
    assert all((w[i]-v[i])%Q==0 for i in range(2))
    # Build gamma using the exact-fiber proof; gamma v=w and gamma=I mod Q.
    _,bv,cv=bezout(*v)
    x=(-cv,bv)
    error=(w[0]*x[1]-w[1]*x[0]-1)//Q
    _,bw,cw=bezout(*w)
    zz=(error*cw,-error*bw)
    y=(x[0]+Q*zz[0],x[1]+Q*zz[1])
    gamma=mm((w[0],y[0],w[1],y[1]),invq((v[0],x[0],v[1],x[1])))
    assert det(gamma)==1 and red(gamma,Q)==ID
    assert (gamma[0]*v[0]+gamma[1]*v[1],gamma[2]*v[0]+gamma[3]*v[1])==w
    assert all(residue(out[i],Q)==act(A,v,Q)[i] for i in range(2))
    return 1


def normalized_cycle_checks():
    """Bounded exact parameter checks; arbitrary parameters/exponents proved in text."""
    count=0
    for n in (2,4,6,8,10,12,18,32,54):
        Q=16*n
        for aa in range(4):
            for dd in range(4):
                for cc in range(4):
                    V=(1+n*aa,3+n*aa,n*cc,1+n*dd)
                    D=det(V)
                    if gcd(D,n)!=1 or (V[0]+V[3])%4!=2:continue
                    B=tuple(x*pow(D,-n//2,Q)%Q for x in mod_power(V,n,Q))
                    for j in range(4):
                        m=(1<<j)*n
                        assert tuple(x%(2*m) for x in mod_power(B,1<<j,2*m))==(1,m,0,1)
                    count+=1
    return count


def run():
    started=perf_counter()
    cases=json.loads((ROOT/"work/large_symmetric_carrier_shallow_certificate.json").read_text())["cases"]
    rng=Random(20260916)
    count=atoms=0
    classes={};examples=[]
    for case in cases:
        p,s=case["p"],case["s"];n=3*p+s
        if n%2:continue
        delta=0
        for pair in case["root_pairs"]:
            a,H,f,g=check_pair(p,s,pair);delta=gcd(delta,H)
        if (p,s)==(11,3):delta=2
        assert delta in (2,4)
        classes[delta]=classes.get(delta,0)+1
        V=V_of(p,s,case["direction"])
        for j in range(delta):
            _,add=terminal(p,s,j);atoms+=add
        c=2*delta;Q=c*n
        units=[x for x in range(1,p+1) if gcd(x,n)==1]
        for _ in range(24):
            eps=rng.choice(units)
            z=eps+n*rng.randrange(-8,9)
            y=eps*p*p+n*rng.randrange(-8,9)
            result=transport(p,s,delta,V,z,y,eps)
            assert result["terminal_j"]<delta
            count+=1
            if (p,s)==(13,3) and len(examples)<3:
                examples.append({"p":p,"s":s,"input_mod_Q":[z%Q,y%Q],"eps":eps,**result})
    # Formula instances beyond the finite certificate.
    from verify_carrier_interval_reduction import family
    large=0
    for p in (83,97,101,307,997):
        for s in range(1,10,2):
            a=s//3+1
            rows0=family(p,s,a,p//(3*a)-1)[:3]
            rows1=family(p,s,a+1,p//(3*(a+1))-1)[:3]
            V=None
            for x in rows0[:2]:
                for y in rows1[:2]:
                    candidate=V_of(p,s,(x,y))
                    if residue(candidate[0]+candidate[3],4)==2:V=candidate;break
                if V is not None:break
            assert V is not None
            for j in range(2):_,add=terminal(p,s,j);atoms+=add
            for _ in range(8):
                n=3*p+s;eps=1
                transport(p,s,2,V,eps+n*rng.randrange(8),p*p+n*rng.randrange(8),eps)
                large+=1
    prep=sum(primitive_preparation(q,h,u) for q,h in ((8,3),(36,5),(42,13),(136,19))
             for u in (-5,0,9))
    cycle_checks=normalized_cycle_checks()
    report={"status":"PASS","even_certificate_cases":sum(classes.values()),"by_delta":classes,
            "finite_case_transports":count,"large_formula_transports":large,
            "literal_zero_sum_terminal_atoms":atoms,"primitive_preparation_examples":prep,
            "normalized_cycle_parameter_checks":cycle_checks,
            "binary_unit_fields_read":0,"special_97_over13_used":False,
            "unchanged_frozen_files":check_frozen_files(),"examples":examples,
            "scope":"Finite exact checks of the written general terminal-fan theorem. "
            "Old root/direction certificates and auxiliary13 for (11,3) remain; no finite orbit search."}
    report["local_links_checked"]=check_local_links()
    report["seconds"]=round(perf_counter()-started,3)
    (HERE/"terminal_fan_verification.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))


if __name__=="__main__":run()
