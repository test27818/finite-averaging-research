"""Exact arithmetic audit of the rational-point theorem for the 3-adic set.

Uses finite residues and integer lifts; no floating p-adic approximation.
The note proves all-depth and all-rational statements separately.
"""
from itertools import product, combinations, combinations_with_replacement
from math import gcd, isqrt
from pathlib import Path
from random import Random
import json
from verify_subcritical_complement_dynamics import core_distance, initial_distance

A = (-3, 0, -1, 1)
B = (1, -1, 0, -3)
I = (1, 0, 0, 1)


def mul(A, B):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def mv(A, x):
    return (A[0]*x[0]+A[1]*x[1], A[2]*x[0]+A[3]*x[1])


def v3(x):
    if not x:
        return float('inf')
    k = 0
    while x % 3 == 0:
        x //= 3
        k += 1
    return k


def mod_direction(x, modulus):
    u, v = x
    assert min(v3(u), v3(v)) == 0
    if v % 3:
        return (u*pow(v, -1, modulus) % modulus, 1)
    return (1, v*pow(u, -1, modulus) % modulus)


def rational_class(u, v):
    if not (u or v):
        return 'zero', 0
    g = gcd(u, v)
    u, v = u//g, v//g
    steps = 0
    while True:
        if not u or not v:
            return 'boundary', steps
        if u+v == 0:
            return 'marked', steps
        before = abs(u)+abs(v)
        if u % 3 == 0:
            u, v = -u//3, v-u//3
        elif v % 3 == 0:
            u, v = u-v//3, -v//3
        else:
            return 'outside', steps
        assert gcd(u, v) == 1
        assert abs(u)+abs(v) < before
        steps += 1


def finite_levels():
    records = []
    for k in range(1, 10):
        modulus = 3**k
        root = mod_direction((1, -1), modulus)
        seen, todo = {root}, [root]
        while todo:
            x = todo.pop()
            for M in (A, B):
                y = mod_direction(mv(M, x), modulus)
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        assert len(seen) == 2**(k+1)-1
        # Eventually constant addresses give representatives for all boundary cylinders.
        boundary = {(0, 1), (1, 0)}
        for _ in range(k-1):
            boundary = {mod_direction(mv(M, x), modulus)
                        for x in boundary for M in (A, B)}
        assert len(boundary) == 2**k
        assert boundary <= seen
        records.append({'k': k, 'K_classes': len(seen), 'boundary_classes': len(boundary),
                        'full_projective_classes': 4*3**(k-1)})
    return records


def local_global_checks():
    """Compare residue-orbit membership with the rational-point classification."""
    levels = {}
    for k in range(1, 10):
        modulus = 3**k
        root = mod_direction((1, -1), modulus)
        orbit, todo = {root}, [root]
        while todo:
            x = todo.pop()
            for M in (A, B):
                y = mod_direction(mv(M, x), modulus)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        levels[k] = orbit
    checked = excluded = 0
    for u in range(-80, 81):
        for v in range(-80, 81):
            if gcd(u, v) != 1:
                continue
            kind, steps = rational_class(u, v)
            if kind != 'outside':
                for k, orbit in levels.items():
                    assert mod_direction((u, v), 3**k) in orbit
                    checked += 1
                continue
            a, b = u, v
            for _ in range(steps):
                if a % 3 == 0:
                    a, b = -a//3, b-a//3
                else:
                    a, b = a-b//3, -b//3
            # A point can agree with e for several digits before being rejected.
            precision = steps+v3(a+b)+1
            if precision in levels:
                assert mod_direction((u, v), 3**precision) not in levels[precision]
                excluded += 1
                checked += 1
    return {'finite_local_membership_checks': checked, 'certified_outside_directions': excluded}


def contractions():
    rng = Random(2026091609)
    count = 0
    for _ in range(12000):
        x = tuple(rng.randrange(-10**8, 10**8) for _ in range(2))
        y = tuple(rng.randrange(-10**8, 10**8) for _ in range(2))
        if (x[0]-x[1]) % 3 == 0 or (y[0]-y[1]) % 3 == 0:
            continue
        det = x[0]*y[1]-x[1]*y[0]
        if not det:
            continue
        for M in (A, B):
            xx, yy = mv(M, x), mv(M, y)
            assert min(v3(xx[0]), v3(xx[1])) == 0
            assert min(v3(yy[0]), v3(yy[1])) == 0
            assert v3(xx[0]*yy[1]-xx[1]*yy[0]) == v3(det)+1
            count += 1
    return count


def rational_points():
    counts = {'marked': 0, 'boundary': 0, 'outside': 0}
    for u in range(-200, 201):
        for v in range(-200, 201):
            if gcd(u, v) != 1:
                continue
            kind, steps = rational_class(u, v)
            counts[kind] += 1
            if kind == 'marked':
                assert (u+v) % 5 == 0
            if kind == 'boundary':
                assert (u+v) % 5 != 0
            answer = core_distance(3, u, v)
            assert (answer is not None) == (kind == 'marked')
            if answer is not None:
                assert answer == steps+1
    return counts


def original_input_interface():
    count = 0
    for x in combinations_with_replacement(range(-4, 5), 5):
        S = sum(x)
        predicted = False
        for i, j in combinations(range(5), 2):
            u, v = 4*x[i]+x[j]-S, x[i]+4*x[j]-S
            if not (u or v):
                predicted = True
                continue
            g = gcd(u, v)
            u, v = u//g, v//g
            kind, _ = rational_class(u, v)
            in_K = kind in ('marked', 'boundary')
            predicted |= in_K and (u+v) % 5 == 0
        assert predicted == (initial_distance(3, tuple(5*t-S for t in x)) is not None)
        count += 1
    return count


def periodic_addresses():
    count = 0
    for length in range(1, 11):
        for word in product((0, 1), repeat=length):
            M = I
            for letter in word:
                M = mul(M, (A, B)[letter])
            det = M[0]*M[3]-M[1]*M[2]
            trace = M[0]+M[3]
            D = trace*trace-4*det
            assert det == (-3)**length
            assert trace % 3 and D % 3 == 1
            if len(set(word)) == 2:
                assert D < 0 or isqrt(D)**2 != D
                count += 1
    assert mul(A, B) == (-3, 3, -1, -2)
    M = mul(A, B)
    assert M[0]+M[3] == -5
    assert M[0]*M[3]-M[1]*M[2] == 9
    x = (1, -1)
    for k in range(1, 81):
        x = mv(M, x)
        assert gcd(*x) == 1 and sum(x) % 5 == 0
        assert core_distance(3, *x) == 2*k+1
    return count


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions required.')
    result = {'exact_contraction_checks': contractions(),
              'finite_precision_counts': finite_levels(),
              'local_global_comparison': local_global_checks(),
              'rational_directions': rational_points(),
              'original_input_multisets': original_input_interface(),
              'mixed_periodic_words': periodic_addresses(),
              'scope': 'Finite checks support written rational-point, dimension and density proofs; not a fixed-modulus test.'}
    Path(__file__).with_name('five_padic_fractal_verification.json').write_text(
        json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
