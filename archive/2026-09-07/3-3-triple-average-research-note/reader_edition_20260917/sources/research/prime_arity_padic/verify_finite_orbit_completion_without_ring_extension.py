"""Finite orbit completion using determinant-content branches, no late ring extension.

Checks prescribed finite matrices, exact Gamma(Q,Z) preparations and physical
two-block digits. Does not derive initial deep kernels or search averaging words.
"""
from pathlib import Path
from math import gcd
from fractions import Fraction as F
from time import perf_counter
import json,sys,re
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work'))
from verify_four_prime_entry_and_band import factors,Ledger
from verify_uniform_odd_middle_cores import bezout
from verify_critical_band_common_controller import check_supply,cutoff,cd
from verify_split_torus_column import digit,dyadic_unit_word
from verify_two_root_column_completion import red
from verify_square_zero_compiler import check_frozen_files
I=(1,0,0,1)


def check_own_links():
    # Other local threads may be drafting unrelated files concurrently.
    path=HERE/'finite_orbit_completion_without_ring_extension.md'
    count=0
    for target in re.findall(r'\[[^\]\n]+\]\(([^\)\n]+)\)',path.read_text(encoding='utf-8')):
        if target.startswith(('https://','http://')):continue
        assert (path.parent/target.split('#',1)[0]).is_file(),target
        count+=1
    return count


def mm(A,B,Q):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%Q for i in range(2) for j in range(2))
def mv(A,v,Q):return ((A[0]*v[0]+A[1]*v[1])%Q,(A[2]*v[0]+A[3]*v[1])%Q)
def inverse(A,Q):
    t=pow(A[0]*A[3]-A[1]*A[2],-1,Q)
    return tuple(x*t%Q for x in (A[3],-A[1],-A[2],A[0]))
def mpow(A,k,Q):
    out=I
    if k<0:A=inverse(A,Q);k=-k
    while k:
        if k&1:out=mm(out,A,Q)
        A=mm(A,A,Q);k//=2
    return out
def crt(a,m,b,n):
    if n==1:return a%m
    return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)


def scalar_word(p,n,target):
    """Signed small-digit word modulo n, via the all-interval unit proof."""
    assert gcd(target,n)==1
    target%=n
    word=[];sign=1
    if n%2:
        a=target
        if 2*a>n:a=n-a;sign=-1
        twopower=0
        while a>p:
            if 3*a<n:a=4*a-n;twopower-=2
            else:a=n-2*a;twopower-=1;sign=-sign
        word=[(2,twopower),(a,1)]
    elif n%4==2:
        m=n//2;a=target%m
        if 2*a>m:a=m-a;sign=-1
        h=0
        while a%2==0:a//=2;h+=1
        eps=1 if m%4==1 else -1
        q=(m+eps)//2
        sign*=eps**h
        word=[(q,-h),(a,1)]
    else:
        for b in range(1,p+1):
            if gcd(b,n)!=1:continue
            a=target*b%n
            if a<=p:word=[(a,1),(b,-1)];break
            if n-a<=p:word=[(n-a,1),(b,-1)];sign=-1;break
        else:raise AssertionError(('unit ratio missing',p,n,target))
    assert all(1<=q<=p and gcd(q,n)==1 for q,e in word)
    assert eval_scalar(sign,word,n)==target
    return sign,word


def eval_scalar(sign,word,Q):
    a=sign
    for q,e in word:a=a*pow(q,e,Q)%Q
    return a%Q


