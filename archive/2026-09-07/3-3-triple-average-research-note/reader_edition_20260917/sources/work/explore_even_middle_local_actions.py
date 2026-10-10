"""Local affine actions of the uniform even-remainder core returns.

This is a structural diagnostic, not an averaging-word search.  A legal
projective direction is represented by x=z/y modulo a prime power, where
y=v+(p+r/2)z is a unit at every prime dividing n=2p+r.
"""

from collections import deque


def primes(value):
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            answer.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        answer.append(value)
    return answer


def allowed_indices(p, r):
    lower = (p - r + 1) // 2
    upper = min(p - r, (p - 1) // 2)
    return range(lower, upper + 1)


def generators(p, r, modulus):
    n = 2 * p + r
    result = []
    # Swapping the two p-blocks: (z,y) -> (z,nz-y).
    result.append((1, 0, n, -1))
    # The two-layer returns, with irrelevant factor 1/p omitted.
    for i in allowed_indices(p, r):
        result.append((p, -1, n * i, -p))
    return [tuple(value % modulus for value in matrix) for matrix in result]


def act(matrix, x, modulus):
    a, b, c, d = matrix
    denominator = (c * x + d) % modulus
    # A prime-power unit is enforced by modular inversion below.
    return ((a * x + b) * pow(denominator, -1, modulus)) % modulus


def orbit(p, r, modulus):
    gens = generators(p, r, modulus)
    seen = {0}
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for matrix in gens:
            y = act(matrix, x, modulus)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def main():
    cases = []
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        for r in range(2, p, 2):
            n = 2 * p + r
            local = []
            for ell in primes(n):
                sizes = []
                for exponent in (1, 2, 3):
                    modulus = ell ** exponent
                    sizes.append((modulus, len(orbit(p, r, modulus))))
                local.append((ell, sizes))
            cases.append((p, r, len(tuple(allowed_indices(p, r))), local))
    for case in cases:
        print(case)


if __name__ == "__main__":
    main()
