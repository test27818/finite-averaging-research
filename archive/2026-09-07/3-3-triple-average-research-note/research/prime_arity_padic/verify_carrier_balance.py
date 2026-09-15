"""Exact bounded checks of the all-arity entrance and single-carrier rigidity.

No macro search. The full entrance is replayed on original labelled positions,
with finite-modulus inverses compiled into actual forward exchanges.
"""
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
import json
import random

HERE=Path(__file__).resolve().parent
from verify_square_zero_compiler import check_frozen_files,check_local_links


def primes_of(n):
    result=[];ell=2
    while ell*ell<=n:
        if n%ell==0:
            result.append(ell)
            while n%ell==0:n//=ell
        ell+=1
    if n>1:result.append(n)
    return result


def res(x,m):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,m)%m


def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def identity(d):
    return [[F(i==j) for j in range(d)] for i in range(d)]


def det(A):
    M=[list(map(F,row)) for row in A];value=F(1)
    for j in range(len(M)):
        hit=next((i for i in range(j,len(M)) if M[i][j]),None)
        if hit is None:return F(0)
        if hit!=j:M[j],M[hit]=M[hit],M[j];value=-value
        pivot=M[j][j];value*=pivot
        for i in range(j+1,len(M)):
            multiple=M[i][j]/pivot
            M[i]=[a-multiple*b for a,b in zip(M[i],M[j])]
    return value


def star(k,m,i):
    M=identity(m)
    for j in range(m):M[j][i]=-F(1,k)
    return M


def star_inverse(k,m,i):
    M=identity(m)
    for j in range(m):M[j][i]-=1
    M[i][i]-=k
    return M


