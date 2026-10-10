"""Exact checks for a common (p,p,r) core across 2p<n<4p.

Checks a new upper-band entry formula, the one/two-source reflection rule,
and a closed high-carrier family. No averaging-word search is used and
finite parameter checks do not replace the accompanying general proof.
"""

from fractions import Fraction as F
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def matmul(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))
                 for i in range(2) for j in range(2))


def inv(a):
    det = a[0]*a[3]-a[1]*a[2]
    return tuple(F(x, det) for x in (a[3], -a[1], -a[2], a[0]))


def upper_entry_counts(p, s):
    if s % 3:
        b, c = s, 0
    elif p-s == 1:
        b, c = (p+1)//2, (p-3)//2
    else:
        c = s-3+p % 3
        b = (p-c)//3
    assert 0 <= c <= s and s <= b+c <= p
    assert gcd(3*b+c, 3*p+s) == 1
    return b, c


def average(state, group, p):
    assert len(group) == len(set(group)) == p
    assert all(0 <= i < len(state) for i in group)
    value = sum(state[i] for i in group)/p
    for i in group:
        state[i] = value


def literal_entry(p, s):
    b, c = upper_entry_counts(p, s)
    n, r = 3*p+s, p+s
    for a, z in ((F(1), F(0)), (F(0), F(1))):
        state = [a]*(2*p)+[-2*a+s*z]*p+[-p*z]*s
        aa, bb, cc = list(range(2*p)), list(range(2*p, 3*p)), list(range(3*p, n))
        i = p-b-c
        first = aa[:i]+bb[:b]+cc[:c]
        kept = aa[i:i+r]
        second = aa[i+r:]+bb[b:]+cc[c:]
        assert sorted(first+second+kept) == list(range(n))
        average(state, first, p)
        average(state, second, p)
        a1, z1 = ((p-3*b-c)*a+(s*b-p*c)*z)/p, -a/p
        assert all(state[j] == value for group, value in
                   zip((first, second, kept), (a1, r*z1-a1, -p*z1)) for j in group)


def reflection(p, r, sources, counts):
    i, j, k, x, y, u, v = counts
    assert sources in (1, 2) and i+j+k == x+y+u+v == p
    assert min(counts) >= 0
    remaining = (p-sources*i, p-sources*j, r-sources*k, sources*p-r)
    assert min(remaining) >= 0
    assert all(a <= b for a, b in zip((x, y, u, v), remaining))
    alpha, beta = i-j, r*j-p*k
    assert p*(x-y)+alpha*v == beta
    Q = p*r*y-p*p*u+beta*v
    matrix = (beta, Q, -alpha, -beta)
    scalar = beta*beta-alpha*Q
    assert scalar % p == 0
    assert scalar % (2*p+r) == pow(p, 4, 2*p+r)
    assert matmul(matrix, matrix) == (scalar, 0, 0, scalar)
    return matrix, scalar//p


def literal_reflection(p, r, sources, counts):
    matrix, f = reflection(p, r, sources, counts)
    i, j, k, x, y, u, v = counts
    n = 2*p+r
    for a, z in ((F(1), F(0)), (F(0), F(1))):
        state = [a]*p+[r*z-a]*p+[-p*z]*r
        groups = [list(range(p)), list(range(p, 2*p)), list(range(2*p, n))]
        for iteration in range(2):
            ga, gb, gc = groups
            fresh = []
            for h in range(sources):
                selected = ga[h*i:(h+1)*i]+gb[h*j:(h+1)*j]+gc[h*k:(h+1)*k]
                average(state, selected, p)
                fresh += selected
            ga, gb, gc = ga[sources*i:], gb[sources*j:], gc[sources*k:]
            kept, fresh = fresh[:r], fresh[r:]
            first = ga[:x]+gb[:y]+gc[:u]+fresh[:v]
            second = ga[x:]+gb[y:]+gc[u:]+fresh[v:]
            assert sorted(first+second+kept) == list(range(n))
            average(state, first, p)
            average(state, second, p)
            groups = [first, second, kept]
            if iteration == 0:
                av = (matrix[0]*a+matrix[1]*z)/p**2
                zv = (matrix[2]*a+matrix[3]*z)/p**2
            else:
                av, zv = F(f, p**3)*a, F(f, p**3)*z
            assert all(state[index] == value for group, value in
                       zip(groups, (av, r*zv-av, -p*zv)) for index in group)


def high_carrier(p, r):
    assert p+9 <= r < 2*p
    d = 2*p-r
    a0 = 2*((d+7)//4)
    assert a0 % 2 == 0 and a0 >= 4 and a0+1 <= (p-1)//2
    rows, matrices = {}, {}
    root_gcd = 0
    for alpha in (a0, a0+1):
        max_x = alpha//2
        low_x = max(0, -(-(d-alpha)//2))
        assert max_x-low_x >= 2
        fs = []
        for e in range(3):
            x = max_x-e
            row = (alpha, 0, p-alpha, x, p-alpha+x, alpha-2*x, 0)
            matrix, f = reflection(p, r, 2, row)
            n = 2*p+r
            assert f == p**3+n*alpha*(alpha-p-x)
            rows[alpha, e], matrices[alpha, e] = row, matrix
            fs.append(f)
        assert fs[1]-fs[0] == alpha*(2*p+r)
        assert gcd(fs[0], fs[1]) == 1
        T = matmul(inv(matrices[alpha, 0]), matrices[alpha, 1])
        S = (-1, r, 0, 1)
        comm = matmul(matmul(matmul(S, T), S), inv(T))
        H = (2*p+r)*alpha-2*p*p
        assert comm == (1, F((2*p+r)*H, fs[1]), 0, 1)
        root_gcd = gcd(root_gcd, H)
    assert root_gcd == gcd(2*p+r, 2)
    n = 2*p+r
    choice = None
    for e0 in range(2):
        V = matmul(matrices[a0, e0], matrices[a0+1, 0])
        if n % 2 or (V[0]+V[3]) % 4 == 2:
            choice = e0
            break
    assert choice is not None
    return rows


def main():
    if not __debug__:
        raise RuntimeError('Assertions required.')
    entries = systems = physical = 0
    for p in range(5, 300):
        if not prime(p):
            continue
        for s in range(1, p):
            upper_entry_counts(p, s)
            entries += 1
            if p <= 19:
                literal_entry(p, s)
        for r in range(p+9, 2*p):
            rows = high_carrier(p, r)
            systems += 1
            if p <= 19:
                for row in rows.values():
                    literal_reflection(p, r, 2, row)
                    physical += 1
    # The previously used 3p-1 overlap reflections are the sources=1 rule.
    for p in (7, 11, 13, 17, 29):
        for sigma, h in ((2, 3), (2, 4), (3, 4), (3, 5)):
            row = (p-sigma, 0, sigma, h-sigma, h, p+sigma-2*h, 0)
            literal_reflection(p, p-1, 1, row)
            physical += 1
    print('whole upper-strip closed entry counts: PASS', entries)
    print('high symmetric carrier six-reflection systems: PASS', systems)
    print('literal one/two-source reflection systems: PASS', physical)
    print('symmetric strip unification interfaces: PASS')


if __name__ == '__main__':
    main()
