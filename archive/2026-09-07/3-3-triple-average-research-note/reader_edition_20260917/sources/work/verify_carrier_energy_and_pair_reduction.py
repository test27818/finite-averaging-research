"""Exact carrier energies and a CRT rank reduction on 2p+2 positions.

No word search. Carrier powers use closed formulas; only small cases are
expanded into labelled averages. Integer rank elimination checks the
common-quadratic-form equations without a numerical SDP solver.
"""

from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm, prod
from random import Random

if not __debug__:
    raise RuntimeError('Assertions are required.')


def primes(n):
    answer, d = [], 2
    while d*d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        answer.append(n)
    return answer


def primitive(values):
    denominator = lcm(*(F(x).denominator for x in values))
    integers = [int(F(x)*denominator) for x in values]
    common = gcd(*integers)
    return tuple(x//common for x in integers) if common else tuple(integers)


def energy(values, weights):
    return sum(w*x*x for w, x in zip(weights, values))


def residue(x, q):
    x = F(x)
    return x.numerator*pow(x.denominator, -1, q) % q


def legal(values, weights, p):
    assert sum(w*x for w, x in zip(weights, values)) == 0
    z = primitive(values)
    return all(len({x % q for x in z}) > 1
               for q in primes(sum(weights)) if q != p)


def swap(values, block, carrier, p):
    result = list(map(F, values))
    a, c = result[block], result[carrier]
    result[block] = ((p-1)*a+c)/p
    result[carrier] = a
    return tuple(result)


def closed_swap(a, c, p, k):
    scale, mass = F((-1)**k, p**k), p*a+c
    return ((mass+(a-c)*scale)/(p+1),
            (mass-p*(a-c)*scale)/(p+1))


def integer_rank(rows, width):
    pivots = {}
    for original in rows:
        row = tuple(original)
        for j, pivot in sorted(pivots.items()):
            if row[j]:
                u, v = pivot[j], row[j]
                row = tuple(u*x-v*y for x, y in zip(row, pivot))
                common = gcd(*row)
                if common:
                    row = tuple(x//common for x in row)
        j = next((j for j in range(width) if row[j]), None)
        if j is not None:
            pivots[j] = row
    return len(pivots)


def verify_common_quadratic():
    checked = 0
    for p in (3, 5, 7):
        for m, r in ((1, 1), (1, 3), (2, 1), (2, 2), (2, 3), (3, 2)):
            weights = [p]*m+[1]*r
            d = m+r-1
            variables = [(i, j) for i in range(d) for j in range(i, d)]
            rows = []
            gram = [[(weights[i] if i == j else 0)+weights[i]*weights[j]
                     for j in range(d)] for i in range(d)]
            for block in range(m):
                for carrier in range(m, m+r):
                    # Restrict p*T to the zero-sum basis e_i-w_i*e_last.
                    matrix = [[0]*d for _ in range(d)]
                    for j in range(d):
                        column = [0]*(d+1)
                        column[j], column[-1] = p, -p*weights[j]
                        a, c = column[block], column[carrier]
                        column[block] = ((p-1)*a+c)//p
                        column[carrier] = a
                        for i in range(d):
                            matrix[i][j] = column[i]
                    for i, j in combinations(range(d), 2):
                        row = []
                        for u, v in variables:
                            def h(s, t):
                                return int((s, t) in ((u, v), (v, u)))
                            row.append(sum(matrix[k][i]*h(k, j)-
                                           h(i, k)*matrix[k][j] for k in range(d)))
                        assert sum(c*gram[u][v] for c, (u, v) in zip(row, variables)) == 0
                        rows.append(row)
            assert integer_rank(rows, len(variables)) == len(variables)-1
            checked += 1
    print('carrier common quadratic form has one dimension: PASS', checked)


def verify_height_identities():
    rng, integer, fractional, local = Random(2026091214), 0, 0, 0
    for p in (3, 5, 7, 11, 13, 23):
        for m, r in ((2, 1), (2, 2), (2, 4), (3, 2)):
            weights = [p]*m+[1]*r
            for _ in range(48):
                values = [rng.randrange(-10000, 10001) for _ in weights[:-1]]
                values.append(-sum(w*x for w, x in zip(weights[:-1], values)))
                values = primitive(values)
                block, carrier = rng.randrange(m), m+rng.randrange(r)
                a, c = values[block], values[carrier]
                following = swap(values, block, carrier, p)
                before, after = energy(values, weights), energy(following, weights)
                assert before-after == F(p-1, p)*(c-a)**2
                assert (following[carrier],
                        p*following[block]-(p-1)*following[carrier]) == (a, c)
                normalized = primitive(following)
                if (c-a) % p == 0:
                    assert normalized == following
                    assert energy(normalized, weights) == after
                    integer += 1
                else:
                    assert normalized == tuple(p*x for x in following)
                    rest = before-p*a*a-c*c
                    difference = energy(normalized, weights)-before
                    assert difference == (p-1)*((p*a+c)**2+(p+1)*rest)
                    assert difference >= 0
                    fractional += 1
                for q in (2, 3, 5, 7, 11):
                    if q == p:
                        continue
                    for power in (q, q*q):
                        for shift in (0, 1):
                            old_constant = all(x % power == shift for x in values)
                            new_constant = all(residue(x, power) == shift for x in following)
                            assert old_constant == new_constant
                            local += 1
                if legal(values, weights, p):
                    assert legal(following, weights, p)
    print('carrier physical and primitive-height identities: PASS', integer, fractional, local)


def crt_selector(a, b, c, p):
    k, modulus = 0, 1
    for q in primes(p+1):
        target = int(residue(a-b, q) == 0)
        if target:
            assert residue(a-c, q)
        correction = (target-k)*pow(modulus, -1, q) % q
        k += modulus*correction
        modulus *= q
    assert 0 <= k < modulus <= p+1
    assert k*k % modulus == k
    return k


def collapse(values, p):
    a, b, c, d = values
    assert legal(values, (p, p, 1, 1), p)
    k = crt_selector(a, b, c, p)
    aa, cc = closed_swap(a, c, p, k)
    for q in primes(p+1):
        assert residue(aa, q) == residue(a+k*(a-c), q)
        assert residue(aa-b, q)
    big = ((p-2)*aa+cc+d)/p
    assert big == -b-F(2, p)*aa
    result = big, b, aa
    assert legal(result, (p, p, 2), p)
    u, v = (big+b)/2, (big-b)/2
    assert aa == -p*u
    uu, vv = primitive((u, v))
    assert gcd(vv, p+1) == 1
    assert energy(result, (p, p, 2)) == 2*p*(v*v+(p+1)*u*u)
    return result, k


def literal_collapse(values, p):
    expected, k = collapse(values, p)
    a, b, c, d = map(F, values)
    state = [a]*p+[b]*p+[c, d]
    first, second, carrier, exterior = list(range(p)), list(range(p, 2*p)), 2*p, 2*p+1
    for _ in range(k):
        group = first[:-1]+[carrier]
        carrier = first[-1]
        mean = sum(state[i] for i in group)/p
        for i in group:
            state[i] = mean
        first = group
        assert legal(state, [1]*len(state), p)
    group, remainder = first[:p-2]+[carrier, exterior], first[p-2:]
    assert len(group) == len(set(group)) == p and len(remainder) == 2
    mean = sum(state[i] for i in group)/p
    for i in group:
        state[i] = mean
    assert tuple(state[i] for i in (group[0], second[0], remainder[0])) == expected
    assert all(state[i] == expected[0] for i in group)
    assert all(state[i] == expected[1] for i in second)
    assert all(state[i] == expected[2] for i in remainder)
    assert legal(state, [1]*len(state), p)
    return k+1


def verify_rank_reduction():
    rng, samples, replayed, maximum = Random(2026091215), 0, 0, 0
    arities = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 59, 89, 419, 2309)
    for p in arities:
        for _ in range(16 if p < 100 else 3):
            while True:
                a, b, c = [rng.randrange(-(1 << 64), 1 << 64) for _ in range(3)]
                values = primitive((a, b, c, -p*(a+b)-c))
                if legal(values, (p, p, 1, 1), p):
                    break
            _, k = collapse(values, p)
            samples += 1
            if p <= 31:
                maximum = max(maximum, literal_collapse(values, p))
                replayed += 1
    # Explicitly exercise every combination of bad/good prime places,
    # including many-prime p+1 where two frozen witnesses need not suffice.
    flags = 0
    for p in (5, 29, 419, 2309):
        qs = primes(p+1)
        for bits in range(1 << len(qs)):
            a, modulus = 0, 1
            for i, q in enumerate(qs):
                target = 0 if bits >> i & 1 else 1
                a += modulus*((target-a)*pow(modulus, -1, q) % q)
                modulus *= q
            values = a, 0, 1, -p*a-1
            assert legal(values, (p, p, 1, 1), p)
            _, k = collapse(values, p)
            for i, q in enumerate(qs):
                assert k % q == (bits >> i & 1)
            flags += 1
    print('two-singleton CRT rank reduction all test inputs: PASS', samples, flags)
    print('two-singleton labelled Fraction rank reductions: PASS', replayed, maximum)


def safe_flatten(values, p, m, ledger=False):
    n, state = len(values), [p*x for x in values]
    r = n-m*p
    qs = [q for q in primes(n) if q != p]
    assert n > 2*p and r >= len(qs)
    assert legal(state, [1]*n, p)
    free, blocks = list(range(n)), []
    for _ in range(m):
        protected = set()
        for q in qs:
            counts = {}
            for i, x in enumerate(state):
                counts.setdefault(x % q, []).append(i)
            majority = next((positions for positions in counts.values()
                             if len(positions) >= n-p), None)
            if majority is None:
                continue
            majority_set = set(majority)
            exceptions = set(range(n))-majority_set
            if not exceptions.issubset(free):
                continue
            if not exceptions.intersection(protected):
                protected.add(min(exceptions))
        group = [i for i in free if i not in protected][:p]
        assert len(group) == p and sum(state[i] for i in group) % p == 0
        mean = sum(state[i] for i in group)//p
        for i in group:
            state[i] = mean
        blocks.append(group)
        used = set(group)
        free = [i for i in free if i not in used]
        assert legal(state, [1]*n, p)
    assert len(free) == r
    if ledger:
        return state, blocks, free
    return tuple(state[group[0]] for group in blocks)+tuple(state[i] for i in free)


def verify_entries_and_core_criterion():
    rng, entries, combined, criterion = Random(2026091216), 0, 0, 0
    for p in (3, 5, 7, 11, 13, 17, 19, 29):
        for m in (2, 3):
            for r in range(1, p):
                n = m*p+r
                if r < len([q for q in primes(n) if q != p]):
                    continue
                for _ in range(2):
                    while True:
                        raw = [rng.randrange(-1000, 1001) for _ in range(n-1)]
                        raw.append(-sum(raw))
                        raw = primitive(raw)
                        if legal(raw, [1]*n, p):
                            break
                    core = safe_flatten(raw, p, m)
                    entries += 1
                    if m == 2 and r == 2:
                        literal_collapse(core, p)
                        combined += 1
        for u in range(-15, 16):
            for v in range(-15, 16):
                if gcd(u, v) != 1:
                    continue
                values = (u+v, u-v, -p*u)
                assert gcd(*values) == 1
                difference_gcd = gcd(2*v, (p+1)*u+v)
                assert (difference_gcd == 1) == (gcd(v, p+1) == 1)
                assert energy(values, (p, p, 2)) == 2*p*(v*v+(p+1)*u*u)
                criterion += 1
    print('safe labelled-block entries and combined reductions: PASS', entries, combined)
    print('equal-pair core norm and complete G criterion: PASS', criterion)


def norm_pair(u, v):
    u, v = primitive((u, v))
    assert v
    return (u, v) if v > 0 else (-u, -v)


def dyadic_plan(u, v, p):
    h = (p+1)//2
    assert h > 1 and h & (h-1) == 0
    u, v = norm_pair(u, v)
    assert v % 2
    plan, decreases = [], []
    while u and abs(u) != v:
        candidate = u if u % 2 else u+v
        r = (candidate+v) % (2*v)-v
        shift = (r-u)//v
        if shift:
            plan.append(('u', shift))
        u = r
        assert u % 2 and abs(u) <= v
        if u < 0:
            plan.append(('s', 0))
            u = -u
        if u == v:
            break
        j = 2*((h*u)//(2*v))+1
        assert 1 <= j <= h-1 and j % 2
        next_u, next_v = -(u+v)//2, j*v-h*u
        assert next_v % 2 and 0 < abs(next_v) < v
        plan.append(('n', j))
        old_v = v
        u, v = norm_pair(next_u, next_v)
        assert v < old_v
        decreases.append((old_v, v))
    return plan, decreases


class PairLedger:
    def __init__(self, p, state, first, second, carriers):
        self.p, self.state = p, list(map(F, state))
        self.first, self.second, self.carriers = list(first), list(second), list(carriers)
        self.steps = 0
        self.parameters()

    def average(self, group):
        p = self.p
        assert len(group) == len(set(group)) == p
        old_energy = sum(x*x for x in self.state)
        mean = sum(self.state[i] for i in group)/p
        for i in group:
            self.state[i] = mean
        assert sum(self.state) == 0
        assert sum(x*x for x in self.state) <= old_energy
        self.steps += 1

    def parameters(self):
        a, b, c = (self.state[group[0]] for group in
                   (self.first, self.second, self.carriers))
        assert all(self.state[i] == a for i in self.first)
        assert all(self.state[i] == b for i in self.second)
        assert all(self.state[i] == c for i in self.carriers)
        u, v = (a+b)/2, (a-b)/2
        assert c == -self.p*u
        return u, v

    def regroup(self, kind, j=0):
        p, aa, bb, cc = self.p, self.first, self.second, self.carriers
        old_u, old_v = self.parameters()
        remainder = aa[-2:]
        if kind == 'u':
            i = (p-3)//2
            first = aa[:i]+bb[:p-1-i]+[cc[0]]
            second = aa[i:p-2]+bb[p-1-i:]+[cc[1]]
            expected = (-(old_u+old_v)/p, -old_v/p)
        else:
            i = j+(p-3)//2
            assert 0 <= i <= p-2
            first = aa[:i]+bb[:p-2-i]+cc
            second = aa[i:p-2]+bb[p-2-i:]
            expected = (-(old_u+old_v)/p, (-(p+1)*old_u+2*j*old_v)/p)
        self.average(first)
        self.average(second)
        self.first, self.second, self.carriers = first, second, remainder
        assert self.parameters() == expected
        # A safe completed macro cannot have passed through an irreversible
        # common-residue obstruction.
        assert legal(self.state, [1]*len(self.state), p)

    def execute(self, plan):
        for kind, parameter in plan:
            if kind == 's':
                self.first, self.second = self.second, self.first
            elif kind == 'u':
                for _ in range(abs(parameter)):
                    if parameter < 0:
                        self.first, self.second = self.second, self.first
                    self.regroup('u')
                    if parameter < 0:
                        self.first, self.second = self.second, self.first
            elif kind == 'n':
                self.regroup('n', parameter)
            else:
                raise AssertionError(kind)
        return self.parameters()

    def finish(self):
        p = self.p
        u, v = self.parameters()
        assert u == 0 or abs(u) == abs(v)
        zero = [i for i, x in enumerate(self.state) if x == 0]
        assert zero
        keep = zero[0]
        if len(zero) >= p:
            outside = zero[1]
            rest = [i for i in range(len(self.state)) if i not in (keep, outside)]
            self.average(rest[:p])
            self.average(rest[p:])
        for count in ((p-1)//2, (p-1)//2, 1):
            plus = [i for i, x in enumerate(self.state) if x > 0]
            minus = [i for i, x in enumerate(self.state) if x < 0]
            zeros = [i for i, x in enumerate(self.state) if x == 0]
            if not plus and not minus:
                break
            assert len(plus) >= count and len(minus) >= count
            assert self.state[plus[0]] == -self.state[minus[0]]
            self.average(plus[:count]+minus[:count]+zeros[:p-2*count])
        assert not any(self.state)


def verify_dyadic_complete():
    checked, paths, longest = 0, 0, 0
    for p in (3, 7, 15, 31, 63, 127):
        for v in range(1, 80, 2):
            for u in range(-2*v, 2*v+1):
                if gcd(u, v) != 1:
                    continue
                plan, decreases = dyadic_plan(u, v, p)
                a, b = u, v
                for kind, parameter in plan:
                    if kind == 's':
                        b = -b
                    elif kind == 'u':
                        a += parameter*b
                    else:
                        assert a % 2 and b % 2
                        a, b = -(a+b)//2, parameter*b-((p+1)//2)*a
                    a, b = norm_pair(a, b)
                    assert b % 2
                assert a == 0 or abs(a) == abs(b)
                checked += 1
        for u, v in ((1, 5), (7, 19), (-13, 31), (60, 73)):
            assert gcd(v, p+1) == 1
            state = [u+v]*p+[u-v]*p+[-p*u]*2
            ledger = PairLedger(p, state, range(p), range(p, 2*p), (2*p, 2*p+1))
            plan, _ = dyadic_plan(u, v, p)
            ledger.execute(plan)
            ledger.finish()
            longest = max(longest, ledger.steps)
            paths += 1
    print('dyadic-neighbour Euclidean direction reductions: PASS', checked)
    print('dyadic-neighbour literal core complete paths: PASS', paths, longest)

    rng, full, maximum = Random(2026091217), 0, 0
    for p in (3, 7, 15, 31):
        n = 2*p+2
        for _ in range(12):
            while True:
                raw = [rng.randrange(-100, 101) for _ in range(n-1)]
                raw.append(-sum(raw))
                raw = primitive(raw)
                if legal(raw, [1]*n, p):
                    break
            scaled_state, blocks, singles = safe_flatten(raw, p, 2, ledger=True)
            state = list(map(F, raw))
            for group in blocks:
                mean = sum(state[i] for i in group)/p
                for i in group:
                    state[i] = mean
            assert [p*x for x in state] == scaled_state
            aa, bb = blocks
            carrier, exterior = singles
            a, b, c = state[aa[0]], state[bb[0]], state[carrier]
            k = crt_selector(a, b, c, p)
            state = list(map(F, state))
            for _ in range(k):
                group = aa[:-1]+[carrier]
                carrier = aa[-1]
                mean = sum(state[i] for i in group)/p
                for i in group:
                    state[i] = mean
                aa = group
            group, pair = aa[:p-2]+[carrier, exterior], aa[-2:]
            mean = sum(state[i] for i in group)/p
            for i in group:
                state[i] = mean
            ledger = PairLedger(p, state, group, bb, pair)
            plan, _ = dyadic_plan(*ledger.parameters(), p)
            ledger.execute(plan)
            ledger.finish()
            maximum = max(maximum, 2+k+1+ledger.steps)
            full += 1
    # Check the entire available digit family, including nonunit digits.
    # At p5, (u,v)=(3,11), only j=2 is safe and it increases height.
    p, u, v = 5, 3, 11
    assert legal((u+v, u-v, -p*u), (p, p, 2), p)
    outcomes = []
    for j in range(-1, 3):
        uu, vv = -(u+v)//2, j*v-3*u
        common = gcd(uu, vv)
        outcomes.append((j, abs(vv)//common, gcd(vv//common, 6) == 1))
    assert outcomes == [(-1, 20, False), (0, 9, False), (1, 2, False), (2, 13, True)]
    # Nonunit j=0 is genuinely safe after cancellation for (u,v)=(1,5).
    assert norm_pair(-3, -3) == (1, 1)
    cancellation = 0
    for h in range(2, 18):
        for v in range(1, 32, 2):
            if gcd(v, 2*h) != 1:
                continue
            for u in range(1, 32, 2):
                if gcd(u, v) != 1:
                    continue
                for j in range(-h+2, h):
                    uu, vv = -(u+v)//2, j*v-h*u
                    common = gcd(uu, vv)
                    assert common == gcd((u+v)//2, h+j)
                    assert common
                    cancellation += 1
    print('dyadic-neighbour arbitrary-input full Fraction paths: PASS', full, maximum)
    print('non-dyadic nearest-digit obstruction retained: PASS')
    print('general bounded-digit common-factor formula: PASS', cancellation)


if __name__ == '__main__':
    verify_common_quadratic()
    verify_height_identities()
    verify_rank_reduction()
    verify_entries_and_core_criterion()
    verify_dyadic_complete()
    print('carrier energy and two-singleton reduction: PASS')
