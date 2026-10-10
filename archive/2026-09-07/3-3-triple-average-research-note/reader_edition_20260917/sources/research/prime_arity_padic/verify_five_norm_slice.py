"""Complete bounded norm-shell enumeration; general proof is in the note."""
from math import gcd, isqrt
from pathlib import Path
import json
from verify_subcritical_complement_dynamics import core_distance


def norm(u, v):
    return u*u-u*v+3*v*v


def run():
    checked = accepted = 0
    shell_counts = []
    for k in range(19):
        N = 5*3**k
        bound = isqrt(4*N//11)
        solutions = set()
        for v in range(-bound, bound+1):
            D = 4*N-11*v*v
            root = isqrt(D)
            if root*root != D:
                continue
            for signed in {root, -root}:
                if (v+signed) % 2:
                    continue
                u = (v+signed)//2
                if gcd(u, v) == 1:
                    solutions.add((u, v))
        local = 0
        for u, v in solutions:
            assert norm(u, v) == N
            prediction = (u+v) % 5 == 0 and (k == 0 or u % 3 == 0)
            answer = core_distance(3, u, v)
            assert prediction == (answer is not None), (k, u, v, answer)
            if prediction:
                assert answer == k+1
                local += 1
            checked += 1
        shell_counts.append({'k': k, 'primitive_solutions': len(solutions), 'solvable': local})
        accepted += local
    for u, v in ((9, 1), (11, 24)):
        assert core_distance(3, u, v) is not None
        N = norm(u, v)
        while N % 3 == 0:
            N //= 3
        assert N != 5
    result = {'primitive_solutions_checked': checked, 'accepted': accepted,
              'complete_shells': shell_counts,
              'scope': 'Static criterion proved for Q=5*3^k only; not a full five-entry criterion.'}
    Path(__file__).with_name('five_norm_slice_verification.json').write_text(
        json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    run()
