"""Unrestricted endpoint entry via literal modular transfer commutators.

The selector uses CRT and fixed eight-run words, never averaging-word search.
Small cases replay every original-position atom with Fraction. Large cases
keep singleton multiplicities and exponentiate the fixed four-role matrices.
"""

from fractions import Fraction as F
from math import gcd, lcm, prod
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import (
    Ledger, factors, residue, is_legal, first_block, carrier_period)
from verify_upper_band_three_value_reduction import full_support, select_parameter
from verify_uniform_two_block_entry import transfer, replay as replay_core

ROOT = Path(__file__).parent
if not __debug__:
    raise RuntimeError("Assertions are required.")


def identity(size):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def mm(left, right, modulus=None):
    size = len(left)
    rows = tuple(tuple(sum(left[i][k]*right[k][j] for k in range(size))
                       for j in range(size)) for i in range(size))
    if modulus is not None:
        rows = tuple(tuple(value % modulus for value in row) for row in rows)
    return rows


def mpow(matrix, exponent, modulus):
    assert exponent >= 0
    result = identity(len(matrix))
    while exponent:
        if exponent & 1:
            result = mm(matrix, result, modulus)
        matrix = mm(matrix, matrix, modulus)
        exponent //= 2
    return result


def mv(matrix, vector, modulus):
    return [sum(a*b for a, b in zip(row, vector)) % modulus for row in matrix]


def exchange_matrix(p, role, size=4, modulus=None, formal_inverse=False):
    rows = [list(row) for row in identity(size)]
    j = role+1
    if formal_inverse:
        rows[0][0], rows[0][j] = 0, 1
        rows[j][0], rows[j][j] = p, -(p-1)
    else:
        reciprocal = F(1, p) if modulus is None else pow(p, -1, modulus)
        rows[0][0], rows[0][j] = (p-1)*reciprocal, reciprocal
        rows[j][0], rows[j][j] = 1, 0
    return tuple(tuple(x if modulus is None else x % modulus for x in row)
                 for row in rows)


def root_expected(p, modulus=None):
    coefficient = F(p-1, p) if modulus is None else (p-1)*pow(p, -1, modulus) % modulus
    rows = [list(row) for row in identity(4)]
    rows[2][0] += coefficient
    rows[2][1] -= coefficient
    rows[3][0] -= coefficient
    rows[3][1] += coefficient
    return tuple(tuple(x if modulus is None else x % modulus for x in row)
                 for row in rows)


def root_runs(period, source, target, buffer):
    assert len({source, target, buffer}) == 3
    # Chronological order for T A_source T^-1 A_source^-1.
    return [(source, period-1), (buffer, 1), (target, period-1),
            (buffer, period-1), (source, 1), (buffer, 1),
            (target, 1), (buffer, period-1)]


def positive_root(p, modulus, period):
    result = identity(4)
    for role, exponent in root_runs(period, 0, 1, 2):
        result = mm(mpow(exchange_matrix(p, role, modulus=modulus),
                         exponent, modulus), result, modulus)
    return result


def choose_root_power(p, primes, delta, source, target):
    conditions = [
        (q, delta[target] % q, -(p-1)*pow(p, -1, q)*delta[source] % q)
        for q in primes if (p-1) % q and (delta[target] % q or delta[source] % q)]
    if p >= 5:
        return select_parameter(p, conditions)
    return next(t for t in range(1, p) if all((a+t*b) % q for q, a, b in conditions))


def check_algebra():
    formal = modular = 0
    positive_inverse = mm(exchange_matrix(3, 0), exchange_matrix(3, 0))
    formal_inverse = exchange_matrix(3, 0, formal_inverse=True)
    assert positive_inverse != formal_inverse
    assert all(residue(a-b, 7) == 0 for left, right in zip(positive_inverse, formal_inverse)
               for a, b in zip(left, right))
    for p in range(2, 81):
        generators = [exchange_matrix(p, i) for i in range(3)]
        inverses = [exchange_matrix(p, i, formal_inverse=True) for i in range(3)]
        chronological = [inverses[0], generators[2], inverses[1], inverses[2],
                         generators[0], generators[2], generators[1], inverses[2]]
        result = identity(4)
        for matrix in chronological:
            result = mm(matrix, result)
        assert result == root_expected(p)
        formal += 1
        for r in range(1, p):
            n = 2*p+r
            if gcd(p, n) != 1:
                continue
            primes = tuple(factors(n))
            modulus = prod(primes)
            period = lcm(*(carrier_period(p, q) for q in primes))
            assert positive_root(p, modulus, period) == root_expected(p, modulus)
            assert all(mpow(exchange_matrix(p, i, modulus=modulus), period, modulus)
                       == identity(4) for i in range(3))
            bad = [q for q in primes if (p-1) % q == 0]
            assert all((r+2) % q == 0 for q in bad)
            assert len(bad) <= r
            modular += 1
    print("three-singleton exact rational commutator: PASS", formal)
    print("positive modular inverses roots and reserve capacity: PASS", modular)
    return {"formal": formal, "modular": modular}


