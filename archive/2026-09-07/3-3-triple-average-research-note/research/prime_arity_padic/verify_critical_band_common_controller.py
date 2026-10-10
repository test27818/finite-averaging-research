"""Closed count rules across the critical band; no averaging-word search.

One or two identical source groups feed the same reflection matrix. Existing
root/deep-kernel theorems remain mathematical dependencies, not tested claims.
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
from verify_common_shape_and_relation_lattice import primes_below, matrix
from verify_four_prime_entry_and_band import Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout
from verify_upper_band_unrestricted_completion import zy
from verify_two_root_column_completion import powq, scale, det, red
from verify_even_odd_half_core import mod_power
from verify_split_torus_column import column
from verify_square_zero_compiler import check_frozen_files, check_local_links

ID = (1, 0, 0, 1)


def cd(a, b):
    return -(-a // b)


def cutoff(p):
    # Exact integer cube root by doubling and binary search.
    low, high = 0, 1
    while 4 * high ** 3 < p:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if 4 * middle ** 3 >= p:
            high = middle
        else:
            low = middle
    return 4 * max(3, high)


def old_small_pair(p, s, a, h):
    i, j, k = a * (h + 1), a * h, p - a * (2 * h + 1)
    e = max(0, a * (3 * h + 2) - p, cd((s - a) * h - a, 2))
    # This is the existing p>=83 capacity formula, with only two rows needed.
    return [(i, j, k, j - e - d, k - e - d,
             (a - s) * h + a + 2 * (e + d), s * h) for d in (0, 1)]


def supply(p, r):
    assert p >= 83 and cutoff(p) <= r < 2 * p and r != p
    s = r - p
    pairs = []
    if r < cd(p, 3) + 4:
        q = 1
        t = min(r // 4, p // r)
        h = t - 1
        a0 = cd(p - r + 3, 2 * h + 1)
        lo = cd(p - r * (h + 1), 2)
        for a in (a0, a0 + 1):
            k = p - (2 * h + 1) * a
            hi = min(p - a * (h + 1), a * (h + 1), ((2 * h + 1) * a - r * h) // 2)
            assert lo + 1 <= hi
            rows = [(a * (h + 1), a * h, k, l, k + l,
                     (2 * h + 1) * a - r * h - 2 * l, r * h)
                    for l in (lo + 1, lo)]
            pairs.append((q, rows))
        chart = 'one_source_balanced'
    elif r < p or 2 * r > 3 * p:
        q = 1 if r < p else 2
        d = q * p - r
        a0 = cd(d + 4, q)
        for a in (a0, a0 + 1):
            lo = max(0, cd(d - (q - 1) * a, 2))
            hi = min(a // 2, p - q * a)
            assert lo + 1 <= hi, (p, r, q, a, lo, hi)
            # l falls by one, hence the output moves by (-1,-1,2,0).
            rows = [(a, 0, p - a, l, p - a + l, a - 2 * l, 0)
                    for l in (lo + 1, lo)]
            pairs.append((q, rows))
        chart = 'carrier_margin'
    elif s <= 9:
        q = 2
        a0 = s // 3 + 1
        for a in (a0, a0 + 1):
            for h in (p // (3 * a) - 1, p // (3 * a)):
                pairs.append((q, old_small_pair(p, s, a, h)))
        chart = 'small_offset_existing_formula'
    else:
        q = 2
        a0 = cd(p, 6)
        for a in (a0, a0 + 1):
            lo = max(5 * a - p, cd(s, 2) - a)
            hi = min(a, 2 * a + s - (p + 1) // 2)
            assert lo + 1 <= hi, (p, r, a, lo, hi)
            rows = [(2 * a, a, p - 3 * a, a - e, p - 3 * a - e,
                     2 * a - s + 2 * e, s) for e in (lo, lo + 1)]
            pairs.append((q, rows))
        chart = 'balanced_source'
    return chart, pairs


def check_row(p, r, q, row):
    i, j, k, x, y, u, v = row
    assert min(row) >= 0 and i + j + k == x + y + u + v == p
    caps = (p - q * i, p - q * j, r - q * k, q * p - r)
    assert min(caps) >= 0 and all(a <= b for a, b in zip(row[3:], caps))
    J = matrix(p, r, row[:3], row[3:])
    assert J[0] + J[3] == 0
    pf = -det(J)
    assert mm(J, J) == scale(pf, ID) and pf % p == 0
    n = 2 * p + r
    assert (pf - p ** 4) % n == 0 and gcd(pf, n) == 1
    return J, pf // p


def check_supply(p, r):
    chart, pairs = supply(p, r)
    delta = 0
    alphas = []
    D = p
    refs = []
    n = 2 * p + r
    S = (-1, r, 0, 1)
    for q, rows in pairs:
        J, f = check_row(p, r, q, rows[0])
        K, g = check_row(p, r, q, rows[1])
        a, j = rows[0][0] - rows[0][1], rows[0][1]
        assert gcd(f, g) == 1 and g - f == a * n
        H = n * (2 * j + a) - 2 * p * p
        T = mm(invq(J), K)
        assert T == (1, -F(J[0] * n, f), 0, F(g, f))
        comm = mm(mm(mm(S, T), S), invq(T))
        assert comm == (1, F(n * H, g), 0, 1)
        delta = gcd(delta, H)
        D *= abs(f * g)
        alphas.append(a)
        refs.append(scale(F(1, p * p), zy(J, p)))
    assert delta == gcd(n, 2)
    d, coeff = 0, []
    for a in alphas:
        dn, x, y = bezout(d, a)
        coeff = [x * c for c in coeff] + [y]
        d = dn
    assert d == 1
    Swap = (1, 0, n, -1)
    V = ID
    for c, J in zip(coeff, refs):
        V = mm(powq(mm(Swap, J), c), V)
    assert red(V, n) == (1, residue(F(-1, p * p), n), 0, 1)
    if n % 2:
        assert D % 2 == 0
    return chart, pairs, delta, V


def replay(p, r, q, row):
    J, f = check_row(p, r, q, row)
    n = 2 * p + r
    atoms = 0
    for a, z in ((F(1), F(0)), (F(0), F(1)), (F(2, 3), F(-5, 7))):
        raw = [a] * p + [r * z - a] * p + [-p * z] * r
        ledger = Ledger(raw, p)
        groups = [list(range(p)), list(range(p, 2 * p)), list(range(2 * p, n))]
        for repeat in (1, 2):
            ga, gb, gc = groups
            i, j, k, x, y, u, v = row
            fresh = []
            for step in range(q):
                selected = ga[step * i:(step + 1) * i] + gb[step * j:(step + 1) * j] + gc[step * k:(step + 1) * k]
                ledger.average(selected)
                fresh += selected
            ga, gb, gc = ga[q * i:], gb[q * j:], gc[q * k:]
            keep, fresh = fresh[:r], fresh[r:]
            left = ga[:x] + gb[:y] + gc[:u] + fresh[:v]
            right = ga[x:] + gb[y:] + gc[u:] + fresh[v:]
            assert len(keep) == r and len(left) == len(right) == p
            assert sorted(left + right + keep) == list(range(n))
            ledger.average(left)
            ledger.average(right)
            groups = [left, right, keep]
            atoms += q + 2
            if repeat == 1:
                aa = (J[0] * a + J[1] * z) / (p * p)
                zz = (J[2] * a + J[3] * z) / (p * p)
            else:
                aa, zz = F(f, p ** 3) * a, F(f, p ** 3) * z
            for group, target in zip(groups, (aa, r * zz - aa, -p * zz)):
                assert all(ledger.state[v] == target for v in group)
        ledger.independent_replay(raw)
    return atoms


def shifted_terminal_transport(p, r, delta, V, z, y, eps):
    # The existing compiler selects j=0 or1. To use arbitrary r, its target
    # can instead be any congruent j; copy only its short deterministic core.
    from verify_split_torus_column import digit, dyadic_unit_word
    from verify_two_root_column_completion import oddpart, crt2, act
    from math import lcm
    n = 2 * p + r
    h, m = delta * n, oddpart(n)
    Q = h * h
    two, M = h // m, (h // m) ** 2
    w = (residue(z, Q), residue(y, Q))
    eps = residue(eps, Q)
    assert w[0] % n == eps % n and w[1] % n == eps * p * p % n
    if n % 2 == 0:
        q = digit(p, n)
        sign, power = dyadic_unit_word(q, w[0] * pow(eps, -1, M) % M, M)
        torus = (F(1, q), 0, (n // 2) * (F(1, q) - 1), 1)
        w = act(mod_power(torus, power, Q), w, Q)
        if sign == -1:
            w = act((-1, 0, -n, 1), w, Q)
        assert red(mod_power(V, M, M), M) == ID
        if m > 1:
            exponent = M * (p * p * (w[0] - eps) * pow(w[1], -1, m) * pow(M, -1, m) % m)
            w = act(mod_power(V, exponent, Q), w, Q)
        assert (w[0] - eps) % M == 0
    start = max(0, cd(p - 1 - r, 2))
    jres = ((eps * p * p - w[1]) // n) * pow(eps, -1, delta) % delta if delta > 1 else 0
    j = start + (jres - start) % delta
    k = p - 1 - 2 * j
    assert 0 <= k <= r and 2 * j + 1 <= p
    goal = (eps, eps * (p * p - n * j))
    assert all((w[i] - goal[i]) % h == 0 for i in range(2))
    E = (0, 0, 1, 0)
    X = mm(mm(V, E), invq(V))
    den = lcm(*(F(a).denominator for a in X))
    if m > 1:
        rhs = ((goal[0] - w[0]) // h % m, (goal[1] - w[1]) // h % m)
        c0, c1 = act(scale(den, E), goal, m), act(scale(den, X), goal, m)
        u1 = rhs[0] * pow(c1[0], -1, m) % m
        u0 = (rhs[1] - u1 * c1[1]) * pow(c0[1], -1, m) % m
        for root, u in ((E, u0), (X, u1)):
            u = crt2(u, m, 0, two)
            w = act(tuple(ID[i] + h * den * u * root[i] for i in range(4)), w, Q)
    if two > 1:
        t = crt2(((goal[1] - w[1]) // h) * pow(w[0], -1, two) % two, two, 0, m)
        w = act((1, 0, h * t, 1), w, Q)
    assert w == tuple(g % Q for g in goal)
    # Literal terminal on the unscaled integer representative.
    a, zz = p * p - n * j - p, 1
    raw = [F(a)] * p + [F(r - a)] * p + [F(-p)] * r
    selected = list(range(j + 1)) + list(range(p, p + j)) + list(range(2 * p, 2 * p + k))
    assert len(selected) == p and sum(raw[i] for i in selected) == 0
    return j


def unit_lemma_checks():
    checks = 0
    for p in primes_below(160):
        for n in range(2 * p + 1, 4 * p):
            if n % p == 0:
                continue
            units = [x for x in range(1, n) if gcd(x, n) == 1]
            if n % 2:
                for x in units:
                    a = min(x, n - x)
                    while a > p:
                        b = abs((4 if 3 * a < n else 2) * a - n)
                        assert 0 < b < a and gcd(b, n) == 1
                        a = b
                    checks += 1
            elif n % 4 == 2:
                m = n // 2
                q = (m + (1 if m % 4 == 1 else -1)) // 2
                assert q % 2 and q <= p and gcd(q, n) == 1 and (2 * q) % m in (1, m - 1)
                for x in units:
                    a = x % m
                    a = min(a, m - a)
                    while a % 2 == 0:
                        a //= 2
                    assert a <= p and a % 2 and gcd(a, n) == 1
                    checks += 1
            else:
                low = [x for x in units if 4 * x < n]
                assert 4 * len(low) == len(units)
                assert gcd(p, n) == 1 and n // 4 < p < n // 2
                checks += 1
    return checks


def large_boundary_checks():
    count = 0
    examples = []
    for p in (1009, 10007, 1000003, 1000000007, 2305843009213693951):
        for r in sorted({cutoff(p), cutoff(p) + 1, cd(p, 3) + 3, cd(p, 3) + 4,
                         p - 1, p + 1, p + 9, p + 10, p + p // 2,
                         p + p // 2 + 1, 2 * p - 1}):
            _, pairs = supply(p, r)
            roots = []
            for q, rows in pairs:
                J, f = check_row(p, r, q, rows[0])
                K, g = check_row(p, r, q, rows[1])
                a = rows[0][0] - rows[0][1]
                assert g - f == a * (2 * p + r) and gcd(f, g) == 1
                roots.append((2 * p + r) * (rows[0][0] + rows[0][1]) - 2 * p * p)
            assert gcd(*roots) == gcd(2 * p + r, 2)
            count += 1
        examples.append({'p': p, 'r0': cutoff(p)})
    return count, examples


def main():
    if not __debug__:
        raise RuntimeError('Assertions required')
    started = perf_counter()
    counts = {}
    cases = 0
    # Only integer capacity/scalar checks on the broad grid. Fractional group
    # identities and transport are tested on branch endpoints below.
    for p in primes_below(1000):
        if p < 83:
            continue
        for r in range(cutoff(p), 2 * p):
            if r == p:
                continue
            chart, pairs = supply(p, r)
            alphas, roots = [], []
            n = 2 * p + r
            for q, rows in pairs:
                J, f = check_row(p, r, q, rows[0])
                K, g = check_row(p, r, q, rows[1])
                a = rows[0][0] - rows[0][1]
                assert gcd(f, g) == 1 and g - f == a * n
                alphas.append(a)
                roots.append(n * (rows[0][0] + rows[0][1]) - 2 * p * p)
            assert gcd(*alphas) == 1 and gcd(*roots) == gcd(n, 2)
            counts[chart] = counts.get(chart, 0) + 1
            cases += 1
    atoms = transports = interfaces = 0
    for p in (83, 89, 97, 101, 307):
        for r in sorted({cutoff(p), cutoff(p) + 1, cd(p, 3) + 3,
                         cd(p, 3) + 4, p // 2, p - 2, p - 1, p + 1, p + 9,
                         p + 10, 3 * p // 2, 3 * p // 2 + 1, 2 * p - 2, 2 * p - 1}):
            chart, pairs, delta, V = check_supply(p, r)
            n, h = 2 * p + r, delta * (2 * p + r)
            for seed in range(6):
                eps = 1 if seed < 4 else F(1, p)
                z = eps + n * (seed - 3)
                y = eps * p * p + n * (seed * seed - 5)
                shifted_terminal_transport(p, r, delta, V, z, y, eps)
                transports += 1
            interfaces += 1
            if p in (83, 89):
                for q, rows in pairs:
                    for row in rows:
                        atoms += replay(p, r, q, row)
    large_count, examples = large_boundary_checks()
    report = {'status': 'PASS', 'formula_parameter_cases': cases, 'capacity_charts': counts,
              'exact_group_interfaces': interfaces, 'column_transports': transports,
              'literal_source_return_atoms': atoms, 'unit_lemma_checks': unit_lemma_checks(),
              'large_integer_boundary_checks': large_count, 'cutoff_examples': examples,
              'frozen_files': check_frozen_files(), 'local_links': check_local_links(),
              'seconds': round(perf_counter() - started, 3),
              'scope': 'Closed counts and complete finite terminal interface; no word search. '
                       'Infinite group containment and existing entry/tail proofs are retained dependencies.'}
    (HERE / 'critical_band_common_controller_verification.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
