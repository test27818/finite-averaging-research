"""Exact sequence-length checks and paired selector benchmarks.

The maximal-drop policy scans single legal moves, not averaging words.
General length bounds are proved in the accompanying research note.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
import json
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter

from verify_all_dimensions_double_triple_invariant import (
    choose, incongruent, initialize, preserves, protected_primes,
)
from verify_prime_double_triple_invariant import changed, heavy, replay_step, terminal

if not __debug__:
    raise RuntimeError("Exact checks require assertions; do not run with -O.")


def pair_distance(state):
    ordered = sorted(state)
    n = len(state)
    return sum((2 * i - n + 1) * x for i, x in enumerate(ordered))


def energy(state):
    return sum(x * x for x in state)


def admissible_fast(counts, triple, mean, n, residue_counts, heavy_count):
    changes = Counter({mean: 3})
    for x in triple:
        changes[x] -= 1
    new_heavy = heavy_count
    for x, delta in changes.items():
        before = counts[x]
        after = before + delta
        assert after >= 0
        new_heavy += int(after >= 3) - int(before >= 3)
    if new_heavy < 2:
        return False
    for q, frequencies in residue_counts.items():
        deltas = Counter()
        for x, delta in changes.items():
            deltas[x % q] += delta
        classes = len(frequencies)
        for residue, delta in deltas.items():
            before = frequencies[residue]
            after = before + delta
            classes += int(after > 0) - int(before > 0)
        if classes <= 1:
            return False
    return True


def maximal_drop(counts, n):
    values = sorted(counts)
    frequencies = {}
    for q in protected_primes(n):
        frequencies[q] = Counter()
        for x, count in counts.items():
            frequencies[q][x % q] += count
    heavy_count = len(heavy(counts))
    best = None
    best_drop = -1
    for triple in combinations_with_replacement(values, 3):
        a, b, c = triple
        if a == c:
            continue
        if a == b and counts[a] < 2 or b == c and counts[b] < 2:
            continue
        total = a + b + c
        if total % 3:
            continue
        mean = total // 3
        drop = a * a + b * b + c * c - 3 * mean * mean
        if drop <= best_drop:
            continue
        if admissible_fast(counts, triple, mean, n, frequencies, heavy_count):
            best, best_drop = triple, drop
    assert best is not None, counts
    return best, "maximal-safe-energy-drop"


def solve_policy(state, policy, step_limit=100000):
    n = len(state)
    assert n >= 11 and sum(state) == 0
    if not any(state):
        return {"status": "solved", "steps": 0, "solve_seconds": 0.0,
                "energy_bound": 0, "distance_bound": 0}
    assert incongruent(Counter(state), n)
    current = [3 * x for x in state]
    word = []
    start = perf_counter()
    for move in initialize(Counter(current), n):
        current, positions = replay_step(current, move)
        word.append(positions)
    selector = choose if policy == "first-fit" else maximal_drop
    while not terminal(Counter(current), n):
        if len(word) >= step_limit:
            return {"status": "step-limit", "steps": len(word),
                    "solve_seconds": perf_counter() - start}
        counts = Counter(current)
        move, _ = selector(counts, n)
        assert preserves(counts, move, n)
        current, positions = replay_step(current, move)
        word.append(positions)
    a = next(x for x in current if x)
    for _ in range(3):
        current, positions = replay_step(current, (a, -a, 0))
        word.append(positions)
    elapsed = perf_counter() - start
    assert not any(current)
    assert 2 * len(word) <= 9 * energy(state)
    assert 4 * len(word) <= 3 * pair_distance(state)

    # Separate exact replay does not rely on the selector or scaled state.
    exact = list(map(Fraction, state))
    for indices in word:
        assert len(indices) == len(set(indices)) == 3
        mean = sum(exact[i] for i in indices) / 3
        assert mean.denominator in (1, 3)
        for i in indices:
            exact[i] = mean
    assert not any(exact)
    return {"status": "solved", "steps": len(word), "solve_seconds": elapsed,
            "energy_bound": 9 * energy(state) // 2,
            "distance_bound": 3 * pair_distance(state) // 4}


def normalized_instance(rng, n, bits):
    upper = 1 << bits
    while True:
        raw = [rng.randrange(-upper, upper + 1) for _ in range(n)]
        total = sum(raw)
        centered = [n * x - total for x in raw]
        divisor = gcd(*centered)
        if not divisor:
            continue
        state = [x // divisor for x in centered]
        if incongruent(Counter(state), n):
            return raw, state


def verify():
    rng = Random(3110912)
    assert solve_policy([0] * 11, "maximal-drop")["steps"] == 0
    potential_checks = selector_checks = 0
    for n in (11, 12, 15, 20, 30):
        for _ in range(30):
            _, state = normalized_instance(rng, n, 5)
            current = [3 * x for x in state]
            for move in initialize(Counter(current), n):
                current, _ = replay_step(current, move)
            counts = Counter(current)
            if terminal(counts, n):
                continue
            best, _ = maximal_drop(counts, n)
            oracle = []
            for move in combinations_with_replacement(sorted(counts), 3):
                if move[0] == move[-1] or sum(move) % 3:
                    continue
                if any(counts[x] < f for x, f in Counter(move).items()):
                    continue
                after = changed(counts, move)
                after_list = list(after.elements())
                span = max(move) - min(move)
                loss = energy(current) - energy(after_list)
                distance_loss = pair_distance(current) - pair_distance(after_list)
                assert loss >= 2 and 2 * loss >= span * span
                assert distance_loss >= 2 * span >= 4
                potential_checks += 1
                if preserves(counts, move, n):
                    oracle.append(loss)
            best_loss = sum(x * x for x in best) - sum(best) ** 2 // 3
            assert best_loss == max(oracle)
            selector_checks += 1
    print("integer energy and pair-distance inequalities: PASS", potential_checks, flush=True)
    print("maximal-drop selector versus exact move oracle: PASS", selector_checks, flush=True)

    gap_checks = 0
    for n in (3, 4, 5, 7, 11, 20):
        for _ in range(30):
            initial = [3 * rng.randrange(-20, 21) for _ in range(n)]
            order = sorted(range(n), key=initial.__getitem__)
            if initial[order[0]] == initial[order[-1]]:
                continue
            split = max(range(1, n), key=lambda j: initial[order[j]] - initial[order[j - 1]])
            left = set(order[:split])
            current = initial.copy()
            for _ in range(8):
                internal = [indices for indices in combinations(range(n), 3)
                            if len(set(indices) & left) in (0, 3)
                            and sum(current[i] for i in indices) % 3 == 0
                            and len({current[i] for i in indices}) > 1]
                if not internal:
                    break
                indices = rng.choice(internal)
                mean = sum(current[i] for i in indices) // 3
                for i in indices:
                    current[i] = mean
            crossing = next((indices for indices in combinations(range(n), 3)
                             if len(set(indices) & left) in (1, 2)
                             and sum(current[i] for i in indices) % 3 == 0), None)
            if crossing is None:
                continue
            mean = sum(current[i] for i in crossing) // 3
            for i in crossing:
                current[i] = mean
            loss = energy(initial) - energy(current)
            diameter = max(initial) - min(initial)
            assert 2 * (n - 1) ** 2 * loss >= diameter ** 2
            assert 2 * n ** 2 * (n - 1) ** 2 * loss >= n * energy(initial) - sum(initial) ** 2
            gap_checks += 1
    print("largest-gap phase contraction with internal interleaving: PASS", gap_checks, flush=True)

    obstructions = 0
    for m in (1, 4, 10, 100, 1000, 10**6):
        assert m % 3 == 1
        a, b = -5 * m, 6 * m
        state = [a] * 4 + [a - 3, a + 3] + [b] * 5
        counts = Counter(state)
        assert incongruent(counts, 11) and energy(state) == 330 * m * m + 18
        possible = []
        for move in combinations_with_replacement(sorted(counts), 3):
            if move[0] == move[-1] or sum(move) % 3:
                continue
            if any(counts[x] < f for x, f in Counter(move).items()):
                continue
            if preserves(counts, move, 11):
                possible.append(move)
                assert sum(x * x for x in move) - sum(move) ** 2 // 3 == 6
        assert len(possible) == 2
        first = (a - 3, a, a)
        after = changed(counts, first)
        second = (b, b, a - 1)
        assert preserves(after, second, 11)
        assert 3 * (sum(x * x for x in second) - sum(second) ** 2 // 3) == 2 * (11 * m + 1) ** 2
        obstructions += 1
    print("single-step contraction obstruction and two-step repair: PASS", obstructions, flush=True)

    lower_checks = 0
    for n in (11, 14, 20):
        for multiplier in (10, 100, 1000):
            m = n * multiplier
            state = [-m] + [1] * (n - 2) + [m - n + 2]
            assert sum(state) == 0 and incongruent(Counter(state), n)
            for steps in range(5):
                denominator = 3 ** steps
                if (n - 2) * denominator >= m:
                    continue
                for alpha in range(denominator + 1):
                    for gamma in range(denominator - alpha + 1):
                        beta = denominator - alpha - gamma
                        assert -m * alpha + beta + (m - n + 2) * gamma != 0
                        lower_checks += 1
    print("positive-row logarithmic length lower bound: PASS", lower_checks, flush=True)
    print("double-triple sequence-length identities: PASS", flush=True)


def benchmark(args):
    rng = Random(args.seed)
    records = []
    for n in args.dimensions:
        for bits in args.bits:
            for sample in range(args.samples):
                raw, state = normalized_instance(rng, n, bits)
                record = {"n": n, "sample_bits": bits, "sample": sample,
                          "raw": raw, "primitive_centered": state,
                          "normalized_max_bits": max(abs(x).bit_length() for x in state)}
                for policy in args.policies:
                    record[policy] = solve_policy(state, policy, args.step_limit)
                records.append(record)
                print("sample", n, bits, sample,
                      [(p, record[p]["status"], record[p]["steps"],
                        round(record[p]["solve_seconds"], 4)) for p in args.policies], flush=True)
    output = {"seed": args.seed, "sampling": "independent uniform integers, then exact legality rejection",
              "scope": "finite paired samples; no worst-case inference",
              "records": records}
    if args.json:
        Path(args.json).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print("paired exact sequence benchmark: PASS", len(records), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--dimensions", nargs="+", type=int, default=[11, 20])
    parser.add_argument("--bits", nargs="+", type=int, default=[8, 16, 32])
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--policies", nargs="+", choices=["first-fit", "maximal-drop"],
                        default=["first-fit", "maximal-drop"])
    parser.add_argument("--seed", type=int, default=3110912)
    parser.add_argument("--step-limit", type=int, default=100000)
    parser.add_argument("--json")
    options = parser.parse_args()
    if options.benchmark:
        benchmark(options)
    else:
        verify()
