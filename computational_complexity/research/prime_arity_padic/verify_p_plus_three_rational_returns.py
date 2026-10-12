"""Independent symbolic, energy, and physical checks of return classification."""
from collections import Counter
from math import gcd
from pathlib import Path
from random import Random
import json

from five_eight_rank_clock import embedding,step_matrix,clock
from p_plus_three_rational_returns import (energy_matrix,analyze_return,fixed_lines,
                                         determinant,multiply,transpose)


def inspect(matrix,word,p):
    pairs=[(i,j,k) for i,j,k in ((0,1,2),(0,2,1),(1,2,0)) if matrix[i]==matrix[j]]
    if not pairs:return None
    assert len(pairs)==1
    i,j,k=pairs[0]
    M=(matrix[i],matrix[k]);t=len(word);P=p**t
    assert clock(matrix,p)==t and (M[0][0]+M[1][1])%p
    d=determinant(M);exponent=0
    while d%p==0:d//=p;exponent+=1
    assert exponent==t
    G=energy_matrix(p)
    gram=multiply(multiply(transpose(M),G),M)
    defect=tuple(tuple(P*P*G[a][b]-gram[a][b] for b in range(2)) for a in range(2))
    assert min(defect[0][0],defect[1][1],determinant(defect))>=0
    lines=fixed_lines(M)
    if all(mask in (1,2,3) for mask in word):
        assert set(lines)=={(0,1),(p+2,2)} and determinant(defect)==0
        return 'local_only'
    if all(mask==4 for mask in word):
        assert set(lines)=={(1,0),(1,p+1)} and determinant(defect)==0
        return 'outside_only'
    assert not lines and determinant(defect)>0
    return 'mixed'


def exhaustive():
    records=[]
    for p,maximum in ((5,7),(7,6),(11,6)):
        level={embedding():()};counts=Counter();matrices=0
        for t in range(1,maximum+1):
            following={}
            for matrix,word in level.items():
                for mask in range(1,7):following.setdefault(step_matrix(matrix,mask,p),word+(mask,))
            for matrix,word in following.items():
                kind=inspect(matrix,word,p)
                if kind:counts[kind]+=1
            matrices+=len(following);level=following
        records.append({'p':p,'maximum_length':maximum,'symbolic_matrices':matrices,
                        'return_classes':dict(counts)})
    return records


def literal_values(u,v,p):
    from fractions import Fraction
    a=Fraction(-2*u-v,p+3)
    return [a]*p+[a+u,a+u,a+v]


def literal_word(u,v,word,p):
    from fractions import Fraction
    # Maintain actual labelled positions and generic groups; no parameter
    # matrix formula is used to compute the physical values.
    values=literal_values(u,v,p)
    common=list(range(p));exceptions=[p,p+1,p+2]
    initial_energy=sum(x*x for x in values)
    for mask in word:
        chosen_ex=[i for i in range(3) if mask>>i&1]
        chosen_common=common[:p-len(chosen_ex)]
        selected=chosen_common+[exceptions[i] for i in chosen_ex]
        mean=sum(values[i] for i in selected)/p
        for i in selected:values[i]=mean
        leftover_common=common[p-len(chosen_ex):]
        cursor=0
        for i in chosen_ex:
            exceptions[i]=leftover_common[cursor];cursor+=1
        common=selected
    result=tuple(values[exceptions[i]]-values[common[0]] for i in range(3))
    assert sum(x*x for x in values)<=initial_energy and sum(values)==0
    return result


def random_and_physical():
    rng=Random(20261015);count=0;return_count=0
    for p in (5,7,11,31):
        for _ in range(250):
            word=tuple(rng.randrange(1,7) for _ in range(rng.randrange(1,41)))
            M=embedding()
            for mask in word:M=step_matrix(M,mask,p)
            kind=inspect(M,word,p)
            if kind:return_count+=1
            u,v=rng.randrange(-100,101),rng.randrange(-100,101)
            actual=literal_word(u,v,word,p)
            from fractions import Fraction
            expected=tuple(Fraction(row[0]*u+row[1]*v,p**len(word)) for row in M)
            assert actual==expected
            count+=1
    long=[]
    for p in (5,7):
        for word in ((4,)*500,(1,3)*200,(1,4,5,4,2,6)*50):
            answer=analyze_return(word,p)
            assert answer['is_return']
            long.append({'p':p,'length':len(word),'kind':answer['kind'],
                         'matrix_height_bits':max(abs(x) for row in answer['matrix'] for x in row).bit_length()})
    return {'literal_physical_words':count,'return_words':return_count,'long_return_words':long}


def main():
    record={'scope':'All-length proof of rational fixed-direction classification for proper three-value returns. This is not full averaging complexity classification.',
            'exhaustive':exhaustive(),'random_and_long':random_and_physical()}
    destination=Path(__file__).with_name('p_plus_three_rational_returns_verification.json')
    destination.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
