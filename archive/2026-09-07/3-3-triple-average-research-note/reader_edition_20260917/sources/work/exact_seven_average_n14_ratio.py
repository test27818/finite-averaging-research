"""Exact and random reachability statistics for 7-average on n=14.

For p <= n <= 2p the non-increasing-denominator lemma lets us restrict an
integer zero-sum input to integer successors.  Unlike the n=15 zero-trigger
experiment, this module computes reachability itself.  Successors retain
their physical integer scale; only sorting and global sign are quotiented.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
import json
from math import gcd
from pathlib import Path
from random import Random
import sys
from time import perf_counter

sys.setrecursionlimit(100000)

P, N = 7, 14


def sign_canonical(values: tuple[int, ...]) -> tuple[int, ...]:
    values = tuple(sorted(values))
    reflected = tuple(sorted(-x for x in values))
    return min(values, reflected)


def primitive(values: tuple[int, ...]) -> tuple[int, ...]:
    g = gcd(*(abs(x) for x in values))
    if g > 1:
        values = tuple(x // g for x in values)
    return sign_canonical(values)


def difference_gcd(values: tuple[int, ...]) -> int:
    return gcd(*(values[i] - values[0] for i in range(1, N)))


def g7_power(values: tuple[int, ...]) -> bool:
    if not any(values):
        return True
    g = difference_gcd(values)
    while g % 7 == 0:
        g //= 7
    return g == 1


def energy(values: tuple[int, ...]) -> int:
    return sum(x * x for x in values)


def apply(values: tuple[int, ...], move: tuple[int, ...]) -> tuple[int, ...]:
    counts = Counter(values)
    used = Counter(move)
    assert len(move) == P and all(counts[x] >= f for x, f in used.items())
    total = sum(move)
    assert total % P == 0
    rest = list((counts - used).elements())
    rest.extend([total // P] * P)
    result = sign_canonical(tuple(rest))
    assert energy(result) < energy(values)
    return result


@lru_cache(maxsize=None)
def successors(values: tuple[int, ...]) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    counts = Counter(values)
    distinct = tuple(sorted(counts))
    capacities = tuple(counts[x] for x in distinct)
    picked: list[int] = []
    seen = set()
    result = []

    def visit(index: int, left: int):
        if index == len(distinct):
            if left:
                return
            move = tuple(picked)
            if len(set(move)) == 1 or sum(move) % P:
                return
            after = apply(values, move)
            if after != values and after not in seen:
                seen.add(after)
                result.append((after, move))
            return
        value, capacity = distinct[index], capacities[index]
        for amount in range(min(capacity, left) + 1):
            picked.extend([value] * amount)
            visit(index + 1, left - amount)
            if amount:
                del picked[-amount:]

    visit(0, P)
    result.sort(key=lambda item: (energy(item[0]), item[0]))
    return tuple(result)


@lru_cache(maxsize=None)
def reachable(values: tuple[int, ...]) -> bool:
    if not any(values):
        return True
    return any(reachable(after) for after, _ in successors(values))


@lru_cache(maxsize=None)
def shortest(values: tuple[int, ...]) -> int | None:
    if not any(values):
        return 0
    distances = [shortest(after) for after, _ in successors(values)]
    distances = [d for d in distances if d is not None]
    return None if not distances else 1 + min(distances)


def enumerate_states(bound: int):
    seen = set()
    for values in combinations_with_replacement(range(-bound, bound + 1), N):
        if sum(values) or not any(values):
            continue
        state = primitive(values)
        if state in seen or not g7_power(state):
            continue
        seen.add(state)
        yield state


def exact_bounded(bound: int):
    started = perf_counter()
    states = list(enumerate_states(bound))
    reachable.cache_clear()
    shortest.cache_clear()
    solvable = 0
    distances = Counter()
    unreachable_states = []
    for state in states:
        if reachable(state):
            solvable += 1
            distance = shortest(state)
            assert distance is not None
            distances[distance] += 1
        else:
            unreachable_states.append(state)
    return {
        "p": P, "n": N, "bound": bound, "states": len(states),
        "solvable": solvable, "unsolvable": len(unreachable_states),
        "ratio": len(unreachable_states) / len(states) if states else None,
        "distance_distribution": dict(sorted(distances.items())),
        "examples": [list(x) for x in unreachable_states[:20]],
        "seconds": perf_counter() - started,
        "memo_states": reachable.cache_info().currsize,
        "sampling_model": "sorted primitive zero-sum states in [-bound,bound], conditioned on G=7^k",
    }


def raw_instance(rng: Random, bound: int) -> tuple[int, ...]:
    values = [rng.randint(-bound, bound) for _ in range(N - 1)]
    values.append(-sum(values))
    return primitive(tuple(values))


def random_experiment(bound: int, samples: int, seed: int):
    rng = Random(seed)
    accepted = rejected = unsolvable = 0
    distances = Counter()
    examples = []
    started = perf_counter()
    while accepted < samples:
        state = raw_instance(rng, bound)
        if not g7_power(state):
            rejected += 1
            continue
        accepted += 1
        ok = reachable(state)
        if not ok:
            unsolvable += 1
            if len(examples) < 10:
                examples.append(list(state))
        else:
            distance = shortest(state)
            assert distance is not None
            distances[distance] += 1
    return {
        "p": P, "n": N, "bound": bound, "samples": samples,
        "accepted": accepted, "rejected": rejected,
        "solvable": samples - unsolvable, "unsolvable": unsolvable,
        "ratio": unsolvable / samples,
        "distance_distribution": dict(sorted(distances.items())),
        "seconds": perf_counter() - started, "examples": examples,
        "sampling_model": "14 independent uniform integers in [-bound,bound], final coordinate closes zero sum, primitive-normalized, conditioned on G=7^k",
    }


def main(args):
    reports = {"exact_bounded": [exact_bounded(b) for b in args.exact_bounds],
               "random": [random_experiment(b, args.samples, args.seed + i)
                          for i, b in enumerate(args.random_bounds)]}
    for row in reports["exact_bounded"]:
        print("exact", json.dumps(row, ensure_ascii=False), flush=True)
    for row in reports["random"]:
        print("random", json.dumps(row, ensure_ascii=False), flush=True)
    Path(args.output).write_text(json.dumps(reports, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("seven-average n14 exact/random experiment: PASS", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-bounds", nargs="+", type=int, default=[1, 2, 3])
    parser.add_argument("--random-bounds", nargs="+", type=int, default=[20, 100])
    parser.add_argument("--samples", type=int, default=500)
    parser.add_argument("--seed", type=int, default=7142026)
    parser.add_argument("--output", default="work/seven_average_n14_ratio.json")
    main(parser.parse_args())
