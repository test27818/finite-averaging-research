"""Uniform even-core completion for r=2t, odd t>=3, 3t<=p.

Checks fixed original-position returns, arithmetic unit lifts and terminal
matrices. Infinite group containment uses the cited Morris/Serre theorems;
this script neither searches averaging words nor infers infinite coverage.
"""

from fractions import Fraction as F
from functools import cache
from math import gcd, lcm, prod
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, factors, triple_return, is_legal
from verify_uniform_odd_middle_cores import mm, invq, bezout, normalize_pair, residue
from verify_unrestricted_endpoint_entry import unrestricted_two_blocks, forced_input
from verify_upper_band_three_value_reduction import full_support
from verify_uniform_two_block_entry import transfer, replay as replay_core

ROOT = Path(__file__).parent
I = (1, 0, 0, 1)
S = (1, 0, 0, -1)

if not __debug__:
    raise RuntimeError("Assertions are required.")


def U(value):
    return (1, value, 0, 1)


def L(value):
    return (1, 0, value, 1)


@cache
def params(p, t):
    assert p >= 3*t and t >= 3 and t % 2 and factors(p) == {p: 1}
    m = p+t
    n = 2*m
    level = 2*n
    auxiliary = t*t+n
    assert gcd(t, n) == gcd(p, level) == gcd(auxiliary, level) == 1
    j0 = (-t, -1, 0, t)
    j1 = (-t, -1, -n, t)
    assert mm(j0, j0) == (t*t, 0, 0, t*t)
    assert mm(j1, j1) == (auxiliary, 0, 0, auxiliary)
    assert tuple(F(x, -t) for x in mm(S, j0)) == U(F(1, t))
    h = mm(j1, invq(j0))
    kappa = F(auxiliary, t*t)
    assert h == (1, 0, F(n, t), kappa)
    root = mm(mm(mm(S, h), S), invq(h))
    assert root == L(F(-2*n, t))
    assert mm(mm(h, L(1)), invq(h)) == L(kappa)
    common, x, y = bezout(auxiliary, t*t)
    assert common == 1
    assert x*kappa+y == F(1, t*t)
    assert x+y/kappa == F(1, auxiliary)
    # In the original (a,z) basis the same pair gives the deep-congruence roots.
    ja, jb, reflection = (0, -t*t, -1, 0), (0, -auxiliary, -1, 0), (-1, 2*t, 0, 1)
    diagonal = mm(invq(ja), jb)
    upper = mm(mm(mm(reflection, diagonal), reflection), invq(diagonal))
    assert upper == U(F(2*t*n, auxiliary))
    # Adding an integer upper root to a deep root supplies arbitrary R0 values.
    for value in (F(1, t**3), F(1, auxiliary**2), F(t+1, t*auxiliary)):
        integer = residue(value, level**2)
        coefficient = (value-integer)/(level**2)
        assert gcd(coefficient.denominator, level) == 1
        assert integer+level**2*coefficient == value
    return m, n, level, auxiliary, j0, j1


@cache
def kernel_units(p, t):
    m, n, level, auxiliary, _, _ = params(p, t)
    h1, h2 = F(-p, t), F(auxiliary, t*t)
    units = (F(1), h2, h1, h1*h2)
    assert {residue(h, level) for h in units} == {(1+k*m) % level for k in range(4)}
    return units


def choose_unit(p, t, wanted):
    m, n, level, _, _, _ = params(p, t)
    assert gcd(wanted, level) == 1
    small = wanted % m
    if 2*small > m:
        small -= m
    assert small and small % 2 and 2*abs(small) <= m and abs(small) <= p
    unit = next(h for h in kernel_units(p, t) if residue(h*small, level) == wanted % level)
    return small, unit


