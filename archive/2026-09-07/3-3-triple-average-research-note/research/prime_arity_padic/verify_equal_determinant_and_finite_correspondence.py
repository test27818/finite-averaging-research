"""Exact determinant fibers, even-carrier roots, and bounded content transitions.

No averaging-word search. Residue enumeration only cross-checks a proved finite
precision lemma on small matrices, including nonunit determinants.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd, lcm
from random import Random
from time import perf_counter
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work'))
from verify_common_shape_and_relation_lattice import primes_below,matrix
from verify_four_prime_entry_and_band import Ledger
from verify_uniform_odd_middle_cores import mm,invq,bezout
from verify_critical_band_common_controller import shifted_terminal_transport
from verify_upper_band_unrestricted_completion import zy
from verify_two_root_column_completion import scale,red,powq
from verify_square_zero_compiler import check_frozen_files,check_local_links
ID=(1,0,0,1)


def det(A):return A[0]*A[3]-A[1]*A[2]
def act(A,v):return A[0]*v[0]+A[1]*v[1],A[2]*v[0]+A[3]*v[1]


def fiber_checks():
    count=0
    for p in primes_below(50):
        for r in range(1,2*p):
            if r==p:continue
            for i,j in ((2,1),(p-2,1),((p-1)//2,(p-3)//2)):
                k=p-i-j;alpha=i-j;beta=r*j-p*k
                if k<0 or not 0<alpha<p:continue
                g=gcd(alpha,beta);n=2*p+r
                assert gcd(g,n)==1
                # Produce an integral determinant-preserving move with root n/g.
                A=p*alpha-beta
                assert A%g==0
                dv=(-n*pow(g,-1,p))%p
                assert (A//g-j*dv)%p==0
                dy=(A//g-j*dv)//p
                assert ((alpha//g)*n+alpha*dv)%p==0
                dx=dy-((alpha//g)*n+alpha*dv)//p
                du=-dx-dy-dv
                top=(p*(dx-dy)+alpha*dv,p*r*dy-p*p*du+beta*dv)
                assert top==(-alpha*F(n,g),-beta*F(n,g))
                # Independent bounded moves verify that no finer root step occurs.
                for dx in range(-3,4):
                    for dy in range(-3,4):
                        A=p*alpha-beta;B=beta+alpha*(p+r)
                        num=-(A*dx+B*dy)
                        if num%(alpha*p):continue
                        dv=num//(alpha*p);du=-dx-dy-dv
                        delta=(dx,dy,du,dv)
                        top=(p*(dx-dy)+alpha*dv,p*r*dy-p*p*du+beta*dv)
                        assert -beta*top[0]+alpha*top[1]==0
                        root=-F(top[0],alpha)
                        assert (root*g/n).denominator==1
                        count+=1
    return count


def even_rows(p,r):
    assert r%2==0 and r>=4 and 2*p>=5*r
    t=r//2;c=((p-1)//2,(p-3)//2,2)
    o=(r-2,t+1,1,p-3*t)
    moved=(r-1,t+4,r-3,p-5*t)
    caps=(p-c[0],p-c[1],r-2,p-r)
    for row in (o,moved):
        assert sum(row)==p and all(0<=x<=y for x,y in zip(row,caps))
    J=matrix(p,r,c,o);M=matrix(p,r,c,moved)
    assert J[0]+J[3]==0 and det(M)==det(J)
    assert mm(M,invq(J))==(1,2*p+r,0,1)
    f=p*(t*t-5*t+7)-t*(5*t-7)
    assert mm(J,J)==scale(p*f,ID) and gcd(f,2*p+r)==1
    if r>=6:
        o2=(o[0]-1,o[1]-1,o[2]+2,o[3])
        assert all(0<=x<=y for x,y in zip(o2,caps))
        K=matrix(p,r,c,o2)
        g=-det(K)//p
        assert g-f==2*p+r and gcd(f,g)==1
    return c,o,moved,J


def odd_rows(p,r):
    assert r>=5 and r%2 and p>=5*r
    c=((p-1)//2,(p-3)//2,2)
    v=(p-3*r)//2
    w=(r-5)//2
    u=(p-v+w)%2
    x=(p-v-u+w)//2;y=(p-v-u-w)//2
    o=(x,y,u,v)
    moved=(x+1,y+3,u+r-4,v-r)
    other=(x-1,y-1,u+2,v)
    caps=(p-c[0],p-c[1],r-2,p-r)
    for row in (o,moved,other):
        assert sum(row)==p and all(0<=x<=y for x,y in zip(row,caps))
    J=matrix(p,r,c,o);M=matrix(p,r,c,moved);K=matrix(p,r,c,other)
    assert J[0]+J[3]==K[0]+K[3]==0
    assert mm(M,invq(J))==(1,2*p+r,0,1)
    f=-det(J)//p;g=-det(K)//p
    assert mm(J,J)==scale(p*f,ID) and g-f==2*p+r and gcd(f,g)==1
    assert gcd(f,2*p+r)==1
    return c,o,moved,J


def replay_return(p,r,c,o,u,z):
    n=2*p+r
    raw=[u]*p+[r*z-u]*p+[-p*z]*r
    led=Ledger(raw,p);ga=list(range(p));gb=list(range(p,2*p));gc=list(range(2*p,n))
    i,j,k=c
    first=ga[:i]+gb[:j]+gc[:k];led.average(first)
    ga,gb,gc=ga[i:],gb[j:],gc[k:]
    kept,fresh=first[:r],first[r:]
    x,y,w,v=o
    left=ga[:x]+gb[:y]+gc[:w]+fresh[:v]
    right=ga[x:]+gb[y:]+gc[w:]+fresh[v:]
    assert sorted(left+right+kept)==list(range(n))
    led.average(left);led.average(right)
    J=matrix(p,r,c,o)
    aa,zz=act(scale(F(1,p*p),J),(u,z))
    for group,val in zip((left,right,kept),(aa,r*zz-aa,-p*zz)):
        assert all(led.state[x]==val for x in group)
    led.independent_replay(raw)
    return 3


def finite_edges(Q,A):
    D=abs(det(A));L=Q*D;edges={};checks=0
    for x in range(L):
        for y in range(L):
            if gcd(x,y,L)!=1:continue
            u,v=act(A,(x,y));g=gcd(u,v,D)
            assert g>0 and u%g==v%g==0
            output=(u//g%Q,v//g%Q)
            assert gcd(*output,Q)==1
            # The same residue determines content and output for all primitive lifts.
            for dx,dy in ((1,0),(0,-1),(2,3)):
                xx,yy=x+L*dx,y+L*dy
                if gcd(xx,yy)!=1:continue
                uu,vv=act(A,(xx,yy));gg=gcd(uu,vv)
                assert gg==g and (uu//gg%Q,vv//gg%Q)==output
                checks+=1
            edges.setdefault((x%Q,y%Q),set()).add(output)
    return checks,edges


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    start=perf_counter();roots=oddroots=atoms=columns=precision=multi=0
    for p in primes_below(250):
        for r in range(4,2*p//5+1,2):
            c,o,moved,J=even_rows(p,r);roots+=1
            if p<=43:
                for u,z in ((F(1),F(0)),(F(0),F(1))):
                    for row in (o,moved):atoms+=replay_return(p,r,c,row,u,z)
            if p>=11:
                n=2*p+r
                T=mm((1,0,n,-1),scale(F(1,p*p),zy(J,p)))
                assert red(T,n)==(1,-pow(p*p,-1,n)%n,0,1)
                for seed in range(2):
                    shifted_terminal_transport(p,r,2,T,1+n*(seed-2),p*p+n*(seed+3),1)
                    columns+=1
        for r in range(5,p//5+1,2):
            c,o,moved,J=odd_rows(p,r);oddroots+=1
            n=2*p+r
            V=mm((1,0,n,-1),scale(F(1,p*p),zy(J,p)))
            for seed in range(2):
                shifted_terminal_transport(p,r,1,V,1+n*(seed-1),p*p+n*seed,1)
                columns+=1
            if p<=43:
                for u,z in ((F(1),F(0)),(F(0),F(1))):
                    for row in (o,moved):atoms+=replay_return(p,r,c,row,u,z)
    for Q in (2,3,4,6):
        for A in ((1,0,0,2),(1,1,0,3),(2,0,0,3),(-1,-1,-3,1)):
            c,edges=finite_edges(Q,A);precision+=c
            multi+=sum(len(v)>1 for v in edges.values())
    # Same mod-Q input, different primitive outputs: ordinary mod-Q action is insufficient.
    A=(1,0,0,2)
    assert (2%2,1%2)==(4%2,1%2)
    assert tuple(x//gcd(*act(A,(2,1)))%2 for x in act(A,(2,1)))==(1,1)
    assert tuple(x//gcd(*act(A,(4,1)))%2 for x in act(A,(4,1)))==(0,1)
    report={'status':'PASS','equal_determinant_kernel_checks':fiber_checks(),
            'even_carrier_direct_root_cases':roots,'literal_return_atoms':atoms,
            'odd_carrier_direct_root_cases':oddroots,
            'common_terminal_transports':columns,'finite_content_lift_checks':precision,
            'genuinely_multivalued_residue_classes':multi,
            'frozen_files':check_frozen_files(),'local_links':check_local_links(),
            'seconds':round(perf_counter()-start,3),
            'scope':'Exact determinant-fiber and finite-precision formulas; explicit odd/even carrier full resource interfaces. Generic finite graph coverage and all small-p resource existence remain unproved.'}
    (HERE/'equal_determinant_finite_correspondence_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