def replay_entry(raw, ledger, blocks, singles, primes):
    state = list(map(F, raw))
    for group in ledger.word:
        assert len(group) == len(set(group)) == ledger.p
        assert all(0 <= i < len(raw) for i in group)
        value = sum(state[i] for i in group)/ledger.p
        for i in group:
            state[i] = value
        assert sum(state) == 0 and is_legal(state, primes)
    assert state == ledger.state
    assert sorted(blocks[0]+blocks[1]+singles) == list(range(len(raw)))
    assert all(len(block) == ledger.p for block in blocks)
    assert all(all(state[i] == state[block[0]] for i in block) for block in blocks)


def unrestricted_two_blocks(raw, p, r, first=None):
    n = len(raw)
    assert n == 2*p+r and 1 <= r < p and gcd(p, n) == 1
    primes = tuple(factors(n))
    modulus = prod(primes)
    period = lcm(*(carrier_period(p, q) for q in primes))
    assert sum(raw) == 0 and gcd(*raw) == 1 and is_legal(raw, primes)
    ledger = Ledger(raw, p)
    block = first_block(raw, p, primes) if first is None else list(first)
    ledger.average(block)
    singles = [i for i in range(n) if i not in set(block)]
    assert is_legal(ledger.state, primes)
    delta = [residue(ledger.state[i]-ledger.state[block[0]], modulus) for i in singles]
    bad = [q for q in primes if (p-1) % q == 0]
    reserved = set()
    for q in bad:
        reserved.add(next(i for i, value in enumerate(delta) if value % q))
    assert len(reserved) <= r
    for i in range(len(singles)):
        if len(reserved) == r:
            break
        reserved.add(i)
    target = min(reserved)
    initial_reserved = sorted(reserved)
    plans = []
    for q in primes:
        if q in bad or delta[target] % q:
            continue
        source = next(i for i, value in enumerate(delta) if value % q)
        assert source != target
        buffer = next(i for i in range(len(singles)) if i not in (source, target))
        exponent = choose_root_power(p, primes, delta, source, target)
        coefficient = (p-1)*pow(p, -1, modulus)*exponent % modulus
        before = delta[:]
        for _ in range(exponent):
            for role, repeats in root_runs(period, source, target, buffer):
                for _ in range(repeats):
                    block, singles[role] = ledger.swap(block, singles[role])
        delta = [residue(ledger.state[i]-ledger.state[block[0]], modulus) for i in singles]
        expected = before[:]
        expected[target] = (expected[target]-coefficient*before[source]) % modulus
        expected[buffer] = (expected[buffer]+coefficient*before[source]) % modulus
        assert delta == expected and delta[target] % q
        assert all(delta[target] % ell for ell in primes
                   if ell not in bad and before[target] % ell)
        assert all(all((delta[h]-before[h]) % ell == 0 for h in range(len(delta)))
                   for ell in bad)
        plans.append({"prime": q, "source": source, "target": target,
                      "buffer": buffer, "root_power": exponent})
    assert all(any(delta[i] % q for i in reserved) for q in primes)
    kept = [singles[i] for i in sorted(reserved)]
    second = [singles[i] for i in range(len(singles)) if i not in reserved]
    ledger.average(second)
    assert len(kept) == r and is_legal(ledger.state, primes)
    replay_entry(raw, ledger, [block, second], kept, primes)
    record = {"p": p, "n": n, "input": raw, "modulus": modulus,
              "period": period, "bad_primes": bad, "reserved_roles": initial_reserved,
              "root_plan": plans, "operations": [group[:] for group in ledger.word],
              "groups": [block[:], second[:], kept[:]]}
    return ledger, block, second, kept, record


