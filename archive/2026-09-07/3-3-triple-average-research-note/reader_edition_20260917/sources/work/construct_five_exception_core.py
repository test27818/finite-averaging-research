from math import gcd, prod

def crt_pair(a, m, b, p):
    t = ((b-a) * pow(m, -1, p)) % p
    return a + m*t, m*p

def build():
    # One exceptional residue-1 position and four residue-2 positions.
    # Every admissible triple is either {u,e0,ej} or a 3-subset of {e1,e2,e3,e4}.
    supports = [(0,j) for j in range(1,5)] + [(1,2), (3,4)]
    primes = [5,7,11,13,17,19]
    assert len(supports) == len(primes)
    residues = [1] * 5
    modulus = 3
    # Set all exceptional residues mod 3 to (1,2,2,2,2).
    residues = [1,2,2,2,2]
    # Add each p-support congruence, with nonzero entries summing to zero.
    for F,p in zip(supports, primes):
        vals = [0]*5
        if len(F)==2:
            vals[F[0]], vals[F[1]] = 1, p-1
        else:
            vals[F[0]], vals[F[1]], vals[F[2]] = 1, 1, p-2
        old_modulus = modulus
        for i in range(5):
            residues[i], _ = crt_pair(residues[i], old_modulus, vals[i], p)
        modulus *= p
    # Choose a nonzero background value. Since it is divisible by every p and by 3,
    # the residue pattern is unchanged; absorb the zero-sum correction in the last exception.
    P = prod(primes)
    n = P
    u = 3 * P
    e = [residues[i] for i in range(4)]
    e.append(-(n - 5) * u - sum(e))
    n = P
    assert n % 3 == 1 or n % 3 == 2
    assert (n-5)*u + sum(e) == 0
    for F,p in zip(supports,primes):
        assert all(e[i] % p != 0 for i in F)
        assert all(e[i] % p == 0 for i in range(5) if i not in F)
    assert [x%3 for x in e] == [1,2,2,2,2]
    g = gcd(u, *[x-u for x in e])
    print('n =', n, 'primes =', primes)
    print('background u =', u)
    print('exceptions =', e)
    print('primitive difference gcd =', g)
    return n, u, e, supports

def check_coverage(e, supports):
    # Encode u as residue 0 mod 3 and as zero mod every dangerous p.
    # Admissible nonconstant triples are exactly cross pairs with u, or 3-subsets in B.
    admissible = [(None,0,j) for j in range(1,5)]
    admissible += [(i,j,k) for i in range(1,5) for j in range(i+1,5) for k in range(j+1,5)]
    for T in admissible:
        if not any(set(F).issubset(set(x for x in T if x is not None)) for F in supports):
            raise AssertionError(('uncovered', T))
    print('covered admissible exceptional triples:', len(admissible))

if __name__ == '__main__':
    n,u,e,supports = build()
    check_coverage(e,supports)
    print('core shape: u^(n-5) plus 5 exceptions, no safe nonconstant triple')
