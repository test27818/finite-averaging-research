"""Linear-time weighted witnesses, fourteen-point closure, and a uniform tail.

No averaging-word search is used. The only exhaustive loop is over unordered
small residue patterns to audit the general constructive inverse lemma.
"""

from collections import Counter
from itertools import combinations_with_replacement, product
from math import gcd
from random import Random

from verify_prime_arity_zero_trigger_bridge import GlobalReplay

if not __debug__:
    raise RuntimeError('Assertions are required.')


def weighted_witness(values, p, r=2):
    """p is prime; len(values)=ceil(p/r)-1. Return weights 0..r, or None.

    Prefix nodes are stored by (layer, prefix kind), not expanded coefficient
    vectors. Only the successful collision is expanded, giving O(p) modular
    operations and O(p) storage; integer bit costs are additional.
    """
    k = (p+r-1)//r-1
    assert 1 < r < p and len(values) == k and r*k < p
    residues = [value % p for value in values]
    if 0 in residues:
        answer = [0]*k
        answer[residues.index(0)] = 1
        return answer
    different = next((i for i, x in enumerate(residues) if x != residues[0]), None)
    if different is None:
        return None
    order = [0, different]+[i for i in range(1, k) if i != different]
    ordered = [residues[i] for i in order]
    prefixes, total = [], 0
    for x in ordered:
        total = (total+x) % p
        prefixes.append(total)
    kinds = [(1, prefixes[0]), (-1, ordered[1])]
    kinds += [(j, prefixes[j-1]) for j in range(2, k+1)]

    def expand(node):
        layer, kind = node
        vector = [layer]*k
        if kind == -1:
            vector[1] += 1
        else:
            for i in range(kind):
                vector[i] += 1
        return vector

    seen = {}
    for layer in range(r):
        for kind, prefix in kinds:
            residue = (layer*total+prefix) % p
            node = (layer, kind)
            if residue == 0:
                weights = expand(node)
            elif residue in seen:
                weights = [a-b for a, b in zip(expand(node), expand(seen[residue]))]
                if min(weights) < 0:
                    weights = [-x for x in weights]
                assert min(weights) >= 0
            else:
                seen[residue] = node
                continue
            answer = [0]*k
            for i, old in enumerate(order):
                answer[old] = weights[i]
            assert 0 < sum(answer) < p and max(answer) <= r
            assert sum(a*b for a, b in zip(answer, values)) % p == 0
            return answer
    raise AssertionError('The inverse-lemma pigeonhole collision was not found.')


