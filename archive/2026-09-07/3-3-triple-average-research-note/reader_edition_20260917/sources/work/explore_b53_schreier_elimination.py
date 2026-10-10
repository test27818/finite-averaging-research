"""Finite Schreier targets with exact unit-pivot tests, without word search."""
from collections import deque
from fractions import Fraction as F
from verify_diagonal_resource_reduction import product, upper, lower
from verify_b53_inverse_closure import inverse
from compile_bn_integer_templates import primitive_matrix
from explore_thirteen_modular import S,U


def generators(p):
    c = (F(1),F(0),F(1),F(1))
    def label(m):
        x,y = int(m[0]-m[2])%p,int(m[1]-m[3])%p
        return (1,y*pow(x,-1,p)%p) if x else (0,1)
    base = (1,p-1)
    reps = {base:(F(1),F(0),F(0),F(1))}
    queue = deque([base])
    while queue:
        at = queue.popleft()
        for g in (S,U):
            value = product(reps[at],g)
            dest = label(value)
            if dest not in reps:
                reps[dest] = value
                queue.append(dest)
    assert len(reps) == p+1
    loops = set()
    for rep in reps.values():
        for g in (S,U):
            value = product(rep,g)
            loop = product(value,inverse(reps[label(value)]))
            moved = product(inverse(c),loop,c)
            key = primitive_matrix(tuple(int(x) for x in moved))
            if key != (-1,0,0,-1):
                loops.add(key)
    return sorted(loops)


def triadic(value):
    d = F(value).denominator
    while d%3 == 0:
        d//=3
    return d == 1


def pivot(m):
    a,b,c,d = map(F,m)
    if not c:
        return (a,0) if triadic(a) and triadic(1/a) else None
    modulus = abs(int(c))
    while modulus%3 == 0:
        modulus//=3
    residue,j = 1,0
    seen = set()
    while residue not in seen:
        seen.add(residue)
        for sign in (1,-1):
            if (sign*residue-int(a))%modulus == 0:
                return F(sign*3**j),j
        residue = residue*3%modulus
        j+=1
    return None


if __name__ == "__main__":
    rows = generators(53)
    failed = []
    for row in rows:
        result = pivot(row)
        print(row,"pivot",result)
        if result is None:
            failed.append(row)
    print("targets",len(rows),"failed",len(failed))
