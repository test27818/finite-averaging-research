"""Exact editorial checks. These finite checks do not prove general quantifiers."""
from pathlib import Path
from fractions import Fraction as F
from functools import reduce
from math import gcd, log
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
if (HERE/'general_k_average_lecture').is_dir():
    HERE=HERE/'general_k_average_lecture'
checks=[]

def record(name,scope,count=None):
    checks.append({'name':name,'scope':scope,'count':count,'result':'PASS'})

def factors(n):
    ans={}; p=2
    while p*p<=n:
        while n%p==0: ans[p]=ans.get(p,0)+1; n//=p
        p+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans

def allowed(n,k):return all(k%p==0 for p in factors(n))
def bounds(k):
    s=max(p**((a+1)//2) for p,a in factors(k).items())
    b=k+s+(not allowed(k+s,k))
    c=k+s+1
    while allowed(c,k):c+=1
    return s,b,c

expected={2:(4,5),4:(7,7),6:(9,10),8:(13,13),9:(13,13),10:(16,17),
          12:(16,17),14:(22,22),15:(21,21),16:(21,21),18:(22,22),
          20:(25,26),25:(31,31),27:(37,37),30:(36,37),32:(41,41),
          36:(40,40),42:(49,50),49:(57,57),54:(64,65),56:(64,65),
          64:(73,73),72:(77,77),81:(91,91),120:(125,126),128:(145,145)}
for k,bc in expected.items():assert bounds(k)[1:]==bc,(k,bounds(k),bc)
automatic=[(k,bounds(k)[1]) for k in range(2,201) if allowed(bounds(k)[1],k)]
assert automatic==[(2,4),(6,9),(10,16),(12,16),(20,25),(30,36),(42,49),
                  (54,64),(56,64),(75,81),(90,96),(110,121),(120,125),
                  (132,144),(138,162),(156,169),(182,196)]
record('B/C values and automatic-G list','Arithmetic only; no sufficiency inferred.',len(expected))

def avg(values,indices,k):
    assert len(indices)==k and len(set(indices))==k
    assert all(0<=i<len(values) for i in indices)
    z=sum((values[i] for i in indices),F(0))/k
    for i in indices:values[i]=z

def fixed_check(n,k,word):
    for j in range(n):
        v=[F(i==j) for i in range(n)]
        for inds in word:avg(v,inds,k)
        assert all(x==F(1,n) for x in v)

def four_word(u,r):
    k=u*r;n=k+r;h=k*r//n
    assert r%(u+1)==0
    first=list(range(k))
    second=list(range(k-r))+list(range(k,n))
    aset=sorted(set(range(n))-set(second))
    third=aset[:h]+second[:k-h]
    fourth=sorted(set(range(n))-set(third))+third[:k-r]
    return n,k,[first,second,third,fourth]

for u,r in [(1,2),(2,3),(3,4),(4,5),(5,6),(7,8),(8,9)]:
    n,k,word=four_word(u,r);fixed_check(n,k,word)
record('Four-step networks','Full standard-basis replay at seven specified parameter pairs.',7)

def dyadic_word(b):
    n=4**b;h=(n-1)//3;k=2*h
    first=list(range(k));second=list(range(h-1))+list(range(k,n))
    old=sorted(set(range(n))-set(second)); single=old[-1]
    blocks=[old[:-1],second[:h],second[h:]]
    word=[first,second];pairs=[(0,1),(1,2),(2,0)]
    for j in range(2*b-1):
        i1,i2=pairs[j%3];last=blocks[i1]+blocks[i2];word.append(last)
    word.append(sorted(set(range(n))-set(last))+last[:h-1])
    return n,k,word
for b in (1,2,3):
    n,k,word=dyadic_word(b);assert len(word)==2*b+2;fixed_check(n,k,word)
record('Dyadic network family','Full basis replay for 2/4, 10/16, 42/64.',3)

v=[F(1)]*5+[F(-1)]*5
avg(v,[0,1,2,5,6,7],6);avg(v,[3,4,8,9,0,1],6)
assert not any(v)
record('Six-average G=2 worked example','Independent two-operation replay.',1)

def mat(a,b,c,d):return ((F(a),F(b)),(F(c),F(d)))
I=mat(1,0,0,1)
def mul(A,B):return tuple(tuple(sum(A[i][h]*B[h][j] for h in range(2)) for j in range(2)) for i in range(2))
def scale(c,A):return tuple(tuple(c*x for x in row) for row in A)
def power(A,n):
    R=I
    for _ in range(n):R=mul(R,A)
    return R
def inv(A):
    a,b=A[0];c,d=A[1];return scale(1/(a*d-b*c),mat(d,-b,-c,a))
def delta(z):return mat(1,0,0,z)
def upper(z):return mat(1,z,0,1)
def lower(z):return mat(1,0,z,1)
sigma=mat(1,-1,0,-1)

for t in range(2,16):
    n=t*t+t+1
    A=mat(t,-1,0,-1);B=mat(-t-1,t,-n,t*t+t);C=mat(-t-1,1,-n,1)
    assert power(C,3)==scale(t**3,I)
    assert power(mul(C,A),2)==scale(t**3,I)
    assert mul(power(C,2),B)==scale(t**3,sigma)
    M0=mat(1,-t,n,-t*(t+1))
    for j in range(t):
        Mj=mat(1,j-t,n,(t+1)*(j-t))
        assert mul(inv(M0),Mj)==delta(F(t-j,t))
    if t%2:
        H=scale(F(1,2*t),mul(mul(delta(2),C),delta(2)))
        assert H==mat(F(-t-1,2*t),F(1,t),F(-n,t),F(2,t))
        assert mul(mul(C,delta(2)),inv(H))==scale(2*t,delta(F(1,2)))
    assert mul(mul(upper(-1),scale(F(1,t*t),C)),delta(t*t))==lower(F(-n,t*t))
record('Square-controller identities','Exact rational substitution for t=2,...,15; general proof remains in lecture/source.',14)

for m in (2,3):
    for s in range(2,14):
        k=m*s*s;r=m*s;n=k+r+1;C=mat(-r-1,1,-n,1)
        assert power(C,4 if m==2 else 6)==scale(-k**(2 if m==2 else 3),I)
        for d in (1,s,r):
            Md=mat(r*r+r-k,-r*d,r*n,-(r+k)*d)
            assert Md==mul(power(C,2),delta(d))
        Hm=scale(F(1,m*k),mul(mul(delta(m),power(C,2)),delta(m)))
        assert Hm==mat(F((m-1)*s+1,m*s),F(-1,s),F(n,s),F(-m*(s+1),s))
        if m==3:
            H2=scale(F(1,2*k*k),mul(mul(delta(2),power(C,4)),delta(2)))
            assert H2==mat(F(s+1,2*s),F(-1,s),F(n,s),-4-F(2,s))
record('Two/three square-multiple identities','Exact rational substitution at 24 parameter pairs.',24)

# New three-step formulas checked directly on the two parameter basis vectors.
for p,s in [(5,12),(5,25),(7,30)]:
    k=p*s*s;r=p*s;n=k+r+1;d=(p-1)*s+1
    for keep_u in (True,False):
        a=s-(p-1)*(p-3 if keep_u else p-2)
        b=(p-1)*s+(3 if keep_u else 2)-p
        h=p*(s-p+(3 if keep_u else 2))
        alpha=n*h-k*(r+1);beta=k*(d-b)-d*h;z=0 if keep_u else k*k
        J=mat(-r*alpha-k*k,-r*beta+z,-(r+k)*alpha-k*k,-(r+k)*beta+z)
        assert J[0][0]+J[1][1]==0
        J2=power(J,2);lam=J2[0][0]
        assert J2==scale(lam,I) and int(lam)%n==pow(k,6,n)
        for basis in ((1,0),(0,1)):
            x,y=basis;u=F(x);v=F(x-y);w=-k*u-r*v
            vals=[u]*k+[v]*r+[w];ui=list(range(k));vi=list(range(k,k+r));wi=n-1
            j=s-1;step1=ui[:k-j-1]+vi[:j]+[wi]
            avg(vals,step1,k)
            uleft=ui[k-j-1:];vleft=vi[j:]
            step2=uleft[:a]+vleft[:b]+step1[:k-a-b]
            avg(vals,step2,k)
            old=(uleft[a:] if keep_u else vleft[b:])[0]
            keep=step2[:r];step3=sorted(set(range(n))-set(keep)-{old})
            avg(vals,step3,k)
            out=(vals[step3[0]],vals[step3[0]]-vals[keep[0]])
            want=tuple(sum(J[i][j]*basis[j] for j in range(2))/k**3 for i in range(2))
            assert out==want
record('High odd-power three-step returns','Position-level replay for six templates and both parameter basis vectors; no general controllability claim.',12)

for k in (5,7,9,15):
    for a,b in [(F(1),F(0)),(F(0),F(1)),(F(6),F(8))]:
        c=((k*k-2*k+8)*a-(k*k-6*k+6)*b)/2
        d=((-k*k+k-8)*a+(k*k-7*k+6)*b)/2
        vals=[a]*k+[b]*k+[c,c,d,d]
        assert sum(vals)==0
        first=list(range(k-4))+list(range(k,k+3))+[2*k]
        avg(vals,first,k)
        assert vals[first[0]]==(k*a+(6-k)*b)/2
        second=[2*k+2,2*k+1,first[0]]+list(range(k+3,2*k))
        avg(vals,second,k)
        assert not any(vals[i] for i in second)
record('Inverse-designed zero-sum family','Twelve exact two-step replays, including composite k=9 and 15; five-step tail inherited.',12)

g={1};todo=[1]
while todo:
    x=todo.pop()
    for a in (-1,2):
        y=x*a%105
        if y not in g:g.add(y);todo.append(y)
assert len(g)==24 and sum(gcd(x,105)==1 for x in range(105))==48
assert [d for d in range(1,11) if gcd(d,105)==1]==[1,2,4,8]
assert 3*log(1000**2+1000+1)**2<573
record('Small-unit illustrations','Exact mod-105 group; numerical illustration at t=1000 (the all-t inequality is proved in text).',2)

for k,n,p,c,m in [(6,14,3,2,7),(6,22,3,2,11),(15,33,5,3,11),(15,35,3,5,7)]:
    calc=p**(factors(k)[p]-1)
    for ell in factors(k):
        if ell!=p:calc*=ell**factors(n).get(ell,0)
    assert calc==c and n==c*m and m>=2*p+1
record('Direct prime-factor substitutions','Arithmetic hypotheses for the four explicitly added examples.',4)

manifest=json.loads((HERE/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
for row in manifest:
    p=HERE/'sources'/row['path']
    assert p.stat().st_size==row['bytes']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
assert len(list((HERE/'sources/outputs/general_arity').rglob('*.md')))==27
text=(HERE/'general_k_average_lecture_single.tex').read_text(encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}',text)
assert len(labels)==len(set(labels))
for label in re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text):assert label in labels,label
for sid in re.findall(r'\\src\{(S\d+)\}',text):assert 'source:'+sid in labels,sid
assert not re.search(r'(?<![A-Za-z\\])(qquad|quad)\b',text)
assert text.count(r'\chapter{')==15 # fourteen lectures plus one source appendix
record('Package and cross-reference integrity','Snapshot hashes, all general-arity articles, source IDs and native-LaTeX references.',len(manifest))

out={'scope':'Editorial arithmetic and finite exact checks; not a new proof or a rerun of all historical verifiers.',
     'checks':checks,'automatic_B_points':automatic,'all_passed':True}
(HERE/'EDITORIAL_CHECKS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'all_passed':True,'check_groups':len(checks),'source_snapshots':len(manifest)},ensure_ascii=False))
