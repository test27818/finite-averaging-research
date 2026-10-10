"""Exact punctured order-three orbit layers on p physical positions."""
from fractions import Fraction as F
from math import gcd,isqrt


INF = None


def mobius(x,p):
    if x is INF:
        return 0
    if (x+1)%p == 0:
        return INF
    return -pow(x+1,-1,p)%p


def shifted(x,c,p):
    if x is INF:
        return INF
    return (x+c)%p


def action(x,c,p):
    y = INF if x is INF else (x-c)%p
    return shifted(mobius(y,p),c,p)


def partition(c,p):
    assert action(action(action(INF,c,p),c,p),c,p) is INF
    special = {action(INF,c,p),action(action(INF,c,p),c,p)}
    assert special == {c%p,(c-1)%p}
    blocks = [(x,) for x in sorted(special)]
    remaining = set(range(p))-special
    while remaining:
        x = min(remaining)
        orbit = tuple(sorted((x,action(x,c,p),action(action(x,c,p),c,p))))
        assert len(set(orbit)) == 3 and set(orbit)<=remaining
        blocks.append(orbit)
        remaining -= set(orbit)
    return tuple(blocks)


def transition(source,target):
    return [[F(len(set(a)&set(b)),len(a)) for b in source] for a in target]


def determinant(matrix):
    a = [row[:] for row in matrix]
    result = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i,len(a)) if a[j][i]),None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i],a[pivot] = a[pivot],a[i]
            result = -result
        value = a[i][i]
        result *= value
        for j in range(i+1,len(a)):
            scale = a[j][i]/value
            for k in range(i+1,len(a)):
                a[j][k] -= scale*a[i][k]
    return result


def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def centered_scalar(matrix,weights):
    # Test A=lambda I on ker(weights^T), allowing a separate constant direction.
    n = len(matrix)
    # Correct the last coefficient so every column has weighted sum zero.
    basis = []
    for j in range(n-1):
        v = [F(0)]*n
        v[j] = 1
        v[-1] = -F(weights[j],weights[-1])
        basis.append(v)
    images = [[sum(matrix[i][k]*v[k] for k in range(n)) for i in range(n)] for v in basis]
    lam = None
    for j,(v,w) in enumerate(zip(basis,images)):
        candidate = w[j]
        if lam is None:
            lam = candidate
        if w != [lam*x for x in v]:
            return None
    return lam


def verify():
    checked = 0
    records = []
    for p in range(5,84):
        if p%3 != 2 or any(p%d==0 for d in range(2,isqrt(p)+1)):
            continue
        parts = [partition(c,p) for c in range(p)]
        assert all(len(q)==(p+4)//3 for q in parts)
        base = parts[0]
        values = []
        for c,target in enumerate(parts):
            matrix = transition(base,target)
            source_weights = [len(x) for x in base]
            target_weights = [len(x) for x in target]
            assert all(sum(row)==1 for row in matrix)
            assert all(sum(target_weights[i]*matrix[i][j] for i in range(len(matrix)))
                       == source_weights[j] for j in range(len(matrix)))
            det = determinant(matrix)
            values.append(det)
            checked += 1
        nonzero = sum(bool(x) for x in values)
        isoclinic = []
        for c,target in enumerate(parts):
            forward = transition(base,target)
            backward = transition(target,base)
            scalar = centered_scalar(multiply(backward,forward),[len(x) for x in base])
            if scalar is not None:
                isoclinic.append((c,scalar))
        translated_base = tuple(tuple((x+1)%p for x in block) for block in base)
        assert {frozenset(b) for b in translated_base} == {frozenset(b) for b in parts[1]}
        step = transition(base,translated_base)
        det_step = determinant(step)
        centered_trace = sum(step[i][i] for i in range(len(step)))-1
        dim = len(step)-1
        spectral = None if not det_step else centered_trace**dim/det_step
        records.append((p,nonzero,len(values),len(isoclinic),spectral))
    print("nonsplit punctured projective layers: PASS",checked)
    print("translation transition ranks",records)
    print("No global scalar cycle or positive inverse is asserted.")


if __name__ == "__main__":
    verify()