def complete(p,r,V,w):
    n=2*p+r;delta=gcd(n,2);h=delta*n;Q=h*h
    m=n
    while m%2==0:m//=2
    two=h//m;M=two*two
    V=red(V,Q);z,y=w[0]%Q,w[1]%Q
    assert gcd(y,n)==1 and tuple(a%n for a in V)==(1,-pow(p*p,-1,n)%n,0,1)
    k=(p*p*z*pow(y,-1,n)-1)%n
    z,y=mv(mpow(V,k,Q),(z,y),Q)
    sign,word=scalar_word(p,n,pow(z,-1,n))
    scalar=eval_scalar(sign,word,Q)
    z,y=scalar*z%Q,scalar*y%Q
    assert z%n==1 and y%n==p*p%n
    if n%2==0:
        q=digit(p,n)
        sign,k=dyadic_unit_word(q,z%M,M)
        # D_q is a finite action built from forward digits + content scalar;
        # no assertion that its rational inverse is physically present.
        qi=pow(q,-1,Q)
        D=(qi,0,(n//2)*(qi-1)%Q,1)
        z,y=mv(mpow(D,k,Q),(z,y),Q)
        if sign==-1:z,y=mv((-1,0,-n,1),(z,y),Q)
        assert z%M==1 and y%n==p*p%n
        assert mpow(V,M,M)==I
        if m>1:
            k=M*(p*p*(z-1)*pow(y,-1,m)*pow(M,-1,m)%m)
            z,y=mv(mpow(V,k,Q),(z,y),Q)
    start=max(0,cd(p-1-r,2))
    jres=((p*p-y)//n)%delta if delta>1 else 0
    j=start+(jres-start)%delta
    assert 0<=p-1-2*j<=r
    goal=(1,p*p-n*j)
    assert (z-1)%h==(y-goal[1])%h==0
    E=(0,0,1,0);X=mm(mm(V,E,Q),inverse(V,Q),Q)
    if m>1:
        rhs=((goal[0]-z)//h%m,(goal[1]-y)//h%m)
        c0,c1=mv(E,goal,m),mv(X,goal,m)
        assert (-c0[1]*c1[0])%m==2*pow(p*p,-1,m)%m
        t1=rhs[0]*pow(c1[0],-1,m)%m
        t0=(rhs[1]-t1*c1[1])*pow(c0[1],-1,m)%m
        for A,t in ((E,t0),(X,t1)):
            t=crt(t,m,0,two)
            B=tuple((I[i]+h*t*A[i])%Q for i in range(4))
            z,y=mv(B,(z,y),Q)
    if two>1:
        t=crt(((goal[1]-y)//h)*pow(z,-1,two)%two,two,0,m)
        z,y=mv((1,0,h*t,1),(z,y),Q)
    assert (z,y)==tuple(x%Q for x in goal)
    return j


def primitive_lift(residue_pair,L):
    x,y=residue_pair;y=y or L
    step=1;k=0
    for ell in factors(abs(y)):
        if L%ell==0:continue
        wanted=(1-x)*pow(L,-1,ell)%ell
        k+=step*((wanted-k)*pow(step,-1,ell)%ell);step*=ell
    out=(x+L*k,y)
    assert gcd(*out)==1 and all((out[i]-residue_pair[i])%L==0 for i in (0,1))
    return out


def exact_fiber_map(v,w,Q):
    _,a,b=bezout(*v);_,c,d=bezout(*w)
    x=(-b,a);y=(-d,c)
    t=(a*(y[0]-x[0])+b*(y[1]-x[1]))%Q
    y=(y[0]-t*w[0],y[1]-t*w[1])
    Bv=(v[0],x[0],v[1],x[1]);Bw=(w[0],y[0],w[1],y[1])
    Bi=(Bv[3],-Bv[1],-Bv[2],Bv[0])
    G=tuple(sum(Bw[2*i+k]*Bi[2*k+j] for k in (0,1)) for i in (0,1) for j in (0,1))
    assert G[0]*G[3]-G[1]*G[2]==1 and tuple(x%Q for x in G)==I
    assert (G[0]*v[0]+G[1]*v[1],G[2]*v[0]+G[3]*v[1])==w
    return G


def content_preparations():
    lifts=atoms=0
    for p in (3,5,7,11):
        r=1;n=2*p+r;Q=n*n
        for q in range(1,p,2):
            if gcd(q,n)!=1:continue
            A=(q,r*(p-q)//2,0,p);D=p*q
            divisors=[g for g in range(1,D+1) if D%g==0]
            candidates={}
            for x in range(D):
                for y in range(D):
                    if gcd(x,y,D)!=1:continue
                    z=(A[0]*x+A[1]*y,p*y);g=gcd(*z,D)
                    candidates.setdefault(g,(x,y))
            assert set(candidates)==set(divisors)
            for g,(x,y) in candidates.items():
                finite_order_bound=1
                for ell,e in factors(Q).items():
                    finite_order_bound*=ell**(4*(e-1))*(ell*ell-1)*(ell*ell-ell)
                assert mpow(A,finite_order_bound,Q)==I
                content_branch=tuple(a*pow(g,-1,Q)%Q for a in A)
                assert mm(mpow(A,finite_order_bound-1,Q),content_branch,Q)==tuple(
                    pow(g,-1,Q)*a%Q for a in I)
                for original in ((1,0),(1,1)):
                    assert gcd(original[0]+p*original[1],n)==1
                    res=(crt(original[0],Q,x,D),crt(original[1],Q,y,D))
                    w=primitive_lift(res,Q*D)
                    assert gcd(w[0]+p*w[1],n)==1
                    exact_fiber_map(original,w,Q)
                    raw=(A[0]*w[0]+A[1]*w[1],p*w[1])
                    assert gcd(*raw)==g
                    target=(raw[0]//g%Q,raw[1]//g%Q)
                    assert target==mv(tuple(a*pow(g,-1,Q)%Q for a in A),original,Q)
                    # Replay actual two complementary p-averages on the prepared core.
                    aa,zz=w
                    state=[F(aa)]*p+[F(r*zz-aa)]*p+[F(-p*zz)]*r
                    led=Ledger(state,p);k=(p-q)//2
                    left=list(range(p-k))+list(range(p,p+k))
                    right=list(range(p-k,p))+list(range(p+k,2*p))
                    led.average(left);led.average(right)
                    expected=F(raw[0],p)
                    assert all(led.state[i]==expected for i in left)
                    assert all(led.state[i]==r*zz-expected for i in right)
                    led.independent_replay(state);atoms+=2;lifts+=1
    return lifts,atoms


def digit_product_checks():
    count=0
    for p in (3,5,7,11,13,17,19):
        for r in range(1,2*p):
            if r==p:continue
            n=2*p+r;Q=(gcd(n,2)*n)**2
            C=(0,1,1,p);Ci=(-p,1,1,0)
            P1=(1,r*(p-1)//2,0,p)
            for q in range(1,p+1,2):
                if gcd(q,n)!=1:continue
                Pq=(q,r*(p-q)//2,0,p)
                T=mm(mm(C,mm(Pq,inverse(P1,Q),Q),Q),Ci,Q)
                T=tuple(a*pow(q,-1,Q)%Q for a in T)
                if n%2==0:
                    expected=(pow(q,-1,Q),0,(n//2)*(pow(q,-1,Q)-1)%Q,1)
                    assert T==expected
                count+=1
    return count


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    started=perf_counter();transports=normalizers=0
    # Existing nontrivial actual directions, including formerly bad mod-4 traces.
    for p in (83,89,101,307):
        for r in sorted({cutoff(p),p-1,p+1,p+9,p+10,3*p//2,3*p//2+1,2*p-1}):
            _,_,_,V=check_supply(p,r)
            n=2*p+r
            for seed in range(8):
                y=1+seed*n
                complete(p,r,V,(seed*seed-9,y));transports+=1
    # The reviewed unimodular-triangle example, using only finite powers.
    p,r=43,65;n=151;Q=n*n
    J=(-600,26365,-15,600);C=(0,1,1,p);Ci=(-p,1,1,0)
    Jzy=mm(mm(C,J,Q),Ci,Q)
    T=mm((1,0,n,-1),tuple(a*pow(p*p,-1,Q)%Q for a in Jzy),Q)
    V=mpow(T,pow(15,-1,n),Q)
    for seed in range(12):complete(p,r,V,(seed*7-13,1+n*seed));transports+=1
    # Universal finite algebra itself has no p>=83 requirement.
    for p in (3,5,7,11,13,17,19):
        for r in range(1,2*p):
            if r==p:continue
            n=2*p+r;Q=(gcd(n,2)*n)**2
            V=(1,-pow(p*p,-1,Q),0,1)
            for y in range(1,n):
                if gcd(y,n)!=1:continue
                complete(p,r,V,(-3+n,y+2*n));transports+=1
                scalar_word(p,n,y);normalizers+=1
    lifts,atoms=content_preparations()
    report={'status':'PASS','finite_column_transports':transports,
            'small_digit_scalar_words':normalizers,'exact_nonunit_content_preparations':lifts,
            'literal_complementary_digit_atoms':atoms,
            'finite_digit_product_checks':digit_product_checks(),
            'late_rational_inverse_activation_used':False,'late_root_ring_reconstruction_used':False,
            'frozen_files':check_frozen_files(),'document_local_links':check_own_links(),
            'seconds':round(perf_counter()-started,3),
            'scope':'Finite terminal algebra and exact content preparations under an already-realized deep kernel. Initial resource supply and uniform small-p coverage are not established by these tests.'}
    (HERE/'finite_orbit_completion_without_ring_extension_verification.json').write_text(
        json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
