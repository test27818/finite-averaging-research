"""Exact checks for unequal ternary-power block compression."""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from random import Random


def primes_nonthree(value):
    result = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            if divisor != 3:
                result.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1 and value != 3:
        result.append(value)
    return result


def ternary_terms(value):
    terms = []
    power = 1
    while value:
        terms.extend([power] * (value % 3))
        value //= 3
        power *= 3
    return terms


def power_partition(value):
    primes = primes_nonthree(value)
    terms = ternary_terms(value)
    target = max(7, len(primes) + 1, len(terms))
    if target % 2 != value % 2:
        target += 1
    assert target <= value
    while len(terms) < target:
        position = next(i for i, term in enumerate(terms) if term > 1)
        term = terms.pop(position)
        terms.extend([term // 3] * 3)
    terms.sort(reverse=True)
    assert sum(terms) == value
    assert all(term > 0 and 3 ** round_log3(term) == term for term in terms)
    return terms


def round_log3(value):
    exponent = 0
    while value > 1:
        assert value % 3 == 0
        value //= 3
        exponent += 1
    return exponent


def block_averages_mod(values, blocks, prime):
    return [sum(values[index] for index in block) * pow(len(block), -1, prime) % prime
            for block in blocks]


def dangerous_edge(averages, weights, left, right, prime):
    others = [averages[index] for index in range(len(averages))
              if index not in (left, right)]
    if not others or len(set(others)) != 1:
        return False
    common = others[0]
    return (weights[left] * (averages[left] - common)
            + weights[right] * (averages[right] - common)) % prime == 0


def good_partition(values, weights):
    blocks = []
    offset = 0
    for weight in weights:
        blocks.append(list(range(offset, offset + weight)))
        offset += weight
    protected = []
    for prime in primes_nonthree(len(values)):
        averages = block_averages_mod(values, blocks, prime)
        if len(set(averages)) > 1:
            protected.append(prime)
            continue
        forbidden = set()
        for old in protected:
            old_averages = block_averages_mod(values, blocks, old)
            dangerous = [(i, j) for i, j in combinations(range(len(blocks)), 2)
                         if dangerous_edge(old_averages, weights, i, j, old)]
            assert len(dangerous) <= 1
            forbidden.update(dangerous)
        chosen = None
        for left, right in combinations(range(len(blocks)), 2):
            if (left, right) in forbidden:
                continue
            for i in blocks[left]:
                for j in blocks[right]:
                    if (values[i] - values[j]) % prime:
                        chosen = left, right, i, j
                        break
                if chosen:
                    break
            if chosen:
                break
        assert chosen is not None
        left, right, i, j = chosen
        left_offset = blocks[left].index(i)
        right_offset = blocks[right].index(j)
        blocks[left][left_offset], blocks[right][right_offset] = j, i
        assert len(set(block_averages_mod(values, blocks, prime))) > 1
        assert all(len(set(block_averages_mod(values, blocks, old))) > 1
                   for old in protected)
        protected.append(prime)
    return blocks


def average(values, indices):
    mean = sum((values[index] for index in indices), F(0)) / 3
    for index in indices:
        values[index] = mean


def equalize(values, indices):
    if len(indices) == 1:
        return 0
    third = len(indices) // 3
    chunks = [indices[offset * third:(offset + 1) * third] for offset in range(3)]
    operations = sum(equalize(values, chunk) for chunk in chunks)
    for offset in range(third):
        average(values, [chunk[offset] for chunk in chunks])
    return operations + third


def difference_gcd(values):
    denominator = 1
    for value in values:
        denominator = denominator * value.denominator // gcd(denominator, value.denominator)
    integers = [int(value * denominator) for value in values]
    content = gcd(*(abs(value) for value in integers))
    integers = [value // content for value in integers]
    return gcd(*(abs(value - integers[0]) for value in integers[1:]))


def check_dangerous_edges():
    """Check the dangerous-edge lemma on its actual quantifiers.

    A dangerous edge only constrains the two endpoints; every other
    average is the same residue.  For a pair of candidate edges, therefore,
    it is enough to enumerate the residues on their union and set all other
    positions to zero (translation by the common residue is harmless).  This
    avoids the old ``prime ** count`` enumeration and also tests repeated,
    arbitrarily ordered ternary-power weights rather than only
    ``1, 3, 9, ...``.
    """
    random = Random(20260909)
    checked = 0
    for count in range(5, 8):
        for prime in (2, 5, 7):
            exponent_vectors = [tuple(range(count)), tuple(reversed(range(count)))]
            exponent_vectors.extend(
                tuple(random.randrange(0, 8) for _ in range(count))
                for _ in range(4)
            )
            weight_vectors = {
                tuple(pow(3, exponent, prime) for exponent in exponents)
                for exponents in exponent_vectors
            }
            for weights in weight_vectors:
                for first, second in combinations(
                        combinations(range(count), 2), 2):
                    union = sorted(set(first) | set(second))
                    for residues in product(range(prime), repeat=len(union)):
                        averages = [0] * count
                        for index, residue in zip(union, residues):
                            averages[index] = residue
                        if len(set(averages)) == 1:
                            continue
                        first_bad = dangerous_edge(
                            averages, weights, *first, prime)
                        second_bad = dangerous_edge(
                            averages, weights, *second, prime)
                        if first_bad and second_bad:
                            assert len(set(averages)) == 1
                        checked += 1
    return checked


def check_random():
    random = Random(3991)
    checked = 0
    for n in list(range(7, 80)) + [91, 105, 210, 2310]:
        weights = power_partition(n)
        assert len(weights) >= 7
        assert len(weights) <= max(8, len(primes_nonthree(n)) + 2,
                                   2 * (round_log3(max(weights)) + 1))
        for _ in range(30):
            values = [random.randrange(-10**6, 10**6) for _ in range(n - 1)]
            values.append(-sum(values))
            content = gcd(*(abs(value) for value in values))
            if content:
                values = [value // content for value in values]
            if any(all((value - values[0]) % prime == 0 for value in values[1:])
                   for prime in primes_nonthree(n)):
                continue
            blocks = good_partition(values, weights)
            assert sorted(index for block in blocks for index in block) == list(range(n))
            state = list(map(F, values))
            operations = 0
            for block in blocks:
                operations += equalize(state, block)
                assert len({state[index] for index in block}) == 1
            expected = sum((round_log3(weight) * weight // 3 for weight in weights))
            assert operations == expected
            assert sum(state, F(0)) == 0
            output_g = difference_gcd(state)
            remainder = output_g
            while remainder % 3 == 0:
                remainder //= 3
            assert remainder == 1
            checked += 1
    return checked


if __name__ == "__main__":
    edge_checks = check_dangerous_edges()
    samples = check_random()
    print("unequal-weight dangerous-edge patterns", edge_checks, "PASS")
    print("power-block partitions and real network samples", samples, "PASS")
