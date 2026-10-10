"""Compile a congruence correction into three conjugate roots and a deep tail.

This is exact rational/finite-ring algebra. Availability of the root families,
T and its inverse, and the remaining deep-kernel word is a proof precondition.
No modulus factorization, discrete logarithm, or orbit search is used.
"""
from fractions import Fraction as F
from math import gcd, lcm

IDENTITY = (F(1), F(0), F(0), F(1))
LOWER_TANGENT = (F(0), F(0), F(1), F(0))


def multiply(A, B):
    a,b,c,d=A
    e,f,g,h=B
    return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h


def determinant(A):
    return A[0]*A[3]-A[1]*A[2]


def inverse(A):
    a,b,c,d=A
    delta=determinant(A)
    if not delta:
        raise ValueError('Singular matrix')
    return tuple(F(v)/delta for v in (d,-b,-c,a))


def conjugate(A, X):
    return multiply(multiply(A,X),inverse(A))


def residue(value, modulus):
    value=F(value)
    return value.numerator*pow(value.denominator,-1,modulus)%modulus


def upper(value):
    return F(1),F(value),F(0),F(1)


def lower(value):
    return F(1),F(0),F(value),F(1)


def compile_correction(T, h, target):
    """Return exact E,K with target=E*K and K=I mod h^2.

    E is the product over j=0,1,2 of T^j L(h*q*r_j) T^-j.
    A ValueError means the supplied target misses the exact tangent-image
    condition. This is not a claim that it is unreachable by other resources.
    """
    T=tuple(map(F,T))
    target=tuple(map(F,target))
    if h<2 or determinant(target)!=1:
        raise ValueError('Require h>=2 and target in SL2')
    if any(residue(v-e,h) for v,e in zip(target,IDENTITY)):
        raise ValueError('Target is not in Gamma(h)')
    # All residues used below must exist, with b and det(T) units modulo h.
    a,b,c,d=(residue(v,h) for v in T)
    delta=residue(determinant(T),h)
    b_inv=pow(b,-1,h)
    delta_inv=pow(delta,-1,h)
    trace=(a+d)%h
    T2=multiply(T,T)
    tangents=(LOWER_TANGENT,conjugate(T,LOWER_TANGENT),conjugate(T2,LOWER_TANGENT))
    q=lcm(*(v.denominator for X in tangents for v in X))
    if gcd(q,h)!=1:
        raise ValueError('A tangent has a denominator at the modulus')
    q_inv=pow(q,-1,h)
    x,y,z=(residue((target[i]-IDENTITY[i])/h,h)*q_inv%h for i in (0,1,2))
    rhs=(-delta*b_inv*(x+d*b_inv*y))%h
    defect=gcd(trace,h)
    if rhs%defect:
        raise ValueError('Target is outside the three-root tangent image')
    reduced_modulus=h//defect
    r2=0 if reduced_modulus==1 else (
        pow(trace//defect,-1,reduced_modulus)*(rhs//defect)%reduced_modulus
    )
    r1=(-delta*b_inv*b_inv*y-trace*trace*delta_inv*r2)%h
    r0=(z-d*d*delta_inv*r1-(b*c+d*d)**2*delta_inv**2*r2)%h
    coefficients=(r0,r1,r2)
    E=IDENTITY
    factors=[]
    for coefficient,X in zip(coefficients,tangents):
        scalar=h*q*coefficient
        factor=tuple(e+scalar*v for e,v in zip(IDENTITY,X))
        if determinant(factor)!=1 or any(v.denominator!=1 for v in factor):
            raise ArithmeticError('Root factor failed exact integrality/determinant')
        E=multiply(E,factor)
        factors.append(factor)
    K=multiply(inverse(E),target)
    if determinant(K)!=1 or any(residue(v-e,h*h) for v,e in zip(K,IDENTITY)):
        raise ArithmeticError('Correction did not land in the deep kernel')
    if multiply(E,K)!=target:
        raise ArithmeticError('Exact product does not recover target')
    return {
        'modulus':h,
        'defect':defect,
        'clearing_integer':q,
        'coefficients':coefficients,
        'root_parameters':tuple(h*q*r for r in coefficients),
        'factors':tuple(factors),
        'correction':E,
        'deep_tail':K,
    }
