"""Uniform completion of all internal even remainders.

Finite 2-adic certificates are exhaustive parameter classes with a proved
principal-congruence lift. Odd-prime cycles and unit kernels use closed
valuation formulas. No averaging-word search is performed.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd, prod
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import factors, Ledger, triple_return
from verify_uniform_odd_middle_cores import mm, invq, residue
from verify_even_odd_half_core import (
    I, U, L, mod_power, valuation, crt_pairs, principal_unit_log)

ROOT = Path(__file__).parent
if not __debug__:
    raise RuntimeError("Assertions are required.")


def scaled(matrix, factor):
    return tuple(factor*x for x in matrix)


def apply_mod(matrix, pair, modulus):
    a, b, c, d = (residue(x, modulus) for x in matrix)
    u, v = pair
    return ((a*u+b*v) % modulus, (c*u+d*v) % modulus)


def two_order(matrix, modulus):
    answer = 1
    current = tuple(residue(x, modulus) for x in matrix)
    for _ in range(4*modulus.bit_length()):
        if current == I:
            return answer
        current = tuple(x % modulus for x in mm(current, current))
        answer *= 2
    raise AssertionError("Expected a power-of-two order.")


def odd_cycle_hit(matrix, t, modulus, u, v, target_u, target_v):
    local = []
    for q, exponent in factors(modulus).items():
        assert q % 2 and gcd(t*v*target_v, q) == 1
        target = target_u*pow(target_v, -1, q**exponent) % q**exponent
        k = t*(target-u*pow(v, -1, q)) % q
        for j in range(1, exponent):
            mod = q**(j+1)
            cur_u, cur_v = apply_mod(mod_power(matrix, k, mod), (u, v), mod)
            x = cur_u*pow(cur_v, -1, mod) % mod
            error = (x-target) % mod
            assert error % q**j == 0
            step = mod_power(matrix, q**j, mod)
            next_x = (step[0]*x+step[1])*pow(step[2]*x+step[3], -1, mod) % mod
            difference = (next_x-x) % mod
            assert difference % q**j == 0 and (difference//q**j) % q
            digit = -(error//q**j)*pow(difference//q**j, -1, q) % q
            k += digit*q**j
        aa, bb = apply_mod(mod_power(matrix, k, q**exponent), (u, v), q**exponent)
        assert (aa*target_v-bb*target_u) % q**exponent == 0
        local.append((k, q**exponent))
    return crt_pairs(local)


def half_helper(m):
    assert m % 2
    sign = 1 if m % 4 == 1 else -1
    value = (m+sign)//2
    assert value % 2 and gcd(value, 2*m) == 1
    return value, F(sign, value)


def companion_inverse_sandwich(trace, determinant, modulus):
    assert gcd(determinant, modulus) == 1
    k = modulus*(trace*pow(modulus, -1, abs(determinant)) % abs(determinant))
    matrix = (trace, determinant, -1, 0)
    h = scaled(mm(mm(matrix, U(k)), matrix), F(1, determinant))
    assert all(F(x).denominator == 1 for x in h)
    assert h[0]*h[3]-h[1]*h[2] == 1
    assert mm(mm(U(k), matrix), invq(h)) == scaled(invq(matrix), determinant)
    return k


def quotient_forest(generators, modulus):
    good = {(u, v) for u in range(modulus) for v in range(modulus) if (u+v) % 2}
    matrices = [tuple(residue(x, modulus) for x in g) for g in generators]
    parents = {(0, 1): None}
    queue = deque(parents)
    while queue:
        u, v = queue.popleft()
        for index, (a, b, c, d) in enumerate(matrices):
            following = ((a*u+b*v) % modulus, (c*u+d*v) % modulus)
            if following not in parents:
                parents[following] = ((u, v), index)
                queue.append(following)
    assert set(parents) == good
    return parents


def edge_data(p, edge):
    if edge == "r4":
        t, r = 2, 4
        m = p+t
        helper, eps2 = half_helper(m)
        tau = eps2
        s0, s1, trace, chosen_s, j = 3, 1, 2, 1, (p-3)//2
        determinant = p-6
        scalar = eps2**2
        dyadic = 64
        extras = (p, p-2, p-6, helper)
    else:
        assert p % 4 == 3 and p % 3
        t, r = (p-3)//2, p-3
        m = p+t
        helper, eps2 = half_helper(m)
        a = valuation(t, 2)
        odd = t//2**a
        tau = eps2**a*odd
        s0, s1 = p-4, p-6
        trace, chosen_s, j = (2, s0, 1) if p % 3 == 1 else (-2, s1, 4)
        determinant = r*j-p*chosen_s
        scalar = -F(determinant)/tau
        dyadic = 16
        extras = (p, tau, helper)
    d, e = p*t-m*s0, p*t-m*s1
    js = [(-t, -1, m*(t-s), t) for s in (s0, s1)]
    macro = (-t, -1, m*(t-chosen_s), t+trace)
    generators = [(-1, 0, 0, 1)]
    generators += [scaled(g, 1/tau) for g in js]
    generators += [scaled(macro, 1/scalar)]
    generators += [(1/F(s), 0, 0, 1) for s in extras]
    return {"p": p, "t": t, "r": r, "m": m, "n": 2*m, "d": d, "e": e,
            "helper": helper, "eps2": eps2, "tau": tau, "trace": trace,
            "s": chosen_s, "j": j, "determinant": determinant, "dyadic": dyadic,
            "generators": generators, "choices": (s0, s1)}


def fixed_certificates():
    four_cases = []
    for p in range(1, 128, 2):
        data = edge_data(p, "r4")
        parents = quotient_forest(data["generators"], 64)
        four_cases.append({"p_mod128": p, "states": len(parents),
                           "generators": [[residue(x, 64) for x in g] for g in data["generators"]]})
    edge_cases = []
    for p in range(7, 192, 4):
        if p % 3 == 0:
            continue
        t, m = (p-3)//2, (3*p-3)//2
        helper, _ = half_helper(m)
        s0, s1 = p-4, p-6
        trace, s, j = (2, s0, 1) if p % 3 == 1 else (-2, s1, 4)
        determinant = (p-3)*j-p*s
        for tau in range(1, 16, 2):
            generators = [(-1, 0, 0, 1)]
            generators += [scaled((-t, -1, m*(t-ss), t), F(1, tau)) for ss in (s0, s1)]
            alpha = F(-determinant, tau)
            generators += [scaled((-t, -1, m*(t-s), t+trace), 1/alpha)]
            generators += [(F(1, a), 0, 0, 1) for a in (p, tau, helper)]
            parents = quotient_forest(generators, 16)
            edge_cases.append({"p_mod192": p, "tau_mod16": tau, "states": len(parents)})
    assert len(four_cases) == 64 and len(edge_cases) == 256
    print("uniform r4 normalized dyadic certificate: PASS", len(four_cases), 2048)
    print("uniform r=p-3 normalized dyadic certificate: PASS", len(edge_cases), 128)
    return four_cases, edge_cases


def two_adic_edge_transport(p, edge, u, v):
    data = edge_data(p, edge)
    assert factors(p) == {p: 1}
    t, r, m, dyadic = (data[k] for k in ("t", "r", "m", "dyadic"))
    assert 4 <= r <= p-3 and gcd(u, v) == gcd(v, m) == 1 and (u+v) % 2
    modulus = dyadic*m*m
    assert gcd(data["determinant"], 2*m) == 1
    companion_inverse_sandwich(data["trace"], data["determinant"], (r*2*m)**2)
    inv_v = pow(v, -1, m)
    if 2*inv_v > m:
        inv_v -= m
    twos = valuation(abs(inv_v), 2)
    small = inv_v//2**twos
    assert small % 2 and abs(small) <= p and gcd(small, m) == 1
    # A principal upper shift makes C_small primitive; it is invisible modulo modulus.
    prime_list = tuple(factors(abs(small)))
    radical = prod(prime_list)
    shift = sum(radical//q*pow(radical//q, -1, q) for q in prime_list if u % q == 0) % radical
    assert gcd(u+modulus*shift*v, small) == 1
    normalizing = residue(data["eps2"]**twos, modulus)
    pair = (u*normalizing % modulus, small*v*normalizing % modulus)
    assert pair[1] % m == 1
    parents = quotient_forest(data["generators"], dyadic)
    state = tuple(x % dyadic for x in pair)
    word = []
    while parents[state] is not None:
        parent, index = parents[state]
        pair = apply_mod(invq(data["generators"][index]), pair, modulus)
        assert tuple(x % dyadic for x in pair) == parent
        state = parent
        word.append(index)
    assert tuple(x % dyadic for x in pair) == (0, 1)
    assert pair[1] % m == 1
    s = next(s for s in data["choices"]
             if m % 3 or residue(F(m*(t-s), t*t), 9) != 6)
    matrix = scaled((t, 1, m*(t-s), t), 1/data["tau"])
    order2 = two_order(matrix, dyadic)
    exponent_odd = odd_cycle_hit(matrix, t, m*m, *pair, 0, 1)
    exponent = crt_pairs(((exponent_odd, m*m), (0, order2)))
    pair = apply_mod(mod_power(matrix, exponent, modulus), pair, modulus)
    assert pair[0] == 0 and pair[1] % dyadic == 1 and pair[1] % m == 1
    kappa = F(data["e"], data["d"])
    unit_power2 = two_order((kappa, 0, 0, kappa), dyadic)
    base = kappa**unit_power2
    unit_exponent = principal_unit_log(base, pair[1], m*m, m, False)
    epsilon = pow(residue(base, modulus), unit_exponent, modulus)
    assert pair == (0, epsilon)
    return {"p": p, "r": r, "uv": [u, v], "small_multiplier": small,
            "dyadic_inverse_word": word, "odd_cycle_power": exponent,
            "unit_power2": unit_power2, "unit_exponent": unit_exponent,
            "principal_modulus": modulus}


def multi_return_data(p, t):
    assert t >= 4 and t % 2 == 0 and 2*t <= p-5
    assert factors(p) == {p: 1}
    m, n, r = p+t, 2*(p+t), 2*t
    counts = (r-1, r-3, r-5)
    ds = tuple(p*t-m*s for s in counts)
    assert all(gcd(d, n) == 1 for d in ds)
    ratios = (F(ds[1], ds[0]), F(ds[2], ds[1]))
    kappa = next(value for value in ratios if residue(value, 8) == 3)
    assert residue(kappa*kappa, 16) == 9
    a = valuation(t, 2)
    two_modulus = 2**(2*a+4)
    modulus = two_modulus*m*m
    helper, eps2 = half_helper(m)
    tau = eps2**a*(t//2**a)
    chosen = next(s for s in counts if m % 3 or residue(F(m*(t-s), t*t), 9) != 6)
    return m, n, r, counts, ds, kappa, modulus, two_modulus, helper, eps2, tau, chosen


def multi_return_transport(p, t, u, v):
    m, n, r, counts, ds, kappa, modulus, two_modulus, helper, eps2, tau, chosen = multi_return_data(p, t)
    assert u % 4 == 2 and v % 2 and gcd(u, v) == gcd(v, m) == 1
    wanted = pow(v, -1, m)
    if 2*wanted > m:
        wanted -= m
    twos = valuation(abs(wanted), 2)
    small = wanted//2**twos
    assert small % 2 and abs(small) <= p
    prime_list = tuple(factors(abs(small)))
    radical = prod(prime_list)
    shift = sum(radical//q*pow(radical//q, -1, q)
                for q in prime_list if u % q == 0) % radical
    assert gcd(u+modulus*shift*v, small) == 1
    pair = (u % modulus, small*v % modulus)
    target_u = 2
    target_v = p-r*(p-1)//2
    target_a = target_v+t*target_u
    target_x = target_u*pow(target_a, -1, two_modulus) % two_modulus
    x = pair[0]*pow(t*pair[0]+pair[1], -1, two_modulus) % two_modulus
    selected = None
    for sign in (0, 1):
        x0 = x if not sign else x*pow(-1+r*x, -1, two_modulus) % two_modulus
        for first_power in (0, 1):
            x1 = x0*pow(residue(kappa, two_modulus), first_power, two_modulus) % two_modulus
            if x1 % 16 == target_x % 16:
                selected = sign, first_power, x1
                break
        if selected is not None:
            break
    assert selected is not None
    sign, first_power, x1 = selected
    ratio = (target_x//2)*pow(x1//2, -1, two_modulus//2) % (two_modulus//2)
    exponent = principal_unit_log(kappa*kappa, ratio, two_modulus//2, 8, False)
    total_power = first_power+2*exponent
    if sign:
        pair = (pair[0], -pair[1] % modulus)
    kk = pow(residue(kappa, modulus), total_power, modulus)
    pair = apply_mod((kk, 0, t*(1-kk), 1), pair, modulus)
    a_value = t*pair[0]+pair[1]
    assert (pair[0]*target_a-a_value*target_u) % two_modulus == 0
    matrix = (t, 1, m*(t-chosen), t)
    order2 = two_order(matrix, two_modulus)
    k_odd = odd_cycle_hit(matrix, t, m*m, *pair, target_u, target_v)
    k = crt_pairs(((k_odd, m*m), (0, order2)))
    pair = apply_mod(mod_power(matrix, k, modulus), pair, modulus)
    assert (pair[0]*target_v-pair[1]*target_u) % modulus == 0
    scalar = pair[1]*pow(target_v, -1, modulus) % modulus
    scalar0 = ((-1)**sign)*pow(residue(eps2, modulus), -twos, modulus)*pow(residue(tau, modulus), k-2, modulus) % modulus
    correction = scalar*pow(scalar0, -1, modulus) % modulus
    assert correction % m == 1
    k0, k1 = F(ds[1], ds[0]), F(ds[2], ds[0])
    flag = int(correction % 4 != 1)
    correction1 = correction*pow(residue(k0, modulus), -flag, modulus) % modulus
    unit_k = principal_unit_log(k1, correction1, modulus, 4*m, False)
    lifted = scalar0*pow(residue(k0, modulus), flag, modulus)*pow(residue(k1, modulus), unit_k, modulus) % modulus
    assert lifted == scalar and pair == (lifted*target_u % modulus, lifted*target_v % modulus)
    return {"p": p, "r": r, "uv": [u, v], "small_multiplier": small,
            "dyadic_sign": sign, "dyadic_torus_power": total_power,
            "odd_cycle_power": k, "principal_unit_flag": flag,
            "principal_unit_power": unit_k, "principal_modulus": modulus}


def physical_trace_returns():
    records = []
    for p, edge in ((11, "r4"), (13, "r4"), (19, "r4"),
                    (7, "edge"), (11, "edge"), (19, "edge"), (23, "edge")):
        data = edge_data(p, edge)
        t, r, s, j = data["t"], data["r"], data["s"], data["j"]
        n = 2*p+r
        assert gcd(data["determinant"], r*n) == 1
        for u, v in ((1, 0), (0, 1)):
            aa, zz = t*u+v, u
            raw = [aa]*p+[r*zz-aa]*p+[-p*zz]*r
            ledger = Ledger(raw, p)
            first, second, carriers = list(range(p)), list(range(p, 2*p)), list(range(2*p, n))
            i = p-j-s
            assert 0 <= i <= p-r
            left = first[:i]+second[:j]+carriers[:s]
            right = first[i:p-r]+second[j:]+carriers[s:]
            kept = first[p-r:]
            ledger.average(left)
            ledger.average(right)
            expected_a = F(data["trace"]*aa+data["determinant"]*zz, p)
            expected_z = F(-aa, p)
            assert [ledger.state[g[0]] for g in (left, right, kept)] == [
                expected_a, r*expected_z-expected_a, -p*expected_z]
            ledger.independent_replay(raw)
        d = data["d"]
        shear = 2*data["trace"]+r*(1-F(data["determinant"], d))
        quotient = shear/n
        assert quotient.denominator % 2 and quotient.numerator % 4 == 2
        records.append({"p": p, "r": r, "trace": data["trace"],
                        "determinant": data["determinant"], "upper_root_over_n": str(quotient)})
    print("uniform safe trace-two returns and root-ideal improvement: PASS", len(records))
    return records


def physical_general_returns():
    checked = bridges = 0
    for p, t in ((13, 4), (17, 6), (23, 8), (13, 5), (17, 7), (61, 23)):
        m, n, r = p+t, 2*(p+t), 2*t
        counts = (r-1, r-3, r-5) if t % 2 == 0 else (r-1, r-3)
        for s in counts:
            d = p*t-m*s
            assert gcd(d, n) == 1
            for u, v in ((1, 0), (0, 1)):
                raw = [t*u+v]*p+[t*u-v]*p+[-p*u]*r
                ledger = Ledger(raw, p)
                groups = [list(range(p)), list(range(p, 2*p)), list(range(2*p, n))]
                groups = triple_return(ledger, groups, p, r, s)
                got_u = -ledger.state[groups[2][0]]/p
                got_v = (ledger.state[groups[0][0]]-ledger.state[groups[1][0]])/2
                assert (got_u, got_v) == (F(-t*u-v, p), F(m*(t-s)*u+t*v, p))
                ledger.independent_replay(raw)
                checked += 1
        odd = t//2**valuation(t, 2)
        g = (-t, -1, m*(1-t), t)
        diag = (1, 0, 0, odd)
        h = scaled(mm(mm(diag, g), diag), F(1, odd))
        assert all(F(x).denominator == 1 for x in h)
        z = mm(h, invq(g))
        assert z[0]*z[3]-z[1]*z[2] == 1
        assert mm(mm(g, diag), invq(h)) == (odd, 0, 0, 1)
        bridges += 1
    print("general interior returns and odd-divisor inverse sandwiches: PASS", checked, bridges)
    return checked, bridges


def run():
    r4, boundary = fixed_certificates()
    traces = physical_trace_returns()
    general_returns = physical_general_returns()
    rng = Random(2026091521)
    multi = []
    for p in (13, 17, 19, 23, 29, 31, 41, 59, 83, 127):
        for t in range(4, (p-5)//2+1, 2):
            for _ in range(3):
                while True:
                    u = 4*rng.randrange(1, 1000)+2
                    v = 2*rng.randrange(1, 1000)+1
                    if gcd(u, v) == gcd(v, p+t) == 1:
                        break
                multi.append(multi_return_transport(p, t, u, v))
    edges = []
    for p, edge in ((11, "r4"), (13, "r4"), (17, "r4"), (19, "r4"),
                    (31, "r4"), (43, "r4"), (7, "edge"), (11, "edge"),
                    (19, "edge"), (23, "edge"), (31, "edge"), (43, "edge")):
        m = edge_data(p, edge)["m"]
        for _ in range(4):
            while True:
                u, v = rng.randrange(1, 1000), rng.randrange(1, 1000)
                if (u+v) % 2 and gcd(u, v) == gcd(v, m) == 1:
                    break
            edges.append(two_adic_edge_transport(p, edge, u, v))
    print("all 4-divisible interior remainders finite terminal lifts: PASS", len(multi))
    print("r4 and r=p-3 complete normalized terminal lifts: PASS", len(edges))
    result = {"r4_dyadic_certificate": r4, "last_interior_dyadic_certificate": boundary,
              "trace_returns": traces, "multiple_return_transports": multi,
              "general_return_checks": general_returns,
              "edge_transports": edges,
              "scope": "All internal even 4<=r<=p-3, together with the odd-half proof. "
                       "Full sufficiency uses existing deep-principal and dyadic-depth "
                       "theorems with stated arithmetic-group dependencies. Does not "
                       "solve r=2 or r=p-1 in general or lower the final threshold."}
    (ROOT/"even_interior_completion_records.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print("all internal even-remainder completion: PASS")


if __name__ == "__main__":
    run()
