"""Exact checks for the general-n ternary averaging synthesis."""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from random import Random


def primitive(values):
    divisor = gcd(*(abs(value) for value in values))
    if not divisor:
        return tuple(values)
    return tuple(value // divisor for value in values)


def difference_gcd(values):
    return gcd(*(abs(value - values[0]) for value in values[1:]))


def b_state(n, u, v):
    m = n - 4
    return (u,) * m + (v,) * 3 + (-m * u - 3 * v,)


def average(values, selected):
    selected = tuple(selected)
    mean = sum((values[index] for index in selected), F(0)) / 3
    result = list(values)
    for index in selected:
        result[index] = mean
    return tuple(result)


def equalize_power_of_three(values, indices, operations):
    if len(indices) == 1:
        return values
    third = len(indices) // 3
    chunks = [indices[offset * third:(offset + 1) * third] for offset in range(3)]
    for chunk in chunks:
        values = equalize_power_of_three(values, chunk, operations)
    for offset in range(third):
        selected = tuple(chunk[offset] for chunk in chunks)
        values = average(values, selected)
        operations.append(selected)
    return values


def good_prime_power_partition(values, m, r, prime):
    different = next(
        (pair for pair in combinations(range(len(values)), 2)
         if (values[pair[0]] - values[pair[1]]) % prime),
        None,
    )
    assert different is not None
    first, second = different
    unused = [index for index in range(len(values)) if index not in different]
    blocks = [[first], [second]] + [[] for _ in range(m - 2)]
    for block in blocks:
        while len(block) < r:
            block.append(unused.pop())
    assert not unused

    sums = [sum(values[index] for index in block) for block in blocks]
    if len({total % prime for total in sums}) == 1:
        blocks[0][0], blocks[1][0] = blocks[1][0], blocks[0][0]
        sums = [sum(values[index] for index in block) for block in blocks]
    assert len({total % prime for total in sums}) > 1
    return blocks, sums


def prime_divisors(value):
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        result.append(value)
    return tuple(result)


def block_sums(values, blocks):
    return [sum(values[index] for index in block) for block in blocks]


def good_simultaneous_partition(values, m, r):
    """Repair an equal-block partition one non-3 prime at a time."""
    blocks = [list(range(start, start + r)) for start in range(0, m * r, r)]
    protected = []
    for prime in (prime for prime in prime_divisors(m) if prime != 3):
        sums = block_sums(values, blocks)
        if len({total % prime for total in sums}) > 1:
            protected.append(prime)
            continue

        chosen = None
        for left, right in combinations(range(m), 2):
            for left_offset, left_index in enumerate(blocks[left]):
                for right_offset, right_index in enumerate(blocks[right]):
                    if (values[left_index] - values[right_index]) % prime == 0:
                        continue
                    trial = [block[:] for block in blocks]
                    trial[left][left_offset], trial[right][right_offset] = (
                        trial[right][right_offset], trial[left][left_offset]
                    )
                    trial_sums = block_sums(values, trial)
                    if all(len({total % old for total in trial_sums}) > 1
                           for old in protected):
                        chosen = trial
                        break
                if chosen is not None:
                    break
            if chosen is not None:
                break
        assert chosen is not None
        blocks = chosen
        protected.append(prime)

    sums = block_sums(values, blocks)
    assert all(len({total % prime for total in sums}) > 1
               for prime in protected)
    return blocks, sums


def dangerous_edges(sums, prime):
    result = []
    for left, right in combinations(range(len(sums)), 2):
        others = [sums[index] % prime for index in range(len(sums))
                  if index not in (left, right)]
        if (len(set(others)) == 1
                and (sums[left] + sums[right] - 2 * others[0]) % prime == 0):
            result.append((left, right))
    return result


def verify_dangerous_edge_lemma():
    checked = 0
    for m in range(5, 8):
        for prime in (2, 3, 5):
            for sums in product(range(prime), repeat=m):
                if len(set(sums)) == 1:
                    continue
                assert len(dangerous_edges(sums, prime)) <= 1
                checked += 1
    return checked


def verify_formulas():
    for n in range(5, 41):
        m = n - 4
        for u in range(-8, 9):
            for v in range(-8, 9):
                state = b_state(n, u, v)
                x, y = u, m * u + 4 * v
                assert 4 * sum(value * value for value in state) == (
                    m * n * x * x + 3 * y * y
                )

                if gcd(u, v) == 1:
                    assert difference_gcd(state) == gcd(abs(u - v), n)

                # Average the singleton together with two of the v entries.
                selected = (m, m + 1, n - 1)
                result = average(tuple(map(F, state)), selected)
                new_v = F(-m * u - v, 3)
                assert sorted(result) == sorted(b_state(n, F(u), new_v))
                new_x, new_y = F(u), F(-y, 3)
                assert new_y == m * new_x + 4 * new_v


def verify_networks():
    random = Random(308)
    for exponent in range(1, 5):
        size = 3 ** exponent
        values = tuple(F(random.randrange(-100, 101)) for _ in range(size))
        operations = []
        result = equalize_power_of_three(values, list(range(size)), operations)
        target = sum(values, F(0)) / size
        assert result == (target,) * size
        assert len(operations) == exponent * 3 ** (exponent - 1)


def verify_lifting_partitions():
    random = Random(783)
    for m, prime in ((7, 7), (8, 2)):
        for exponent in range(4):
            r = 3 ** exponent
            n = m * r
            for _ in range(200):
                values = [random.randrange(-10**6, 10**6) for _ in range(n - 1)]
                values.append(-sum(values))
                values = list(primitive(values))
                if not any(values) or difference_gcd(values) % prime == 0:
                    continue
                blocks, sums = good_prime_power_partition(values, m, r, prime)
                assert sorted(index for block in blocks for index in block) == list(range(n))
                assert all(len(block) == r for block in blocks)
                assert sum(sums) == 0
                compressed = primitive(sums)
                assert difference_gcd(compressed) == 1

                rational_values = tuple(map(F, values))
                operations = []
                for block in blocks:
                    rational_values = equalize_power_of_three(
                        rational_values, block, operations
                    )
                for block, total in zip(blocks, sums):
                    assert all(rational_values[index] == F(total, r) for index in block)

                if m >= 3:
                    chosen_blocks = (0, 1, 2)
                    compressed_mean = sum((F(sums[j], r) for j in chosen_blocks), F(0)) / 3
                    for offset in range(r):
                        selected = tuple(blocks[j][offset] for j in chosen_blocks)
                        rational_values = average(rational_values, selected)
                    for j in chosen_blocks:
                        assert all(
                            rational_values[index] == compressed_mean
                            for index in blocks[j]
                        )


def verify_simultaneous_partitions():
    random = Random(1010)
    checked = 0
    for m in (7, 8, 10, 14, 20, 35, 70):
        nonthree = tuple(prime for prime in prime_divisors(m) if prime != 3)
        for exponent in range(4):
            r = 3 ** exponent
            n = m * r
            for _ in range(40):
                values = [random.randrange(-10**6, 10**6) for _ in range(n - 1)]
                values.append(-sum(values))
                values = list(primitive(values))
                if not any(values):
                    continue
                if any(difference_gcd(values) % prime == 0 for prime in nonthree):
                    continue
                blocks, sums = good_simultaneous_partition(values, m, r)
                assert sorted(index for block in blocks for index in block) == list(range(n))
                assert all(len(block) == r for block in blocks)
                assert sum(sums) == 0
                compressed = primitive(sums)
                compressed_g = difference_gcd(compressed)
                assert all(compressed_g % prime for prime in nonthree)
                checked += 1
    return checked


def verify_ten_point_witness():
    state = tuple(map(F, (-10,) + (1,) * 8 + (2,)))
    assert not any(
        sum(state[index] for index in selected).denominator == 1
        and sum(state[index] for index in selected) % 3 == 0
        and len({state[index] for index in selected}) > 1
        for selected in combinations(range(10), 3)
    )

    # First enter B_10(3,-8), then create three zero coordinates.
    state = average(state, (0, 1, 2))
    assert sorted(state) == sorted(F(value, 3) for value in b_state(10, 3, -8))
    singleton = state.index(F(2))
    u_positions = [index for index, value in enumerate(state) if value == 1]
    state = average(state, (singleton, u_positions[0], u_positions[1]))
    four_positions = [index for index, value in enumerate(state) if value == F(4, 3)]
    minus_positions = [index for index, value in enumerate(state) if value == F(-8, 3)]
    state = average(state, (four_positions[0], four_positions[1], minus_positions[0]))
    assert state.count(F(0)) == 3

    distinguished_zero = state.index(F(0))
    remaining = [index for index in range(10) if index != distinguished_zero]
    operations = []
    state = equalize_power_of_three(state, remaining, operations)
    assert state == (F(0),) * 10
    assert len(operations) == 6


if __name__ == "__main__":
    verify_formulas()
    verify_networks()
    verify_lifting_partitions()
    simultaneous = verify_simultaneous_partitions()
    dangerous = verify_dangerous_edge_lemma()
    verify_ten_point_witness()
    print("general-n formulas and lifting theorem: PASS")
    print("checked n=5..40, ternary networks through 3^4, and 1,600 lift samples")
    print("blockwise simulation commutes with a compressed averaging step")
    print("simultaneous non-3-prime partition samples", simultaneous)
    print("dangerous-edge sum patterns", dangerous)
    print("ten-point no-integral-edge witness reaches zero in nine operations")
