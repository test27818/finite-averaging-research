"""Five-averaging n=16,17,18 via exact collision rigidity and witnesses.

Finite residue patterns produce rational linear systems, not averaging-word
searches. Runtime choices use cardinality/residue extrema on original labels.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations_with_replacement
from random import Random

import verify_inverse_egz_threshold as previous

base, linear, middle, old = previous.base, previous.linear, previous.middle, previous.old

if not __debug__:
    raise RuntimeError('Assertions must remain enabled.')


CERTIFICATE = (
    (0,0,5,(0,2,2,2,2),('5','-8','-8','-8','-8')),
    (0,0,5,(0,3,3,3,3),('5','-2','-2','-2','-2')),
    (0,0,5,(0,4,4,4,4),('5','-7/2','-7/2','-7/2','-7/2')),
    (0,0,5,(1,2,2,2,2),('-4','9/2','9/2','9/2','9/2')),
    (0,0,5,(1,3,3,3,3),('-4','3','3','3','3')),
    (0,0,5,(1,4,4,4,4),('-4','9','9','9','9')),
    (0,0,5,(2,2,2,2,3),('-3','-3','-3','-3','8')),
    (0,0,5,(2,2,2,2,4),('7','7','7','7','-16')),
    (0,0,5,(2,3,3,3,3),('12','-7','-7','-7','-7')),
    (0,0,5,(2,4,4,4,4),('17','-6','-6','-6','-6')),
    (0,0,5,(3,3,3,3,4),('8','8','8','8','-11')),
    (0,0,5,(3,4,4,4,4),('-7','4','4','4','4')),
    (1,0,5,(2,2,2,2),('2','2','2','2')),
    (1,0,5,(3,3,3,3),('4/3','4/3','4/3','4/3')),
    (1,0,5,(3,4,4,4),('-7','4','4','4')),
    (1,0,5,(4,4,4,4),('4','4','4','4')),
    (1,0,6,(3,4,4,4,4),('-7','4','4','4','4')),
    (1,1,5,(0,3,3),('5','-7','-7')),
    (1,1,5,(1,3,3),('-4','8','8')),
    (2,0,5,(2,2,2),('2','2','2')),
    (2,0,5,(2,2,3),('2','2','3')),
    (2,0,6,(2,2,2,2),('2','2','2','2')),
)


def equations(sequence, alpha, beta):
    length = len(sequence)
    for i, residue in enumerate(sequence):
        if residue in (0, 1):
            yield tuple(int(i == j) for j in range(length)), 5 if residue == 0 else -4
    for mask in range(1, 1 << length):
        count = mask.bit_count()
        if count > 5:
            continue
        row = tuple((mask >> i) & 1 for i in range(length))
        residue = sum(x*c for x, c in zip(sequence, row)) % 5
        i = -residue % 5
        if i <= min(alpha, 5-count):
            if 5-count-i <= beta:
                yield (0,)*length, 1
                return
            yield row, 5-i
        j = (residue-count) % 5
        if j <= min(beta, 5-count):
            yield row, count+j-5


def linear_system(rows, width):
    pivots = {}
    original = list(rows)
    for coefficients, rhs in original:
        row = list(map(F, coefficients)) + [F(rhs)]
        for column, pivot in sorted(pivots.items()):
            factor = row[column]
            if factor:
                row = [x-factor*y for x, y in zip(row, pivot)]
        first = next((j for j in range(width) if row[j]), None)
        if first is None:
            if row[-1]:
                return None
        else:
            factor = row[first]
            pivots[first] = [x/factor for x in row]
    assert len(pivots) == width, 'No unchecked positive-dimensional case is allowed.'
    result = [F(0)]*width
    for column, row in sorted(pivots.items(), reverse=True):
        result[column] = row[-1]-sum(row[j]*result[j] for j in range(column+1, width))
    assert all(sum(a*x for a, x in zip(row, result)) == rhs for row, rhs in original)
    return tuple(result)


def verify_certificate():
    expected = {(a,b,c,s):tuple(map(F,v)) for a,b,c,s,v in CERTIFICATE}
    observed, systems = {}, 0
    for alpha, beta in ((0,0), (1,0), (1,1), (2,0)):
        for capacity in (5,6,7,8):
            length = capacity-alpha-beta
            for sequence in combinations_with_replacement(range(5), length):
                frequencies = Counter(sequence)
                if max(frequencies.values()) >= 5 or frequencies[0] > 1 or frequencies[1] > 1:
                    continue
                systems += 1
                solution = linear_system(equations(sequence, alpha, beta), length)
                if solution is not None:
                    assert all(x.denominator % 5 and x.numerator*pow(x.denominator,-1,5) % 5 == r
                               for x, r in zip(solution, sequence))
                    observed[(alpha,beta,capacity,sequence)] = solution
    assert observed == expected and systems == 903
    for (alpha,beta,capacity,sequence), values in expected.items():
        assert capacity in (5,6)
        if capacity == 6:
            assert all(x.denominator == 1 for x in values)
            assert 5+alpha+sum(values) == 15
        elif any(x.denominator % 2 == 0 for x in values):
            assert alpha == beta == 0
            assert sum(x.denominator == 2 for x in values) == 4
            assert all(x.denominator in (1,2) for x in values)
        else:
            assert all(x.denominator % 2 for x in values)
        if capacity == 5:
            assert (5+alpha+sum(values)).denominator % 2 == 1
    return systems, len(expected)


def protected_light(counts, a, b, factors, p=5):
    values = [x for x, f in sorted(counts.items()) if x not in (a,b) for _ in range(f)]
    n = sum(counts.values())
    dangerous = []
    for q in factors:
        classes = Counter()
        for x, f in counts.items():
            classes[x % q] += f
        majority = next((r for r, f in classes.items() if f >= n-p), None)
        if majority is None or a % q != majority or b % q != majority:
            continue
        support = {i for i, x in enumerate(values) if x % q != majority}
        assert 2 <= len(support) <= p
        dangerous.append((q, support))
    protected = set()
    for _, support in dangerous:
        if not support & protected:
            protected.add(min(support))
    for position in sorted(protected):
        if all(support & (protected-{position}) for _, support in dangerous):
            protected.remove(position)
    private = {}
    for position in protected:
        q, support = next((q, s) for q, s in dangerous if s & protected == {position})
        assert (a-b) % q == 0
        private[position] = q
    return [x for i,x in enumerate(values) if i not in protected], protected, private, values


def candidates(pool, padding, p=5):
    nodes = [(0,None,None)]
    minima = [[None]*p for _ in range(p+1)]
    maxima = [[None]*p for _ in range(p+1)]
    minima[0][0] = maxima[0][0] = 0
    for position, x in enumerate(pool):
        value = x-padding
        for size in range(min(position+1,p),0,-1):
            parents = set(i for i in minima[size-1]+maxima[size-1] if i is not None)
            for parent in parents:
                total = nodes[parent][0]+value
                r = total % p
                lo = minima[size][r] is None or total < nodes[minima[size][r]][0]
                hi = maxima[size][r] is None or total > nodes[maxima[size][r]][0]
                if lo or hi:
                    node = len(nodes)
                    nodes.append((total,parent,position))
                    if lo:
                        minima[size][r] = node
                    if hi:
                        maxima[size][r] = node
    for size in range(1,p+1):
        for node in set(i for i in (minima[size][0],maxima[size][0]) if i is not None):
            selected = []
            total = nodes[node][0]
            while node:
                _,node,position = nodes[node]
                selected.append(pool[position])
            assert len(selected) == size and sum(x-padding for x in selected) == total
            yield tuple(selected)+(padding,)*(p-size)


def choose(counts, factors):
    n = sum(counts.values())
    assert n in (16,17,18) and sum(x*f for x,f in counts.items()) == 0
    heavy = sorted(base.heavy(counts,5))
    assert len(heavy) >= 2 and base.legal(counts,factors)
    if len(heavy) >= 3:
        a,b,c = heavy[:3]
        if len(counts) == 3 and counts[a] == counts[c] == 5 and len({x%5 for x in heavy}) == 3:
            if n == 16:
                move = base.controller(a,c,b,5)
                if sum(move) == 5*b:
                    assert b == 0 and a == -c
                    return None, 'three-sixteen-terminal', c
                return move, 'three-sixteen-one-middle', None
            move,branch = previous.triple.choose_three(counts,5)
            return move,'three-'+branch,c if move is None else None
        return old.choose(counts,n,5,factors)
    a,b = sorted(heavy,key=lambda x:counts[x],reverse=True)
    if max(counts[a],counts[b]) >= 9:
        return linear.choose(counts,n,5,factors)
    if (a-b) % 5 == 0:
        return tuple(middle.same_residue_move(counts,5,factors)), 'same-residue', None
    for anchor,other in ((a,b),(b,a)):
        for x in counts:
            if x in (a,b) or (x-anchor) % 5:
                continue
            move = (anchor,)*4+(x,)
            if sum(move) != 5*other:
                return move,'anchor-residue-single',None
            if counts[x] >= 2:
                return (anchor,)*3+(x,x),'anchor-residue-double',None
    if counts[a]+counts[b] >= 13:
        move,branch = previous.combined_reserve(counts,a,b,5)
        return move,branch,None
    light,protected,private,_ = protected_light(counts,a,b,factors)
    for target,padding in ((a,b),(b,a)):
        pool = [target]*(counts[target]-5)+light
        for move in candidates(pool,padding):
            if len(set(move)) == 1:
                continue
            after = base.change(counts,move,5)
            if len(base.heavy(after,5)) >= 2:
                assert base.legal(after,factors)
                return move,'protected-modular-fiber',None
    raise AssertionError(('Certified all-collision obstruction would contradict legality', n,counts,light,private))


def audit(counts,branches):
    n = sum(counts.values())
    factors = base.protected_primes(n,5)
    if not base.legal(counts,factors) or len(base.heavy(counts,5)) < 2:
        return False
    move,branch,delta = choose(counts,factors)
    branches[branch] += 1
    if move is None:
        assert set(counts) == {-delta,0,delta} and counts[delta] == counts[-delta]
    else:
        after = base.change(counts,move,5)
        assert base.legal(after,factors) and len(base.heavy(after,5)) >= 2
    return True


def solve(initial):
    n, branches = len(initial), Counter()
    factors = base.protected_primes(n,5)
    assert base.legal(Counter(initial),factors)
    replay = base.LabelledReplay(initial,5)
    for move in base.initialize(replay.counts(),n,5,factors):
        replay.step(move)
        assert base.legal(replay.counts(),factors)
    while any(replay.state):
        move,branch,delta = choose(replay.counts(),factors)
        branches[branch] += 1
        if move is None:
            for _ in range(replay.counts()[delta]):
                replay.step((delta,-delta,0,0,0))
            break
        replay.step(move)
        assert base.legal(replay.counts(),factors) and len(base.heavy(replay.counts(),5)) >= 2
    old.previous.replay_original(initial,replay.word,5)
    return len(replay.word),branches


def main():
    print('five-average complete collision linear certificate: PASS',*verify_certificate())
    from itertools import combinations, product
    transversals = 0
    for n,factors in ((16,(2,)),(17,(17,)),(18,(2,3))):
        for a,b,c,d in product(range(-3,4),repeat=4):
            counts = Counter({a:5,b:5})
            if a == b:
                continue
            counts.update([c,d]*((n-10)//2))
            if n % 2:
                counts.update([-(sum(x*f for x,f in counts.items()))])
            elif sum(x*f for x,f in counts.items()):
                continue
            if sum(counts.values()) != n or not base.legal(counts,factors):
                continue
            light,protected,private,all_light = protected_light(counts,a,b,factors)
            assert len(protected) <= len(factors) and set(private) == protected
            transversals += 1
    print('minimal protected transversals and private witnesses: PASS',transversals)

    random, branches, local = Random(2026091216), Counter(), 0
    for n in (16,17,18):
        for _ in range(2500):
            count = random.randrange(3,8)
            weights = [5,5]+[1]*(count-2)
            for _ in range(n-sum(weights)):
                weights[random.randrange(count)] += 1
            values = [random.randrange(-10**15,10**15)*weights[-1] for _ in range(count-1)]
            values.append(-sum(x*f for x,f in zip(values,weights))//weights[-1])
            counts = Counter()
            for x,f in zip(values,weights):
                counts[x] += f
            local += audit(counts,branches)
    print('five-average three-p-scale large-integer closure: PASS',local)

    paths,longest = 0,0
    for n in (16,17,18):
        for size in (20,10000):
            for _ in range(20):
                while True:
                    values = [random.randrange(-size,size+1) for _ in range(n-1)]
                    values.append(-sum(values))
                    if base.legal(Counter(values),base.protected_primes(n,5)):
                        break
                length,used = solve(values)
                branches.update(used)
                paths += 1
                longest = max(longest,length)
    print('five-average n16-n18 literal one-digit full paths: PASS',paths,longest)
    print('five-average three-p-scale observed branches:',dict(sorted(branches.items())))
    print('five-average uniform threshold at most fifteen: PASS')


if __name__ == '__main__':
    main()