def rigidity_checks():
    count=0
    for p in (2,3,5,11):
        for m in (2,3,5):
            W=identity(m);inverse=identity(m)
            indices=[(j*j+j//2)%m for j in range(1,13)]
            for length,i in enumerate(indices,1):
                A=star(p,m,i);Ai=star_inverse(p,m,i)
                assert mm(A,Ai)==identity(m)
                W=mm(A,W);inverse=mm(inverse,Ai)
                assert mm(W,inverse)==identity(m)
                assert all(x.denominator==1 for row in inverse for x in row)
                leading=[[res(p**length*x,p) for x in row] for row in W]
                expected=[[((-1)**length)%p if j==indices[0] else 0
                           for j in range(m)] for _ in range(m)]
                assert leading==expected
                assert det(W)==(-F(1,p))**length
                assert res(p**length*sum(W[j][j] for j in range(m)),p)!=0
                count+=1
    return count


def multirole_checks():
    count=0
    rng=random.Random(937)
    for k in (2,3,4,5,6,10):
        for m in (k+1,k+3):
            for t in range(1,k+1):
                chosen=list(range(t))
                delta=[F(rng.randrange(-10,11)) for _ in range(m)]
                a=F(rng.randrange(-5,6))
                avg=a+sum(delta[i] for i in chosen)/k
                expected=[a-avg if j in chosen else a+delta[j]-avg for j in range(m)]
                s=sum(delta[j] for j in chosen)
                formula=[-s/k if j in chosen else delta[j]-s/k for j in range(m)]
                assert formula==expected
                for ell in (2,3,5,7):
                    if k%ell==0:continue
                    mod_delta=[rng.randrange(ell) for _ in range(m-1)]
                    mod_delta.append(-sum(mod_delta)%ell)
                    residue_sum=sum(mod_delta[i] for i in chosen)%ell
                    output=[(-residue_sum*pow(k,-1,ell))%ell if j in chosen
                            else (mod_delta[j]-residue_sum*pow(k,-1,ell))%ell
                            for j in range(m)]
                    support_outside=any(mod_delta[j] for j in range(t,m))
                    assert any(output)==support_outside
                    count+=1
    return count


def exchange_order(k,ell):
    inv=pow(k,-1,ell);A=((k-1)*inv%ell,inv,1,0)
    current=(1,0,0,1)
    def product(a,b):
        return ((a[0]*b[0]+a[1]*b[2])%ell,(a[0]*b[1]+a[1]*b[3])%ell,
                (a[2]*b[0]+a[3]*b[2])%ell,(a[2]*b[1]+a[3]*b[3])%ell)
    # Eigenvalues1 and -1/k: order divides ell*(ell-1).
    for j in range(1,ell*(ell-1)+1):
        current=product(A,current)
        if current==(1,0,0,1):return j
    raise AssertionError('No finite exchange order')


def safe_entrance(k,initial):
    n=len(initial);r=n-2*k;m=n-k
    P=[ell for ell in primes_of(n) if k%ell]
    values=list(map(F,initial));words=[];repairs=0
    def complete():
        return all(len({res(x,ell) for x in values})>1 for ell in P)
    assert sum(values)==0 and r>=1 and complete()
    def average(indices):
        assert len(indices)==k and len(set(indices))==k
        avg=sum(values[j] for j in indices)/k
        for j in indices:values[j]=avg
        words.append(tuple(indices))
        assert sum(values)==0 and complete()

    protected={0}
    for ell in P:
        protected.add(next(j for j in range(n) if res(values[j]-values[0],ell)))
    anchor=[j for j in range(n) if j not in protected][:k]
    assert len(anchor)==k
    average(anchor)
    roles=[j for j in range(n) if j not in anchor]
    def deltas():
        return [values[j]-values[anchor[0]] for j in roles]
    B=[ell for ell in P if (k-1)%ell==0]
    J={next(i for i,x in enumerate(deltas()) if res(x,ell)) for ell in B}
    for i in range(m):
        if len(J)==r:break
        J.add(i)
    assert len(J)==r
    j=min(J)
    L=lcm(*(exchange_order(k,ell) for ell in P)) if P else 1
    good=[ell for ell in P if ell not in B]
    def exchange(i):
        nonlocal anchor
        old_anchor=anchor[-1]
        selected=anchor[:-1]+[roles[i]]
        average(selected)
        anchor=selected
        roles[i]=old_anchor
        assert len(anchor)==k and len(set(anchor+roles))==n
        assert all(values[u]==values[anchor[0]] for u in anchor)
    for ell in good:
        if res(deltas()[j],ell):continue
        before=deltas()
        i=next(i for i,x in enumerate(before) if i!=j and res(x,ell))
        other=next(i0 for i0 in range(m) if i0 not in (i,j))
        mod=1
        for q in good:mod*=q
        N=mod//ell;t=N*pow(N,-1,ell)%mod
        for _ in range(t):
            for role,times in ((i,L-1),(other,1),(j,L-1),(other,L-1),
                               (i,1),(other,1),(j,1),(other,L-1)):
                for _ in range(times):exchange(role)
        after=deltas();coeff=F(k-1,k)*t
        for q in P:
            for z in range(m):
                expected=before[z]-coeff*before[i] if z==j else (
                    before[z]+coeff*before[i] if z==other else before[z])
                assert res(after[z]-expected,q)==0
        repairs+=1
    assert all(any(res(deltas()[i],ell) for i in J) for ell in P)
    second=[roles[i] for i in range(m) if i not in J]
    average(second)
    assert len(second)==k and not set(second)&set(anchor)
    assert all(values[u]==values[anchor[0]] for u in anchor)
    assert all(values[u]==values[second[0]] for u in second)
    # Independently replay just the physical index list.
    replay=list(map(F,initial))
    for word in words:
        avg=sum(replay[i] for i in word)/k
        for i in word:replay[i]=avg
    assert replay==values
    return len(words),repairs


def entrance_checks():
    rng=random.Random(2057);count=repairs=atoms=noncoprime=0;longest=0
    pairs=((2,5),(2,6),(2,7),(3,7),(3,8),(3,9),(3,10),(3,12),
           (4,9),(4,10),(4,11),(4,12),(4,15),(5,11),(5,12),(5,15),
           (5,16),(6,13),(6,14),(6,15),(6,16),(6,18),(10,21),(10,24))
    for k,n in pairs:
        for trial in range(6):
            raw=[rng.randrange(-8,9) for _ in range(n-3)]+[0,1]
            raw.append(-sum(raw))
            length,patched=safe_entrance(k,raw)
            count+=1;atoms+=length;repairs+=patched;longest=max(longest,length)
            noncoprime+=gcd(k,n)>1
    assert repairs>0 and noncoprime>0
    return dict(cases=count,noncoprime_cases=noncoprime,
                commutator_repair_stages=repairs,atoms_replayed=atoms,longest=longest)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    result={'status':'PASS','single_carrier_prefixes':rigidity_checks(),
            'multi_role_formula_and_support_checks':multirole_checks(),
            'full_original_position_entrance':entrance_checks(),
            'unchanged_existing_documents':check_frozen_files(),
            'scope':'Exact finite checks of carrier inverses/first symbol/determinant, multi-role support criterion, and full labelled entrance including composite arity and noncoprime dimensions. All-parameter theorems are proved in accompanying text. No complete core termination claim.'}
    (HERE/'carrier_balance_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
