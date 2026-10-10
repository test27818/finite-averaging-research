"""Exact history precision compiler; all prefixes, no primitive rescaling.

Uses one mod-p constraint per atom and independent Fraction replay. No word
search, orbit enumeration, floating point, or external algebra library.
"""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import argparse
import json
import random
from verify_critical_endpoint_precision_return import parameters

HERE=Path(__file__).resolve().parent
RECORD=HERE/'history_lattices_verification.json'


def identity(d):
    return [[int(i==j) for j in range(d)] for i in range(d)]


def multiply(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)]
            for row in A]


def inverse(A):
    d=len(A)
    M=[[F(x) for x in row]+list(map(F,tail))
       for row,tail in zip(A,identity(d))]
    for k in range(d):
        pivot=next(i for i in range(k,d) if M[i][k])
        M[k],M[pivot]=M[pivot],M[k]
        a=M[k][k]
        M[k]=[x/a for x in M[k]]
        for i in range(d):
            if i!=k:
                a=M[i][k]
                M[i]=[x-a*y for x,y in zip(M[i],M[k])]
    return [row[d:] for row in M]


def valuation(x,p):
    x=F(x)
    if not x:
        return 10**9
    num,den=x.numerator,x.denominator
    answer=0
    while num % p==0:
        num//=p
        answer+=1
    while den % p==0:
        den//=p
        answer-=1
    return answer


def local_smith_exponents(A,p):
    M=[[F(x) for x in row] for row in A]
    out=[]
    while M:
        _,i,j=min((valuation(x,p),i,j) for i,row in enumerate(M)
                  for j,x in enumerate(row) if x)
        M[0],M[i]=M[i],M[0]
        for row in M:
            row[0],row[j]=row[j],row[0]
        pivot=M[0][0]
        out.append(valuation(pivot,p))
        M=[[M[i][j]-M[i][0]*M[0][j]/pivot
            for j in range(1,len(M))] for i in range(1,len(M))]
    assert out==sorted(out)
    return out


def kernel_update(B,Z,h,p):
    pivot=next(j for j,x in enumerate(h) if x%p)
    inv=pow(h[pivot],-1,p)
    factors=[x*inv%p for x in h]
    for matrix in (B,Z):
        for row in matrix:
            a=row[pivot]
            for j in range(len(row)):
                if j!=pivot:
                    row[j]-=factors[j]*a
            row[pivot]=p*a


