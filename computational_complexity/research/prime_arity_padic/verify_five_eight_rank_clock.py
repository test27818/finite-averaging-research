"""Exact symbolic audits of rank stabilization and p-adic word clocks."""
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
import json

from five_eight_rank_clock import (embedding,step_matrix,wedge,clock,primitive,
                                  plane_update,decode_plane,kernel_row,strip_singleton)
from verify_subcritical_uniform_np_hard import integer_oracle,primitive as primitive_state


def scalar_matrix_step(matrix,mask,p):
    # Derive each new difference from a literal rational p-position average.
    from fractions import Fraction
    answer=[]
    for column in range(len(matrix[0])):
        u=[row[column] for row in matrix]
        a=Fraction(-sum(u),p+3)
        chosen=[a]*(p-mask.bit_count())+[a+u[i] for i in range(3) if mask>>i&1]
        common=sum(chosen)/p
        leftovers=[a if mask>>i&1 else a+u[i] for i in range(3)]
        differences=tuple(p*(x-common) for x in leftovers)
        assert all(x.denominator==1 for x in differences)
        answer.append(tuple(int(x) for x in differences))
    return tuple(tuple(answer[j][i] for j in range(len(answer))) for i in range(3))


def suffix_descriptor(word):
    pair=(0,1)
    tail=[]
    for mask in word:
        if mask.bit_count()==2:
            pair=tuple(i for i in range(3) if mask>>i&1)
            tail=[]
        else:
            tail.append(mask.bit_length()-1)
    missing=next(i for i in range(3) if i not in pair)
    while tail and tail[0]==missing:
        tail.pop(0)
    return pair,tuple(tail)


def all_symbolic_words():
    records=[]
    for p in (5,7,11):
        level={embedding():()}
        checks=0
        for length in range(1,7):
            following={}
            for matrix,word in level.items():
                for mask in range(1,7):
                    child=step_matrix(matrix,mask,p)
                    following.setdefault(child,word+(mask,))
            for matrix,word in following.items():
                assert clock(matrix,p)==length
                assert all(tuple(x%p for x in row)==tuple(x%p for x in matrix[0]) for row in matrix)
                assert any(x%p for x in matrix[0])
                normal=primitive(wedge(matrix))
                decoded=decode_plane(normal,p)
                assert decoded is not None
                assert (decoded['pair'],decoded['word'])==suffix_descriptor(word)
                peeled=matrix
                for i in reversed(decoded['word']):
                    peeled=strip_singleton(peeled,i,p)
                    assert peeled is not None
                i,j=decoded['pair']
                assert peeled[i]==peeled[j]
                checks+=1
            level=following
        records.append({'p':p,'distinct_symbolic_prefix_matrices_checked':checks,
                        'matrices_at_length_six':len(level)})
    return records


def random_checks():
    rng=Random(20261013)
    literal=0
    for p in (5,7,11,31):
        for _ in range(100):
            pair=rng.choice(((0,1),(0,2),(1,2)))
            matrix=embedding(pair)
            for length in range(1,26):
                mask=rng.randrange(1,7)
                raw=step_matrix(matrix,mask,p)
                assert scalar_matrix_step(matrix,mask,p)==raw
                assert clock(raw,p)==length
                old_kernel=kernel_row(matrix,p)
                new_kernel=kernel_row(raw,p)
                if length>1:
                    old_row=old_kernel['row'];new_row=new_kernel['row'];mod=old_kernel['modulus']
                    assert (old_row[0]*new_row[1]-old_row[1]*new_row[0])%mod==0
                matrix=raw;literal+=1
    long=[]
    for p in (5,7):
        for word in ((2,)*300+(0,)*1000+(1,)*500,
                     tuple(rng.randrange(3) for _ in range(2000))):
            normal=(1,-1,0)
            for i in word:normal=plane_update(normal,i,p)
            decoded=decode_plane(normal,p)
            expected=list(word)
            while expected and expected[0]==2:expected.pop(0)
            assert decoded['word']==tuple(expected)
            long.append({'p':p,'given_letters':len(word),'nonstationary_letters':len(expected),
                         'normal_height_bits':max(map(abs,normal)).bit_length(),
                         'decoded_runs':len(decoded['runs'])})
    return {'literal_column_replays':literal,'long_plane_decodings':long}


