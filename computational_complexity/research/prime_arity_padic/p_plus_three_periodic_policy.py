"""Polynomial decision for any prescribed periodic proper averaging policy.

The solver checks all repetitions and all stopping positions before a final
terminal operation, including periods consisting only of singleton steps.
It does not search over all policies and is not a full averaging P algorithm.
"""
from math import gcd
from five_eight_rank_clock import step_matrix,valuation


def multiply(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def matrix_power(a,k):
    answer=tuple(tuple(int(i==j) for j in range(len(a))) for i in range(len(a)))
    while k:
        if k&1:answer=multiply(answer,a)
        a=multiply(a,a);k//=2
    return answer


def apply(a,u):
    return tuple(sum(x*y for x,y in zip(row,u)) for row in a)


def determinant3(a):
    x,y,z=a
    return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])


def second_coefficient(a):
    return sum(a[i][i]*a[j][j]-a[i][j]*a[j][i] for i,j in ((0,1),(0,2),(1,2)))


def cubic_norm(trace,second,determinant,constant,linear,quadratic):
    """Norm of constant+linear*x+quadratic*x² modulo a monic cubic."""
    q0,q1,q2=constant,linear,quadratic
    multiplication=(
        (q0,q2*determinant,determinant*(q1+trace*q2)),
        (q1,q0-second*q2,-second*q1+(determinant-trace*second)*q2),
        (q2,q1+trace*q2,q0+trace*q1+(trace*trace-second)*q2))
    return determinant3(multiplication)


def universal_period_bound(height,length,p=5):
    """A deliberately coarse proved repetition bound for fixed-height inputs."""
    if height<1 or length<1:
        raise ValueError('positive height and period length required')
    power=1;digits=0
    while power<height:power*=p;digits+=1
    return 100+(100*(1+digits)+length-1)//length


def first_zero_cubic(trace,second,determinant,f0,f1,f2,maximum):
    """Finite exact evaluation; maximum comes from a proved p-adic bound."""
    values=[f0,f1,f2]
    for k in range(maximum+1):
        if k>=len(values):
            values.append(trace*values[-1]-second*values[-2]+determinant*values[-3])
        if values[k]==0:return k
    return None


def zero_in_singleton_period(matrix,distinct_indices,length,f0,f1,f2,p=5):
    """Complete scalar zero test for an all-singleton period.

    Uses the actual singleton-period factorization, not an assumed generic
    cubic Skolem procedure. The valuation bound handles all repetitions.
    """
    if f0==0:return 0
    P=p**length
    trace=sum(matrix[i][i] for i in range(3))
    second=second_coefficient(matrix)
    determinant=determinant3(matrix)
    assert trace%p and valuation(second,p)==length
    assert determinant==(-1)**length*P*P
    if distinct_indices==1:
        root=(-1)**length
        return zero_in_recurrence(P+root,P*root,f0,f1,p)
    if distinct_indices==2:
        a=trace-P;b=determinant//P
        assert second==P*a+b and b==(-1)**length*P
        linear=f1-P*f0
        constant=f2-trace*f1+P*a*f0
        norm=constant*constant+a*linear*constant+b*linear*linear
        if not norm:
            assert not linear and not constant
            return None # Only the fixed P-eigenvalue remains, with f0 nonzero.
        separation=P*P-a*P+b
        assert separation
        bound=(valuation(norm,p)+valuation(separation,p))//length
        return first_zero_cubic(trace,second,determinant,f0,f1,f2,bound)
    assert distinct_indices==3
    linear=f1-trace*f0
    constant=f2-trace*f1+second*f0
    norm=cubic_norm(trace,second,determinant,constant,linear,f0)
    assert norm
    discriminant=(trace*trace*second*second-4*second**3
                  -4*trace**3*determinant-27*determinant**2
                  +18*trace*second*determinant)
    assert discriminant
    bound=(valuation(norm,p)+valuation(discriminant,p))//length
    return first_zero_cubic(trace,second,determinant,f0,f1,f2,bound)


