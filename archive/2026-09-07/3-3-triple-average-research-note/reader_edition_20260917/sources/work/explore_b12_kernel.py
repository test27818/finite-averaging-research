"""Exact finite exploration of the single-prime B_12 kernel.

This is deliberately an explorer rather than a theorem certificate.  It
tests the proposed first standard interface on primitive pairs (u,v) with
gcd(u-v,4)=1, using the same exact transition and zero-sum subset oracle as
the n=91 search.
"""

from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from itertools import product
from math import gcd
import os

from search_n91_missing_class import signatures, step, subset_counts_any


def pair_classes(bound, g1_only=False):
    result = set()
    for u, v in product(range(-bound, bound + 1), repeat=2):
        if max(abs(u), abs(v)) == 0:
            continue
        if gcd(abs(u), abs(v)) != 1 or gcd(u - v, 12 if g1_only else 4) != 1:
            continue
        pair = (u, v)
        opposite = (-u, -v)
        result.add(min(pair, opposite))
    return sorted(result)


def kernel_state(pair):
    u, v = pair
    state = Counter()
    for value, count in ((u, 8), (v, 3), (-8 * u - 3 * v, 1)):
        state[F(value)] += count
    return state


def search_pair(task):
    pair, depth = task
    start = kernel_state(pair)
    queue = deque([(start, ())])
    seen = {tuple(sorted(start.items()))}
    while queue:
        state, path = queue.popleft()
        terminal = subset_counts_any(state, (3, 9))
        if terminal is not None:
            size, witness = terminal
            return pair, (path, size, witness), len(seen)
        if len(path) >= depth:
            continue
        for selected in signatures(state):
            following = step(state, selected)
            identifier = tuple(sorted(following.items()))
            if identifier not in seen:
                seen.add(identifier)
                queue.append((following, path + (selected,)))
    return pair, None, len(seen)


def verify(pair, certificate):
    path, size, witness = certificate
    state = kernel_state(pair)
    for selected in path:
        required = Counter(selected)
        assert all(state[value] >= count for value, count in required.items())
        state = step(state, selected)
    assert size in (3, 9)
    assert sum(count for _, count in witness) == size
    assert sum(value * count for value, count in witness) == 0
    assert all(count <= state[value] for value, count in witness)


def explore(bound, depth, jobs, g1_only=False):
    if bound < 1 or depth < 0 or jobs < 1:
        raise ValueError("bound/jobs must be positive and depth nonnegative")
    pairs = pair_classes(bound, g1_only)
    tasks = [(pair, depth) for pair in pairs]
    if jobs <= 1:
        results = map(search_pair, tasks)
        executor = None
    else:
        executor = ProcessPoolExecutor(max_workers=min(jobs, len(tasks)))
        results = executor.map(search_pair, tasks)
    found = {}
    state_counts = {}
    try:
        for pair, certificate, states in results:
            state_counts[pair] = states
            if certificate is not None:
                verify(pair, certificate)
                found[pair] = certificate
    finally:
        if executor is not None:
            executor.shutdown()
    print("B12 primitive pair classes", len(pairs))
    print("B12 terminal coverage", len(found), "/", len(pairs),
          "depth", depth, "bound", bound)
    missing = [pair for pair in pairs if pair not in found]
    print("B12 missing", missing)
    if missing:
        print("missing state counts", [(pair, state_counts[pair]) for pair in missing])
    for pair in sorted(found):
        certificate = found[pair]
        if len(certificate[0]) >= depth - 1:
            print("hard pair", pair, "certificate", certificate)
    return pairs, found


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=8)
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--jobs", type=int, default=os.cpu_count() or 1)
    parser.add_argument("--g1-only", action="store_true",
                        help="reproduce the historical 44-class G=1 subset")
    arguments = parser.parse_args()
    explore(arguments.bound, arguments.depth, arguments.jobs, arguments.g1_only)
