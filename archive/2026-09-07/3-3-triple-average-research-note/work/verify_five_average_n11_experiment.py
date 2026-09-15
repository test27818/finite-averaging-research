"""Independent checks and structural stress cases for the n11 experiment."""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
from math import gcd
from pathlib import Path
from random import Random
from time import perf_counter

import explore_five_average_n11 as engine


ROOT = Path(__file__).resolve().parent.parent


def rational_shape(values):
    """Independent translation-free projective key using exact fractions."""
    values = tuple(sorted(values))
    if not any(values):
        return values
    scale = abs(values[0])
    positive = tuple(x / scale for x in values)
    reflected = tuple(-x for x in reversed(values))
    negative = tuple(x / abs(reflected[0]) for x in reflected)
    return min(positive, negative)


def validate_engine():
    rng = Random(5120312)
    states = []
    for bound in (3, 20, 1000):
        raw, _ = engine.sample_cases(11, 4, -bound, bound, rng.randrange(10**9))
        for values in raw:
            state = engine.centered(values)
            states.append(state)
            states.append(next(engine.moves_and_states(state))[1])
    equivalences = 0
    for state in states:
        expected = set()
        for indices in combinations(range(11), 5):
            values = list(map(Fraction, state))
            chosen = [values[i] for i in indices]
            if len(set(chosen)) == 1:
                continue
            mean = sum(chosen) / 5
            for i in indices:
                values[i] = mean
            expected.add(rational_shape(values))
        actual = set()
        for move, after in engine.moves_and_states(state):
            actual.add(rational_shape(tuple(map(Fraction, after))))
            assert engine.apply_values(state, move) == after
        assert actual == expected
        equivalences += 1
    print("five-average successor oracle and sign quotient: PASS", equivalences, flush=True)

    tails = 0
    for _ in range(40):
        values = [0] + [rng.randrange(-10**9, 10**9) for _ in range(9)]
        values.append(-sum(values))
        state = engine.centered(values)
        moves = engine.zero_tail(state)
        assert len(moves) <= 5
        result = engine.replay(values, moves)
        assert result["verified"]
        tails += 1
    print("critical zero-coordinate labelled tails: PASS", tails, flush=True)

    examples = (
        ("Y5-exact-four", [1] * 5 + [2] * 5 + [-15], 4),
        ("natural-return-escape", [5] * 5 + [-4] * 5 + [-5], None),
        ("padded-ten-point-obstruction", [-5] + [0] * 5 + [1] * 5, None),
    )
    for name, values, optimal in examples:
        result = engine.search(values, seconds=3)
        assert result["status"] == "solved" and result["verified"]
        if optimal is not None:
            assert result["steps"] == result["lower_bound"] == optimal and result["optimal"]
        print("critical exact control", name, result["steps"], flush=True)

    # At n10 the G filter passes a known nonreachable state. The only
    # nonidentity integral move enters the nonzero common mod2 class.
    obstruction = engine.centered([-5] + [0] * 4 + [1] * 5)
    assert engine.difference_gcd(obstruction) == 1 and engine.passes_rule(obstruction)
    integer_moves = [(move, after) for move, after in engine.moves_and_states(obstruction)
                     if sum(move) % 5 == 0]
    assert len(integer_moves) == 1
    assert not engine.passes_rule(integer_moves[0][1])
    print("n10 G1 obstruction integral boundary: PASS", flush=True)

    difficult = [1000000000000] * 5 + [-999999999999] * 5 + [-5]
    result = engine.search(difficult, seconds=0)
    assert result["status"] == "not-found-within-budget"
    assert not result["optimal"] and "operations" not in result
    print("five-average resource limit semantics: PASS", flush=True)


def replay_saved_reports():
    reports = sorted((ROOT / "work").glob("five_average_n11_range*.json"))
    saved = 0
    for filename in reports:
        report = json.loads(filename.read_text(encoding="utf-8"))
        settings = report["settings"]
        generated, attempts = engine.sample_cases(settings["n"], settings["count"],
                                                  -settings["bound"], settings["bound"], settings["seed"])
        assert attempts == report["summary"]["attempts"]
        assert generated == [row["input"] for row in report["cases"]]
        for row in report["cases"]:
            assert engine.passes_rule(engine.centered(row["input"]))
            if row["status"] != "solved":
                continue
            result = engine.verify_operations(row["input"], row["operations"])
            assert len(row["operations"]) == row["steps"]
            assert result["max_denominator_exponent"] == row["max_denominator_exponent"]
            saved += 1
    print("independent random regeneration and saved Fraction replay: PASS", len(reports), saved, flush=True)
    core_file = ROOT / "work/five_average_n11_core_stress.json"
    if core_file.exists():
        core_report = json.loads(core_file.read_text(encoding="utf-8"))
        core_saved = 0
        for item in core_report["cases"]:
            row = item["result"]
            assert engine.passes_rule(engine.centered(row["input"]))
            if row["status"] == "solved":
                engine.verify_operations(row["input"], row["operations"])
                assert row["steps"] == len(row["operations"])
                core_saved += 1
        assert core_saved == core_report["summary"]["solved"]
        print("saved critical-core Fraction replay: PASS", core_saved, flush=True)
    return len(reports), saved


def stress(output):
    cases = {}
    for a in range(-12, 13):
        for b in range(-12, 13):
            if gcd(a, b) != 1 or (a - b) % 11 == 0:
                continue
            raw = [a] * 5 + [b] * 5 + [-5 * (a + b)]
            key = engine.centered(raw)
            if key not in cases:
                cases[key] = {"a": a, "b": b, "input": raw, "type": "bounded-K5"}
    for bits in (32, 64, 128):
        for a, b in ((1 << bits, 1 - (1 << bits)), (1 << bits, -(1 << (bits - 1)) + 1)):
            if (a - b) % 11 == 0:
                b += 2
            raw = [a] * 5 + [b] * 5 + [-5 * (a + b)]
            key = engine.centered(raw)
            assert engine.passes_rule(key)
            cases[key] = {"a": a, "b": b, "input": raw, "type": "large-K5", "bits": bits}
    results = []
    start = perf_counter()
    for index, parameters in enumerate(cases.values()):
        row = engine.search(parameters["input"], seconds=10, max_nodes=30000,
                            width=128, max_depth=200)
        results.append({"parameters": parameters, "result": row})
        if index % 20 == 0 or row["status"] != "solved" or parameters["type"] == "large-K5":
            print("K5 stress", index, row["status"], row["steps"],
                  round(row["solve_seconds"], 3), flush=True)
    solved = [row["result"] for row in results if row["result"]["status"] == "solved"]
    summary = {"cases": len(results), "solved": len(solved),
               "min_steps": min(row["steps"] for row in solved),
               "max_steps": max(row["steps"] for row in solved),
               "wall_seconds": perf_counter() - start}
    Path(output).write_text(json.dumps({"scope": "deterministic core tests, not random original instances",
                                       "summary": summary, "cases": results}, indent=2) + "\n", encoding="utf-8")
    print("K5 stress summary", json.dumps(summary), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stress", action="store_true")
    parser.add_argument("--output", default="work/five_average_n11_core_stress.json")
    args = parser.parse_args()
    if args.stress:
        stress(args.output)
    else:
        validate_engine()
        replay_saved_reports()
        print("five-average n11 experiment verification: PASS", flush=True)
