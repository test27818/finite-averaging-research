"""Audit the imported binary HTML and compare exact ternary constructions.

Embedded script blocks are parsed as HTML data. The original solver runs in
Node with a small browser-worker shim; the imported file is never rewritten.
"""

import argparse
from fractions import Fraction
import hashlib
from html.parser import HTMLParser
from itertools import combinations, permutations, product
import json
from pathlib import Path
from random import Random
import subprocess

from triple_average_optimal_search import (
    apply_values, breadth_first_distance, centered, invariant_bound, lower_bound,
    possible, primitive, replay_original, solve, successors,
)

ROOT = Path(__file__).resolve().parent.parent


class ScriptParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.active = None
        self.scripts = {}

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.active = dict(attrs).get("id")
            if self.active:
                self.scripts[self.active] = ""

    def handle_data(self, data):
        if self.active:
            self.scripts[self.active] += data

    def handle_endtag(self, tag):
        if tag == "script":
            self.active = None


class BinarySolver:
    def __enter__(self):
        parser = ScriptParser()
        parser.feed((ROOT / "2-average-solver.html").read_text(encoding="utf-8"))
        self.process = subprocess.Popen(
            ["node", str(ROOT / "work/run_binary_html_solver.cjs")],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, encoding="utf-8",
        )
        self.request({"action": "initialize", "scripts": [parser.scripts[key] for key in
                      ("solver-source", "verifier-source", "runner-source")]})
        return self

    def request(self, payload):
        self.process.stdin.write(json.dumps(payload) + "\n")
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if not line:
            raise RuntimeError(self.process.stderr.read())
        response = json.loads(line)
        if not response["ok"]:
            raise RuntimeError(response["error"])
        return response["result"]

    def solve(self, raw, opt_ms=0):
        return self.request({"action": "solve", "input": list(map(str, raw)),
                             "options": {"optMs": opt_ms, "hardMs": 5000}})

    def __exit__(self, *args):
        self.process.stdin.close()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()
        self.process.stdout.close()
        self.process.stderr.close()


def verify_indices(raw, operations, q):
    state = list(map(Fraction, raw))
    for operation in operations:
        assert len(operation) == len(set(operation)) == q
        assert all(isinstance(i, int) and 1 <= i <= len(state) for i in operation)
        mean = sum(state[i - 1] for i in operation) / q
        for i in operation:
            state[i - 1] = mean
    assert all(x == Fraction(sum(raw), len(raw)) for x in state)


def packing_number(state):
    from functools import lru_cache

    values = tuple(x for x in state if x)
    edges = []
    for size in (2, 3):
        for indices in combinations(range(len(values)), size):
            if sum(values[i] for i in indices) == 0:
                edges.append(sum(1 << i for i in indices))

    @lru_cache(None)
    def visit(mask):
        if not mask:
            return 0
        first = mask & -mask
        best = visit(mask ^ first)
        for edge in edges:
            if edge & first and edge & mask == edge:
                best = max(best, 1 + visit(mask ^ edge))
        return best

    return visit((1 << len(values)) - 1)


def numerical_matching_encoding(xs, ys, zs, target):
    assert len(xs) == len(ys) == len(zs)
    assert sum(xs + ys + zs) == len(xs) * target
    c = 1 + target + max(xs + ys + zs)
    k = 10 * c
    encoded = ([k + x for x in xs] + [3 * k + y for y in ys]
               + [-4 * k + z - target for z in zs])
    largest = max(map(abs, encoded))
    pad = 10 * largest + 1
    return encoded + [pad, pad + 1, -2 * pad - 1]


def zero_triple_partition(values):
    from functools import lru_cache

    @lru_cache(None)
    def visit(state):
        if not state:
            return True
        for j, k in combinations(range(1, len(state)), 2):
            if state[0] + state[j] + state[k] == 0:
                tail = tuple(x for i, x in enumerate(state) if i not in (0, j, k))
                if visit(tail):
                    return True
        return False

    return visit(tuple(sorted(values)))


