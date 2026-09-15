"""Exact B_p-subspace conformality of punctured Reynolds round trips."""
from fractions import Fraction as F
from math import isqrt
from verify_nonsplit_projective_layers import partition,transition,multiply


def transpose_weighted(matrix,source_weights,target_weights):
    return [[F(target_weights[j],source_weights[i])*matrix[j][i]
             for j in range(len(target_weights))] for i in range(len(source_weights))]


def matvec(a,x):
    return [sum(row[j]*x[j] for j in range(len(x))) for row in a]


def dot(x,y,w):
    return sum(w[i]*x[i]*y[i] for i in range(len(x)))


def inspect(p):
    parts=[partition(c,p) for c in range(p)]
    base=parts[0];weights=[len(b) for b in base]
    m=p-4
    # singleton0=w, singleton-1=u, first triple=v, remaining triples=u
    j0=[F(-m),F(1)]+[F(0)]+[F(1)]*(len(base)-3)
    j1=[F(-3),F(0)]+[F(1)]+[F(0)]*(len(base)-3)
    gram=((dot(j0,j0,weights),dot(j0,j1,weights)),
          (dot(j1,j0,weights),dot(j1,j1,weights)))
    hits=[]
    for c in range(1,p):
        forward=transition(base,parts[c])
        target_weights=[len(b) for b in parts[c]]
        adjoint=transpose_weighted(forward,weights,target_weights)
        # W=Q_c on F0; W*W is the two-layer round trip.
        images=[matvec(forward,j) for j in (j0,j1)]
        pull=((dot(images[0],images[0],target_weights),dot(images[0],images[1],target_weights)),
              (dot(images[1],images[0],target_weights),dot(images[1],images[1],target_weights)))
        lam=F(pull[0][0],gram[0][0])
        if pull==tuple(tuple(lam*x for x in row) for row in gram):
            hits.append((c,lam))
        # Independent matrix-adjoint action matches pullback entries.
        back=multiply(adjoint,forward)
        assert dot(j0,matvec(back,j1),weights)==pull[0][1]
    return hits


if __name__=='__main__':
    for p in range(5,150):
        if p%3==2 and not any(p%q==0 for q in range(2,isqrt(p)+1)):
            print(p,inspect(p))
    print('Finite structural survey; no all-prime extrapolation.')
