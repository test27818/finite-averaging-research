"""Join all small remainders >=3 to the common terminal interface.

Closed old-carrier rows, a proved short arithmetic progression for one digit,
and exact common column transport. No averaging-word or orbit search.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from time import perf_counter
import json
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'work'))
from verify_critical_band_common_controller import cutoff, primes_below, shifted_terminal_transport
from verify_four_prime_entry_and_band import Ledger
from verify_uniform_odd_middle_cores import mm, invq
from verify_upper_band_unrestricted_completion import zy
from verify_two_root_column_completion import scale, powq, red
from verify_square_zero_compiler import check_frozen_files, check_local_links

ID = (1, 0, 0, 1)


def repair_digit(p, r):
    assert r % 4 == 0 and 6 * r <= p
    lower = 2 * r - 1
    first = lower + (p - 2 - lower) % 4
    for q in range(first, p - 1, 4):
        if gcd(q, 2 * p + r) == 1:
            return q
    raise AssertionError(('proved progression unexpectedly empty', p, r))


def retained_matrix(p, r, j, s):
    i = p - j - s
    assert 0 <= i <= p - r and 0 <= j <= p and 0 <= s <= r
    return (p - 2 * j - s, r * j - p * s, -1, 0)


def data(p, r):
    n = 2 * p + r
    assert p >= 83 and 3 <= r < cutoff(p) and 6 * r <= p
    s0 = r if r % 2 else r - 1
    d = (p * r - n * s0) // 2
    e = d + n
    J = retained_matrix(p, r, (p - s0) // 2, s0)
    K = retained_matrix(p, r, (p - s0 + 2) // 2, s0 - 2)
    assert J == (0, d, -1, 0) and K == (0, e, -1, 0)
    assert gcd(d, e) == gcd(d * e, n) == 1
    T = mm(invq(J), K)
    S = (-1, r, 0, 1)
    root = mm(mm(mm(S, T), S), invq(T))
    assert root == (1, F(r * n, e), 0, 1)
    rows = [((p - s0) // 2, s0), ((p - s0 + 2) // 2, s0 - 2)]
    if r % 2:
        assert d % r == 0 and (d * e) % 2 == 0
        delta = 1
    else:
        t = r // 2
        odd = t
        while odd % 2 == 0:
            odd //= 2
        m = p + t
        # The existing sandwich activates every odd factor of t.
        C = (1, 0, 0, odd)
        Juv = (-t, -1, m * (t - s0), t)
        H = scale(F(1, odd), mm(mm(C, Juv), C))
        assert all(F(x).denominator == 1 for x in H)
        assert H[0] * H[3] - H[1] * H[2] == d
        assert mm(mm(Juv, C), invq(H)) == scale(odd, invq(C))
        delta = 2
        if r % 4 == 0:
            q = repair_digit(p, r)
            j = (q - 1) // 2
            M = retained_matrix(p, r, j, 1)
            a, D = M[0], M[1]
            assert a % 4 == 2 and gcd(D, r * n) == 1
            T = mm(M, invq(J))
            repair = mm(mm(mm(S, T), S), invq(T))
            value = 2 * a + r * (1 - F(D, d))
            assert repair == (1, value, 0, 1)
            assert value / n == F((2 - r) * (a + r), 2 * d)
            c = F(value / n)
            assert c.denominator % 2 and c.numerator % 4 == 2
            twopart = r // gcd(r, odd)
            assert gcd(twopart, abs(c.numerator)) == 2
            rows.append((j, 1))
    # J/p has modular translation -1/p after role swap.
    T = mm((1, 0, n, -1), scale(F(1, p), zy(J, p)))
    assert red(T, n) == (1, -pow(p, -1, n) % n, 0, 1)
    V = powq(T, pow(p, -1, n))
    assert red(V, n) == (1, -pow(p * p, -1, n) % n, 0, 1)
    return delta, V, rows


def replay(p, r, j, s):
    mat = retained_matrix(p, r, j, s)
    atoms = 0
    for a, z in ((F(1), F(0)), (F(0), F(1)), (F(2, 3), F(-5, 7))):
        raw = [a] * p + [r * z - a] * p + [-p * z] * r
        led = Ledger(raw, p)
        ga, gb, gc = list(range(p)), list(range(p, 2 * p)), list(range(2 * p, 2 * p + r))
        keep = ga[:r]
        ga = ga[r:]
        i = p - j - s
        left = ga[:i] + gb[:j] + gc[:s]
        right = ga[i:] + gb[j:] + gc[s:]
        assert len(left) == len(right) == p
        assert sorted(left + right + keep) == list(range(2 * p + r))
        led.average(left)
        led.average(right)
        aa, zz = (mat[0] * a + mat[1] * z) / p, -a / p
        for group, value in ((left, aa), (right, r * zz - aa), (keep, -p * zz)):
            assert all(led.state[v] == value for v in group)
        led.independent_replay(raw)
        atoms += 2
    return atoms


def main():
    if not __debug__:
        raise RuntimeError('Assertions required')
    started = perf_counter()
    capacities = repairs = transports = atoms = endpoint_transports = 0
    # Large exact powers are unnecessary for the broad grid.
    for p in primes_below(5000):
        if p < 83:
            continue
        for r in range(3, cutoff(p)):
            assert 6 * r <= p
            s = r if r % 2 else r - 1
            d = (p * r - (2 * p + r) * s) // 2
            e = d + 2 * p + r
            assert gcd(d, e) == gcd(d * e, 2 * p + r) == 1
            retained_matrix(p, r, (p - s) // 2, s)
            retained_matrix(p, r, (p - s + 2) // 2, s - 2)
            if r % 4 == 0:
                q = repair_digit(p, r)
                a = p - q
                D = r * ((q - 1) // 2) - p
                assert gcd(D, r * (2 * p + r)) == 1
                assert 2 * a * d + r * (d - D) == (2 * p + r) * (2 - r) * (a + r) // 2
                repairs += 1
            capacities += 1
    for p in (83, 89, 97, 101, 251, 1153):
        n = 2 * p + 1
        C = (2, -1, n, -p)
        V = mm(mm(C, (1, F(-1, 4 * p * p), 0, 1)), invq(C))
        assert red(V, n) == (1, -pow(p * p, -1, n) % n, 0, 1)
        for seed in range(3):
            shifted_terminal_transport(p, 1, 1, V,
                1 + n * (seed - 2), p * p + n * (seed * seed - 3), 1)
            endpoint_transports += 1
        for r in range(3, cutoff(p)):
            delta, V, rows = data(p, r)
            n = 2 * p + r
            for seed in range(3):
                eps = F(1, p) if seed == 2 else F(1)
                shifted_terminal_transport(p, r, delta, V,
                    eps + n * (seed - 2), eps * p * p + n * (seed * seed - 3), eps)
                transports += 1
            if p in (83, 89):
                for j, s in rows:
                    atoms += replay(p, r, j, s)
    report = {'status': 'PASS', 'small_remainder_formula_cases': capacities,
              'dyadic_repair_cases': repairs, 'common_terminal_transports': transports,
              'endpoint_common_terminal_transports': endpoint_transports,
              'retained_carrier_literal_atoms': atoms, 'frozen_files': check_frozen_files(),
              'local_links': check_local_links(), 'seconds': round(perf_counter() - started, 3),
              'scope': 'Explicit retained-carrier counts, root identities and shared terminal interface. '
                       'No averaging-word search. Existing deep-kernel, inverse-activation and tail theorems retained.'}
    (HERE / 'retained_carrier_bridge_verification.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