def zero_in_recurrence(trace,product,f0,f1,p=5):
    """Find the earliest zero of f(k+2)=trace*f(k+1)-product*f(k).

    Requires p not dividing trace and v_p(product)>0. There are no bounded
    search heuristics: in the nondegenerate case the eigenvalue valuations
    determine the only candidate k. An initial zero is accepted immediately.
    """
    if trace%p==0 or product==0 or product%p:
        raise ValueError('requires a p-unit trace and a nonzero p-divisible product')
    if f0==0:return 0
    norm=trace*f0*f1-f1*f1-product*f0*f0
    if norm==0:return None
    exponent=valuation(product,p)
    total=valuation(norm,p)
    precision=total+1
    root=0;known=1
    while known<precision:
        known=min(2*known,precision)
        modulus=p**known
        polynomial=root*root-trace*root+product
        derivative=2*root-trace
        root=(root-polynomial*pow(derivative,-1,modulus))%modulus
    modulus=p**precision
    root%=modulus
    unit_root=(trace-root)%modulus
    a=(f1-root*f0)%modulus
    b=(unit_root*f0-f1)%modulus
    assert a and b
    va,vb=valuation(a,p),valuation(b,p)
    assert va+vb==total
    difference=va-vb
    if difference<0 or difference%exponent:return None
    k=difference//exponent
    if k==0:return None  # f0 was already checked.
    companion=((trace,-product),(1,0))
    actual=apply(matrix_power(companion,k-1),(f1,f0))[0]
    return k if actual==0 else None


def decide_periodic_core(values,word,p=5):
    """Decide W* followed by a prefix of W and a terminal all-exception step.

    Values are three rational-direction integer differences; normalize common
    scale. Success has a compact (repetitions,prefix) witness and an optional
    expanded mask word. Selecting all three exceptions is recorded as mask 7.
    """
    values=tuple(values);word=tuple(word)
    if p<5 or p%2==0:
        raise ValueError('the theorem assumes a prime p>=5')
    if len(values)!=3 or not word or any(mask not in range(1,7) for mask in word):
        raise ValueError('three differences and a nonempty proper word are required')
    has_pair=any(mask.bit_count()==2 for mask in word)
    g=gcd(*values)
    if not g:return {'possible':True,'steps':0,'word':()}
    u=tuple(x//g for x in values)
    if sum(u)%(p+3):return {'possible':False,'reason':'G obstruction'}
    identity=((1,0,0),(0,1,0),(0,0,1))
    prefixes=[];matrix=identity
    for mask in word:
        prefixes.append(tuple(sum(matrix[i][j] for i in range(3)) for j in range(3)))
        matrix=step_matrix(matrix,mask,p)
    assert (determinant3(matrix)==0)==has_pair
    trace=sum(matrix[i][i] for i in range(3))
    product=second_coefficient(matrix)
    assert trace%p and valuation(product,p)==len(word)
    once=apply(matrix,u);twice=apply(matrix,once)
    choices=[]
    for j,row in enumerate(prefixes):
        f0=sum(x*y for x,y in zip(row,u))
        if f0==0:
            k=0
        else:
            f1=sum(x*y for x,y in zip(row,once))
            f2=sum(x*y for x,y in zip(row,twice))
            if has_pair:
                index=zero_in_recurrence(trace,product,f1,f2,p)
                if index is None:continue
                k=index+1
            else:
                k=zero_in_singleton_period(matrix,len(set(word)),len(word),f0,f1,f2,p)
                if k is None:continue
        choices.append((len(word)*k+j,k,j))
    if not choices:return {'possible':False,'reason':'no terminal point on this periodic policy'}
    _,k,j=min(choices)
    assert k<=universal_period_bound(max(map(abs,u)),len(word),p)
    masks=word*k+word[:j]+(7,)
    return {'possible':True,'steps':len(masks),'repetitions':k,'prefix_length':j,'word':masks}
