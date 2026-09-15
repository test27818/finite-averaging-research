"""Exact n=10 five-average ratio experiment.

For integer zero-sum states with 5 <= n <= 2*5, the documented
non-increasing-denominator lemma says every successful path stays integral.
Thus the recursive solver below enumerates all integer five-average successors;
energy strictly decreases for every nonidentity move, so reachability is exact
on each bounded state, with no depth or time cutoff.
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
from time import perf_counter


def sign_canonical(state: tuple[int, ...]) -> tuple[int, ...]:
    """Quotient only by global sign, never by a p-divisible scale."""
    ordered = tuple(sorted(state))
    reflected = tuple(-x for x in reversed(ordered))
    return min(ordered, reflected)


def primitive(state: tuple[int, ...]) -> tuple[int, ...]:
    d = gcd(*(abs(x) for x in state))
    if d > 1:
        state = tuple(x // d for x in state)
    return sign_canonical(state)


def centered(raw: tuple[int, ...]) -> tuple[int, ...]:
    n = len(raw)
    total = sum(raw)
    return primitive(tuple(n * x - total for x in raw))


def difference_gcd(state: tuple[int, ...]) -> int:
    return gcd(*(x - state[0] for x in state))


def g5_power(state: tuple[int, ...]) -> bool:
    """Candidate condition for n=10: G must be a power of 5."""
    if not any(state):
        return True
    value = difference_gcd(state)
    while value % 5 == 0:
        value //= 5
    return value == 1


# Compatibility alias for earlier notebooks and ad-hoc checks.
g5 = g5_power


def energy(state: tuple[int, ...]) -> int:
    return sum(x * x for x in state)


def apply(state: tuple[int, ...], move: tuple[int, ...], q: int = 5) -> tuple[int, ...]:
    counts = Counter(state)
    used = Counter(move)
    assert len(move) == q and all(counts[x] >= f for x, f in used.items())
    assert sum(move) % q == 0
    rest = counts - used
    # Unselected positions keep their original values.  Only the q selected
    # positions are replaced by their common average.
    values = [x for x, f in rest.items() for _ in range(f)]
    values.extend([sum(move) // q] * q)
    return primitive(tuple(sorted(values)))


@lru_cache(maxsize=None)
def successors(state: tuple[int, ...]) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    counts = Counter(state)
    values = tuple(sorted(counts))
    result = []
    seen = set()
    capacities = tuple(counts[x] for x in values)

    def visit(index: int, left: int, picked: list[int]) -> None:
        if index == len(values):
            if left or len(set(picked)) < 2 or sum(picked) % 5:
                return
            move = tuple(picked)
            after = apply(state, move)
            if after == state or after in seen:
                return
            if energy(after) >= energy(state):
                raise AssertionError((state, move, after))
            seen.add(after)
            result.append((after, move))
            return
        value, capacity = values[index], capacities[index]
        for amount in range(min(capacity, left) + 1):
            picked.extend([value] * amount)
            visit(index + 1, left - amount, picked)
            if amount:
                del picked[-amount:]

    visit(0, 5, [])
    result.sort(key=lambda item: (energy(item[0]), item[0]))
    return tuple(result)


@lru_cache(maxsize=None)
def reachable(state: tuple[int, ...]) -> bool:
    if not any(state):
        return True
    # A successful path remains integral; all nonidentity successors reduce
    # integer energy, so this recursion is a finite DAG on bounded states.
    return any(reachable(after) for after, _ in successors(state))


@lru_cache(maxsize=None)
def shortest(state: tuple[int, ...]) -> int | None:
    if not any(state):
        return 0
    distances = [shortest(after) for after, _ in successors(state)]
    distances = [d for d in distances if d is not None]
    return None if not distances else 1 + min(distances)


def enumerate_states(bound: int):
    for state in combinations_with_replacement(range(-bound, bound + 1), 10):
        if sum(state) != 0:
            continue
        state = primitive(state)
        if state == (0,) * 10:
            continue
        if g5_power(state):
            yield state


def exact_bounded(bound: int):
    started = perf_counter()
    states = sorted(set(enumerate_states(bound)))
    reachable.cache_clear()
    shortest.cache_clear()
    solvable = 0
    unreachable_states = []
    distances = Counter()
    for state in states:
        if reachable(state):
            solvable += 1
            distance = shortest(state)
            assert distance is not None
            distances[distance] += 1
        else:
            unreachable_states.append(state)
    elapsed = perf_counter() - started
    return {
        "bound": bound,
        "states": len(states),
        "solvable": solvable,
        "unsolvable": len(unreachable_states),
        "ratio": len(unreachable_states) / len(states) if states else None,
        "distance_distribution": dict(sorted(distances.items())),
        "examples": [list(state) for state in unreachable_states[:25]],
        "seconds": elapsed,
        "memo_states": reachable.cache_info().currsize,
        "sampling_model": "sorted primitive zero-sum states with coordinates initially in [-bound,bound]",
    }


def random_raw(rng: Random, bound: int) -> tuple[int, ...]:
    return tuple(rng.randint(-bound, bound) for _ in range(10))


def random_experiment(bound: int, samples: int, seed: int):
    rng = Random(seed)
    accepted = rejected = 0
    records = []
    started = perf_counter()
    while accepted < samples:
        raw = random_raw(rng, bound)
        state = centered(raw)
        if not g5_power(state):
            rejected += 1
            continue
        accepted += 1
        exact = reachable(state)
        distance = shortest(state) if exact else None
        records.append({"raw": list(raw), "state": list(state),
                        "reachable": exact, "shortest": distance,
                        "energy": energy(state)})
        if accepted % 100 == 0:
            print("random", bound, accepted, "unreachable", sum(not r["reachable"] for r in records), flush=True)
    unsolvable = sum(not r["reachable"] for r in records)
    return {
        "bound": bound, "samples": samples, "accepted": accepted,
        "rejected": rejected, "ratio": unsolvable / samples,
        "solvable": samples - unsolvable, "unsolvable": unsolvable,
        "mean_shortest_solvable": (sum(r["shortest"] for r in records if r["reachable"])
                                   / max(1, samples - unsolvable)),
        "min_shortest": min((r["shortest"] for r in records if r["reachable"]), default=None),
        "max_shortest": max((r["shortest"] for r in records if r["reachable"]), default=None),
        "seconds": perf_counter() - started, "records": records,
        "sampling_model": "10 independent uniform integers in [-bound,bound], centered and primitive-normalized, conditioned on G=5^k",
    }


def ci_zero_failures(samples: int, confidence: float = 0.95) -> float:
    """One-sided binomial upper bound if zero failures are observed."""
    return 1.0 - (1.0 - confidence) ** (1.0 / samples)


def sample_size_for_detection(rate: float, confidence: float = 0.95) -> int:
    if rate <= 0:
        return 0
    import math
    return math.ceil(math.log(1 - confidence) / math.log(1 - rate))


def main(args):
    reports = {"exact_bounded": [exact_bounded(bound) for bound in args.exact_bounds]}
    for report in reports["exact_bounded"]:
        print("exact", json.dumps(report), flush=True)

    reachable.cache_clear()
    shortest.cache_clear()
    reports["random"] = [random_experiment(bound, args.samples, args.seed + i)
                         for i, bound in enumerate(args.random_bounds)]
    for report in reports["random"]:
        print("random-summary", json.dumps({k: v for k, v in report.items() if k != "records"}), flush=True)

    rates = [row["ratio"] for row in reports["random"]]
    reference = max(rates + [0.0])
    reports["sampling_guidance"] = {
        "reference_observed_rate": reference,
        "samples_for_95pct_one_detection_at_reference": sample_size_for_detection(reference),
        "zero_failures_upper_95pct_after_1000": ci_zero_failures(1000),
        "zero_failures_upper_95pct_after_10000": ci_zero_failures(10000),
        "formula_for_true_rate_r": "ceil(log(0.05)/log(1-r)) samples gives 95% chance to see >=1 counterexample",
        "warning": "Random ratios depend strongly on the sampling distribution; explicit sparse families can have positive existence but negligible independent-draw probability.",
    }
    Path(args.output).write_text(json.dumps(reports, indent=2) + "\n", encoding="utf-8")
    print("sampling-guidance", json.dumps(reports["sampling_guidance"]), flush=True)
    print("five-average n10 exact ratio experiment: PASS", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exact-bounds", nargs="+", type=int, default=[2, 3, 4])
    parser.add_argument("--random-bounds", nargs="+", type=int, default=[2, 5, 20, 100])
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=5102026)
    parser.add_argument("--output", default="work/five_average_n10_ratio.json")
    main(parser.parse_args())