def verify_hardness_encoding():
    rng = Random(310031)
    checked = yes = no = 0
    for _ in range(100):
        m = 3
        groups = [[rng.randrange(1, 10) for _ in range(m)] for _ in range(3)]
        remainder = sum(sum(group) for group in groups) % m
        groups[2][-1] += (-remainder) % m
        xs, ys, zs = groups
        target = sum(xs + ys + zs) // m
        expected = any(all(x + y + z == target for x, y, z in zip(xs, yp, zp))
                       for yp, zp in product(permutations(ys), permutations(zs)))
        encoded = numerical_matching_encoding(xs, ys, zs, target)
        assert len(encoded) == 12 and sum(encoded) == 0 and all(encoded)
        from math import gcd
        assert gcd(*(x - encoded[0] for x in encoded)) == 1
        assert possible(centered(encoded), 2) and possible(centered(encoded), 3)
        for indices in combinations(range(len(encoded)), 3):
            if sum(encoded[i] for i in indices):
                continue
            if min(indices) >= 3 * m:
                assert indices == (3 * m, 3 * m + 1, 3 * m + 2)
            else:
                assert tuple(i // m for i in indices) == (0, 1, 2)
                assert xs[indices[0]] + ys[indices[1] - m] + zs[indices[2] - 2 * m] == target
        assert zero_triple_partition(encoded) == expected
        checked += 1
        yes += expected
        no += not expected
    assert yes and no
    print("promised-G1 numerical matching hardness encoding: PASS", checked, yes, no, flush=True)
    return {"checked": checked, "yes": yes, "no": no}


def verify(binary):
    selftests = binary.request({"action": "selftest"})
    assert all(test["ok"] for test in selftests), selftests
    print("imported binary HTML built-in tests: PASS", len(selftests), flush=True)

    examples = [
        ("ternary-faster", [1, 1, -2, 0, 0, 0, 0]),
        ("binary-faster", [1, 5, -3, -3, 0, 0, 0]),
        ("equal-length", [-1, 1, 0, 0, 0, 0, 0]),
        ("two-zero-triples", [-3, -2, -1, 0, 1, 2, 3]),
    ]
    records = []
    for name, raw in examples:
        pair = binary.solve(raw, 1000)
        triple = solve(raw, seconds=5)
        assert pair["verified"] and pair["optimal"]
        assert triple["verified"] and triple["optimal"], triple
        verify_indices(raw, pair["operations"], 2)
        verify_indices(raw, triple["operations"], 3)
        binary_distance = breadth_first_distance(raw, q=2, max_depth=pair["steps"])
        ternary_distance = breadth_first_distance(raw, q=3, max_depth=triple["steps"])
        assert binary_distance == pair["steps"]
        assert ternary_distance == triple["steps"]
        records.append({"name": name, "input": raw, "binary": pair, "ternary": triple})
        print("independent shortest comparison", name, pair["steps"], triple["steps"], flush=True)

    rng = Random(231109)
    checks = 0
    for _ in range(50):
        raw = [rng.randrange(-4, 5) for _ in range(7)]
        state = centered(raw)
        if not any(state) or not possible(state):
            continue
        before = packing_number(state)
        for after, move in successors(state):
            after_packing = packing_number(after)
            if sum(move) == 0:
                assert after_packing <= before - 1
            else:
                assert after_packing <= before + 3
            checks += 1
    print("ternary zero-sum packing lower-bound transitions: PASS", checks, flush=True)
    hard = centered([1, 5, -3, -3, 0, 0, 0])
    limited = solve(list(hard), seconds=1e-9)
    assert not limited["optimal"] and limited["lowerBound"] < limited["steps"]
    print("ternary budget exhaustion does not claim optimality: PASS", flush=True)
    hardness = verify_hardness_encoding()
    print("pair-triple optimality audit: PASS", flush=True)
    return {"html_sha256": hashlib.sha256((ROOT / "2-average-solver.html").read_bytes()).hexdigest(),
            "binary_selftests": selftests, "exact_examples": records,
            "packing_checks": checks, "hardness_encoding": hardness}


def benchmark(binary, args):
    rng = Random(args.seed)
    records, attempts = [], 0
    for n in args.dimensions:
        for sample in range(args.samples):
            while True:
                raw = [rng.randrange(-args.bound, args.bound + 1) for _ in range(n)]
                attempts += 1
                state = centered(raw)
                if any(state) and possible(state, 2) and possible(state, 3):
                    break
            pair = binary.solve(raw, 0)
            triple = solve(raw, seconds=0)
            old_moves = invariant_bound(state)
            assert pair["status"] == triple["status"] == "solved"
            verify_indices(raw, pair["operations"], 2)
            verify_indices(raw, triple["operations"], 3)
            replay_original(raw, old_moves)
            records.append({"n": n, "sample": sample, "input": raw, "binary": pair,
                            "ternary": triple, "ternary_invariant_steps": len(old_moves)})
            print("same-input construction", n, sample, pair["steps"],
                  len(old_moves), triple["steps"], flush=True)
    return {"seed": args.seed, "range": [-args.bound, args.bound], "attempts": attempts,
            "sampling": "independent uniform integers, rejected unless both criteria hold",
            "optimization_budget_ms": 0, "scope": "feasible upper bounds, not optimal distance statistics",
            "records": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--dimensions", nargs="+", type=int, default=[11, 12, 16, 20])
    parser.add_argument("--samples", type=int, default=6)
    parser.add_argument("--bound", type=int, default=20)
    parser.add_argument("--seed", type=int, default=231109)
    parser.add_argument("--json")
    options = parser.parse_args()
    with BinarySolver() as binary:
        result = benchmark(binary, options) if options.benchmark else verify(binary)
    if options.json:
        Path(options.json).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