def activate_p_inverse(p, t):
    _, _, level, _, _, _ = params(p, t)
    order = level
    for q in factors(level):
        order = order//q*(q-1)
    for q in factors(order):
        while order % q == 0 and pow(p, order//q, level) == 1:
            order //= q
    delta = p**order
    assert delta % level == 1
    a = -level*pow(level, -1, delta)
    g = mm(mm(U(a), L(-a)), U(a))
    assert tuple(x % level for x in g) == I
    assert tuple(x % delta for x in g) == (0, delta-1, 1, 0)
    matrix = (delta, 0, 0, 1)
    hq = tuple(F(x, delta) for x in mm(mm(matrix, g), matrix))
    assert all(x.denominator == 1 for x in hq)
    h = tuple(int(x) for x in hq)
    assert h[0]*h[3]-h[1]*h[2] == 1 and tuple(x % level for x in h) == I
    assert mm(mm(g, matrix), invq(h)) == (1, 0, 0, delta)
    return order, max(abs(x).bit_length() for x in g+h)


def transport(u, v, p, t):
    m, n, level, auxiliary, _, _ = params(p, t)
    assert gcd(u, v) == gcd(v, m) == 1
    small, kernel = choose_unit(p, t, pow(v, -1, level))
    epsilon = 1/kernel
    primes = tuple(factors(abs(small)))
    radical = prod(primes)
    shift = sum(radical//q*pow(radical//q, -1, q) for q in primes if u % q == 0) % radical
    prepared = u+shift*v
    assert gcd(prepared, small) == gcd(prepared, v) == 1
    scaled_v = small*v
    assert residue(scaled_v-epsilon, level) == 0
    final_shift = -prepared*pow(scaled_v, -1, level) % level
    if 2*final_shift > level:
        final_shift -= level
    final_u = prepared+final_shift*scaled_v
    assert final_u % level == 0 and gcd(final_u, scaled_v) == 1
    common, a, b = bezout(final_u, scaled_v)
    assert common == 1
    adjust = residue(-epsilon*a, level)*pow(scaled_v, -1, level) % level
    alpha = epsilon*a+adjust*scaled_v
    beta = epsilon*b-adjust*final_u
    matrix = (scaled_v/epsilon, -final_u/epsilon, alpha, beta)
    assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == 1
    assert tuple(residue(x, level) for x in matrix) == I
    assert matrix[0]*final_u+matrix[1]*scaled_v == 0
    assert matrix[2]*final_u+matrix[3]*scaled_v == epsilon
    allowed = set(factors(p*t*auxiliary))
    assert all(set(factors(F(x).denominator)) <= allowed for x in matrix)
    total = mm(matrix, mm(U(final_shift), mm((1, 0, 0, small), U(shift))))
    assert total[0]*u+total[1]*v == 0 and total[2]*u+total[3]*v == epsilon
    return {"uv": [u, v], "small_multiplier": small, "unit": str(epsilon),
            "upper_shifts": [shift, final_shift],
            "principal_terminal_matrix": [str(x) for x in matrix]}


def zero_tail(ledger):
    p = ledger.p
    for count in ((p-1)//2, (p-1)//2, 1):
        plus = [i for i, value in enumerate(ledger.state) if value > 0]
        minus = [i for i, value in enumerate(ledger.state) if value < 0]
        zeros = [i for i, value in enumerate(ledger.state) if value == 0]
        assert ledger.state[plus[0]] == -ledger.state[minus[0]]
        ledger.average(plus[:count]+minus[:count]+zeros[:p-2*count])
    assert not any(ledger.state)


def physical_pair(ledger, groups, p, t):
    a, b, c = (ledger.state[g[0]] for g in groups)
    u, v = -c/p, (a-b)/2
    assert a == t*u+v and b == t*u-v
    return u, v


def literal_checks():
    identities = 0
    complete = []
    for p, t in ((11, 3), (13, 3), (17, 5), (23, 7), (31, 9)):
        m, n, level, auxiliary, j0, j1 = params(p, t)
        for u, v in ((1, 0), (0, 1), (-2, t)):
            raw = [t*u+v]*p+[t*u-v]*p+[-p*u]*(2*t)
            groups0 = [list(range(p)), list(range(p, 2*p)), list(range(2*p, n))]
            for plan in (("0", "s"), ("+", "0", "s", "0", "+", "s")):
                ledger = Ledger(raw, p)
                groups = [g[:] for g in groups0]
                matrix = I
                for step in plan:
                    if step == "s":
                        groups[0], groups[1] = groups[1], groups[0]
                        matrix = mm(S, matrix)
                    else:
                        s = t if step == "0" else t+2
                        groups = list(triple_return(ledger, groups, p, 2*t, s))
                        factor = j0 if step == "0" else j1
                        matrix = mm(tuple(F(x, p) for x in factor), matrix)
                got = physical_pair(ledger, groups, p, t)
                assert got == (matrix[0]*u+matrix[1]*v, matrix[2]*u+matrix[3]*v)
                if plan == ("0", "s"):
                    assert got == (F(-t*u-v, p), F(-t*v, p))
                else:
                    assert got[1]*u == got[0]*(v-F(2*n, t)*u)
                ledger.independent_replay(raw)
                if gcd(u, v) == gcd(v, m) == 1:
                    assert is_legal(ledger.state, factors(n))
                identities += 1
        raw = [-t]*p+[-3*t]*p+[2*p]*(2*t)
        ledger = Ledger(raw, p)
        groups = [g[:] for g in groups0]
        for _ in range(2):
            groups = list(triple_return(ledger, groups, p, 2*t, t))
            groups[0], groups[1] = groups[1], groups[0]
        assert physical_pair(ledger, groups, p, t)[0] == 0
        zero_tail(ledger)
        ledger.independent_replay(raw)
        assert len(ledger.word) == 7
        complete.append({"p": p, "t": t, "input": raw, "operations": ledger.word})
    print("odd-half even-core literal upper and lower roots: PASS", identities)
    print("uniform seven-atom full zero paths: PASS", len(complete))
    return complete


def finite_ring_checks():
    count = 0
    for modulus, level in ((8, 2), (16, 4), (24, 4), (36, 6), (40, 8)):
        for a in range(1, modulus, level):
            for c in range(0, modulus, level):
                for d in range(1, modulus, level):
                    for b in range(modulus):
                        if (a*d-b*c) % modulus == 1:
                            primes = tuple(factors(modulus))
                            radical = prod(primes)
                            k = sum(radical//q*pow(radical//q, -1, q)
                                    for q in primes if a % q == 0) % radical
                            pivot = (a+k*c) % modulus
                            other = (b+k*d) % modulus
                            reciprocal = pow(pivot, -1, modulus)
                            word = [U(-k), L(c*reciprocal), U(1), L(pivot-1),
                                    U(-reciprocal), L(-pivot*(pivot-1)), U(other*reciprocal)]
                            result = I
                            for atom in word:
                                assert atom[2] % level == 0
                                result = tuple(x % modulus for x in mm(result, atom))
                            assert result == (a, b, c, d)
                            count += 1
    print("Gamma1 finite-ring elimination including even levels: PASS", count)
    return count


def run():
    rng = Random(2026091513)
    systems = units = 0
    transports = []
    inverse_records = []
    for p in (11, 13, 17, 19, 23, 29, 31, 41, 59, 83, 127):
        for t in range(3, p//3+1, 2):
            m, n, level, auxiliary, _, _ = params(p, t)
            systems += 1
            for wanted in range(level):
                if gcd(wanted, level) == 1:
                    choose_unit(p, t, wanted)
                    units += 1
            for _ in range(8):
                while True:
                    u, v = rng.randrange(-10**6, 10**6), rng.randrange(1, 10**6)
                    if gcd(u, v) == gcd(v, m) == 1:
                        break
                record = transport(u, v, p, t)
                record.update({"p": p, "t": t, "n": n})
                transports.append(record)
            if t == 3 or (p, t) in ((17, 5), (31, 9)):
                inverse_records.append({"p": p, "t": t, "order_bits": activate_p_inverse(p, t)})
    print("odd-half even-core uniform algebra systems: PASS", systems)
    print("all finite unit classes have small realizable representatives: PASS", units)
    print("exact principal terminal transports: PASS", len(transports))
    print("positive p-inverse activation identities: PASS", len(inverse_records))
    full_paths = literal_checks()
    entries = []
    for p, t in ((11, 3), (17, 3), (17, 5)):
        r = 2*t
        raw = forced_input(p, r)
        ledger, first, second, singles, record = unrestricted_two_blocks(raw, p, r, range(p))
        primes = tuple(factors(len(raw)))
        anchor = singles[0]
        first, second, singles, _ = full_support(ledger, first, second, singles, anchor, primes)
        first, second, singles, _ = transfer(ledger, first, second, singles, anchor, primes)
        merged, kept = first[:p-r]+singles, first[p-r:]
        ledger.average(merged)
        groups = [merged, second, kept]
        replay_core(raw, ledger, groups, p, r)
        u, v = normalize_pair(*physical_pair(ledger, groups, p, t))
        if u == 0:
            terminal = {"already_terminal": True}
        else:
            terminal = transport(u, v, p, t)
        entries.append({"p": p, "t": t, "input": raw, "operations": ledger.word,
                        "groups": groups, "abstract_terminal_transport": terminal})
    print("unrestricted input entry joined to even-core terminal matrix: PASS", len(entries))
    finite = finite_ring_checks()
    return {"systems": systems, "unit_classes": units, "transports": transports,
            "inverse_activation": inverse_records, "literal_full_paths": full_paths,
            "input_entries": entries, "finite_ring_checks": finite,
            "scope": "Full r=2t core and all-input theorem for odd t>=3, 3t<=p follows "
                     "from written proof and stated Morris/Serre dependencies. Finite "
                     "checks do not prove infinite group containment or compile "
                     "arbitrary principal matrices to short physical words."}


def mod_power(matrix, exponent, modulus):
    matrix = tuple(residue(x, modulus) for x in matrix)
    result = tuple(x % modulus for x in I)
    while exponent:
        if exponent & 1:
            result = tuple(x % modulus for x in mm(result, matrix))
        matrix = tuple(x % modulus for x in mm(matrix, matrix))
        exponent //= 2
    return result


def valuation(value, q):
    answer = 0
    while value % q == 0:
        answer += 1
        value //= q
    return answer


def crt_pairs(pairs):
    value, modulus = 0, 1
    for wanted, new_modulus in pairs:
        if new_modulus == 1:
            continue
        value += modulus*((wanted-value)*pow(modulus, -1, new_modulus) % new_modulus)
        modulus *= new_modulus
    return value % modulus


@cache
def general_params(p, t):
    assert p >= 11 and factors(p) == {p: 1}
    assert t >= 3 and t % 2 and 2*t <= p-3
    m, n, r = p+t, 2*(p+t), 2*t
    s0, s1 = r-1, r-3
    d = p*t-m*s0
    e = d+n
    assert gcd(d, e) == gcd(d*e*t*p, n) == 1
    ring = set(factors(abs(p*t*d*e)))
    level = (2*n)**2
    candidates = [s0, s1]
    if p >= 3*t:
        candidates.insert(0, t)
    chosen = next(s for s in candidates
                  if m % 3 or residue(F(m*(t-s), t*t), 9) != 6)
    lower = m*(t-chosen)
    matrix = (t, 1, lower, t)
    assert set(factors(abs(t*t-lower))) <= ring
    assert (p-chosen)//2 <= p-r
    return {"m": m, "n": n, "r": r, "d": d, "e": e, "s": chosen,
            "level": level, "matrix": matrix, "ring_primes": ring}


def check_t_inverse_bridge(p, t):
    data = general_params(p, t)
    m, n, r, d = (data[key] for key in ("m", "n", "r", "d"))
    g = (-t, -1, m*(1-t), t)
    diagonal = (1, 0, 0, t)
    h = tuple(F(x, t) for x in mm(mm(diagonal, g), diagonal))
    assert all(x.denominator == 1 for x in h)
    z = mm(h, invq(g))
    assert z[0]*z[3]-z[1]*z[2] == 1
    old_modulus = (r*n)**2
    for q in set(factors(abs(data["d"]*data["e"]))):
        while old_modulus % q == 0:
            old_modulus //= q
    order = old_modulus**3
    for q in factors(old_modulus):
        order = order//(q*q)*(q*q-1)
    assert mod_power(z, order, old_modulus) == tuple(x % old_modulus for x in I)
    inverse_word = mm(mm(g, diagonal), invq(h))
    assert inverse_word == (t, 0, 0, 1)
    return {"finite_modulus": old_modulus, "sl2_order": order}


def principal_unit_log(base, target, modulus, m, extra_two):
    local = []
    for q, exponent in factors(modulus).items():
        start = valuation(m, q)+(1 if q == 2 and extra_two else 0)
        digits = max(0, exponent-start)
        k = 0
        for j in range(digits):
            next_modulus = q**(start+j+1)
            actual_base = residue(base, next_modulus)
            step = pow(actual_base, q**j, next_modulus)
            coefficient = ((step-1)//q**(start+j)) % q
            assert coefficient
            residual = target*pow(pow(actual_base, k, next_modulus), -1, next_modulus) % next_modulus
            assert (residual-1) % q**(start+j) == 0
            digit = ((residual-1)//q**(start+j))*pow(coefficient, -1, q) % q
            k += digit*q**j
        assert pow(residue(base, q**exponent), k, q**exponent) == target % q**exponent
        local.append((k, q**digits))
    return crt_pairs(local)


def lift_general_unit(p, t, target, exact=False):
    data = general_params(p, t)
    m, level = data["m"], data["level"]
    assert target % m == 1
    h1, h2 = F(-p, t), F(data["e"], data["d"])
    flag = 0
    if m % 4 == 0:
        base = h1
        exponent = principal_unit_log(base, target, level, m, False)
    else:
        flag = int(target % 4 != 1)
        corrected = target*pow(residue(h1, level), -flag, level) % level
        base = h2
        exponent = principal_unit_log(base, corrected, level, m, True)
    assert pow(residue(h1, level), flag, level)*pow(residue(base, level), exponent, level) % level == target % level
    record = {"h1_power": flag, "base": str(base), "power": exponent}
    return (h1**flag)*(base**exponent) if exact else record


def cycle_to_zero(p, t, u, v):
    data = general_params(p, t)
    level, matrix = data["level"], data["matrix"]
    assert gcd(v, level) == 1
    local = []
    for q, exponent in factors(level).items():
        k = -t*u*pow(v, -1, q) % q
        for j in range(1, exponent):
            next_modulus = q**(j+1)
            current = mod_power(matrix, k, next_modulus)
            numerator = (current[0]*u+current[1]*v) % next_modulus
            denominator = (current[2]*u+current[3]*v) % next_modulus
            x = numerator*pow(denominator, -1, next_modulus) % next_modulus
            assert x % q**j == 0
            step = mod_power(matrix, q**j, next_modulus)
            following = (step[0]*x+step[1])*pow(step[2]*x+step[3], -1, next_modulus) % next_modulus
            change = (following-x) % next_modulus
            assert change % q**j == 0 and (change//q**j) % q
            digit = -(x//q**j)*pow(change//q**j, -1, q) % q
            k += digit*q**j
        final = mod_power(matrix, k, q**exponent)
        assert (final[0]*u+final[1]*v) % q**exponent == 0
        local.append((k, q**exponent))
    k = crt_pairs(local)
    final = mod_power(matrix, k, level)
    assert (final[0]*u+final[1]*v) % level == 0
    assert gcd(final[2]*u+final[3]*v, level) == 1
    return k


def integer_cycle_power(p, t, exponent):
    data = general_params(p, t)
    c = data["matrix"][2]
    result, current = (1, 0), (t, 1)
    while exponent:
        if exponent & 1:
            a, b = result
            x, y = current
            result = (a*x+c*b*y, a*y+b*x)
        a, b = current
        current = (a*a+c*b*b, 2*a*b)
        exponent //= 2
    a, b = result
    return (a, b, c*b, a)


def general_transport(p, t, u, v):
    data = general_params(p, t)
    m, level = data["m"], data["level"]
    assert gcd(u, v) == gcd(v, m) == 1
    exponent = cycle_to_zero(p, t, u, v)
    matrix = integer_cycle_power(p, t, exponent)
    uu, vv = matrix[0]*u+matrix[1]*v, matrix[2]*u+matrix[3]*v
    common = gcd(uu, vv)
    remainder = common
    for q in data["ring_primes"]:
        while remainder % q == 0:
            remainder //= q
    assert remainder == 1
    uu, vv = uu//common, vv//common
    assert uu % level == 0 and gcd(vv, level) == 1
    small = pow(vv, -1, m)
    if 2*small > m:
        small -= m
    assert small % 2 and 0 < abs(small) <= p
    prime_list = tuple(factors(abs(small)))
    radical = prod(prime_list)
    shift = sum(radical//q*pow(radical//q, -1, q) for q in prime_list if uu % q == 0) % radical
    uu += level*shift*vv
    vv *= small
    assert gcd(uu, vv) == 1 and vv % m == 1
    epsilon = lift_general_unit(p, t, vv % level, exact=True)
    common, a, b = bezout(uu, vv)
    assert common == 1
    adjust = residue(-epsilon*a, level)*pow(vv, -1, level) % level
    alpha, beta = epsilon*a+adjust*vv, epsilon*b-adjust*uu
    terminal = (F(vv)/epsilon, F(-uu)/epsilon, alpha, beta)
    assert terminal[0]*terminal[3]-terminal[1]*terminal[2] == 1
    assert tuple(residue(x, level) for x in terminal) == I
    assert terminal[0]*uu+terminal[1]*vv == 0
    assert terminal[2]*uu+terminal[3]*vv == epsilon
    return {"p": p, "t": t, "uv": [u, v], "cycle_power": exponent,
            "small_multiplier": small, "deep_upper_shift": shift,
            "unit_word": lift_general_unit(p, t, vv % level),
            "largest_integer_bits": max(abs(uu).bit_length(), abs(vv).bit_length())}


def extended_checks():
    rng = Random(2026091517)
    systems = orbit_checks = unit_checks = repaired = 0
    bridge = []
    for p in (11, 13, 17, 19, 23, 29, 31, 41, 59, 61, 83, 127):
        for t in range(3, (p-3)//2+1, 2):
            data = general_params(p, t)
            m, level = data["m"], data["level"]
            systems += 1
            repaired += int(m % 3 == 0 and residue(F(m*(1-t), t*t), 9) == 6)
            bridge.append({"p": p, "t": t, **check_t_inverse_bridge(p, t)})
            for _ in range(8):
                while True:
                    u, v = rng.randrange(level), rng.randrange(1, level)
                    if gcd(v, level) == 1:
                        break
                cycle_to_zero(p, t, u, v)
                orbit_checks += 1
                target = 1+m*rng.randrange(level//m)
                lift_general_unit(p, t, target)
                unit_checks += 1
    # The first return really can have period3 rather than9; the adjacent one repairs it.
    p, t = 61, 23
    data = general_params(p, t)
    bad_matrix = (t, 1, data["m"]*(1-t), t)
    x, seen = 0, set()
    while x not in seen:
        seen.add(x)
        x = (bad_matrix[0]*x+bad_matrix[1])*pow(bad_matrix[2]*x+bad_matrix[3], -1, 9) % 9
    assert len(seen) == 3
    x, seen = 0, set()
    while x not in seen:
        seen.add(x)
        matrix = data["matrix"]
        x = (matrix[0]*x+matrix[1])*pow(matrix[2]*x+matrix[3], -1, 9) % 9
    assert len(seen) == 9
    exact = [general_transport(13, 5, 2, 5), general_transport(17, 7, 3, 5)]
    print("all interior odd-half even-core systems: PASS", systems)
    print("finite congruence bridge activates odd t inverse: PASS", len(bridge))
    print("prime-power projective cycles and principal-unit lifts: PASS", orbit_checks, unit_checks)
    print("exceptional mod9 return repaired by adjacent choice: PASS", repaired)
    print("beyond balanced-capacity exact terminal matrices: PASS", len(exact))
    return {"systems": systems, "cycle_checks": orbit_checks, "unit_lifts": unit_checks,
            "t_inverse_bridges": bridge, "exact_beyond_capacity_transports": exact,
            "scope": "All odd t>=3 with 2t<=p-3, not just 3t<=p. "
                     "Principal subgroup and finite-to-exact inverse lifting "
                     "use the existing stated Morris/Serre dependencies."}


if __name__ == "__main__":
    result = run()
    result["all_interior_extension"] = extended_checks()
    (ROOT/"even_odd_half_core_records.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print("uniform odd-half even-remainder completion: PASS")
