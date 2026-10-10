"""Checks for new bounded-fiber and primitive-content structural lemmas.

Theorems are proved in the accompanying report. No averaging-word search or
reachability conclusion for unbounded p is inferred from these finite checks.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

from fiber_geometry_probe import fiber

ROOT = Path(__file__).parent


def matrix(p, r, source, output):
    i, j, k = source
    x, y, u, v = output
    alpha, beta = i-j, r*j-p*k
    return (p*(x-y)+alpha*v, p*r*y-p*p*u+beta*v, -alpha, -beta)


def multiply(A, B):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def inverse(A):
    d = A[0]*A[3]-A[1]*A[2]
    return tuple(F(x, d) for x in (A[3], -A[1], -A[2], A[0]))


def primitive(v):
    g = gcd(*v)
    assert g > 0
    return tuple(x//g for x in v), g


def mv(A, v):
    return (A[0]*v[0]+A[1]*v[1], A[2]*v[0]+A[3]*v[1])


def geometry():
    cases = json.loads((ROOT.parents[2]/'work/large_symmetric_carrier_small_certificate.json')
                       .read_text(encoding='utf-8'))['cases']
    counts = Counter()
    checked = 0
    for case in cases:
        p, s = case['p'], case['s']
        for pair in case['root_pairs']:
            source, base = pair[0][:3], pair[0][3:]
            result = fiber(p, p+s, 2, source, base)
            points = result['points']
            base_matrix = matrix(p, p+s, source, base)
            for point, index in zip(points, result['step_indices']):
                relative = multiply(matrix(p, p+s, source, point), inverse(base_matrix))
                g = gcd(source[0]-source[1], (p+s)*source[1]-p*source[2])
                assert relative == (1, F((3*p+s)*index, g), 0, 1)
            if result['dimension'] == 1:
                delta = next(tuple(a-b for a, b in zip(pt, base))
                             for pt in points if tuple(pt) != tuple(base))
                common = gcd(*delta)
                direction = tuple(a//common for a in delta)
                alpha = source[0]-source[1]
                g = gcd(alpha, (p+s)*source[1]-p*source[2])
                step = -F(p*(direction[0]-direction[1])+alpha*direction[3], alpha)
                assert abs(step/F(3*p+s, g)) == result['root_index']
            counts[result['dimension'], result['root_index']] += 1
            checked += 1
    print('complete fixed-base fiber classification:', checked, dict(counts))

    # A unimodular triangle creates the primitive shear without a direct n move.
    p, r = 43, 65
    source = (19, 4, 20)
    base = (5, 20, 15, 3)
    outputs = ((0, 28, 15, 0), (4, 13, 10, 16))
    J = matrix(p, r, source, base)
    assert J == (-600, 26365, -15, 600)
    assert multiply(J, J) == (-35475, 0, 0, -35475)
    roots = [multiply(matrix(p, r, source, o), inverse(J)) for o in outputs]
    assert roots == [(1, F(604, 15), 0, 1), (1, F(-151, 5), 0, 1)]
    assert multiply(*roots) == (1, F(151, 15), 0, 1)
    basis_effect = (-6, 1, -5, 10)
    basis_zero = (-19, -4, -20, 43)
    for output, coefficients in zip(outputs, ((4, -1), (-3, 1))):
        assert tuple(a-b for a, b in zip(output, base)) == tuple(
            coefficients[0]*x+coefficients[1]*y for x, y in zip(basis_effect, basis_zero))
    assert 4*1-(-1)*(-3) == 1
    print('unimodular same-determinant triangle: PASS')

    # Singleton persists for arbitrarily large p; finite checks guard its formula.
    for p in range(5, 102, 2):
        z = fiber(p, 2*p-1, 2, (1, 0, p-1), (0, p-1, 1, 0))
        assert z['dimension'] == 0 and len(z['points']) == 1
    print('large-carrier singleton formula checks: PASS 49')
    return {'base_fibers': checked,
            'counts': [{'dimension': a, 'root_index': b, 'count': c}
                       for (a, b), c in sorted(counts.items())]}


def content():
    rng = Random(20260916)
    count = 0
    for _ in range(2000):
        A = tuple(rng.randrange(-25, 26) for _ in range(4))
        D = A[0]*A[3]-A[1]*A[2]
        if not D:
            continue
        x = (rng.randrange(-50, 51), rng.randrange(-50, 51))
        if gcd(*x) != 1:
            continue
        y, g = primitive(mv(A, x))
        adj = (A[3], -A[1], -A[2], A[0])
        back, h = primitive(mv(adj, y))
        assert g*h == abs(D)
        assert back == tuple((1 if D > 0 else -1)*a for a in x)
        c = gcd(*A)
        reduced = tuple(a//c for a in A)
        assert abs(reduced[0]*reduced[3]-reduced[1]*reduced[2]) == abs(D)//(c*c)
        assert primitive(mv(reduced, x))[0] == y
        count += 1
    print('content-adjugate duality and projective determinant: PASS', count)
    return count


def physical_triangle():
    p, r = 43, 65
    source = (19, 4, 20)
    base = (5, 20, 15, 3)
    others = ((0, 28, 15, 0), (4, 13, 10, 16))
    atom_count = 0
    for a, z in ((F(1), F(0)), (F(0), F(1))):
        raw = [a]*p+[r*z-a]*p+[-p*z]*r
        state = raw[:]
        groups = (list(range(p)), list(range(p, 2*p)), list(range(2*p, 2*p+r)))
        word = []

        def average(indices):
            assert len(indices) == len(set(indices)) == p
            value = sum(state[i] for i in indices)/p
            for i in indices:
                state[i] = value
            word.append(indices[:])

        for out in (base, others[0], base, others[1]):
            ga, gb, gc = groups
            i, j, k = source
            first = ga[:i]+gb[:j]+gc[:k]
            second = ga[i:2*i]+gb[j:2*j]+gc[k:2*k]
            average(first)
            average(second)
            fresh = first+second
            kept, fresh = fresh[:r], fresh[r:]
            ga, gb, gc = ga[2*i:], gb[2*j:], gc[2*k:]
            x, y, u, v = out
            left = ga[:x]+gb[:y]+gc[:u]+fresh[:v]
            right = ga[x:]+gb[y:]+gc[u:]+fresh[v:]
            assert sorted(left+right+kept) == list(range(2*p+r))
            average(left)
            average(right)
            groups = (left, right, kept)
        scalar = F(-825, p**3)**2
        aa, zz = scalar*(a+F(151, 15)*z), scalar*z
        assert all(state[i] == value for g, value in
                   zip(groups, (aa, r*zz-aa, -p*zz)) for i in g)
        replay = raw[:]
        for indices in word:
            value = sum(replay[i] for i in indices)/p
            for i in indices:
                replay[i] = value
        assert replay == state
        atom_count += len(word)
    print('triangle shear literal original-position replay: PASS', atom_count)
    return atom_count


def good_determinant_correspondences():
    """Enumerate exact finite lifts, independently of the Smith/CRT proof."""
    matrices_checked = 0
    branch_lifts = 0
    scalar_checks = 0
    for q in range(2, 11):
        states = [(x, y) for x in range(q) for y in range(q)
                  if gcd(x, y, q) == 1]
        for d in range(1, 11):
            if gcd(q, d) != 1:
                continue
            divisors = [g for g in range(1, d+1) if d % g == 0]
            # Primitive matrices with determinant d or -d, with mixed axes.
            for A in ((1, 0, 0, d), (1, 2, 3, 6+d), (3, 6+d, 1, 2)):
                assert gcd(*A) == 1
                assert abs(A[0]*A[3]-A[1]*A[2]) == d
                observed = {state: set() for state in states}
                modulus = q*d
                for x in range(modulus):
                    for y in range(modulus):
                        if gcd(x, y, modulus) != 1:
                            continue
                        raw = mv(A, (x, y))
                        g = gcd(*raw, d)
                        target = tuple(a//g % q for a in raw)
                        observed[x % q, y % q].add(target)
                        branch_lifts += 1
                for state in states:
                    expected = {tuple(pow(g, -1, q)*a % q for a in mv(A, state))
                                for g in divisors}
                    assert observed[state] == expected
                    # A finite positive cycle replaces the inverse on this state.
                    cursor = tuple(a % q for a in mv(A, state))
                    period = 1
                    while cursor != state:
                        cursor = tuple(a % q for a in mv(A, cursor))
                        period += 1
                        assert period <= len(states)
                    for g in divisors:
                        cursor = tuple(pow(g, -1, q)*a % q for a in mv(A, state))
                        for _ in range(period-1):
                            cursor = tuple(a % q for a in mv(A, cursor))
                        assert cursor == tuple(pow(g, -1, q)*a % q for a in state)
                        scalar_checks += 1
                matrices_checked += 1
    # Non-coprime determinants really do have direction-dependent content.
    A = (1, 0, 0, 2)
    assert tuple(a % 2 for a in primitive(mv(A, (2, 1)))[0]) == (1, 1)
    assert tuple(a % 2 for a in primitive(mv(A, (4, 1)))[0]) == (0, 1)
    print('coprime-determinant correspondence and finite scalars: PASS',
          matrices_checked, branch_lifts, scalar_checks)
    return {'matrix_modulus_pairs': matrices_checked, 'primitive_finite_lifts': branch_lifts,
            'positive_cycle_scalar_checks': scalar_checks}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions are required.')
    result = geometry()
    result['content_checks'] = content()
    result['literal_atoms'] = physical_triangle()
    result['good_determinant_correspondences'] = good_determinant_correspondences()
    result['scope'] = 'Finite checks supplement written structural proofs; no all-parameter resource or terminal-coverage theorem.'
    (ROOT/'verification.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
