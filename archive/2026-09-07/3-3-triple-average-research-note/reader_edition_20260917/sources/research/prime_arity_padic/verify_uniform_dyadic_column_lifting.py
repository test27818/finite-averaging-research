"""Audit and compile the uniform dyadic column lemma, without orbit search.

The theorem for all parameters and precisions is proved in the companion note.
This checker uses only the standard library, exact fractions, 2x2 modular
arithmetic, cached expression evaluation and repeated squaring. No frozen
project file is written. Run with: python -B <this file>
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter
import json
import sys

if not __debug__:
    raise RuntimeError("Assertions must remain enabled.")
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ID = (1, 0, 0, 1)


def mm(A, B, modulus=None):
    a, b, c, d = A
    e, f, g, h = B
    out = (a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h)
    return out if modulus is None else tuple(x % modulus for x in out)


def sc(c, A):
    return tuple(c*x for x in A)


def residue(x, modulus):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def red(A, modulus):
    return tuple(residue(x, modulus) for x in A)


def inverse(A, modulus=None):
    a, b, c, d = A
    delta = a*d-b*c
    factor = F(1, delta) if modulus is None else pow(delta, -1, modulus)
    out = sc(factor, (d, -b, -c, a))
    return out if modulus is None else tuple(x % modulus for x in out)


def power(A, exponent, modulus):
    if exponent < 0:
        A, exponent = inverse(A, modulus), -exponent
    result = ID
    while exponent:
        if exponent & 1:
            result = mm(result, A, modulus)
        A = mm(A, A, modulus)
        exponent >>= 1
    return result


def act(A, w, modulus):
    a, b, c, d = A
    u, v = w
    return ((a*u+b*v) % modulus, (c*u+d*v) % modulus)


def mul(*args):
    return ("mul", args)


def inv(expr):
    return ("inv", expr)


def pw(expr, exponent):
    return ("pow", expr, exponent)


def evaluator(generators, modulus):
    @lru_cache(None)
    def evaluate(expr):
        kind = expr[0]
        if kind == "g":
            return red(generators[expr[1]], modulus)
        if kind == "inv":
            return inverse(evaluate(expr[1]), modulus)
        if kind == "pow":
            return power(evaluate(expr[1]), expr[2], modulus)
        if kind == "mul":
            result = ID
            for item in expr[1]:
                result = mm(result, evaluate(item), modulus)
            return result
        raise ValueError(kind)
    return evaluate


def data(m, t, s0, a, tau, alpha, chosen):
    assert m % 2 and t % 2 == 0 and s0 % 2
    assert chosen in (0, 1)
    assert residue(F(a)/2, 2) == 1
    assert residue(tau, 2) == residue(alpha, 2) == 1
    tau, alpha, a = F(tau), F(alpha), F(a)
    ss = (s0, s0-2)
    js = [(-t, -1, m*(t-s), t) for s in ss]
    ds = [m*(t-s)-t*t for s in ss]
    M = list(js[chosen])
    M[3] += a
    generators = (sc(1/tau, js[0]), sc(1/tau, js[1]), sc(1/alpha, M))
    z0, z1, T = tuple(("g", i) for i in range(3))
    V = mul(T, inv((z0, z1)[chosen]))
    index = 0 if ds[0] % 4 == 1 else 1
    S = pw((z0, z1)[index], 2)
    epsilon = 0 if residue(tau/alpha, 4) == 1 else 1
    low = mul(pw(S, epsilon), V)
    up = mul(z0, low, inv(z0))
    conjugate_v = mul(z0, V, inv(z0))
    scale = mul(V, conjugate_v, inv(V), inv(conjugate_v))
    recipes = {
        "Z": z0, "S": S, "L": low, "U": up,
        "V": V, "K21": pw(V, 2),
        "K12": mul(z0, pw(V, 2), inv(z0)), "K0": scale,
    }
    return {
        "generators": generators, "recipes": recipes, "js": js, "ds": ds,
        "M": tuple(M), "chosen": chosen, "m": m, "t": t,
        "s0": s0, "a": a, "tau": tau, "alpha": alpha,
    }


def local_identities(d):
    ev8 = evaluator(d["generators"], 8)
    ev4 = evaluator(d["generators"], 4)
    r = d["recipes"]
    assert ev4(r["S"]) == (3, 0, 0, 3)
    assert ev4(r["L"]) == (1, 0, 2, 1)
    assert ev4(r["U"]) == (1, 2, 0, 1)
    assert ev8(r["K21"]) == (1, 0, 4, 1)
    assert ev8(r["K12"]) == (1, 4, 0, 1)
    assert ev8(r["K0"]) == (5, 0, 0, 5)


def compile_column(d, bits, w, modulus=None):
    """Return chronological named powers, keeping the complete column."""
    assert bits >= 1
    if modulus is None:
        modulus = 1 << bits
    assert modulus % (1 << bits) == 0
    assert (w[0]+w[1]) % 2 == 1
    ev = evaluator(d["generators"], modulus)
    r = d["recipes"]
    current = tuple(x % modulus for x in w)
    word = []
    def step(name, exponent=1, matrix=None):
        nonlocal current
        mat = power(ev(r[name]), exponent, modulus) if matrix is None else matrix
        current = act(mat, current, modulus)
        word.append((name, exponent))
    if current[0] & 1:
        step("Z")
    if bits == 1:
        assert tuple(x % 2 for x in current) == (0, 1)
        return current, word
    if current[0] % 4 == 2:
        step("U")
    if current[1] % 4 == 3:
        step("S")
    assert tuple(x % 4 for x in current) == (0, 1)
    up, scale = ev(r["K12"]), ev(r["K0"])
    for k in range(2, bits):
        dx = (current[0] >> k) & 1
        dy = ((current[1]-1) >> k) & 1
        if dx:
            step("K12", 1 << (k-2), up)
        if dy:
            step("K0", 1 << (k-2), scale)
        assert tuple(x % (1 << (k+1)) for x in current) == (0, 1)
        up, scale = mm(up, up, modulus), mm(scale, scale, modulus)
    assert tuple(x % (1 << bits) for x in current) == (0, 1)
    return current, word


def chronological_leaves(expr, backwards=False):
    """Independent expansion to signed original-generator actions."""
    kind = expr[0]
    if kind == "g":
        yield expr[1], -1 if backwards else 1
    elif kind == "inv":
        yield from chronological_leaves(expr[1], not backwards)
    elif kind == "pow":
        count = expr[2]
        for _ in range(abs(count)):
            yield from chronological_leaves(expr[1], backwards != (count < 0))
    elif kind == "mul":
        items = expr[1] if backwards else reversed(expr[1])
        for item in items:
            yield from chronological_leaves(item, backwards)
    else:
        raise ValueError(kind)


def replay(d, initial, word, modulus, expand=False):
    current = tuple(x % modulus for x in initial)
    count = 0
    ev = evaluator(d["generators"], modulus)
    total = ID
    base = [red(g, modulus) for g in d["generators"]]
    signed = {(i, 1): g for i, g in enumerate(base)}
    signed.update({(i, -1): inverse(g, modulus) for i, g in enumerate(base)})
    for name, exponent in word:
        expr = pw(d["recipes"][name], exponent)
        total = mm(ev(expr), total, modulus)
        if expand:
            for index, sign in chronological_leaves(expr):
                current = act(signed[index, sign], current, modulus)
                count += 1
    via_matrix = act(total, initial, modulus)
    if expand:
        assert current == via_matrix
    return via_matrix, count, total


def check_residue_identities():
    """All relevant modulo-8 parameters, not a group/orbit enumeration."""
    units = (1, 3, 5, 7)
    count = 0
    for m, t, s0, a, tau, alpha, chosen in product(
            units, (0, 2, 4, 6), units, (2, 6), units, units, (0, 1)):
        local_identities(data(m, t, s0, a, tau, alpha, chosen))
        count += 1
    return count


def check_rational_and_precision():
    rng = Random(20260916)
    cases = columns = leaves = 0
    precisions = (1, 2, 3, 4, 6, 10, 17, 32, 65)
    for i in range(48):
        m = 2*rng.randrange(-80, 81)+1
        t = 2*rng.randrange(-60, 61)
        s = 2*rng.randrange(-60, 61)+1
        odd = lambda: 2*rng.randrange(1, 25)+1
        a = F((-1 if i % 2 else 1)*2*odd(), odd())
        tau, alpha = F(odd(), odd()), F((-1 if i % 3 else 1)*odd(), odd())
        d = data(m, t, s, a, tau, alpha, i % 2)
        local_identities(d)
        js, ds = d["js"], d["ds"]
        assert mm(js[0], js[0]) == sc(-ds[0], ID)
        assert mm(js[1], js[1]) == sc(-ds[1], ID)
        assert ds[1]-ds[0] == 2*m
        selected = i % 2
        c = -a*m*(t-(s-2*selected))/ds[selected]
        e = -a*t/ds[selected]
        assert mm(d["generators"][2], inverse(d["generators"][selected])) == sc(
            tau/alpha, (1, 0, c, 1+e))
        cases += 1
        for bits in precisions:
            mod = 1 << bits
            u = rng.randrange(mod)
            v = 2*rng.randrange(max(1, mod//2)) + (1-(u % 2))
            initial = (u, v % mod)
            result, word = compile_column(d, bits, initial)
            got, expanded, _ = replay(d, initial, word, mod, expand=bits <= 10)
            assert got == result == (0, 1)
            columns += 1
            leaves += expanded
    return cases, columns, leaves


def old_cases():
    # Import solely for read-only comparison with the existing exact generators.
    sys.path.insert(0, str(ROOT/"work"))
    import verify_even_interior_completion as old
    for p in range(1, 128, 2):
        o = old.edge_data(p, "r4")
        d = data(o["m"], 2, 3, 2, o["tau"], o["eps2"]**2, 1)
        assert d["generators"] == tuple(o["generators"][1:4])
        yield "r4", p, d, 6
    for p in range(7, 192, 4):
        if p % 3 == 0:
            continue
        t, m = (p-3)//2, (3*p-3)//2
        ss = (p-4, p-6)
        a, chosen, j = (2, 0, 1) if p % 3 == 1 else (-2, 1, 4)
        det = (p-3)*j-p*ss[chosen]
        for tau in range(1, 16, 2):
            d = data(m, t, ss[0], a, tau, F(-det, tau), chosen)
            assert d["M"] == (-t, -1, m*(t-ss[chosen]), t+a)
            yield "edge", p, d, 4


def check_old_parameter_classes():
    rng = Random(14701)
    counts = {"r4": 0, "edge": 0}
    columns = leaves = 0
    for label, p, d, bits in old_cases():
        counts[label] += 1
        local_identities(d)
        modulus = 1 << bits
        # Fixed adversarial columns and random columns; never enumerate an orbit.
        inputs = [(0, 1), (1, 0), (0, modulus-1), (modulus-1, 0),
                  (modulus-2, modulus-1), (modulus-1, modulus-2)]
        for _ in range(6):
            u = rng.randrange(modulus)
            inputs.append((u, 2*rng.randrange(modulus//2)+1-u%2))
        for initial in inputs:
            out, word = compile_column(d, bits, initial)
            got, count, _ = replay(d, initial, word, modulus, expand=True)
            assert got == out == (0, 1)
            columns += 1
            leaves += count
    assert counts == {"r4": 64, "edge": 256}
    return counts, columns, leaves


def isprime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5)+1))


def physical_two_average_check(p, t, s, j, expected):
    """Replay the existing two-average count rule on both full core basis inputs."""
    r, n = 2*t, 2*(p+t)
    i = p-j-s
    assert min(i, j, s) >= 0 and i <= p-r and j <= p and s <= r
    ga, gb, gc = list(range(p)), list(range(p, 2*p)), list(range(2*p, n))
    kept = ga[p-r:]
    left = ga[:i]+gb[:j]+gc[:s]
    right = ga[i:p-r]+gb[j:]+gc[s:]
    assert len(left) == len(right) == p and len(kept) == r
    assert sorted(left+right+kept) == list(range(n))
    for u, v in ((1, 0), (0, 1)):
        state = [F(t*u+v)]*p+[F(t*u-v)]*p+[F(-p*u)]*r
        for group in (left, right):
            avg = sum(state[q] for q in group)/p
            for q in group:
                state[q] = avg
        a, b, c, d = expected
        uu, vv = F(a*u+b*v, p), F(c*u+d*v, p)
        for group, val in ((left, t*uu+vv), (right, t*uu-vv), (kept, -p*uu)):
            assert all(state[q] == val for q in group)
    return 4  # Two basis inputs, two physical atoms each.


def check_actual_interfaces():
    import verify_even_interior_completion as old
    counts = columns = atoms = leaves = 0
    rng = Random(23981)
    examples = []
    primes = [p for p in range(7, 151) if isprime(p)]
    for p in primes:
        labels = (["r4"] if p >= 11 else []) + (["edge"] if p % 4 == 3 else [])
        for label in labels:
            o = old.edge_data(p, label)
            tau = o["tau"]
            alpha = o["eps2"]**2 if label == "r4" else -F(o["determinant"])/tau
            chosen = o["choices"].index(o["s"])
            d = data(o["m"], o["t"], o["choices"][0], o["trace"], tau, alpha, chosen)
            assert d["generators"] == tuple(o["generators"][1:4])
            m = o["m"]
            assert residue(tau, m) == o["t"] % m
            assert residue(alpha, m) == (o["t"]+o["trace"]) % m
            assert gcd(o["determinant"], 2*m) == 1
            for gen in d["generators"]:
                reduced = red(gen, m)
                assert reduced[2:] == (0, 1)
                assert gcd(reduced[0], m) == 1
            for i, s in enumerate(o["choices"]):
                atoms += physical_two_average_check(p, o["t"], s, (p-s)//2, d["js"][i])
            atoms += physical_two_average_check(p, o["t"], o["s"], o["j"], d["M"])
            bits = 6 if label == "r4" else 4
            modulus = (1 << bits)*m*m
            for index in range(8):
                v = 1+m*rng.randrange(2*m)
                u = 2*rng.randrange(modulus//2) + 1-v%2
                initial = (u, v)
                out, word = compile_column(d, bits, initial, modulus)
                got, expanded, total = replay(d, initial, word, modulus, expand=True)
                assert got == out and out[1] % m == 1
                assert (total[2] % m, total[3] % m) == (0, 1)
                columns += 1
                leaves += expanded
                if index == 3 and ((p == 11 and label == "r4") or (p == 7 and label == "edge")):
                    examples.append({"p": p, "r": o["r"], "modulus": modulus,
                                     "input": initial, "output": out,
                                     "chronological_named_powers": word})
            counts += 1
    return counts, columns, atoms, leaves, examples


def main():
    started = perf_counter()
    from verify_square_zero_compiler import check_frozen_files, check_local_links
    frozen = check_frozen_files()
    residues = check_residue_identities()
    rational, high, high_leaves = check_rational_and_precision()
    old, old_columns, old_leaves = check_old_parameter_classes()
    physical, interfaces, atoms, interface_leaves, examples = check_actual_interfaces()
    report = {
        "status": "PASS", "date": "2026-09-16",
        "complete_mod8_parameter_classes": residues,
        "exact_rational_parameter_cases": rational,
        "finite_precision_column_checks": high,
        "tested_bit_precisions": [1, 2, 3, 4, 6, 10, 17, 32, 65],
        "old_parameter_classes": old,
        "old_class_deterministic_transports_checked": old_columns,
        "actual_prime_parameter_interfaces": physical,
        "mixed_modulus_transports_preserving_v_mod_m": interfaces,
        "literal_original_position_average_atoms": atoms,
        "signed_original_generator_actions_replayed": high_leaves+old_leaves+interface_leaves,
        "unchanged_frozen_files": frozen,
        "examples": examples,
        "scope": "All-parameter theorem is proved by identities and induction in the note. "
                 "No group/orbit or averaging-word search. Transports are compressed words in "
                 "old generators and their already-proved positive projective inverses; "
                 "the full inverse/deep-kernel atomic words are not expanded here.",
    }
    target = HERE/"uniform_dyadic_column_lifting_verification.json"
    # Link checking needs the new result file to exist.
    target.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    report["local_links_checked"] = check_local_links()
    report["unchanged_frozen_files"] = check_frozen_files()
    report["wall_seconds"] = round(perf_counter()-started, 3)
    target.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "examples"}, indent=2))


if __name__ == "__main__":
    main()

