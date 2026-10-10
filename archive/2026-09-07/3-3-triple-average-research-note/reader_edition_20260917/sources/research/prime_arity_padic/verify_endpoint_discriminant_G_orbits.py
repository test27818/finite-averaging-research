"""Exact finite audits for the endpoint G-orbit and quadratic-order statements.

Infinite group inclusion is a dependency of the written proof, not inferred from
these finite images. Existing physical replay code is imported without running
its main routine or rewriting any historical results.
"""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'work'))
from verify_uniform_endpoint_controller import Replay


def primes(n):
    result = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        result.append(n)
    return result


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def primitive_state(values):
    den = lcm(*(F(z).denominator for z in values))
    raw = tuple(int(F(z)*den) for z in values)
    g = gcd(*raw)
    assert g
    return tuple(z//g for z in raw)


def state_G(values):
    values = primitive_state(values)
    return gcd(*(z-values[0] for z in values))


def qform(n, x, y):
    return n*x*x-n*x*y+((n+1)//4)*y*y


def order_mul(a, b, h):
    # omega^2=omega-h, Tr(omega)=1.
    return a[0]*b[0]-h*a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1]


def arithmetic_identities():
    checked = local = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 31, 37):
        n, h = 2*p+1, (p+1)//2
        assert 2*n*(p+1)-n*n == n
        assert gcd(2*n, n, p+1) == 1
        delta = (-1, 2)
        assert order_mul(delta, delta, h) == (-n, 0)
        for x, y in product(range(-28, 29), repeat=2):
            if gcd(x, y) != 1:
                continue
            state = (x,)*p+(x-y,)*p+(-p*(2*x-y),)
            expected = gcd(y, n)
            norm = qform(n, x, y)
            assert gcd(*state) == 1 and sum(state) == 0
            assert state_G(state) == expected
            assert sum(z*z for z in state) == 2*p*norm
            assert 4*norm == y*y+n*(2*x-y)**2
            assert gcd(norm, n) == gcd(y*y, n)
            pairing = (2*n*x-n*y, -n*x+(p+1)*y)
            assert gcd(*pairing) == expected
            eta = (x, y-2*x)
            eta_bar = (eta[0]+eta[1], -eta[1])
            assert order_mul(eta, eta_bar, h) == (norm, 0)
            columns = [delta, order_mul(delta, (0, 1), h),
                       eta, order_mul(eta, (0, 1), h)]
            ideal_index = gcd(*(a[0]*b[1]-a[1]*b[0] for a, b in combinations(columns, 2)))
            assert ideal_index == expected
            assert (eta[0]+eta[1]*pow(2, -1, n)-y*pow(2, -1, n)) % n == 0
            checked += 1
        for ell in primes(n):
            assert tuple(z % ell for z in order_mul(delta, delta, h)) == (0, 0)
            assert tuple(z % ell for z in delta) != (0, 0)
            for a, b in product(range(ell), repeat=2):
                scalar = (a+b*pow(2, -1, ell)) % ell
                ring_norm = (a*a+a*b+h*b*b) % ell
                assert ring_norm == scalar*scalar % ell
                local += 1
    # Conductor-prime example: -63=3^2*(-7), with 3 inert in Q(sqrt(-7)).
    assert not any((z*z+7) % 3 == 0 for z in range(3))
    assert qform(63, 1, 3) == 18 and qform(63, 1, 9) == 792
    return {'primitive_core_and_order_ideal_checks': checked,
            'dual_number_norm_checks_at_bad_primes': local,
            'conductor_example': {'n': 63, 'field_discriminant': -7, 'conductor': 3,
                                  'same_norm_gcd_different_G': [[1, 3, 3, 9], [1, 9, 9, 9]]}}


def borel_orbits(n, general_linear):
    units = [(a, pow(a, -1, n)) for a in range(n) if gcd(a, n) == 1]
    todo = {(x, y) for x in range(n) for y in range(n) if gcd(x, y, n) == 1}
    parts = []
    while todo:
        start = next(iter(todo))
        seen, queue = {start}, deque([start])
        while queue:
            x, y = queue.popleft()
            candidates = [((x+y) % n, y)]
            if general_linear:
                candidates += [(a*x % n, y) for a, _ in units]
                candidates += [(x, a*y % n) for a, _ in units]
            else:
                candidates += [(a*x % n, b*y % n) for a, b in units]
            for z in candidates:
                if z not in seen:
                    seen.add(z)
                    queue.append(z)
        labels = {gcd(y, n) for x, y in seen}
        assert len(labels) == 1
        label = labels.pop()
        parts.append({'G': label, 'primitive_residue_columns': len(seen)})
        todo -= seen
    return sorted(parts, key=lambda r: (r['G'], r['primitive_residue_columns']))