def forced_input(p, r):
    n = 2*p+r
    primes = tuple(factors(n))
    modulus = prod(primes)
    deltas = [modulus//q*pow(modulus//q, -1, q) % modulus for q in primes]
    deltas.append(-n-sum(deltas))
    assert len(deltas) <= p+r
    singles = [1+d for d in deltas]+[1]*(p+r-len(deltas))
    return [1]*p+singles


def check_literal_entries():
    rng = Random(2026091507)
    records = []
    core_records = []
    levels = [(2, 1), (3, 1), (5, 1), (7, 1), (9, 1), (13, 1),
              (5, 2), (5, 3), (5, 4), (7, 2), (7, 3), (7, 4), (7, 6), (29, 2)]
    for p, r in levels:
        for forced in (False, True):
            if forced:
                raw = forced_input(p, r)
            else:
                while True:
                    raw = [rng.randrange(-30, 31) for _ in range(2*p+r-1)]
                    raw.append(-sum(raw))
                    common = gcd(*raw)
                    if common:
                        raw = [x//common for x in raw]
                    if common and is_legal(raw, factors(len(raw))):
                        break
            ledger, first, second, singles, record = unrestricted_two_blocks(
                raw, p, r, range(p) if forced else None)
            records.append(record)
            if r == 1:
                a, b, c = [ledger.state[g[0]] for g in (first, second, singles)]
                assert c == -p*(a+b)
                assert all(residue(a-b, q) for q in factors(2*p+1))
            elif p >= 5:
                primes = tuple(factors(len(raw)))
                anchor = singles[0]
                first, second, singles, _ = full_support(
                    ledger, first, second, singles, anchor, primes)
                first, second, singles, _ = transfer(
                    ledger, first, second, singles, anchor, primes)
                merged, kept = first[:p-r]+singles, first[p-r:]
                ledger.average(merged)
                groups = [merged, second, kept]
                replay_core(raw, ledger, groups, p, r)
                core_records.append({"p": p, "r": r, "input": raw,
                                     "operations": ledger.word, "groups": groups})
    print("unrestricted original-position two-block entries: PASS", len(records))
    print("unrestricted entry joined to weighted-core reduction: PASS", len(core_records))
    return records, core_records


def check_large_cover():
    primes = (3, 5, 7, 13, 17, 241, 19)
    n = prod(primes)
    p = (n-1)//2
    assert p == 53127847 and factors(p) == {p: 1}
    forbidden = (0, 1, 2, 7, 7, 3)
    periods = [carrier_period(p, q) for q in primes]
    period = lcm(*periods)
    assert sum((F(1, d) for d in periods), F(0))-min(F(1, d) for d in periods) >= 1
    assert all(any(k % d == b for d, b in zip(periods[:6], forbidden))
               for k in range(24))
    delta_i = delta_j = delta_k = delta_l = 0
    for position, q in enumerate(primes):
        unit = n//q*pow(n//q, -1, q) % n
        di = int(position < 6)
        dj = (-2*(pow(2, forbidden[position], q)-1)) % q if position < 6 else 1
        dk = (-di-dj) % q if position < 3 or position == 6 else 0
        dl = (-di-dj-dk) % q
        delta_i += unit*di
        delta_j += unit*dj
        delta_k += unit*dk
        delta_l += unit*dl
    deltas = [x % n for x in (delta_i, delta_j, delta_k, delta_l)]
    deltas[-1] -= n+sum(deltas)
    assert sum(deltas) == -n
    assert all(any(d % q for d in deltas) for q in primes)
    assert all(any(d % q == 0 for q in primes) for d in deltas)
    assert all(any((deltas[1]+2*(pow(2, k, q)-1)*deltas[0]) % q == 0
                   for q in primes[:6]) for k in range(24))
    # Four distinguished singleton positions; all others have actual value1.
    initial = [1]+[1+d for d in deltas]
    values = [value % n for value in initial]
    target = next(i for i in range(4) if (values[i+1]-values[0]) % 3)
    root = positive_root(p, n, period)
    assert root == root_expected(p, n)
    plans = []
    for q in primes:
        if q == 3 or (values[target+1]-values[0]) % q:
            continue
        source = next(i for i in range(4) if (values[i+1]-values[0]) % q)
        buffer = next(i for i in range(4) if i not in (source, target))
        delta = [(values[i+1]-values[0]) % n for i in range(4)]
        exponent = choose_root_power(p, primes, delta, source, target)
        local = [values[0], values[source+1], values[target+1], values[buffer+1]]
        following = mv(mpow(root, exponent, n), local, n)
        assert following[0] == local[0] and following[1] == local[1]
        values[0], values[source+1], values[target+1], values[buffer+1] = following
        assert (values[target+1]-values[0]) % q
        plans.append({"prime": q, "source": source, "target": target,
                      "buffer": buffer, "root_power": exponent})
    assert all((values[target+1]-values[0]) % q for q in primes)
    assert (p*values[0]+sum(values[1:])+(p+1-4)) % n == 0
    second = (-p*values[0]-values[target+1])*pow(p, -1, n) % n
    assert gcd(values[0]-second, n) == 1
    print("seven-prime covering obstruction crossed by fixed positive roots: PASS", p, n)
    return {"p": p, "n": n, "initial_block": 1,
            "distinguished_singletons": initial[1:],
            "remaining_singletons_value": 1, "remaining_singletons_count": p-3,
            "period": period, "target": target, "root_plan": plans,
            "final_role_values_mod_n": values,
            "scope": "Compressed modular evaluation of a fixed finite physical program. "
                     "No huge raw array or full rational word is expanded."}


def check_old_entry_gaps():
    records = []
    for p, r in ((29, 2), (3271, 3), (53127847, 1)):
        n = 2*p+r
        primes = tuple(factors(n))
        modulus = prod(primes)
        assert len(primes) > r and factors(p) == {p: 1}
        period = lcm(*(carrier_period(p, q) for q in primes))
        deltas = [modulus//q*pow(modulus//q, -1, q) % modulus for q in primes]
        deltas.append(-n-sum(deltas))
        initial_values = [1]+[1+x for x in deltas]
        values = [x % modulus for x in initial_values]
        bad = [q for q in primes if (p-1) % q == 0]
        reserved = {next(i for i, d in enumerate(deltas) if d % q) for q in bad}
        for i in range(len(deltas)):
            if len(reserved) == r:
                break
            reserved.add(i)
        assert len(reserved) == r
        target = min(reserved)
        root = positive_root(p, modulus, period)
        plans = []
        for q in primes:
            delta = [(x-values[0]) % modulus for x in values[1:]]
            if q in bad or delta[target] % q:
                continue
            source = next(i for i, d in enumerate(delta) if d % q)
            buffer = next(i for i in range(len(delta)) if i not in (source, target))
            exponent = choose_root_power(p, primes, delta, source, target)
            local = [values[0], values[source+1], values[target+1], values[buffer+1]]
            following = mv(mpow(root, exponent, modulus), local, modulus)
            assert following[0] == local[0] and following[1] == local[1]
            values[0], values[source+1], values[target+1], values[buffer+1] = following
            plans.append({"prime": q, "source": source, "target": target,
                          "buffer": buffer, "power": exponent})
        assert all(any((values[i+1]-values[0]) % q for i in reserved) for q in primes)
        default_count = p+r-len(deltas)
        assert default_count >= 0
        second = (sum(values[1:])+default_count-sum(values[i+1] for i in reserved))
        second = second*pow(p, -1, modulus) % modulus
        assert (p*values[0]+p*second+sum(values[i+1] for i in reserved)) % modulus == 0
        records.append({"p": p, "r": r, "n": n, "primes": primes,
                        "period": period, "initial_distinguished_values": initial_values,
                        "default_singletons": default_count, "reserved_roles": sorted(reserved),
                        "root_plan": plans, "second_block_modulus": second})
    print("old r-below-prime-count entry gaps crossed: PASS", len(records))
    return records


if __name__ == "__main__":
    data = {"algebra": check_algebra()}
    data["literal_entries"], data["weighted_core_paths"] = check_literal_entries()
    data["large_seven_prime_case"] = check_large_cover()
    data["old_entry_gap_cases"] = check_old_entry_gaps()
    data["scope"] = ("Unrestricted two-block entry and original-position commutator "
                     "identities. Full endpoint and odd-band sufficiency additionally "
                     "use the established core theorems with their external dependencies.")
    (ROOT/"unrestricted_endpoint_entry_records.json").write_text(
        json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print("unrestricted endpoint and lower-band entry: PASS")
