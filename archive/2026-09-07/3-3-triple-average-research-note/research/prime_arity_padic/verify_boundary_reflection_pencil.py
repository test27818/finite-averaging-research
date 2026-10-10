"""Check a closed-form reflection pencil, not a word or orbit search.

The companion proof carries all quantifiers. Integer formulas are checked
first; Fraction matrices and literal positions are confined to small cases.
Running this file only writes its own verification record.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
from time import perf_counter
import json
import re
import sys

sys.dont_write_bytecode = True


HERE = Path(__file__).resolve().parent
IDENTITY = (F(1), F(0), F(0), F(1))
SWAP = (F(1), F(0), F(0), F(-1))


def mm(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def det(a):
    return a[0]*a[3]-a[1]*a[2]


def inv(a):
    d = det(a)
    assert d
    return (a[3]/d, -a[1]/d, -a[2]/d, a[0]/d)


def scale(a, t):
    return tuple(t*x for x in a)


def U(t):
    return (F(1), F(t), F(0), F(1))


def L(t):
    return (F(1), F(0), F(t), F(1))


def mv(a, x):
    return (a[0]*x[0]+a[1]*x[1], a[2]*x[0]+a[3]*x[1])


def primes(limit):
    sieve = bytearray(b'\1')*(limit+1)
    sieve[:2] = b'\0\0'
    for q in range(2, isqrt(limit)+1):
        if sieve[q]:
            sieve[q*q:limit+1:q] = b'\0'*(((limit-q*q)//q)+1)
    return [q for q in range(3, limit+1, 2) if sieve[q]]


def data(p, r):
    assert p % 2 == r % 2 == 1 and 1 <= r <= p-2
    n = 2*p+r
    eps = ((p-r)//2) % 2
    d = r-2*eps
    divisor = r if eps == 0 else 1
    alphas = (-r, 4-r)
    rows = []
    scalars = []
    for alpha in alphas:
        assert (p+alpha) % 2 == 0
        source = ((p+alpha)//2, (p-alpha)//2, 0)
        numerators = (p+2*r-alpha-2*eps, p+alpha-2*eps)
        assert all(x % 4 == 0 for x in numerators)
        row = (numerators[0]//4, numerators[1]//4, eps, (p-r)//2)
        stock = (p-source[0], p-source[1], r, p-r)
        assert min(source) >= 0 and sum(source) == p
        assert sum(row) == p and all(0 <= x <= c for x, c in zip(row, stock))
        beta = r*source[1]
        J = (beta, p*r*row[1]-p*p*eps+beta*row[3], -alpha, -beta)
        assert p*(row[0]-row[1])+alpha*row[3] == beta
        numerator = p*r*r-n*d*alpha
        assert numerator % 4 == 0
        Falpha = numerator//4
        assert Falpha % divisor == 0
        f = Falpha//divisor
        assert f and Falpha and J[0]*J[0]+J[1]*J[2] == p*Falpha
        assert (p*Falpha-p**4) % n == 0
        assert gcd(Falpha, n) == 1
        primitive_content = gcd(*J)
        assert primitive_content % 2 == 1
        rows.append((source, row, J, Falpha))
        scalars.append(f)
    f0, f1 = scalars
    assert gcd(f0, f1) == 1
    assert f0 % r == 0
    assert (f0-f1) % 2 == 1
    assert (f0-f1) == n*d//divisor
    assert any(det(J)//gcd(*J)**2 % 2 == 0 for _, _, J, _ in rows)
    return n, eps, d, divisor, rows, scalars


def average(state, positions):
    assert len(positions) == len(set(positions))
    mean = sum((state[i] for i in positions), F(0))/len(positions)
    for i in positions:
        state[i] = mean


def replay(p, r, source, row, coordinate):
    """Execute the three specified averages on the original positions."""
    a, z = coordinate
    values = (a, r*z-a, -p*z)
    state = [F(values[0])]*p+[F(values[1])]*p+[F(values[2])]*r
    pools = [list(range(p)), list(range(p, 2*p)), list(range(2*p, 2*p+r))]
    first = []
    for pool, count in zip(pools, source):
        first.extend(pool[:count])
        del pool[:count]
    assert len(first) == p
    average(state, first)
    carrier = first[:r]
    pools.append(first[r:])
    second = []
    for pool, count in zip(pools, row):
        second.extend(pool[:count])
        del pool[:count]
    third = [index for pool in pools for index in pool]
    assert len(second) == len(third) == p and len(carrier) == r
    assert sorted(carrier+second+third) == list(range(2*p+r))
    average(state, second)
    average(state, third)
    out_a = state[second[0]]
    out_z = -state[carrier[0]]/p
    assert all(state[i] == out_a for i in second)
    assert all(state[i] == r*out_z-out_a for i in third)
    assert all(state[i] == -p*out_z for i in carrier)
    return (out_a, out_z), 3


def matrix_checks(p, r, info):
    n, eps, d, divisor, rows, fs = info
    # (a,z) -> (u=z, v=a-rz/2).
    B = (F(0), F(1), F(1), -F(r, 2))
    Js = []
    for (source, row, integral_J, Falpha), alpha in zip(rows, (-r, 4-r)):
        J = (-F(r*p, 2), F(-alpha), F(p*n*d, 4), F(r*p, 2))
        assert mm(mm(B, tuple(F(x) for x in integral_J)), inv(B)) == J
        assert mm(J, J) == scale(IDENTITY, p*Falpha)
        Js.append(J)
    T = mm(Js[1], inv(Js[0]))
    assert T == (F(fs[1], fs[0]), -F(2*r, divisor*fs[0]), F(0), F(1))
    comm = mm(mm(mm(SWAP, T), SWAP), inv(T))
    assert comm == U(F(4*r, divisor*fs[0]))
    K = (-F(r, 2), F(1), F(r*n, 4), F(r, 2))
    assert mm(K, K) == scale(IDENTITY, F(r*(p+r), 2))
    H = mm(K, U(F(2, r)))
    assert H == (-F(r, 2), F(0), F(r*n, 4), F(p+r))
    assert mm(mm(mm(SWAP, H), SWAP), inv(H)) == L(n)
    P = (F(1), F(-2), F(0), F(n))
    assert mm(mm(inv(P), U(1)), P) == U(n)
    K_conj = mm(mm(K, U(F(8*(p+r), r))), inv(K))
    assert mm(mm(inv(P), K_conj), P) == L(n)
    # The final common terminal coordinates (z,y).
    C = (F(1), F(0), F(n, 2), F(1))
    assert mm(mm(C, L(n)), inv(C)) == L(n)
    k = 4*((-pow(p*p, -1, n)*pow(4, -1, n)) % n)
    V = mm(mm(C, U(k)), inv(C))
    assert all(x.denominator == 1 for x in V)
    assert det(V) == 1
    assert tuple(int(x) % n for x in V) == (1, (-pow(p*p, -1, n)) % n, 0, 1)
    terminal = (F(1), F(p*p-n*(p-1)//2))
    terminal_az = (terminal[1]-p, terminal[0])
    a, z = terminal_az
    assert (p+1)//2*a+(p-1)//2*(r*z-a) == 0
    return 13


def terminal_interfaces():
    from verify_finite_orbit_completion_without_ring_extension import complete
    count = 0
    for p in primes(71):
        for r in range(1, p, 2):
            n = 2*p+r
            k = 4*((-pow(p*p, -1, n)*pow(4, -1, n)) % n)
            V = (1-k*n//2, k, -k*n*n//4, 1+k*n//2)
            for z in (0, 1, -1, n+2):
                for y in (1, -1, p, n-1):
                    # Every chosen residue column is primitive modulo n^2.
                    # complete() only verifies the finite terminal arithmetic;
                    # the companion proof supplies all physical prerequisites.
                    assert gcd(y, n) == 1
                    complete(p, r, V, (z, y))
                    count += 1
    return count


def document_checks():
    from verify_square_zero_compiler import check_frozen_files
    links = 0
    for name in ("odd_lower_band_boundary_reflection_pencil_20260916.md",
                 "unified_stable_range_saturation_candidate_20260916.md"):
        path = HERE/name
        body = path.read_text(encoding="utf-8")
        assert not any(ord(c) < 32 and c not in "\n\r\t" for c in body)
        assert "\ufffd" not in body
        assert body.count(r"\[") == body.count(r"\]")
        assert body.count(r"\(") == body.count(r"\)")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", body):
            if target.startswith(("https://", "http://")):
                continue
            assert (HERE/target.split("#", 1)[0]).is_file(), target
            links += 1
    return {"new_document_links": links, "frozen_files_unchanged": check_frozen_files()}


def main():
    start = perf_counter()
    integer_cases = matrices = literal_steps = boundary_cases = 0
    for p in primes(2000):
        for r in range(1, p, 2):
            info = data(p, r)
            integer_cases += 1
            if p <= 71:
                matrices += matrix_checks(p, r, info)
            if p <= 31:
                for source, row, J, _ in info[4]:
                    for coordinate in ((F(1), F(0)), (F(0), F(1))):
                        actual, count = replay(p, r, source, row, coordinate)
                        assert actual == mv(scale(J, F(1, p*p)), coordinate)
                        literal_steps += count
                # The retained-B reflection, with its identity first average.
                source = (0, p, 0)
                row = ((p+r)//2, 0, 0, (p-r)//2)
                K_az = (F(r), F(r*(p-r), 2), F(1), F(-r))
                for coordinate in ((F(1), F(0)), (F(0), F(1))):
                    actual, count = replay(p, r, source, row, coordinate)
                    assert actual == mv(scale(K_az, F(1, p)), coordinate)
                    literal_steps += count
    for p in (1000000007, 1000000009, 2**31-1, 2**61-1):
        for r in sorted({1, 3, 5, p-2, p-4, p-6, (p//2)|1, (p//3)|1}):
            info = data(p, r)
            matrices += matrix_checks(p, r, info)
            boundary_cases += 1
    report = {
        "status": "PASS",
        "integer_formula_and_capacity_cases": integer_cases,
        "exact_matrix_identities": matrices,
        "literal_original_position_averages": literal_steps,
        "large_integer_boundary_cases": boundary_cases,
        "new_menu_finite_terminal_interfaces": terminal_interfaces(),
        "document_checks": document_checks(),
        "seconds": round(perf_counter()-start, 3),
        "scope": "Checks closed formulas and physical returns. No word search, group enumeration, or numerical substitute for the proof. Morris/Serre and the previously proved entrance/terminal are referenced, not proved here."
    }
    (HERE/"boundary_reflection_pencil_verification.json").write_text(
        json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Assertions required.")
    main()
