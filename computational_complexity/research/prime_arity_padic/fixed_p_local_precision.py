"""Construct local words of length O_p(d^2) attaining a residue modulo p^d.

Only p=5 or p=7 is implemented. This controls a local numerator, not exact
zero reachability. The accompanying note proves the scope and G preservation.
"""
from math import gcd
import json

def rho(p,t):
    # t is a positive even return-word length: t-1 repeats of S, then D.
    assert t>=2 and t%2==0
    return (p+2-p**t)//(p+1)

def params(p):
    assert p in (5,7)
    return (2,4) if p==5 else (4,3) # safe length spacing, order of 2 mod p

def scalar_mod(p,word,M):
    out=1
    for t in word:out=out*(rho(p,t)%M)%M
    return out

def pairs(p,d):
    tau,h=params(p)
    # Basic equal-length pair A=rho(2tau), B=rho(tau)^2.
    A=[2*tau];B=[tau,tau]
    oneA=A*h;oneB=B*h
    out=[]
    for i in range(1,d):
        if i<tau:
            W=oneA*(p**(i-1));V=oneB*(p**(i-1))
        else:
            base=i-i%tau;extra=i%tau
            W=[base,base+2*tau]*(p**extra)
            V=[base+tau,base+tau]*(p**extra)
        assert sum(W)==sum(V)
        mod=p**(i+1)
        g=scalar_mod(p,W,mod)*pow(scalar_mod(p,V,mod),-1,mod)%mod
        assert (g-1)%(p**i)==0 and (g-1)//p**i%p
        out.append((W,V))
    return A,B,out

def synthesize(p,d,target,L=None):
    assert d>=1
    M=p**d;assert target%p
    tau,h=params(p);A,B,ps=pairs(p,d)
    T=(h-1)*sum(A)+(p-1)*sum(sum(W) for W,V in ps)
    if L is None:L=T+(1 if p==7 else 0)
    assert L>=T
    tail=(L-T)%tau
    padding=(L-T-tail)//tau
    # The final tail is repeated single-S, with no final double.
    coeff=(p**(tail+1)+(p+2)*(-1)**tail)//(p+1)
    pad=pow(rho(p,tau),padding,M)
    wanted=(2*pow(p,L,M)-(p+2)*target)*pow(coeff*pad,-1,M)%M
    base=1
    for W,V in ps:base=base*pow(scalar_mod(p,V,M),p-1,M)%M
    cal=None
    for j in range(h):
        word=A*j+B*(h-1-j)
        if scalar_mod(p,word,M)*base%p==wanted%p:cal=word;break
    # An incompatible first digit, not a global nonreachability certificate.
    if cal is None:return None
    current=scalar_mod(p,cal,M)*base%M
    word=list(cal)
    for i,(W,V) in enumerate(ps,1):
        g=scalar_mod(p,W,M)*pow(scalar_mod(p,V,M),-1,M)%M
        chosen=next(j for j in range(p) if (current*pow(g,j,M)-wanted)%p**(i+1)==0)
        current=current*pow(g,chosen,M)%M
        word+=W*chosen+V*(p-1-chosen)
    assert current==wanted and sum(word)==T
    result=scalar_mod(p,word,M)*pad%M
    attained=(2*pow(p,L,M)-coeff*result)*pow(p+2,-1,M)%M
    assert attained==target%M
    assert all(gcd(rho(p,t),p+3)==1 for t in word)
    return {'returns':word,'padding':padding,'tail':tail,'T':T,'L':L,'target':target%M,'p':p,'digits':d}

def replay(plan):
    p=plan['p'];d=plan['digits'];L=plan['L'];M=p**d
    a,b,c=0,1,1;steps=0
    for t in plan['returns']+[params(p)[0]]*plan['padding']:
        for _ in range(t-1):
            a,b,c=(p-1)*a+b,p*a,p*c;steps+=1
        a,b,c=(p-2)*a+b+c,p*a,p*a;steps+=1
    for _ in range(plan['tail']):
        a,b,c=(p-1)*a+b,p*a,p*c;steps+=1
    assert steps==L and p*a+b+c==2*p**L and a%M==plan['target']
    return steps

if __name__=='__main__':
    rows=[]
    for p,maxd in ((5,5),(7,5)):
        for d in range(1,maxd+1):
            plan=synthesize(p,d,1)
            assert plan
            replay(plan)
            rows.append({'p':p,'d':d,'T':plan['T'],'L':plan['L'],'return_blocks':len(plan['returns'])})
    print(json.dumps(rows,indent=2))
