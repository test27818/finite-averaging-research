"""Exact original-position roots from formula-selected output exchanges.

No word or orbit search. Existing documents and registries are read only.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from square_zero_compiler import multiply,inverse,determinant
from verify_square_zero_compiler import check_frozen_files,check_local_links
from verify_uniform_even_carrier_inverse import prime

HERE=Path(__file__).resolve().parent


def general_formula_checks():
    count=0
    for p in (5,7,11,17,31):
        for t in range(2,p,2):
            s=t//2;alpha=int(s%2==0);m=p+t;d=p*t-m*s
            W0=tuple(F(x,p*p) for x in (-d,-alpha,-alpha*p*m,p*s))
            delta=-p*(d*s+alpha*alpha*m)
            for e in (-1,1):
                We=tuple(F(x,p*p) for x in
                         (-d,-alpha,-alpha*p*m+e*m*(p-s),p*s+e*alpha))
                quotient=multiply(We,inverse(W0))
                expected=(1,0,F(e*p*m*(s*(p-s)+alpha*alpha),delta),
                          1+F(e*alpha*p*p,delta))
                assert quotient==expected
                if alpha==0:assert determinant(quotient)==1
                else:assert determinant(quotient)!=1
                count+=1
    return count


def literal_root(p,t,e,u,v):
    assert t%4==2 and p>t and e in (-1,1)
    s=t//2;m=p+t;c=p-t;d=s*c
    q=-F(e*m*(p-s),s*c)
    scalar=F(d*d,p**4)
    values=[F(t*u+v)]*p+[F(t*u-v)]*p+[F(-p*u)]*(2*t)
    initial=values[:];n=len(values);words=[]
    groups=(list(range(p)),list(range(p,2*p)),list(range(2*p,n)))
    def average(indices):
        assert len(indices)==p and len(set(indices))==p
        value=sum(values[i] for i in indices)/p
        for i in indices:values[i]=value
        words.append(tuple(indices))
        assert sum(values)==0
    def mix(groups):
        ga,gb,gc=groups;k=(p+c)//2
        left=ga[:k]+gb[:p-k];right=ga[k:]+gb[p-k:]
        average(left);average(right)
        return left,right,gc
    def rebuild(groups,shift):
        ga,gb,gc=groups;k=(p-s)//2
        first=ga[:k]+gb[:k]+gc[:s]
        second=ga[k:2*k]+gb[k:2*k]+gc[s:2*s]
        average(first);average(second)
        ga=ga[2*k:];gb=gb[2*k:];gc=gc[2*s:]
        fresh=first+second;kept=fresh[:2*t];fresh=fresh[2*t:]
        z=s-shift;w=p-t+shift
        assert 0<=z<=2*s and 0<=w<=2*(p-t)
        left=ga+gc[:z]+fresh[:w]
        right=gb+gc[z:]+fresh[w:]
        assert sorted(left+right+kept)==list(range(n))
        average(left);average(right)
        return left,right,kept

    # F,W0,F = scalar * W0^-1, followed by We.
    groups=mix(groups)
    groups=rebuild(groups,0)
    groups=mix(groups)
    groups=rebuild(groups,e)
    assert len(words)==12
    expected_u=scalar*u;expected_v=scalar*(v+q*u)
    for indices,wanted in zip(groups,(t*expected_u+expected_v,
                                      t*expected_u-expected_v,-p*expected_u)):
        assert all(values[i]==wanted for i in indices)
    replay=initial[:]
    for indices in words:
        value=sum(replay[i] for i in indices)/p
        for i in indices:replay[i]=value
    assert values==replay
    return len(words)


def main():
    if not __debug__:raise RuntimeError('Assertions required')
    pairs=replays=atoms=0
    for p in [p for p in range(3,61,2) if prime(p)]:
        for t in range(2,p,4):
            pairs+=1
            for e in (-1,1):
                for u,v in ((F(1),F(0)),(F(0),F(1)),(F(3,5),F(-7,3))):
                    atoms+=literal_root(p,t,e,u,v);replays+=1
    result={'status':'PASS',
            'general_root_or_affine_identities':general_formula_checks(),
            'root_parameter_pairs':pairs,
            'signed_twelve_atom_root_replays':replays,
            'atomic_steps_replayed':atoms,
            'unchanged_existing_documents':check_frozen_files(),
            'scope':'Exact finite formula and original-position checks for t=2 mod4, both root signs, basis and mixed rational inputs. The unbounded root-family claim follows from the written identities and Laurent multiplier ring argument. Other t, transverse roots, full ideal/terminal coverage remain unproved by this work.'}
    (HERE/'output_exchange_roots_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
