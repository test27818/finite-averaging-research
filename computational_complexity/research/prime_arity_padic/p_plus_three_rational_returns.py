"""Rational-direction classification for arbitrary proper three-value returns.

Assumes a fixed prime p>=5. This classifies a GIVEN symbolic return word;
it is not a P/NP-hard classification of averaging reachability.
"""
from math import isqrt
from five_eight_rank_clock import embedding,step_matrix,clock,primitive


def energy_matrix(p=5):
    # (p+3) times physical squared energy in coordinates (u,u,v).
    return ((2*(p+1),-2),(-2,p+2))


def multiply(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(zip(*a))


def determinant(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def fixed_lines(matrix):
    a,b=matrix[0];c,d=matrix[1]
    delta=(a-d)**2+4*b*c
    if delta<0 or isqrt(delta)**2!=delta:
        return ()
    square=isqrt(delta)
    lines=set()
    for sign in (-1,1):
        vector=(2*b,d-a+sign*square)
        if not any(vector):vector=(a-d+sign*square,2*c)
        if any(vector):lines.add(primitive(vector))
    return tuple(sorted(lines))


def analyze_return(word,p=5):
    word=tuple(word)
    if not word or p<5:
        raise ValueError('a nonempty proper word and a prime p>=5 are required')
    matrix=embedding()
    for mask in word:matrix=step_matrix(matrix,mask,p)
    if clock(matrix,p)!=len(word):
        raise AssertionError('symbolic p-adic clock failed')
    matches=[(i,j,k) for i,j,k in ((0,1,2),(0,2,1),(1,2,0)) if matrix[i]==matrix[j]]
    if not matches:
        return {'is_return':False,'symbolic_matrix':matrix}
    assert len(matches)==1
    i,j,k=matches[0]
    reduced=(matrix[i],matrix[k])
    power=p**len(word)
    G=energy_matrix(p)
    gram=multiply(multiply(transpose(reduced),G),reduced)
    defect=tuple(tuple(power*power*G[a][b]-gram[a][b] for b in range(2)) for a in range(2))
    assert defect[0][0]>=0 and defect[1][1]>=0 and determinant(defect)>=0
    lines=fixed_lines(reduced)
    if all(mask in (1,2,3) for mask in word):
        kind='local_only'
        expected=tuple(sorted(((0,1),(p+2,2))))
        assert (i,j)==(0,1) and lines==expected and determinant(defect)==0
    elif all(mask==4 for mask in word):
        kind='outside_only'
        expected=tuple(sorted(((1,0),(1,p+1))))
        assert (i,j)==(0,1) and lines==expected and determinant(defect)==0
    else:
        kind='mixed'
        assert not lines and determinant(defect)>0
    return {'is_return':True,'kind':kind,'pair':(i,j),'matrix':reduced,
            'length':len(word),'energy_defect':defect,'rational_fixed_lines':lines}
