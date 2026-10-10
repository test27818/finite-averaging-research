"""Check explicit common-shape entry and the full trace-zero output lattice.

No averaging-word or orbit search. Small bounded output fibers are enumerated
only to cross-check the proved lattice parametrization against raw inequalities.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import json
import sys
from time import perf_counter

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "work"))
from verify_four_prime_entry_and_band import Ledger
from verify_square_zero_compiler import check_frozen_files, check_local_links


def primes_below(limit):
    sieve = bytearray(b"\1") * limit
    sieve[:2] = b"\0\0"
    for q in range(2, int(limit ** 0.5) + 1):
        if sieve[q]:
            start = q * q
            sieve[start:limit:q] = b"\0" * ((limit - 1 - start) // q + 1)
    return [q for q in range(5, limit) if sieve[q]]


def entry_parameters(p, s):
    if s % 3:
        return s, 0
    rho = p % 3
    if rho == 1 and s == p - 1:
        return (p + 1) // 2, (p - 3) // 2
    u = s - 3 + rho
    return (p - u) // 3, u


def matrix(p, r, c, o):
    i, j, k = c
    x, y, u, v = o
    alpha, beta = i - j, r * j - p * k
    return (p * (x - y) + alpha * v,
            p * r * y - p * p * u + beta * v, -alpha, -beta)


def entry_check():
    instances = atoms = 0
    for p in primes_below(501):
        for s in range(1, p):
            t, u = entry_parameters(p, s)
            n, r, q = 3 * p + s, p + s, 3 * t + u
            assert 0 <= u <= s and s <= t + u <= p
            assert gcd(q, n) == 1
            # Integer numerator of the actual two-atom matrix; determinant
            # is st-pu and is congruent to -pq modulo n.
            assert (s * t - p * u + p * q) % n == 0
            instances += 1
            if p > 43:
                continue
            for a, z in ((F(1), F(0)), (F(0), F(1)), (F(5, 7), F(-3, 5))):
                raw = [a] * (2 * p) + [-2 * a + s * z] * p + [-p * z] * s
                ledger = Ledger(raw, p)
                ga, gb, gc = (list(range(2 * p)), list(range(2 * p, 3 * p)),
                              list(range(3 * p, n)))
                first = ga[:p - t - u] + gb[:t] + gc[:u]
                ledger.average(first)
                olda = ga[p - t - u:]
                carrier = olda[:r]
                second = olda[r:] + gb[t:] + gc[u:]
                assert len(carrier) == r and len(second) == p
                assert sorted(first + second + carrier) == list(range(n))
                ledger.average(second)
                aa = ((p - q) * a + (s * t - p * u) * z) / p
                zz = -a / p
                for group, value in ((first, aa), (second, r * zz - aa),
                                     (carrier, -p * zz)):
                    assert all(ledger.state[v] == value for v in group)
                ledger.independent_replay(raw)
                atoms += 2
    return instances, atoms


def ceildiv(a, b):
    return -(-a // b)


def fiber_check():
    sources = outputs = pair_checks = kernel_checks = disconnected = 0
    for p in (5, 7, 11, 13, 17):
        for r in range(1, 2 * p):
            if r == p:
                continue
            for i in range(p // 2 + 1):
                for j in range(i):
                    k = p - i - j
                    if k < 0 or 2 * k > r:
                        continue
                    c = (i, j, k)
                    alpha, beta = i - j, r * j - p * k
                    caps = (p - 2 * i, p - 2 * j, r - 2 * k, 2 * p - r)
                    v0 = beta * pow(alpha, -1, p) % p
                    t0 = (beta - alpha * v0) // p
                    # A fixed integral particular solution, not necessarily feasible.
                    o0 = (t0, 0, p - v0 - t0, v0)
                    b1, b2 = (-1, -1, 2, 0), (-i, -j, -k, p)
                    predicted = {}
                    e_intervals = []
                    hmax = (caps[3] - v0) // p
                    for h in range(hmax + 1):
                        base = tuple(o0[a] + h * b2[a] for a in range(4))
                        lo = max(base[0] - caps[0], base[1] - caps[1], ceildiv(-base[2], 2))
                        hi = min(base[0], base[1], (caps[2] - base[2]) // 2)
                        if lo <= hi:
                            e_intervals.append((lo, hi))
                        for e in range(lo, hi + 1):
                            o = tuple(base[a] + e * b1[a] for a in range(4))
                            predicted[o] = (h, e)
                    actual = set()
                    for x in range(caps[0] + 1):
                        for y in range(caps[1] + 1):
                            for v in range(min(p - x - y, caps[3]) + 1):
                                u = p - x - y - v
                                if 0 <= u <= caps[2] and p * (x - y) + alpha * v == beta:
                                    actual.add((x, y, u, v))
                    assert actual == set(predicted), (p, r, c, actual, predicted)
                    sources += 1
                    outputs += len(actual)
                    assert len(e_intervals) <= 2
                    if r > p:
                        assert len(e_intervals) <= 1
                    if len(e_intervals) == 2:
                        a, b = sorted(e_intervals)
                        disconnected += int(a[1] + 1 < b[0])
                    J0 = matrix(p, r, c, o0)
                    for o, (h, e) in predicted.items():
                        J = matrix(p, r, c, o)
                        assert J == (J0[0], J0[1] - e * p * (2 * p + r), J0[2], J0[3])
                        scalar = J[0] ** 2 + J[1] * J[2]
                        x, y, u, v = o
                        n = 2 * p + r
                        assert beta == n * j + p * alpha - p * p
                        assert J[1] == -p ** 3 + p * beta + n * (p * y + j * v)
                        assert J[1] - 2 * p * beta + p * p * alpha == n * (p * (y - j) + j * v)
                        assert scalar % p == 0
                        assert (scalar - p ** 4) % (2 * p + r) == 0
                        assert gcd(scalar, 2 * p + r) == 1 and scalar != 0
                        neighbor = tuple(o[a] + b1[a] for a in range(4))
                        if neighbor in actual:
                            K = matrix(p, r, c, neighbor)
                            scalar2 = K[0] ** 2 + K[1] * K[2]
                            assert scalar2 - scalar == alpha * p * (2 * p + r)
                            pair_checks += 1
                    # Arbitrary lattice differences, independent of capacity.
                    for h, e in ((-3, 2), (0, 5), (2, -4)):
                        delta = tuple(h * b2[a] + e * b1[a] for a in range(4))
                        assert sum(delta) == 0 and p * (delta[0] - delta[1]) + alpha * delta[3] == 0
                        hh = delta[3] // p
                        ee = -delta[1] - hh * j
                        assert (hh, ee) == (h, e)
                        kernel_checks += 1
    return {'source_fibers': sources, 'feasible_outputs': outputs,
            'adjacent_scalar_checks': pair_checks, 'kernel_reconstructions': kernel_checks,
            'two_interval_gap_diagnostics': disconnected}


def boundary_family():
    checked = 0
    for p in primes_below(501):
        r, c = 2 * p - 1, (1, 0, p - 1)
        cap = (p - 2, p, 1, 1)
        for v in range(2):
            # trace congruence forces v=0; then y-x=p-1.
            if v:
                assert (p * (p - 1) + v) % p
        o = (0, p - 1, 1, 0)
        assert all(0 <= o[i] <= cap[i] for i in range(4))
        J = matrix(p, r, c, o)
        assert J[0] + J[3] == 0
        scalar = J[0] ** 2 + J[1] * J[2]
        assert scalar == p * (p ** 3 - 4 * p ** 2 + 5 * p - 1)
        checked += 1
    return checked


def main():
    if not __debug__:
        raise RuntimeError('Assertions required')
    started = perf_counter()
    entries, atoms = entry_check()
    report = {'status': 'PASS', 'entry_formula_instances': entries,
              'entry_physical_atoms': atoms, **fiber_check(),
              'singleton_boundary_family': boundary_family(),
              'frozen_files': check_frozen_files(), 'local_links': check_local_links()}
    report['seconds'] = round(perf_counter() - started, 3)
    report['scope'] = ('Explicit entry and lattice identities. Small fibers validate the exact '
                       'parametrization; no word search and no proof of full terminal reachability.')
    (HERE / 'common_shape_relation_lattice_verification.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
