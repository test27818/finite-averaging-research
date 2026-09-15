"""Read-only review of the external ternary-mixing proof.

Enumerate only the 35/56/220 triples of explicit counterexamples. No BFS or
unbounded search is run. Original source files are hashed, never modified.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from math import comb, gcd
from pathlib import Path
import json
import sys

if not __debug__:
    raise RuntimeError('Assertions are required.')
sys.dont_write_bytecode = True
SOURCE = Path('C:/Users/19226/Documents/deepseek/test/mean3')
OUT = Path(__file__).resolve().parents[1]/'outputs'


def prime_factors(n):
    result, q = [], 2
    while q*q <= n:
        if n % q == 0:
            result.append(q)
            while n % q == 0:
                n //= q
        q += 1
    return result+([n] if n > 1 else [])


def mc_integer(values, arity=3):
    n, total = len(values), sum(values)
    centered = [n*x-total for x in values]
    content = gcd(*centered)
    if not content:
        return True
    centered = [x//content for x in centered]
    G = gcd(*(x-centered[0] for x in centered))
    return all(arity % q == 0 for q in prime_factors(G))


def near_final(values):
    mu = F(sum(values), len(values))
    sizes, power = [], 1
    while power <= len(values):
        sizes.append(power)
        power *= 3

    @lru_cache(None)
    def split(rest):
        if not rest:
            return True
        for size in sizes:
            if size > len(rest):
                break
            for tail in combinations(range(1, len(rest)), size-1):
                selected = (0,)+tail
                if sum(rest[i] for i in selected) != size*mu:
                    continue
                used = set(selected)
                if split(tuple(x for i, x in enumerate(rest) if i not in used)):
                    return True
        return False
    return split(tuple(sorted(values)))


def analyze(values):
    n, mu = len(values), F(sum(values), len(values))
    assert mu.denominator == 1 and mc_integer(values)
    qlist = [q for q in prime_factors(n) if q != 3]
    assert all(len({x % q for x in values}) > 1 for q in qlist)
    records, integral, constants = [], 0, 0
    for group in combinations(range(n), 3):
        chosen = [values[i] for i in group]
        if sum(chosen) % 3:
            continue
        integral += 1
        if len(set(chosen)) == 1:
            constants += 1
            continue
        result = list(values)
        mean = sum(chosen)//3
        for i in group:
            result[i] = mean
        bad = [q for q in qlist if len({x % q for x in result}) == 1]
        records.append({'indices_1based': [i+1 for i in group],
                        'values': chosen, 'mean': mean, 'output': result,
                        'unsafe_primes': bad, 'output_MC3': mc_integer(result)})
    counts, residues = Counter(values), Counter(x % 3 for x in values)
    formula = sum(comb(residues[r], 3) for r in range(3))
    formula += residues[0]*residues[1]*residues[2]
    assert integral == formula
    assert constants == sum(comb(f, 3) for f in counts.values())
    assert all(record['unsafe_primes'] for record in records)
    assert not near_final(values)
    return {'input': values, 'n': n, 'mean': int(mu), 'MC3': True,
            'old_I1': sum(f >= 2 for f in counts.values()) >= 2,
            'weak_Iprime': any(f >= 2 for f in counts.values()),
            'near_final': False, 'position_triples_checked': comb(n, 3),
            'integral_triples': integral, 'constant_triples': constants,
            'safe_nonconstant_integral_triples': 0, 'nonconstant': records}


def load_readonly(name, filename):
    spec = spec_from_file_location(name, SOURCE/filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_distinct_value_repair():
    records = []
    for k in (2, 3, 4, 5, 7):
        n = 2*k+12
        evens = list(range(0, 2*(n-2), 2))
        raw = evens+[1, -sum(evens)-1]
        qlist = [q for q in prime_factors(n) if k % q]
        assert all(len({x % q for x in raw}) > 1 for q in qlist)
        forbidden_values = set()
        for q in qlist:
            counts = Counter(x % q for x in raw)
            majority = next((r for r, f in counts.items() if f >= n-k), None)
            if majority is not None:
                forbidden_values.add(next(x for x in raw if x % q != majority))
        distinct = list(dict.fromkeys(raw))
        assert len(distinct) >= len(qlist)+2*k-1
        candidates = [x for x in distinct if x not in forbidden_values][:2*k-1]
        dp = [dict() for _ in range(k+1)]
        dp[0][0] = ()
        for x in candidates:
            for size in range(k, 0, -1):
                for r, path in dp[size-1].items():
                    dp[size].setdefault((r+x) % k, path+(x,))
        chosen = dp[k][0]
        assert len(chosen) == len(set(chosen)) == k
        positions = [raw.index(x) for x in chosen]
        result = raw[:]
        mean = sum(chosen)//k
        for i in positions:
            result[i] = mean
        assert sum(result) == sum(raw) == 0
        assert all(len({x % q for x in result}) > 1 for q in qlist)
        assert sum(x*x for x in result) < sum(x*x for x in raw)
        records.append({'arity': k, 'n': n, 'input': raw,
                        'protected_values': sorted(forbidden_values),
                        'operation_1based': [i+1 for i in positions],
                        'mean': mean})
    print('repaired distinct-value lemma for general arity: PASS', len(records))
    return records


def main():
    files = ['3平均混合图的完美混合性.md', 'README.md', 'kmean.py',
             'kmean_fast.py', 'n0_final7.py', 'n0_general.py', 'exp4.py']
    hashes = {name: sha256((SOURCE/name).read_bytes()).hexdigest() for name in files}
    records = [analyze(values) for values in (
        [0]*5+[1, 13], [0]*6+[1, 7], [0]*4+[5, 8, 8],
        [0]*9+[2, 5, 5], [0]*15+[1, 1, 16])]
    assert [r['integral_triples'] for r in records] == [10, 20, 5, 85, 456]
    print('independent counterexamples to the iteration lemma: PASS', len(records),
          sum(r['position_triples_checked'] for r in records))

    library = load_readonly('external_review_kmean', 'kmean.py')
    fast = load_readonly('external_review_fast', 'kmean_fast.py')
    for r in records[:4]:
        assert library.MC_holds(r['input'], 3)
        assert library.MC_reduced(r['input'], 3)[0]
        assert not library.is_near_final(r['input'], 3)
    assert library.MC_reduced([-1, -1, 1, 1], 3) == (True, None)
    assert not library.MC_holds([-1, -1, 1, 1], 3)
    assert not mc_integer([-1, -1, 1, 1], 3)
    assert fast.mc_ok([-1, -1, 1, 1], 3)
    malformed = fast.successors((0, 1, 2, 3, 4), k=5)
    assert malformed and all(len(s) == 5 for s in malformed)
    assert not any(s[0] == s[-1] for s in malformed)
    assert library.successors((0, 1, 2, 3, 4), k=5)[0][0][0] == 10
    print('external near-final confirmation and implementation counterexamples: PASS')

    # Infinite-family proofs are in the report; these are exact sample checks.
    frozen, unsafe = [], []
    for n in (8, 11, 20, 101, 1001):
        values = [0]*(n-2)+[1, n-1]
        assert n % 3 == 2 and sum(values) == n and mc_integer(values)
        assert all((k+l*(n-1)) % 3 for k in range(2) for l in range(2) if k+l)
        frozen.append(n)
    for exponent in range(1, 7):
        n = 6*3**exponent
        assert (n-2) % 3 == 1 and n//3 % 2 == 0
        # Apart from constant zero groups, the only integral group is (1,1,n-2).
        assert all((i+j*(n-2)) % 3 != 0
                   for i in range(3) for j in range(2) if 0 < i+j < 3)
        assert n//2 < n-2
        unsafe.append(n)
    print('unbounded frozen and unsafe families: PASS', len(frozen), len(unsafe))

    two_phase = []
    for u in (2, 8, 20, 200, 2000):
        raw = [0]*6+[u, u, u+3]
        mu = (u+1)//3
        initial = sum((x-mu)**2 for x in raw)
        first = [0]*6+[u+1]*3
        middle = sum((x-mu)**2 for x in first)
        assert initial-middle == 6
        final = first.copy()
        for i in (0, 1, 6):
            final[i] = (u+1)//3
        loss = middle-sum((x-mu)**2 for x in final)
        assert F(loss, middle) == F(1, 3)
        two_phase.append({'u': u, 'first_drop': 6, 'second_drop_fraction': '1/3'})
    assert sum((14 if i < 4 else 19) for i in range(5))//5 == 15
    assert mc_integer([0]*10+[14]*4+[19], 5)
    assert not mc_integer([0]*10+[15]*5, 5)
    print('useful two-phase energy identity and p5 transfer boundary: PASS')
    distinct_repair = verify_distinct_value_repair()
    assert all(sha256((SOURCE/name).read_bytes()).hexdigest() == value
               for name, value in hashes.items())
    (OUT/'external_mean3_review_checks.json').write_text(json.dumps({
        'scope': 'Counterexamples to proof lemmas, not to ternary reachability.',
        'source_directory': str(SOURCE), 'source_sha256': hashes,
        'counterexamples': records, 'frozen_family_dimensions': frozen,
            'unsafe_family_dimensions': unsafe, 'useful_two_phase': two_phase,
            'repaired_distinct_value_paths': distinct_repair},
        ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('external mean3 proof review: PASS')


if __name__ == '__main__':
    main()