def primitive(values):
    common = gcd(*values)
    assert common
    return tuple(x//common for x in values)


def difference_g(values):
    values = primitive(values)
    return gcd(*(x-values[0] for x in values))


def counts14(a, b, c, d):
    result = Counter()
    for value, count in ((a, 5), (b, 5), (c, 2), (d, 2)):
        result[value] += count
    return result


def integer_after(counts, chosen, p):
    chosen_counts = Counter(chosen)
    assert len(chosen) == p and len(set(chosen)) > 1 and sum(chosen) % p == 0
    assert all(counts[x] >= count for x, count in chosen_counts.items())
    result = counts-chosen_counts
    result[sum(chosen)//p] += p
    return result


def safe14(counts):
    return all(len({x % q for x in counts}) > 1 for q in (2, 7))


def choose14(a, b, c, d):
    assert len({a, b, c, d}) == 4
    assert 5*(a+b)+2*(c+d) == 0 and (a-b) % 5
    counts = counts14(a, b, c, d)
    assert safe14(counts)
    for anchor, other in ((a, b), (b, a)):
        for x in (c, d):
            if (x-anchor) % 5 == 0:
                first = [anchor]*4+[x]
                if sum(first) != 5*other:
                    return first, 'same-residue-single'
                return [anchor]*3+[x]*2, 'same-residue-double'
    inverse = pow(b-a, -1, 5)
    residues = {(c-a)*inverse % 5, (d-a)*inverse % 5}
    if len(residues) == 1:
        assert c % 5 == d % 5 == 0 and a % 5 and b % 5
        return None, 'constant-light-obstruction'
    if residues == {3, 4}:
        a, b = b, a
        inverse = pow(b-a, -1, 5)
    if (c-a)*inverse % 5 > (d-a)*inverse % 5:
        c, d = d, c
    residues = ((c-a)*inverse % 5, (d-a)*inverse % 5)
    if residues == (2, 3):
        first = [a]*3+[c, d]
        if sum(first) != 5*b:
            return first, '23-first'
        assert a == 15*b and c+d == -40*b
        return [b]*2+[c]+[d]*2, '23-collision-repair'
    assert residues == (2, 4)
    first = [a]*2+[c]+[d]*2
    after = integer_after(counts, first, 5)
    if safe14(after) and sum(first) != 5*b:
        return first, '24-first'
    return [b]*2+[c]*2+[d], '24-safety-or-collision-repair'


def audit14(values, branches):
    a, b, c, d = primitive(values)
    if len({a, b, c, d}) < 4 or (a-b) % 5 == 0:
        return False
    before = counts14(a, b, c, d)
    if not safe14(before):
        return False
    move, branch = choose14(a, b, c, d)
    branches[branch] += 1
    if move is None:
        assert c % 5 == d % 5 == 0 and a % 5 and b % 5
        return True
    after = integer_after(before, move, 5)
    assert safe14(after)
    assert sum(count >= 5 for count in after.values()) >= 2
    assert sum(x*x*n for x, n in after.items()) < sum(x*x*n for x, n in before.items())
    return True


def solve_family(p, a, b):
    assert p >= 5 and p % 2 and (a-b) % 2 == 0
    c = ((p*p-2*p+8)*a-(p*p-6*p+6)*b)//2
    d = ((-p*p+p-8)*a+(p*p-7*p+6)*b)//2
    values = [a]*p+[b]*p+[c]*2+[d]*2
    replay = GlobalReplay(values, p)
    first = list(range(p-4))+list(range(p, p+3))+[2*p]
    replay.average(first)
    assert replay.state[first[0]] == (p*a+(6-p)*b)//2
    second = [2*p+2, 2*p+1, first[0]]+list(range(p+3, 2*p))
    assert sum(replay.state[i] for i in second) == 0
    replay.average(second)
    assert all(replay.state[i] == 0 for i in second)
    replay.small_tail()
    assert not any(replay.state) and len(replay.operations) <= 7
    return len(replay.operations)


def main():
    exact = 0
    for p in (5, 7, 11):
        k = (p-1)//2
        for values in combinations_with_replacement(range(p), k):
            result = weighted_witness(values, p)
            assert (result is None) == (len(set(values)) == 1 and values[0] != 0)
            exact += 1
    random = Random(2026091210)
    general = 0
    for p in (5, 7, 11, 17, 31, 61, 101):
        for r in range(2, p):
            k = (p+r-1)//r-1
            for _ in range(5):
                values = [random.randrange(-10**20, 10**20) for _ in range(k)]
                result = weighted_witness(values, p, r)
                residues = {x % p for x in values}
                assert (result is None) == (len(residues) == 1 and 0 not in residues)
                general += 1
    print('inverse zero-sum exact unordered residue witnesses: PASS', exact)
    print('inverse zero-sum arbitrary-copy linear witnesses: PASS', general)

    branches, cases = Counter(), 0
    for a, b, c in product(range(-8, 9), repeat=3):
        if (a+b) % 2:
            continue
        d = -5*(a+b)//2-c
        if a == b == c == d == 0:
            continue
        cases += audit14((a, b, c, d), branches)
    for _ in range(2500):
        a, b, c = [random.randrange(-10**18, 10**18) for _ in range(3)]
        b += (a-b) % 2
        d = -5*(a+b)//2-c
        cases += audit14((a, b, c, d), branches)
    for values in ((15, 1, 2, -42), (1, 5, -53, 38),
                   (1, 9, 7, -32), (1, 5, 21, -36), (1, 3, 10, -20)):
        cases += audit14(values, branches)
    assert all(branches[key] for key in ('same-residue-single', 'same-residue-double',
               '23-first', '23-collision-repair', '24-first',
               '24-safety-or-collision-repair', 'constant-light-obstruction'))
    print('fourteen paired-kernel exact safe closure: PASS', cases)
    print('fourteen paired-kernel branches:', dict(sorted(branches.items())))

    restored = 0
    for p in (5, 7, 11, 17, 31):
        k = 2*p*p
        values = [-1]*p+[1]*p+[2*p-1]*2+[-(2*p-1)]*2+[k, -k]
        replay = GlobalReplay(values, p)
        replay.average(list(range(p-1))+[2*p])
        replay.average(list(range(p, 2*p-1))+[2*p+2])
        counts = Counter(replay.state)
        assert counts[-1] == counts[1] == p+1
        assert all(x.denominator == 1 for x in replay.state)
        assert difference_g([int(x) for x in replay.state]) == 1
        restored += 1
    print('two colliding averages restore both heavy values: PASS', restored)

    paths, longest = 0, 0
    for p in (5, 7, 9, 11, 13, 17, 19, 31, 61):
        longest = max(longest, solve_family(p, 6, 8))
        paths += 1
        for _ in range(12):
            a, b = [random.randrange(-10**8, 10**8) for _ in range(2)]
            b += (a-b) % 2
            longest = max(longest, solve_family(p, a, b))
            paths += 1
    print('two-p-plus-four two-parameter literal terminal paths: PASS', paths, longest)
    print('inverse zero-sum transfer: PASS')


if __name__ == '__main__':
    main()
