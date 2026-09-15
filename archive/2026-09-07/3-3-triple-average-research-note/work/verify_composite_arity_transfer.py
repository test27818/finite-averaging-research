"""Exact checks for composite_arity_four_six_transfer.md.

The universal statements are proved in the report.  This program checks the
original-position interfaces and examples, not an exhaustive reachability tree.
Binary paths come from the existing HTML; Fraction replay trusts only indices.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, prod
from pathlib import Path
from random import Random
import json

from compare_pair_triple_solvers import BinarySolver


def factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def primitive_center(raw):
    xs = list(map(Fraction, raw))
    mean = sum(xs) / len(xs)
    den = lcm(*(x.denominator for x in xs + [mean]))
    zs = [int((x - mean) * den) for x in xs]
    g = gcd(*zs)
    return [x // g for x in zs] if g else zs


def gap_gcd(raw):
    xs = primitive_center(raw)
    return gcd(*(x - xs[0] for x in xs))


def legal(raw, q):
    g = gap_gcd(raw)
    if not g:
        return True
    for p in factors(q):
        while g % p == 0:
            g //= p
    return g == 1


def apply(state, ids):
    value = sum(state[i] for i in ids) / len(ids)
    out = state[:]
    for i in ids:
        out[i] = value
    return out


def independent_replay(raw, operations, q, require_consensus=True):
    # No normalization, quotient labels, or solver states are trusted here.
    state = list(map(Fraction, raw))
    target = sum(state) / len(state)
    for ids in operations:
        assert len(ids) == len(set(ids)) == q
        assert all(type(i) is int and 0 <= i < len(state) for i in ids)
        value = sum((state[i] for i in ids), Fraction()) / q
        for i in ids:
            state[i] = value
    if require_consensus:
        assert all(x == target for x in state)
    return state


def tensor_network(q, n):
    """A fixed word on n positions, for q|n and identical prime supports."""
    qf, nf = factors(q), factors(n)
    assert n % q == 0 and set(qf) == set(nf)
    radices, axes = [], {}
    for p, exponent in nf.items():
        axes[p] = list(range(len(radices), len(radices) + exponent))
        radices += [p] * exponent
    digits = list(product(*(range(p) for p in radices)))
    layers = max((nf[p] + qf[p] - 1) // qf[p] for p in qf)
    ops = []
    for layer in range(layers):
        selected = set()
        for p, exponent in qf.items():
            selected.update(axes[p][(layer * exponent + j) % nf[p]]
                            for j in range(exponent))
        groups = defaultdict(list)
        for i, ds in enumerate(digits):
            groups[tuple(d for j, d in enumerate(ds) if j not in selected)].append(i)
        assert len(groups) == n // q
        assert all(len(ids) == q for ids in groups.values())
        ops += list(groups.values())
    assert len(ops) == layers * n // q
    return ops


def six_nine_network():
    return [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8],
            [0, 1, 2, 6, 3, 4], [0, 1, 2, 5, 7, 8]]


def six_threepower_network(n):
    exponent = factors(n).get(3)
    assert exponent and exponent >= 2 and n == 3 ** exponent
    digits = list(product(range(3), repeat=exponent))
    ops = []
    for layer in range((exponent + 1) // 2):
        selected = {2 * layer % exponent, (2 * layer + 1) % exponent}
        groups = defaultdict(list)
        for i, ds in enumerate(digits):
            groups[tuple(d for j, d in enumerate(ds) if j not in selected)].append(i)
        for ids in groups.values():
            assert len(ids) == 9
            ops += [[ids[i] for i in atom] for atom in six_nine_network()]
    return ops


def reduction_shape(q, n):
    assert q % 2 == 0 and n % q == 0
    qf, nf = factors(q), factors(n)
    block = 2 ** qf[2] * prod(p ** nf[p] for p in qf if p != 2)
    return block, n // block, block // 2


def halfblock_construct(raw, q, binary):
    """General transfer: q/2 divides n; residual quotient M=2 or M>=4."""
    n = len(raw)
    assert q % 2 == 0 and n % (q // 2) == 0 and legal(raw, q)
    xs = primitive_center(raw)
    qf, nf = factors(q), factors(n)
    copies = 2 ** (qf[2] - 1) * prod(p ** nf[p] for p in qf if p != 2)
    count, block = n // copies, 2 * copies
    assert count == 2 or count >= 4
    if count % 2:
        sizes = [block, copies] + [block] * ((count - 3) // 2)
    else:
        sizes = [block] * (count // 2)
    groups, swaps = partition_by_sizes(xs, sizes,
                                      sorted(set(factors(count)) - {2}))
    local = tensor_network(q, block)
    def average_block(ids):
        return [[ids[i] for i in atom] for atom in local]
    labels, ops = [], []
    if count % 2:
        u, v = groups[:2]
        ops += average_block(u)
        ops += average_block(u[copies:] + v)
        labels += [u[:copies], u[copies:], v]
        tail = groups[2:]
    else:
        tail = groups
    for ids in tail:
        ops += average_block(ids)
        labels += [ids[:copies], ids[copies:]]
    state = independent_replay(xs, ops, q, False)
    quotient = [state[ids[0]] for ids in labels]
    assert len(quotient) == count
    assert all(all(state[i] == value for i in ids) for ids, value in zip(labels, quotient))
    assert legal(quotient, 2), (q, n, quotient)
    denominator = lcm(*(x.denominator for x in quotient))
    solution = binary.solve([int(x * denominator) for x in quotient])
    assert solution["status"] == "solved", solution
    binary_ops = [[i - 1 for i in pair] for pair in solution["operations"]]
    independent_replay(quotient, binary_ops, 2)
    ops += lift_binary(q, labels, binary_ops)
    return ops, {"copies": copies, "quotient_n": count, "swaps": swaps,
                 "binary_steps": len(binary_ops), "route": "uniform-half-block"}


def dangerous_edge(sums, p, i, j):
    other = [s % p for k, s in enumerate(sums) if k not in (i, j)]
    return (len(set(other)) == 1
            and (sums[i] + sums[j] - 2 * other[0]) % p == 0)


def partition_by_sizes(xs, sizes, primes):
    groups, start = [], 0
    for size in sizes:
        groups.append(list(range(start, start + size)))
        start += size
    assert start == len(xs)
    protected, swaps = [], []
    for p in primes:
        assert len({x % p for x in xs}) > 1
        means = lambda ell: [sum(xs[i] for i in ids) * pow(len(ids), -1, ell) % ell
                             for ids in groups]
        if len(set(means(p))) == 1:
            assert len(groups) >= 5 or (len(groups) >= 3 and not protected)
            found = None
            for i, j in combinations(range(len(groups)), 2):
                def bad(ell):
                    vals = means(ell)
                    outside = [v for k, v in enumerate(vals) if k not in (i, j)]
                    return (len(set(outside)) == 1
                            and (sizes[i] * (vals[i] - outside[0])
                                 + sizes[j] * (vals[j] - outside[0])) % ell == 0)
                if any(bad(ell) for ell in protected):
                    continue
                for a in groups[i]:
                    for b in groups[j]:
                        if (xs[a] - xs[b]) % p:
                            found = i, j, a, b
                            break
                    if found:
                        break
                if found:
                    break
            assert found is not None
            i, j, a, b = found
            groups[i][groups[i].index(a)] = b
            groups[j][groups[j].index(b)] = a
            swaps.append([p, i, j, a, b])
        protected.append(p)
        assert all(len(set(means(ell))) > 1 for ell in protected)
    return groups, swaps


def good_partition(xs, q):
    block, m, copies = reduction_shape(q, len(xs))
    groups, swaps = partition_by_sizes(xs, [block] * m,
                                      sorted(set(factors(len(xs))) - set(factors(q))))
    sums = [sum(xs[i] for i in ids) for ids in groups]
    quotient, labels = [], []
    for ids, total in zip(groups, sums):
        quotient += [total, total]
        labels += [ids[:copies], ids[copies:]]
    assert legal(quotient, 2)
    return groups, quotient, labels, swaps


def lift_binary(q, labels, binary_ops):
    chunk = q // 2
    ops = []
    for i, j in binary_ops:
        assert i != j and len(labels[i]) == len(labels[j])
        assert len(labels[i]) % chunk == 0
        for start in range(0, len(labels[i]), chunk):
            ops.append(labels[i][start:start + chunk] + labels[j][start:start + chunk])
    return ops


def construct(raw, q, binary):
    xs = primitive_center(raw)
    assert legal(xs, q)
    block, m, copies = reduction_shape(q, len(xs))
    if m == 1:
        ops = tensor_network(q, len(xs))
        return ops, {"block": block, "quotient_n": 2, "swaps": [], "binary_steps": 0}
    groups, quotient, labels, swaps = good_partition(xs, q)
    local = tensor_network(q, block)
    ops = [[ids[i] for i in atom] for ids in groups for atom in local]
    solution = binary.solve(quotient)
    assert solution["status"] == "solved", solution
    binary_ops = [[i - 1 for i in pair] for pair in solution["operations"]]
    # Independently verify the binary witness before compiling it.
    independent_replay(quotient, binary_ops, 2)
    ops += lift_binary(q, labels, binary_ops)
    return ops, {"block": block, "quotient_n": 2 * m, "swaps": swaps,
                 "binary_steps": len(binary_ops)}


def construct_six_odd(raw, binary):
    n = len(raw)
    assert n % 6 == 3 and n >= 9 and legal(raw, 6)
    xs = primitive_center(raw)
    if n == 9:
        return six_nine_network(), {"quotient_n": 3, "swaps": [], "binary_steps": 0}
    swaps = []
    if factors(n)[3] >= 2:
        block = 3 ** factors(n)[3]
        groups, swaps = partition_by_sizes(xs, [block] * (n // block),
                                          sorted(set(factors(n)) - {2, 3}))
        local = six_threepower_network(block)
        ops = [[ids[i] for i in atom] for ids in groups for atom in local]
        labels = groups
        if len(groups) == 1:
            return ops, {"quotient_n": 1, "swaps": swaps, "binary_steps": 0}
    elif n == 15:
        # The initial six-set U is split only after it has been averaged.
        groups = [list(range(6)), list(range(6, 9)), list(range(9, 15))]
        def entry(groups):
            u, v, w = groups
            return [u[:], u[3:] + v, w[:]]
        state = independent_replay(xs, entry(groups), 6, False)
        if not legal(state, 2):
            found = False
            for i, j in combinations(range(3), 2):
                for a in groups[i]:
                    for b in groups[j]:
                        if (xs[a] - xs[b]) % 5:
                            groups[i][groups[i].index(a)] = b
                            groups[j][groups[j].index(b)] = a
                            swaps.append([5, i, j, a, b])
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            assert found
        ops = entry(groups)
        u, v, w = groups
        labels = [u[:3], u[3:], v, w[:3], w[3:]]
    else:
        sizes = [9] + [6] * ((n - 9) // 6)
        groups, swaps = partition_by_sizes(xs, sizes,
                                          sorted(set(factors(n)) - {2, 3}))
        ops, labels = [], []
        for ids in groups:
            local = six_nine_network() if len(ids) == 9 else [list(range(6))]
            ops += [[ids[i] for i in atom] for atom in local]
            labels += [ids[i:i + 3] for i in range(0, len(ids), 3)]
    state = independent_replay(xs, ops, 6, False)
    quotient = [state[ids[0]] for ids in labels]
    assert all(all(state[i] == value for i in ids) for ids, value in zip(labels, quotient))
    assert legal(quotient, 2), (n, quotient, gap_gcd(quotient))
    denominator = lcm(*(x.denominator for x in quotient))
    solution = binary.solve([int(x * denominator) for x in quotient])
    assert solution["status"] == "solved", solution
    binary_ops = [[i - 1 for i in pair] for pair in solution["operations"]]
    independent_replay(quotient, binary_ops, 2)
    ops += lift_binary(6, labels, binary_ops)
    return ops, {"quotient_n": len(quotient), "swaps": swaps,
                 "binary_steps": len(binary_ops)}


def valuation(x, p):
    x = Fraction(x)
    if x == 0:
        return float("inf")
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def minimum_block(state, q, p):
    vals = [valuation(x, p) for x in state]
    low = min(vals)
    ids = [i for i, v in enumerate(vals) if v == low]
    assert len(ids) == q and len({state[i] for i in ids}) == 1
    return low, ids


def check_networks_and_lifts():
    cases = [(4, n) for n in (4, 8, 16, 32)]
    cases += [(6, n) for n in (6, 12, 18, 24, 36, 54, 72)]
    cases += [(10, 20), (12, 24), (12, 36), (18, 54)]
    basis_count = 0
    for q, n in cases:
        ops = tensor_network(q, n)
        for j in range(n):
            independent_replay([int(i == j) for i in range(n)], ops, q)
            basis_count += 1
    for j in range(9):
        independent_replay([int(i == j) for i in range(9)], six_nine_network(), 6)
        basis_count += 1
    for n in (27, 81):
        for j in range(n):
            independent_replay([int(i == j) for i in range(n)], six_threepower_network(n), 6)
            basis_count += 1
    lift_count = 0
    for q, copies in [(4, 2), (4, 8), (6, 3), (6, 9), (6, 27), (10, 5), (12, 18)]:
        labels = [list(range(i * copies, (i + 1) * copies)) for i in range(4)]
        for raw in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
                    (Fraction(-17, 13), Fraction(19, 7), 5, -11)]:
            ops = lift_binary(q, labels, [[0, 2], [1, 3], [0, 1], [2, 3]])
            original = [v for v in raw for _ in range(copies)]
            independent_replay(original, ops, q)
            lift_count += 1
    print("composite fixed tensor networks and duplicate lifts: PASS", basis_count, lift_count)


def check_traps():
    rng = Random(2026091204)
    large_prime_checks = 0
    for q, p, extra in [(6, 3, 2), (10, 5, 2), (10, 5, 3), (10, 5, 4), (14, 7, 3)]:
        state = list(map(Fraction, [-1] * q + [0] * (extra - 1) + [q]))
        assert gap_gcd(state) == 1
        for _ in range(15):
            low, ids = minimum_block(state, q, p)
            for chosen in combinations(range(len(state)), q):
                out = apply(state, chosen)
                newlow, _ = minimum_block(out, q, p)
                assert newlow == low if set(chosen) == set(ids) else newlow == low - factors(q)[p]
                large_prime_checks += 1
            state = apply(state, rng.sample(range(len(state)), q))
    state = list(map(Fraction, [-1] * 4 + [0, 4]))
    assert gap_gcd(state) == 1
    binary_checks = 0
    for _ in range(100):
        low, ids = minimum_block(state, 4, 2)
        outside = list(set(range(6)) - set(ids))
        for chosen in combinations(range(6), 4):
            out = apply(state, chosen)
            taken = len(set(chosen) & set(outside))
            if taken == 2:
                assert gap_gcd(out) == 3
            else:
                newlow, _ = minimum_block(out, 4, 2)
                assert newlow == low - 2 * taken
            binary_checks += 1
        state = apply(state, rng.sample(ids, 3) + [rng.choice(outside)])
    print("composite G1 counterexample invariant transitions: PASS", large_prime_checks, binary_checks)


def check_partitions_and_paths():
    rng = Random(46060912)
    repaired = 0
    # Deliberately bad equal-sum starting blocks force multi-prime repair.
    for q, n in [(4, 12), (4, 60), (6, 210), (10, 210), (12, 420)]:
        block, m, _ = reduction_shape(q, n)
        for _ in range(30):
            xs = []
            for _ in range(m):
                row = [rng.randrange(-30, 31) for _ in range(block - 1)]
                xs += row + [-sum(row)]
            xs = primitive_center(xs)
            if not legal(xs, q):
                continue
            groups, quotient, labels, swaps = good_partition(xs, q)
            assert sorted(i for ids in groups for i in ids) == list(range(n))
            assert legal(quotient, 2)
            repaired += len(swaps)
    cases = [(4, n) for n in (4, 8, 12, 16, 20, 24, 28, 40, 60, 84, 120)]
    cases += [(6, n) for n in (6, 12, 18, 24, 30, 36, 42, 54, 60, 72, 90, 126, 180)]
    cases += [(10, n) for n in (10, 30, 60, 70, 150)]
    cases += [(12, n) for n in (12, 36, 60, 84, 180)]
    records = []
    with BinarySolver() as binary:
        for q, n in cases:
            for _ in range(3):
                # Independent draws screened by the criterion, not inverse scrambling.
                while True:
                    raw = [rng.randrange(-25, 26) for _ in range(n)]
                    if legal(raw, q):
                        break
                ops, detail = construct(raw, q, binary)
                independent_replay(raw, ops, q)
                records.append({"q": q, "n": n, "input": raw,
                                "G": gap_gcd(raw), "steps": len(ops), **detail,
                                "operations": [[i + 1 for i in ids] for ids in ops]})
        # Explicit nonbinary G factors must disappear in the binary quotient.
        for n, k in [(30, 1), (90, 3), (60, 2)]:
            raw = [1] * (n - 2) + [1 + 3 * k, -(n - 1) - 3 * k]
            assert gap_gcd(raw) in (3, 6, 9)
            ops, detail = construct(raw, 6, binary)
            independent_replay(raw, ops, 6)
            records.append({"q": 6, "n": n, "input": raw, "G": gap_gcd(raw),
                            "steps": len(ops), **detail,
                            "operations": [[i + 1 for i in ids] for ids in ops]})
        for n in (9, 15, 21, 27, 33, 39, 45, 63, 81, 99, 105, 135, 315):
            for _ in range(4):
                while True:
                    raw = [rng.randrange(-25, 26) for _ in range(n)]
                    if legal(raw, 6):
                        break
                ops, detail = construct_six_odd(raw, binary)
                independent_replay(raw, ops, 6)
                records.append({"q": 6, "n": n, "input": raw,
                                "G": gap_gcd(raw), "steps": len(ops), **detail,
                                "operations": [[i + 1 for i in ids] for ids in ops]})
        for _ in range(25):
            raw = []
            for size, total in [(6, 1), (3, 3), (6, -4)]:
                row = [rng.randrange(-20, 21) for _ in range(size - 1)]
                raw += row + [total - sum(row)]
            assert legal(raw, 6)
            ops, detail = construct_six_odd(raw, binary)
            assert len(detail["swaps"]) == 1
            independent_replay(raw, ops, 6)
            records.append({"q": 6, "n": 15, "input": raw, "G": gap_gcd(raw),
                            "steps": len(ops), **detail,
                            "operations": [[i + 1 for i in ids] for ids in ops]})
        extra_cases = [(4, n) for n in (4, 8, 10, 14, 18, 22, 26, 30, 42, 66, 70, 90, 210)]
        extra_cases += [(6, n) for n in (6, 12, 15, 21, 33, 45, 63, 105, 315)]
        extra_cases += [(8, n) for n in (8, 16, 20, 28, 36, 60, 84)]
        extra_cases += [(10, n) for n in (10, 20, 35, 45, 55, 175, 225)]
        extra_cases += [(12, n) for n in (12, 24, 30, 42, 66, 90, 126)]
        for q, n in extra_cases:
            for _ in range(3):
                while True:
                    raw = [rng.randrange(-30, 31) for _ in range(n)]
                    if legal(raw, q):
                        break
                ops, detail = halfblock_construct(raw, q, binary)
                independent_replay(raw, ops, q)
                records.append({"q": q, "n": n, "input": raw, "G": gap_gcd(raw),
                                "steps": len(ops), **detail,
                                "operations": [[i + 1 for i in ids] for ids in ops]})
        # Independent bad-partition patterns for the final, general odd-quotient route.
        for q, count in [(4, 15), (4, 105), (6, 35), (8, 15), (10, 21)]:
            copies = q // 2
            sizes = [q, copies] + [q] * ((count - 3) // 2)
            for _ in range(5):
                raw = []
                for size in sizes:
                    row = [rng.randrange(-20, 21) for _ in range(size - 1)]
                    raw += row + [-sum(row)]
                assert legal(raw, q)
                ops, detail = halfblock_construct(raw, q, binary)
                assert detail["swaps"]
                independent_replay(raw, ops, q)
                records.append({"q": q, "n": len(raw), "input": raw,
                                "G": gap_gcd(raw), "steps": len(ops), **detail,
                                "operations": [[i + 1 for i in ids] for ids in ops]})
    target = Path(__file__).with_name("composite_arity_transfer_witnesses.json")
    target.write_text(json.dumps({"index_base": 1, "seed": 46060912,
                                 "scope": "finite interface and witness checks; general proofs are in the report",
                                 "cases": records}, indent=2) + "\n", encoding="utf-8")
    print("composite simultaneous repairs and literal full paths: PASS", repaired, len(records))
    print("composite witness steps:", min(r["steps"] for r in records), max(r["steps"] for r in records))


def main():
    check_networks_and_lifts()
    check_traps()
    check_partitions_and_paths()
    print("composite even-arity transfer and local obstructions: PASS")


if __name__ == "__main__":
    main()
