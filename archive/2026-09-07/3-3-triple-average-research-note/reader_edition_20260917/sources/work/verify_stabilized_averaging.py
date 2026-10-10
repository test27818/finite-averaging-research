"""Exact checks for uniform-replication stabilization and its limitations."""

from fractions import Fraction
from math import gcd
from random import Random


def bezout_pair(a, b):
    old_r, r = abs(a), abs(b)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s * (1 if a >= 0 else -1), old_t * (1 if b >= 0 else -1)


def bezout_list(values):
    common = 0
    coefficients = []
    for value in values:
        new_common, left, right = bezout_pair(common, value)
        coefficients = [left * c for c in coefficients] + [right]
        common = new_common
    assert sum(c * v for c, v in zip(coefficients, values)) == common
    return common, coefficients


def primitive(values):
    common = gcd(*values)
    return tuple(v // common for v in values) if common else tuple(values)


def gap_gcd(values):
    return gcd(*(v - values[0] for v in values[1:]))


def supported_by_arity(g, arity):
    while g > 1:
        factor = gcd(g, arity)
        if factor == 1:
            return False
        g //= factor
    return g == 1


def construct(values, arity=3):
    x = primitive(values)
    n = len(x)
    assert n >= 2 and sum(x) == 0 and any(x)
    g, coefficients = bezout_list([v - x[0] for v in x[1:]])
    assert n % g == 0
    if not supported_by_arity(g, arity):
        raise ValueError("Non-arity prime in the primitive difference gcd")

    a = [-sum(coefficients)] + coefficients
    b = [-x[0] * c for c in a]
    b[0] += g
    assert sum(b) == g and sum(v * c for v, c in zip(x, b)) == 0

    bound_b = max(map(abs, b))
    bound_c = (n - 1) * (n // g) * bound_b
    replication, depth = 1, 0
    while replication < n * (bound_c + 1) or replication % g:
        replication *= arity
        depth += 1
    q, remainder = divmod(replication, n)
    assert remainder % g == 0
    row = [q + (remainder // g) * v for v in b]
    last = [replication - (n - 1) * v for v in row]
    matrix = [tuple(row)] * (n - 1) + [tuple(last)]
    verify_matrix(x, replication, matrix)
    return replication, depth, matrix


def verify_matrix(x, replication, matrix):
    n = len(x)
    assert len(matrix) == n
    for row in matrix:
        assert len(row) == n and all(v > 0 for v in row)
        assert sum(row) == replication
        assert sum(a * b for a, b in zip(row, x)) == 0
    assert all(sum(row[j] for row in matrix) == replication for j in range(n))


def replay_partition(x, replication, matrix):
    assert replication > 0
    depth, scale = 0, replication
    while scale > 1:
        assert scale % 3 == 0
        scale //= 3
        depth += 1
    buckets = [[i for _ in range(replication)] for i in range(len(x))]
    operations = 0
    for row in matrix:
        block = []
        for j, count in enumerate(row):
            for _ in range(count):
                block.append(Fraction(x[buckets[j].pop()]))
        stride = 1
        for _ in range(depth):
            for base in range(0, replication, 3 * stride):
                for offset in range(stride):
                    indices = [base + offset + k * stride for k in range(3)]
                    mean = sum(block[i] for i in indices) / 3
                    for i in indices:
                        block[i] = mean
                    operations += 1
            stride *= 3
        assert all(v == 0 for v in block)
    assert all(not bucket for bucket in buckets)
    assert operations == len(x) * depth * replication // 3
    return operations


def verify_lower_bound():
    checked = 0
    for n in (5, 7, 8, 10, 11, 13, 14, 16):
        for multiple in range(1, 41):
            h = n * multiple
            x = (-h, h - n + 2) + (1,) * (n - 2)
            assert sum(x) == 0 and gap_gcd(x) == 1
            r = 1
            while (n - 1) * r < h + 1:
                for a in range(r + 1):
                    for b in range(r - a + 1):
                        c = r - a - b
                        assert -h * a + (h - n + 2) * b + c != 0
                checked += 1
                r *= 3
    return checked


def verify_corrections():
    support_input = (-7, 1, 1, 1, 1, 1, 2)
    support_output_primitive = (-4, -4, -4, 3, 3, 3, 3)
    assert gap_gcd(support_input) == 1
    assert gap_gcd(support_output_primitive) == 7

    reset_input = (3, 3, 3, 3, 3, 1, -16)
    assert sum(reset_input) == 0 and gap_gcd(reset_input) == 1
    reset_output = (3, 3, 3, 3, -4, -4, -4)
    assert sum(reset_output) == 0 and gap_gcd(reset_output) == 7
    shifted_quotient = (0, 0, 0, 0, -1, -1, -1)
    assert tuple(7 * v + 3 for v in shifted_quotient) == reset_output
    assert Fraction(sum(shifted_quotient), 7) == Fraction(-3, 7)

    def energy(u, v):
        return 9 * u * u + 3 * v * v + (-9 * u - 3 * v) ** 2

    for u in range(-10, 11):
        for v in range(-10, 11):
            out_u = -Fraction(u, 3) - Fraction(v, 9)
            assert energy(out_u, u) == (
                energy(u, v) / Fraction(3) - Fraction(26, 9) * (3 * u + v) ** 2
            )
            assert 4 * energy(u, v) == 117 * u * u + 3 * (9 * u + 4 * v) ** 2


def verify_tripled_counterexamples():
    for base in ((-3, 0, 1, 1, 1), (-3, 0, 0, 1, 1, 1)):
        state = list(base) * 3

        def average(selected):
            for value in selected:
                state.remove(value)
            mean = Fraction(sum(selected), 3)
            state.extend([mean] * 3)

        average((-3, 0, 0))
        for _ in range(3):
            average((-1, 0, 1))
        nonzero = [int(v) for v in state if v]
        assert sorted(nonzero) == [-3, -3] + [1] * 6
        block = nonzero + [0]
        for stride in (1, 3):
            for start in range(0, 9, 3 * stride):
                for offset in range(stride):
                    indices = [start + offset + j * stride for j in range(3)]
                    average(tuple(block[i] for i in indices))
                    mean = sum(block[i] for i in indices) / Fraction(3)
                    for i in indices:
                        block[i] = mean
        assert len(state) == 3 * len(base) and all(v == 0 for v in state)


def main():
    random = Random(20260909)
    checked, max_replication_bits = 0, 0
    for arity in (2, 3, 4, 6):
        for n in range(2, 31):
            for _ in range(20):
                x = [random.randrange(-10000, 10001) for _ in range(n - 1)]
                x.append(-sum(x))
                x = primitive(x)
                if not any(x):
                    continue
                if not supported_by_arity(gap_gcd(x), arity):
                    try:
                        construct(x, arity)
                    except ValueError:
                        continue
                    raise AssertionError("Inadmissible input accepted")
                replication, _, _ = construct(x, arity)
                max_replication_bits = max(max_replication_bits, replication.bit_length())
                checked += 1

    for n in range(2, 81):
        for r in range(1, n):
            common = gcd(r, n)
            block_size = n // common
            a, b = (n - r) // common, -r // common
            x = (a,) * r + (b,) * (n - r)
            assert gap_gcd(x) == block_size
            if supported_by_arity(block_size, 3):
                assert (r // common) * a + ((n - r) // common) * b == 0

    counterexample = (-3, 0, 1, 1, 1)
    explicit_matrix = [(2, 1, 2, 2, 2)] * 4 + [(1, 5, 1, 1, 1)]
    verify_matrix(counterexample, 9, explicit_matrix)
    operations = replay_partition(counterexample, 9, explicit_matrix)
    lower_bound_cases = verify_lower_bound()
    verify_corrections()
    verify_tripled_counterexamples()
    print("stabilized matrix checks:", checked, "PASS")
    print("maximum replication bit length in checks:", max_replication_bits)
    print("five-point example: 9 replicas, 45 positions,", operations, "operations PASS")
    print("explicit lower-bound exclusions:", lower_bound_cases, "PASS")
    print("tripled five- and six-point counterexamples: 10 operations each PASS")
    print("two-value criterion and correction checks: PASS")


if __name__ == "__main__":
    main()
