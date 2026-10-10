"""Finite images supporting the explicit thin-subgroup warning.

The proof of infinite index is the rank formula for finite-index subgroups
of the free group Gamma(3); the finite checks do not establish that theorem.
"""

from collections import deque
from itertools import product


def multiply(a, b, modulus):
    return ((a[0]*b[0]+a[1]*b[2]) % modulus,
            (a[0]*b[1]+a[1]*b[3]) % modulus,
            (a[2]*b[0]+a[3]*b[2]) % modulus,
            (a[2]*b[1]+a[3]*b[3]) % modulus)


def generated_group(generators, modulus):
    identity = (1,0,0,1)
    queue = deque([identity])
    seen = {identity}
    while queue:
        current = queue.popleft()
        for generator in generators:
            following = multiply(current,generator,modulus)
            if following not in seen:
                seen.add(following)
                queue.append(following)
    return seen


def verify():
    upper, lower = (1,3,0,1),(1,0,3,1)
    for prime in (2,5,7,11):
        group = generated_group((upper,lower),prime)
        expected = {matrix for matrix in product(range(prime),repeat=4)
                    if (matrix[0]*matrix[3]-matrix[1]*matrix[2]) % prime == 1}
        assert group == expected
        assert len(group) == prime*(prime**2-1)
        print("two-generator level-3 subgroup mod",prime,"full SL2 image",len(group))
    assert len(generated_group((upper,lower),3)) == 1

    modular_s, modular_u = (0,-1,1,0),(0,-1,1,1)
    sl2_3 = generated_group((modular_s,modular_u),3)
    projectivize = lambda matrix: min(matrix,tuple(-x % 3 for x in matrix))
    cosets = {projectivize(matrix) for matrix in sl2_3}
    assert len(sl2_3) == 24 and len(cosets) == 12
    for generator in (modular_s,modular_u):
        assert all(projectivize(multiply(matrix,generator,3)) != matrix
                   for matrix in cosets)
    # Torsion-free index 12 in C2*C3 gives Euler characteristic -2, rank 3.
    assert 1+12//6 == 3
    print("Gamma(3) index-12 torsion-free quotient data: PASS")
    print("large finite images do not certify finite index: supporting checks PASS")


if __name__ == "__main__":
    verify()
