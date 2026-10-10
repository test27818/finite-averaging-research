"""Exact checks of the retained counts and the newly composed capacity ranges."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def ceildiv(a,b): return -(-a//b)

def reflection(p,s,row):
    r=p+s; n=3*p+s
    i,j,k,x,y,u,v=row
    assert min(row)>=0 and i+j+k==x+y+u+v==p
    stock=(p-2*i,p-2*j,r-2*k,p-s)
    assert all(0<=z<=bound for z,bound in zip((x,y,u,v),stock))
    alpha=i-j; beta=r*j-p*k
    assert p*(x-y)+alpha*v==beta
    top=p*r*y-p*p*u+beta*v
    scalar=beta*beta-alpha*top
    assert scalar and scalar%p==0 and scalar%n==pow(p,4,n)
    return alpha,n*(2*j+alpha)-2*p*p,scalar//p

def upper_rows(p,s):
    if 2*s>p:
        d=p-s; a0=ceildiv(d,2)+2
        for a in (a0,a0+1):
            low=max(0,ceildiv(d-a,2))
            high=min(a//2,p-2*a)
            assert low+1<=high
            yield [(a,0,p-a,l,p-a+l,a-2*l,0) for l in (low+1,low)]
    else:
        a0=ceildiv(p,6)
        for a in (a0,a0+1):
            low=max(5*a-p,ceildiv(s,2)-a)
            high=min(a,2*a+s-ceildiv(p,2))
            assert low+1<=high
            yield [(2*a,a,p-3*a,a-e,p-3*a-e,2*a-s+2*e,s) for e in (low,low+1)]

def check_rows(p,s,pairs):
    root=transverse=0
    for first,second in pairs:
        a,h,f=reflection(p,s,first)
        b,_,g=reflection(p,s,second)
        assert a==b and g-f==a*(3*p+s)
        assert tuple(second)==tuple(first[:3])+(first[3]-1,first[4]-1,first[5]+2,first[6])
        transverse=gcd(transverse,a); root=gcd(root,h)
    return transverse,root

def prime(p): return p>=2 and all(p%d for d in range(2,int(p**.5)+1))

def check_upper():
    total=0
    for p in range(11,1001):
        if not prime(p): continue
        for s in range(10,p):
            assert check_rows(p,s,list(upper_rows(p,s)))==(1,gcd(3*p+s,2))
            total+=1
    p=2**61-1
    for s in (10,(p-1)//2,(p+1)//2,p-2,p-1):
        assert check_rows(p,s,list(upper_rows(p,s)))==(1,gcd(3*p+s,2))
        total+=1
    return total

def check_retained():
    cases=json.loads((HERE/'root_certificate.json').read_text())['cases']
    for case in cases:
        p,s=case['p'],case['s']
        a,d=check_rows(p,s,case['root_pairs'])
        if (p,s)!=(11,3):
            assert a==1 and d in ((1,) if (3*p+s)%2 else (2,4))
    assert len(cases)==114
    return {'cases':len(cases),'pairs':sum(len(c['root_pairs']) for c in cases)}

def mm(A,B):
    a,b,c,d=A;e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)

def check_even_interface():
    total=0
    for p in range(5,101):
        if not prime(p):continue
        for r in range(2,p,2):
            n=2*p+r; s=r-1; d=(p*r-n*s)//2
            chart=(0,1,1,p); inverse=(-p,1,1,0)
            J=mm(mm(chart,(0,d,-1,0)),inverse)
            assert J==(p,-1,n*((p-s)//2),-p)
            S=(1,0,n,-1)
            V=mm(S,J)
            assert tuple((x*pow(p,-1,n))%n for x in V)==(1,(-pow(p,-1,n))%n,0,1)
            assert gcd(d,n)==1
            total+=1
    return total

if __name__=='__main__':
    result={'upper_capacity_instances':check_upper(), 'retained':check_retained(),
            'even_standard_reflection_interfaces':check_even_interface(),
            'scope':'Exact checks of formulas and finite data. General bounds are proved in the article.'}
    (HERE/'revision_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