def audit_plane_membership():
    from collections import deque
    bound=20;records=[]
    for p in (5,7):
        roots=[primitive(tuple(1 if k==i else -1 if k==j else 0 for k in range(3)))
               for i,j in ((0,1),(0,2),(1,2))]
        orbit=set(roots);queue=deque(roots)
        while queue:
            g=queue.popleft()
            for i in range(3):
                child=primitive(plane_update(g,i,p))
                if max(map(abs,child))<=bound and child not in orbit:
                    orbit.add(child);queue.append(child)
        queries=0
        for raw in product(range(-bound,bound+1),repeat=3):
            normalized=primitive(raw)
            answer=decode_plane(raw,p)
            assert (answer is not None)==(normalized in orbit),(p,raw,answer)
            if answer is not None:
                i,j=answer['pair']
                g=tuple(1 if k==i else -1 if k==j else 0 for k in range(3))
                for letter in answer['word']:g=plane_update(g,letter,p)
                assert primitive(g)==normalized
            queries+=1
        records.append({'p':p,'height_bound':bound,'plane_candidates':queries,
                        'projective_orbit_planes':len(orbit)})
    return records


def audit_global_kernel():
    rng=Random(20261014);checked=0
    def determinant(m):
        a,b,c=m
        return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
    def cross(a,b):
        return a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]
    for p in (5,7,11):
        for _ in range(100):
            matrix=((1,0,0),(0,1,0),(0,0,1));kernel=None
            for _ in range(60):
                mask=rng.randrange(1,7)
                matrix=step_matrix(matrix,mask,p)
                if kernel is None and mask.bit_count()==1:
                    assert determinant(matrix)!=0
                    continue
                assert determinant(matrix)==0
                candidates=[cross(matrix[i],matrix[j]) for i,j in ((0,1),(0,2),(1,2))]
                found=primitive(next(v for v in candidates if any(v)))
                if kernel is None:kernel=found
                assert found==kernel
                assert all(sum(a*b for a,b in zip(row,kernel))==0 for row in matrix)
                checked+=1
    return {'rank_two_kernel_checks':checked,'full_words':300}


def kernel_fiber_counterexample():
    # Same source, same four-step clock, same integrality kernel; opposite
    # global outcomes. Reuse the independently audited earliest-exit source.
    p=5;initial_pair=(125,-274)
    rows=[]
    edge,distance=integer_oracle(5,8)
    for word in ((1,1,1,4),(1,2,2,4)):
        matrix=embedding()
        for mask in word:matrix=step_matrix(matrix,mask,p)
        values=tuple(sum(a*b for a,b in zip(row,initial_pair)) for row in matrix)
        assert all(x%p**len(word)==0 for x in values)
        u=tuple(x//p**len(word) for x in values)
        a=-sum(u)//8
        physical=tuple(sorted((a,)*5+tuple(a+x for x in u)))
        result=distance(primitive_state(physical))
        rows.append({'word':word,'matrix':matrix,'kernel':kernel_row(matrix,p),
                     'endpoint':physical,'full_distance':result})
    assert rows[0]['kernel']==rows[1]['kernel']
    assert [r['full_distance'] for r in rows]==[None,6]
    return {'rows':rows,'independent_oracle_states':distance.cache_info().currsize}


def main():
    record={'scope':'All-word rank and p-adic clock structure, not full P or NP-hardness.',
            'exhaustive':all_symbolic_words(),'random_and_long':random_checks(),
            'plane_membership':audit_plane_membership(),'global_kernel':audit_global_kernel(),
            'same_kernel_different_outcome':kernel_fiber_counterexample()}
    out=Path(__file__).with_name('five_eight_rank_clock_verification.json')
    out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