def compile_lattice(E,word,p,budget=0,integer_finish=False):
    d=len(E[0])
    B=identity(d)
    Z=[[p**budget*x for x in row] for row in E]
    increments=[]
    for selected in word:
        assert len(selected)==p and len(set(selected))==p
        h=[sum(Z[i][j] for i in selected) for j in range(d)]
        if any(x%p for x in h):
            kernel_update(B,Z,h,p)
            increments.append(1)
        else:
            increments.append(0)
        totals=[sum(Z[i][j] for i in selected) for j in range(d)]
        assert all(x%p==0 for x in totals)
        mean=[x//p for x in totals]
        for i in selected:
            Z[i]=mean.copy()
    end_restrictions=0
    if integer_finish and budget:
        target=p**budget
        for i in range(len(Z)):
            while any(x%target for x in Z[i]):
                order=min(valuation(x,p) for x in Z[i])
                assert 0<=order<budget
                h=[x//(p**order) for x in Z[i]]
                kernel_update(B,Z,h,p)
                end_restrictions+=1
    exponents=local_smith_exponents(B,p)
    assert sum(exponents)==sum(increments)+end_restrictions
    return {'basis':B,'exponents':exponents,'increments':increments,
            'finish_restrictions':end_restrictions}


def belongs(Binv,x,p):
    return all(valuation(sum(a*b for a,b in zip(row,x)),p)>=0
               for row in Binv)


def lattice_subset(B,C,p):
    return all(valuation(x,p)>=0 for row in multiply(inverse(C),B) for x in row)


def replay(E,word,x,p):
    current=[sum(F(a)*b for a,b in zip(row,x)) for row in E]
    max_depth=max(0,max(-valuation(z,p) for z in current))
    for selected in word:
        mean=sum(current[i] for i in selected)/p
        for i in selected:
            current[i]=mean
        max_depth=max(max_depth,max(-valuation(z,p) for z in current))
    return max_depth,current


def operator(E,word,p):
    n,d=len(E),len(E[0])
    M=[[F(x) for x in row] for row in E]
    for selected in word:
        mean=[sum(M[i][j] for i in selected)/p for j in range(d)]
        for i in selected:
            M[i]=mean.copy()
    return M


def zero_sum_embedding(n):
    return identity(n-1)+[[-1]*(n-1)]


def core_embedding(p,r=1):
    return [[1,0] for _ in range(p)]+[[-1,r] for _ in range(p)]+[[0,-p] for _ in range(r)]


def two_block_embedding(p,first,second,single):
    E=[[0,0] for _ in range(2*p+1)]
    for i in first:
        E[i]=[1,0]
    for i in second:
        E[i]=[0,1]
    E[single]=[-p,-p]
    return E


def six_positions(a):
    p=6*a-1
    ones=list(range(p+2))
    twos=list(range(p+2,2*p))
    neg=2*p
    first=[neg]+ones[:3*a]+twos[:3*a-2]
    second=ones[3*a:6*a]+twos[3*a-2:]
    single=ones[-1]
    third=first[:3*a-1]+second[:3*a]
    U=first[3*a-1:]
    V=second[3*a:]
    fourth=U[:a]+V[:a-1]+third[:4*a-1]+[single]
    rem_U,rem_V,rem_D=U[a:],V[a-1:],third[4*a-1:]
    fifth=rem_U[:a]+rem_V[:a]+rem_D[:a]+fourth[:3*a-1]
    sixth=rem_U[a:]+rem_V[a:]+rem_D[a:]+fourth[3*a-1:6*a-2]
    assert all(len(s)==p and len(set(s))==p for s in [first,second,third,fourth,fifth,sixth])
    return [first,second,third,fourth,fifth,sixth],single


def five_cleanup_positions(p):
    u,v,k,l=parameters(p)
    q=k+l
    first,second=list(range(p)),list(range(p,2*p))
    third=first[:p-u]+second[:p-v]+[2*p]
    U,V=first[p-u:],second[p-v:]
    fourth=U[:k]+V[:l]+third[:p-q]
    fifth=U[k:]+V[l:]+third[p-q:p-2]+fourth[:1]
    assert len(fifth)==p
    return [third,fourth,fifth]


def G_of(values,p):
    if not any(values):
        return 1
    den=max(x.denominator for x in values)
    nums=[int(x*den) for x in values]
    content=gcd(*nums)
    return gcd(*(x-nums[0] for x in nums))//content


def general_compiler_checks():
    rng=random.Random(7302026)
    words=points=0
    samples=[]
    for p in (2,3,5):
        n=2*p+1
        E=core_embedding(p)
        for length in range(1,7):
            word=[sorted(rng.sample(range(n),p)) for _ in range(length)]
            L0=compile_lattice(E,word,p)
            for e in (0,1,2):
                compiled=compile_lattice(E,word,p,e)
                expected=[max(a-e,0) for a in L0['exponents']]
                assert compiled['exponents']==expected
                Binv=inverse(compiled['basis'])
                finishing=compile_lattice(E,word,p,e,True)
                Cinv=inverse(finishing['basis'])
                assert lattice_subset(finishing['basis'],compiled['basis'],p)
                candidates=[[rng.randint(-p**5,p**5) for _ in range(2)] for _ in range(35)]
                for B in (compiled['basis'],finishing['basis']):
                    candidates += [[sum(row[j]*rng.randint(-3,3) for j in range(2)) for row in B]
                                   for _ in range(8)]
                    for _ in range(8):
                        z=[rng.randint(-3,3) for _ in range(2)]
                        candidates.append([sum(a*b for a,b in zip(row,z)) for row in B])
                for x in candidates:
                    depth,final=replay(E,word,x,p)
                    assert belongs(Binv,x,p)==(depth<=e)
                    assert belongs(Cinv,x,p)==(depth<=e and all(y.denominator==1 for y in final))
                    points+=1
                words+=1
            samples.append({'p':p,'length':length,'L0':L0['exponents']})
    return {'compiled_budget_domains':words,'direct_input_checks':points,'samples':samples}


def same_operator_checks():
    out=[]
    for p in (2,3,5):
        n=p*p
        rows=[list(range(i*p,(i+1)*p)) for i in range(p)]
        cols=[[i*p+j for i in range(p)] for j in range(p)]
        R,C=rows+cols,cols+rows
        E=zero_sum_embedding(n)
        A,B=compile_lattice(E,R,p),compile_lattice(E,C,p)
        assert sum(A['exponents'])==sum(B['exponents'])==p-1
        assert max(A['exponents'])==max(B['exponents'])==1
        assert not lattice_subset(A['basis'],B['basis'],p)
        assert not lattice_subset(B['basis'],A['basis'],p)
        full=operator(identity(n),R,p)
        assert full==operator(identity(n),C,p)==[[F(1,n)]*n for _ in range(n)]
        x=[0]*(n-1)
        x[0],x[1]=1,-1
        assert replay(E,R,x,p)[0]==0
        assert replay(E,C,x,p)[0]==1
        out.append({'p':p,'lattice_index_exponent':p-1,'same_final_operator':True,'incomparable_domains':True})
    return out


def six_rank_and_perturbation_checks():
    out=[]
    for a in (1,2,3,4,5,7):
        p=6*a-1
        # All listed p are primes; no primality hypothesis is needed for the identities.
        word,single=six_positions(a)
        E=two_block_embedding(p,word[0],word[1],single)
        M=operator(E,word[2:],p)
        common=[F(a*(9*a-2),p**3),F(a*(9*a-1),p**3)]
        expected=sorted([common]* (2*p)+[[-2*p*x for x in common]])
        assert sorted(M)==expected
        precision=compile_lattice(E,word[2:],p)
        assert precision['exponents']==[0,3]
        original=[1]*(p+2)+[2]*(p-2)+[2-3*p]
        assert replay(identity(2*p+1),word,original,p)[0]==1
        assert not any(replay(identity(2*p+1),word,original,p)[1])
        for m in (4,5,8):
            t=(2*p+1)*p**m
            x=original.copy()
            i=next(i for i in word[0] if original[i]==1)
            j=next(i for i in word[1] if original[i]==1)
            x[i]+=t
            x[j]-=t
            assert G_of(list(map(F,x)),p)==1
            used_depth,final=replay(identity(2*p+1),word,x,p)
            assert used_depth==1
            # After the initial pair, generic safety lasts until the final atom.
            for prefix in range(2,6):
                _,middle=replay(identity(2*p+1),word[:prefix],x,p)
                assert G_of(middle,p)==1
            assert all(v.denominator==1 for v in final)
            assert G_of(final,p)==2*p+1
        out.append({'p':p,'cleanup_history_exponents':precision['exponents'],
                    'same_word_bad_perturbations':[4,5,8]})
    return out


def five_lattice_checks():
    results=[]
    for p in (7,11,13,17,19,23):
        E=two_block_embedding(p,list(range(p)),list(range(p,2*p)),2*p)
        word=five_cleanup_positions(p)
        M=operator(E,word,p)
        assert any(M[i][0]*M[j][1]-M[i][1]*M[j][0]
                   for i in range(len(M)) for j in range(i))
        L=compile_lattice(E,word,p)
        assert L['exponents']==[0,3]
        results.append({'p':p,'cleanup_history_exponents':L['exponents']})
    return results


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    result={'status':'PASS','general_compiler':general_compiler_checks(),
            'same_operator_different_history':same_operator_checks(),
            'six_step_rank_and_perturbations':six_rank_and_perturbation_checks(),
            'five_step_history_lattices':five_lattice_checks(),
            'scope':'Exact prefix-lattice computation and independent physical replay; no global coverage, new threshold or arbitrary-input precision theorem.'}
    if args.write:
        RECORD.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    elif RECORD.exists():
        assert result==json.loads(RECORD.read_text(encoding='utf-8'))
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':
    main()
