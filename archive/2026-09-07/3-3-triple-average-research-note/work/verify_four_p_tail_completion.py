"""Uniform repair of the d_p tail above4p.

Sieve-generated parameter list, closed capacities, exact matrix identities,
literal five-atom replays and logarithmic prime-power direction lifting.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, prod
from random import Random

from verify_four_prime_entry_and_band import factors, Ledger
from verify_uniform_odd_middle_cores import mm, invq, residue
from verify_upper_band_unrestricted_completion import (
    ceildiv, scale, det, zy, apply_mod, local_cycle_hit, pure_prime_order)
from verify_even_odd_half_core import I, U, mod_power, valuation, crt_pairs, principal_unit_log


if not __debug__:
    raise RuntimeError("Assertions are required.")


def digit_interval(p, s):
    r = p+s
    return r//2+(2 if r % 2 == 0 else 5), 2*p-1


def safe_a(p, s, q):
    r, n = p+s, 4*p+s
    j = max(0, ceildiv(q-r//2, 3), ceildiv(q-p, 2))
    high = min(p//2, q//3, (q-ceildiv(r, 2))//2)
    assert j <= high, (p, s, q, j, high)
    k = q-3*j
    i = p-j-k
    assert i >= 0 and 2*i <= 2*p-r and 2*j <= p and 2*k <= r
    return (p-q, n*j-p*q, -1, 0), j, k


def data(p, s):
    assert p >= 16*s+21
    n, r = 4*p+s, p+s
    eps = 1 if p % 4 == 1 else -1
    t0 = (p-eps)//4
    first = (t0, t0+s)
    ja = ceildiv(p-s, 6)
    assert ja+2 <= (p-s)//4
    ds = tuple(p*p-n*(ja+k) for k in range(3))
    aa = tuple((0, -d, -1, 0) for d in ds)
    records = []
    for t in first:
        b = p-s-3*t
        low = max(0, ceildiv(5*p-5*s-16*t, 6))
        high = b
        assert low+1 <= high and 0 <= b and 2*b <= r and 2*t <= p
        beta = r*t-p*b
        assert beta == n*t-p*p+p*s and gcd(beta, s) == 1
        fs, matrices = [], []
        for y in (low, low+1):
            x, u, v = 2*y+t-b, p-2*t+b-3*y, t
            assert min(x, y, u, v) >= 0 and x+y+u+v == p
            assert x <= b+t and 2*y <= p-2*t and 2*u <= r-2*b and 2*v <= 2*p-r
            q = p*r*y-p*p*u+t*beta
            jmat = (beta, q, -s, -beta)
            f = p**3+n*(4*t*t+(s-2*p)*t-s*y)
            assert mm(jmat, jmat) == scale(I, p*f)
            assert gcd(f, n) == 1
            assert zy(jmat, p) == (p*p-n*t, -s, n*(p*y-t*(p-t)), -p*p+n*t)
            fs.append(f)
            matrices.append(jmat)
        assert fs[1] == fs[0]-s*n and gcd(*fs) == 1
        affine = mm(invq(matrices[0]), matrices[1])
        assert affine == (1, F(beta*n, fs[0]), 0, F(fs[1], fs[0]))
        diagonal = mm(invq(aa[0]), aa[1])
        root = mm(mm(mm(diagonal, affine), invq(diagonal)), invq(affine))
        assert root == U(F(beta*n*n, ds[1]*fs[1]))
        records.append((t, b, low, beta, fs, matrices))
    g = gcd(n, 5)
    assert gcd(records[0][3], records[1][3]) == g
    assert gcd(ds[0], ds[1]) == 1 and all(gcd(d, n) == 1 for d in ds)
    lower, upper = digit_interval(p, s)
    for q in (lower, lower+1, upper-1, upper):
        safe_a(p, s, q)
    return n, r, ja, ds, aa, records, g


def phi(n):
    result = n
    for q in factors(n):
        result = result//q*(q-1)
    return result


def interval_units(low, high, primes):
    value = 0
    for size in range(len(primes)+1):
        for subset in combinations(primes, size):
            divisor = prod(subset)
            value += (-1)**size*(high//divisor-(low-1)//divisor)
    return value


def choose_affine(p, constraints):
    blocked = bytearray(p)
    for ell, constant, slope in constraints:
        c, a = residue(constant, ell), residue(slope, ell)
        if a == 0:
            assert c != 0
        else:
            first = (-c*pow(a, -1, ell)) % ell
            for k in range(first, p, ell):
                blocked[k] = 1
    return next(k for k in range(1, p) if not blocked[k])


def mix(ledger, a, b, k):
    left, right = a[:-k]+b[:k], a[-k:]+b[k:]
    ledger.average(left)
    ledger.average(right)
    return left, right


def fold_three(ledger, blocks):
    p = ledger.p
    eps = 1 if p % 3 == 1 else -1
    m = (p-eps)//3
    counts = (m+eps, m, m)
    left = sum((g[:c] for g, c in zip(blocks, counts)), [])
    right = sum((g[c:2*c] for g, c in zip(blocks, counts)), [])
    other = sum((g[2*c:] for g, c in zip(blocks, counts)), [])
    for group in (left, right, other):
        ledger.average(group)
    return left+right, other


def full_input_entry(p, s, rng):
    n, primes = 4*p+s, tuple(factors(4*p+s))
    raw = [rng.randrange(-10000, 10001) for _ in range(n-1)]
    raw.append(-sum(raw))
    assert all(any((x-raw[0]) % q for x in raw) for q in primes)
    ledger = Ledger(raw, p)
    val = lambda g: ledger.state[g[0]]
    w = 0
    protected = {w}
    for q in primes:
        protected.add(next(i for i, x in enumerate(raw) if (x-raw[w]) % q))
    free = [i for i in range(n) if i not in protected]
    a, b = free[:p], free[p:2*p]
    for group in (a, b):
        ledger.average(group)
    used = set(a+b)
    singles = [i for i in range(n) if i not in used]
    while True:
        missing = [q for q in primes if residue(val(a)-ledger.state[w], q) == 0]
        if not missing:
            break
        q0 = missing[0]
        if residue(val(b)-ledger.state[w], q0) == 0:
            x = next(i for i in singles if i != w and residue(ledger.state[i]-ledger.state[w], q0))
            selected, old = b[:-1]+[x], b[-1]
            ledger.average(selected)
            b = selected
            singles[singles.index(x)] = old
        constraints = [(q, val(a)-ledger.state[w], (val(b)-val(a))/p) for q in primes
                       if residue(val(a)-ledger.state[w], q) or residue(val(b)-ledger.state[w], q)]
        a, b = mix(ledger, a, b, choose_affine(p, constraints))
    free = [i for i in singles if i != w]
    c, d = free[:p], free[p:2*p]
    for group in (c, d):
        ledger.average(group)
    used = set(c+d)
    singles = [i for i in singles if i not in used]
    constraints = [(q, val(c)-val(a), (val(b)-val(c))/p) for q in primes
                   if residue(val(b)-val(a), q) or residue(val(c)-val(a), q)]
    b, c = mix(ledger, b, c, choose_affine(p, constraints))
    selected, old = b[:-1]+[w], b[-1]
    ledger.average(selected)
    b = selected
    singles[singles.index(w)] = old
    assert all(residue(val(b)-val(a), q) or residue(val(c)-val(a), q) for q in primes)

    constraints = [(q, val(b)-val(a), (val(c)-val(b))/p) for q in primes
                   if residue(val(b)-val(a), q) or residue(val(c)-val(a), q)]
    b, c = mix(ledger, b, c, choose_affine(p, constraints))
    eps = 1 if p % 3 == 1 else -1
    m = (p-eps)//3
    total = val(a)+val(b)+val(c)
    constraints = [(q, m*total+eps*val(a)-p*val(d), eps*(val(b)-val(a))/p) for q in primes]
    a, b = mix(ledger, a, b, choose_affine(p, constraints))
    big, b = fold_three(ledger, (a, b, c))
    assert all(residue(val(big)-val(d), q) for q in primes)
    e, carriers = big[:p-s]+singles, big[p-s:]
    ledger.average(e)
    assert len(carriers) == p+s
    constraints = [(q, val(e)-val(carriers), (val(b)-val(e))/p) for q in primes]
    e, b = mix(ledger, e, b, choose_affine(p, constraints))
    big, b = fold_three(ledger, (e, b, d))
    groups = (big, b, carriers)
    assert [len(g) for g in groups] == [2*p, p, p+s]
    a, z = val(big), -val(carriers)/p
    assert val(b) == -2*a+(p+s)*z
    assert all(residue(a+p*z, q) for q in primes)
    assert sorted(big+b+carriers) == list(range(n))
    ledger.independent_replay(raw)
    return len(ledger.word)


def arithmetic_bounds(p, s):
    n = 4*p+s
    primes = tuple(factors(n))
    d = len(primes)
    assert d >= s+3
    assert (n % 2 and d >= 4) or (n % 2 == 0 and d >= 5)
    assert p >= 16*s+21
    ph = phi(n)
    assert ph > 8*2**d+7*s+36
    low, high = digit_interval(p, s)
    count = interval_units(low, high, primes)
    assert 4*count > ph and high < n/2
    assert (p-1)*F(ph, n) > 2**d-1
    return count


def five_return(ledger, groups, s, record, index):
    ga, gb, gc = (list(g) for g in groups)
    p, r = ledger.p, len(gc)
    t, b, y0, _, _, _ = record
    i = p-b-t
    created = []
    for k in range(2):
        group = ga[k*i:(k+1)*i]+gb[k*t:(k+1)*t]+gc[k*b:(k+1)*b]
        ledger.average(group)
        created += group
    ga, gb, gc = ga[2*i:], gb[2*t:], gc[2*b:]
    kept, created = created[:r], created[r:]
    y = y0+index
    x, u, v = 2*y+t-b, p-2*t+b-3*y, t
    left = ga[:x]+gb[:y]+gc[:u]+created[:v]
    right = ga[x:2*x]+gb[y:2*y]+gc[u:2*u]+created[v:2*v]
    other = ga[2*x:]+gb[2*y:]+gc[2*u:]+created[2*v:]
    assert sorted(left+right+other+kept) == list(range(3*p+r))
    for group in (left, right, other):
        ledger.average(group)
    return [left+right, other, kept]


def physical(p, s, system):
    n, r, _, _, _, records, _ = system
    checked = 0
    for record in records:
        for index in range(2):
            for a, z in ((1, 0), (0, 1)):
                raw = [a]*(2*p)+[-2*a+r*z]*p+[-p*z]*r
                ledger = Ledger(raw, p)
                groups = [list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))]
                groups = five_return(ledger, groups, s, record, index)
                matrix = record[5][index]
                av, zv = F(matrix[0]*a+matrix[1]*z, p*p), F(matrix[2]*a+matrix[3]*z, p*p)
                expected = (av, -2*av+r*zv, -p*zv)
                assert all(ledger.state[j] == value
                           for group, value in zip(groups, expected) for j in group)
                groups = five_return(ledger, groups, s, record, index)
                scalar = F(record[4][index], p**3)
                assert [ledger.state[group[0]] for group in groups] == [scalar*a, scalar*(-2*a+r*z), -scalar*p*z]
                ledger.independent_replay(raw)
                checked += 1
    return checked


def unit_lift(p, s, wanted):
    n = 4*p+s
    low, high = digit_interval(p, s)
    for b in range(low, high+1):
        if gcd(b, n) != 1:
            continue
        a = wanted*b % n
        sign = 1
        if 2*a > n:
            a, sign = n-a, -1
        if low <= a <= high:
            ma = safe_a(p, s, a)[0]
            mb = safe_a(p, s, b)[0]
            answer = sign*F(ma[1], mb[1])
            assert residue(answer, n) == wanted % n
            return answer
    raise AssertionError("Pigeonhole unit intersection is empty.")


def direction_matrix(p, s, system):
    n, r, ja, ds, aa, records, _ = system
    t, _, y0, _, _, matrices = records[0]
    yi = int(n % 4 == 2 and y0 % 2)
    y = y0+yi
    ai = 0
    if n % 3 == 0 and n % 9:
        while (n//3)*((p-s)*(ja+ai+t-y)-5*t*t)*pow(p, -3, 3) % 3 == 2:
            ai += 1
    assert ai <= 1
    v = scale(zy(mm(matrices[yi], aa[ai]), p), F(1, p**3))
    assert tuple(residue(x, n) for x in v) == (1, residue(F(-5, p), n), 0, 1)
    trace = v[0]+v[3]
    if n % 2 == 0:
        assert residue(trace, 4) == 2
    if n % 3 == 0:
        c = 1-4*det(v)/(trace*trace)
        assert residue(c, 3) == 0 and residue(c, 9) != 6
    return v


def transport(p, s, system, pair):
    n, r, ja, ds, aa, records, g = system
    modulus = g*g*n**4
    v = direction_matrix(p, s, system)
    local = []
    if n % 5 == 0:
        low, high = digit_interval(p, s)
        q = low+(-p-low) % 5
        while gcd(q, n) != 1:
            q += 5
        assert q <= high
        matrix = scale(zy(safe_a(p, s, q)[0], p), F(1, p))
        e5 = 4*valuation(n, 5)+2
        power = local_cycle_hit(matrix, 5, e5, pair)
        pair = apply_mod(mod_power(matrix, power, modulus), pair, modulus)
        local.append((0, pure_prime_order(v, 5, e5)))
    for ell, e in factors(n).items():
        if ell == 5:
            continue
        local.append((local_cycle_hit(v, ell, 4*e, pair), ell**(4*e)))
    power = crt_pairs(local)
    pair = apply_mod(mod_power(v, power, modulus), pair, modulus)
    assert pair[0] == 0 and gcd(pair[1], modulus) == 1
    first = unit_lift(p, s, pair[1] % n)
    target = pair[1]*pow(residue(first, modulus), -1, modulus) % modulus
    k1, k2 = F(ds[1], ds[0]), F(ds[2], ds[0])
    if n % 4 == 2:
        flag = int(target % 4 != 1)
        target = target*pow(residue(k1, modulus), -flag, modulus) % modulus
        base, start = k2, 2*n
    else:
        flag, base, start = 0, k1, n
    k = principal_unit_log(base, target, modulus, start, False)
    result = residue(first, modulus)*pow(residue(k1, modulus), flag, modulus)*pow(residue(base, modulus), k, modulus)
    assert result % modulus == pair[1]


def tail_parameters(limit):
    bound = 4*limit+limit.bit_length()
    spf = list(range(bound+1))
    for p in range(2, int(bound**0.5)+1):
        if spf[p] == p:
            for n in range(p*p, bound+1, p):
                if spf[n] == n:
                    spf[n] = p
    omega = [0]*(bound+1)
    for n in range(2, bound+1):
        q = spf[n]
        m = n//q
        omega[n] = omega[m]+int(m % q != 0)
    for p in range(5, limit+1):
        if spf[p] != p:
            continue
        for s in range(1, (p-1).bit_length()):
            if omega[4*p+s] >= s+3:
                yield p, s


def main():
    cases = list(tail_parameters(20000))
    assert (761, 1) in cases
    # Six distinct factors and a nontrivial5-adic depth beyond the sieve window.
    assert factors(10103843) == {10103843: 1}
    cases.append((10103843, 3))
    rng = Random(2026091505)
    words = transports = 0
    for i, (p, s) in enumerate(cases):
        arithmetic_bounds(p, s)
        system = data(p, s)
        if i < 4 or (p, s) == (761, 1):
            words += physical(p, s, system)
        for _ in range(2):
            z, y = rng.randrange(-10**8, 10**8), rng.randrange(1, 10**8)
            if gcd(y, system[0]) != 1:
                y = 1
            transport(p, s, system, (z, y))
            transports += 1
    # Extra capacity checks cover offsets larger than occur in the finite tail.
    extra = 0
    for p in (101, 211, 401):
        for s in range(1, (p-21)//16+1):
            data(p, s)
            extra += 1
    print("four-p tail arithmetic and unit-density bounds: PASS", len(cases))
    print("four-p tail five-atom systems and root gcd: PASS", len(cases), extra)
    print("four-p tail literal return cycles: PASS", words)
    print("four-p tail complete direction-scale transports: PASS", transports)
    print("four-p tail formerly missing761-3045: PASS")
    entries = [full_input_entry(p, s, rng) for p, s in cases[:3]]
    print("four-p tail unrestricted original-input entries: PASS", len(entries), max(entries))
    print("four-p tail repair interfaces: PASS")


if __name__ == "__main__":
    main()