def exact_finite_orbits():
    rows = []
    for n in (7, 11, 15, 23, 27, 35, 63, 75):
        sl = borel_orbits(n, False)
        gl = borel_orbits(n, True)
        assert [r['G'] for r in gl] == divisors(n)
        assert sum(r['primitive_residue_columns'] for r in sl) == sum(
            r['primitive_residue_columns'] for r in gl)
        rows.append({'n': n, 'p': (n-1)//2, 'classical_cusp_count': len(sl),
                     'classical_cusps_by_G': dict(sorted(Counter(r['G'] for r in sl).items())),
                     'localized_G_orbits': gl})
    assert next(r for r in rows if r['n'] == 27)['classical_cusp_count'] == 6
    assert next(r for r in rows if r['n'] == 75)['classical_cusp_count'] == 12
    return rows


def unit_image():
    checked = 0
    for p in range(3, 120, 2):
        n = 2*p+1
        for a in range(1, n):
            if gcd(a, n) != 1:
                continue
            balanced = a if a <= p else a-n
            assert 0 < abs(balanced) <= p
            assert all(ell <= p and n % ell for ell in primes(abs(balanced)))
            checked += 1
    return checked


def local_density_crt():
    checked = 0
    for p, max_precision in ((3, 4), (5, 3), (7, 2), (13, 2), (31, 1)):
        n = 2*p+1
        for precision in range(1, max_precision+1):
            modulus = p**precision
            directions = [(1, t) for t in range(modulus)]
            directions += [(t, 1) for t in range(0, modulus, p)]
            for a, b in directions:
                for d in divisors(n):
                    x = a+modulus*((1-a)*pow(modulus, -1, n) % n)
                    y = b+modulus*((d-b)*pow(modulus, -1, n) % n)
                    content = gcd(x, y)
                    assert content and gcd(content, n*p) == 1
                    x, y = x//content, y//content
                    assert gcd(y, n) == d
                    assert (x*b-y*a) % modulus == 0
                    assert gcd(x, y, p) == 1
                    checked += 1
    return checked


def physical_returns_all_G():
    returns = atoms = 0
    for p in (3, 5, 7, 11, 13, 17, 31, 37):
        n = 2*p+1
        js = [j for j in range(1, p+1) if gcd(j, n) == 1]
        rs = [r for r in range(-p, p+1, 2) if gcd(r, n) == 1]
        for d in divisors(n):
            x, y = 1, d
            for typ, indices in (('t', js), ('f', rs)):
                for j in indices:
                    replay = Replay(p, x, x-y)
                    replay.letter((typ, j))
                    actual = replay.parameters()
                    if typ == 't':
                        expected = (F(-(p+1)*x+j*y, p), F(-n*x+2*j*y, p))
                    else:
                        expected = (x+F(j-p, 2*p)*y, F(j, p)*y)
                    assert actual == expected
                    assert state_G(replay.state) == d
                    returns += 1
                    atoms += replay.count
    return {'literal_returns_across_all_G_layers': returns, 'atomic_averages': atoms,
            'scope': 'Two-atom return formulas are replayed on legal and illegal cores. '
                     'No claim that arbitrary infinite-group words have been expanded.'}


def run():
    return {'status': 'PASS', 'arithmetic': arithmetic_identities(),
            'finite_orbits': exact_finite_orbits(), 'balanced_unit_lifts': unit_image(),
            'all_G_padic_density_crt_checks': local_density_crt(),
            'physical_returns': physical_returns_all_G(),
            'evidence_boundary': 'Finite exact audits of written identities and orbit classification. '
                                 'General Gamma0 containment reuses the established endpoint '
                                 'Morris/Serre proof; not inferred from finite group images. '
                                 'No new all-n threshold, shortest-path, or polynomial construction theorem.'}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    result = run()
    Path(__file__).with_name('endpoint_discriminant_G_orbits_verification.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    brief = {k: v for k, v in result.items() if k != 'finite_orbits'}
    brief['orbit_counts'] = [
        {k: row[k] for k in ('n', 'p', 'classical_cusp_count')} |
        {'G_orbit_count': len(row['localized_G_orbits'])}
        for row in result['finite_orbits']]
    print(json.dumps(brief, ensure_ascii=False, indent=2))
