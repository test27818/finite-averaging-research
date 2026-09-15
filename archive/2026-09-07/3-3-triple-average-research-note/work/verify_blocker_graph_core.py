"""Checks for the n-d-2 safe-core theorem; general proof is in the note."""

from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import gcd

from verify_multi_prime_core import prime_divisors, dangerous, has_safe, power_three


def graph_checks():
    checked = 0
    for size in range(3, 8):
        all_edges = list(combinations(range(size), 2))
        for count in range(size-2):
            for edges in combinations(all_edges, count):
                parent = list(range(size))

                def root(i):
                    while i != parent[i]:
                        i = parent[i]
                    return i

                for a, b in edges:
                    parent[root(a)] = root(b)
                assert len({root(i) for i in range(size)}) >= 3
                # Build the independent-triple equality relation separately.
                equality = [set((i,)) for i in range(size)]
                edge_set = set(edges)
                for triple in combinations(range(size), 3):
                    if any(pair in edge_set for pair in combinations(triple, 2)):
                        continue
                    merged = set().union(*(equality[i] for i in triple))
                    for i in merged:
                        equality[i] = merged
                assert all(len(component) == size for component in equality)
                checked += 1
    return checked


def state_checks():
    checked, terminal = 0, 0
    for n in (7, 8, 10, 14, 15, 18, 22, 26, 30):
        primes = prime_divisors(n)
        for values in combinations_with_replacement(range(-3, 4), n):
            if sum(values) or gcd(*values) != 1:
                continue
            if not power_three(gcd(*(x-values[0] for x in values))):
                continue
            checked += 1
            if has_safe(values, primes):
                continue
            terminal += 1
            d = len(dangerous(values, primes))
            assert max(Counter(values).values()) >= n-d-2
    for values in ((3,)*4+(1,1,-14), (1,)*10+(8,-34,5,11)):
        n = len(values)
        primes = prime_divisors(n)
        assert sum(values) == 0 and gcd(*values) == 1
        assert gcd(*(x-values[0] for x in values)) == 1
        assert not has_safe(values, primes)
        d = len(dangerous(values, primes))
        assert max(Counter(values).values()) == n-d-2
    return checked, terminal


if __name__ == "__main__":
    print("blocker graph independent-triple connectivity: PASS", graph_checks())
    checked, terminal = state_checks()
    print("n-d-2 safe core finite checks: PASS", checked, "terminal", terminal)
    print("sharp d=1 and d=2 core examples: PASS")
