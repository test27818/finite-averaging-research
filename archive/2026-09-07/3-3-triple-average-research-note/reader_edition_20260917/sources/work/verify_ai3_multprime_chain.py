"""Exact checks for multi-prime weighted-kernel coupling macros.

This file only checks finite instances of the algebraic claims in
``outputs/triple_average/history/ai3_multprime_chain_report.md``.  It does not search for a
terminating controller for arbitrary weighted kernels.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from random import Random


def is_power_three(value):
    return value > 0 and (lambda x: x == 1)(
        _strip_three(value)
    )


def _strip_three(value):
    while value % 3 == 0:
        value //= 3
    return value


def mod_fraction(value, prime):
    value = F(value)
    assert value.denominator % prime
    return value.numerator * pow(value.denominator, -1, prime) % prime


def nonthree_primes(value):
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


def average(state, indices):
    mean = sum((state[index] for index in indices), F(0)) / 3
    for index in indices:
        state[index] = mean


def expand_tree(state, seed, available, target_size):
    """Expand one seed to ``target_size`` positions by real ternary means."""
    block = [seed]
    while len(block) < target_size:
        following = []
        for position in block:
            fresh = available[-2:]
            del available[-2:]
            average(state, [position] + fresh)
            following.extend((position, fresh[0], fresh[1]))
        block = following
    return block


def weighted_sum(weights, values):
    return sum((F(weight) * F(value)
                for weight, value in zip(weights, values)), F(0))


def exchange_blocks(weights, values, large, small):
    """Algebraic block exchange, with the larger block first.

    If R = s*q, the real macro sends (u,v) to
    (((s-1)u+v)/s, u).  The returned block weights are unchanged.
    """
    assert weights[large] > weights[small]
    ratio = weights[large] // weights[small]
    assert weights[large] == ratio * weights[small]
    assert is_power_three(ratio)
    output = list(map(F, values))
    output[large] = (F(ratio - 1) * output[large] + output[small]) / ratio
    output[small] = F(values[large])
    return tuple(output)


def real_exchange(weights, values, large, small):
    """Replay the same exchange with position-level multiplicity ledger."""
    weights = list(weights)
    values = list(map(F, values))
    ratio = weights[large] // weights[small]
    assert ratio * weights[small] == weights[large]
    assert is_power_three(ratio)
    blocks = []
    state = []
    for weight, value in zip(weights, values):
        block = list(range(len(state), len(state) + weight))
        state.extend([value] * weight)
        blocks.append(block)
    large_positions = blocks[large]
    small_positions = blocks[small]
    retained = large_positions[:weights[small]]
    available = large_positions[weights[small]:]
    outputs = []
    operations = 0
    for seed in small_positions:
        before = len(available)
        outputs.extend(expand_tree(state, seed, available, ratio))
        operations += (before - len(available)) // 2
    assert not available
    old_large = values[large]
    old_small = values[small]
    target = (F(ratio - 1) * old_large + old_small) / ratio
    assert all(state[index] == target for index in outputs)
    assert all(state[index] == old_large for index in retained)
    assert len(outputs) == weights[large]
    assert len(retained) == weights[small]
    result = list(values)
    result[large] = target
    result[small] = old_large
    assert weighted_sum(weights, values) == weighted_sum(weights, result)
    return tuple(result), operations


def carrier_exchange(weights, values, singleton, block):
    """Real singleton/r-block exchange and its difference-coordinate formula."""
    assert weights[singleton] == 1
    assert weights[block] > 1 and is_power_three(weights[block])
    r = weights[block]
    weights = list(weights)
    values = list(map(F, values))
    blocks = []
    state = []
    for weight, value in zip(weights, values):
        positions = list(range(len(state), len(state) + weight))
        blocks.append(positions)
        state.extend([value] * weight)
    seed = blocks[singleton][0]
    available = blocks[block][:-1]
    outputs = expand_tree(state, seed, available, r)
    assert not available
    old_w = values[singleton]
    old_u = values[block]
    target = (old_w + F(r - 1) * old_u) / r
    assert all(state[index] == target for index in outputs)
    assert state[blocks[block][-1]] == old_u
    result = list(values)
    result[singleton] = old_u
    result[block] = target
    d = old_u - old_w
    assert result[block] - result[singleton] == -d / r
    assert weighted_sum(weights, values) == weighted_sum(weights, result)
    return tuple(result), (r - 1) // 2


def merge_equal_blocks(weights, values, selected):
    """Algebraic result of a real equal-weight carry of three blocks."""
    selected = tuple(selected)
    assert len(selected) == 3
    r = weights[selected[0]]
    assert all(weights[index] == r for index in selected)
    mean = sum((F(values[index]) for index in selected), F(0)) / 3
    output_weights = [weight for index, weight in enumerate(weights)
                      if index not in selected] + [3 * r]
    output_values = [F(value) for index, value in enumerate(values)
                     if index not in selected] + [mean]
    return tuple(output_weights), tuple(output_values), r


def real_merge_equal_blocks(weights, values, selected):
    """Position-level ledger for the equal-weight carry."""
    selected = tuple(selected)
    r = weights[selected[0]]
    assert all(weights[index] == r for index in selected)
    blocks = []
    state = []
    for weight, value in zip(weights, values):
        block = list(range(len(state), len(state) + weight))
        blocks.append(block)
        state.extend([F(value)] * weight)
    for offset in range(r):
        average(state, [blocks[index][offset] for index in selected])
    output_values = [F(value) for index, value in enumerate(values)
                     if index not in selected]
    output_values.append(state[blocks[selected[0]][0]])
    output_weights = [weight for index, weight in enumerate(weights)
                      if index not in selected] + [3 * r]
    assert all(state[blocks[selected[0]][offset]] == output_values[-1]
               for offset in range(r))
    assert weighted_sum(weights, values) == weighted_sum(output_weights,
                                                          output_values)
    return tuple(output_weights), tuple(output_values), r


def witness(values, prime):
    return len({mod_fraction(value, prime) for value in values}) > 1


def merge_safe_condition(weights, values, selected, prime):
    out_weights, out_values, _ = merge_equal_blocks(weights, values, selected)
    del out_weights
    return witness(out_values, prime)


def chain_sums(weights, values, chains):
    return tuple(sum((F(weights[index]) * F(values[index])
                      for index in chain), F(0))
                 for chain in chains)


def transfer_delta(weights, values, large, small, large_chain, small_chain):
    assert large_chain != small_chain
    q = F(weights[small])
    delta = q * (F(values[small]) - F(values[large]))
    return delta if large_chain < small_chain else -delta


def check_real_ledgers():
    cases = [
        ((9, 3, 1), (F(1), F(-2), F(-3))),
        ((27, 9, 3, 1), (F(5), F(-4), F(1), F(-102))),
        ((81, 9, 1), (F(2), F(-7), F(-99))),
    ]
    checked = 0
    for weights, values in cases:
        assert weighted_sum(weights, values) == 0
        for large, small in combinations(range(len(weights)), 2):
            if weights[large] < weights[small]:
                large, small = small, large
            if weights[large] == weights[small]:
                continue
            output, operations = real_exchange(weights, values, large, small)
            assert operations == (weights[large] - weights[small]) // 2
            assert output == exchange_blocks(weights, values, large, small)
            checked += 1
        if 1 in weights:
            singleton = weights.index(1)
            for block, weight in enumerate(weights):
                if weight == 1:
                    continue
                output, operations = carrier_exchange(weights, values,
                                                       singleton, block)
                assert operations == (weight - 1) // 2
                checked += 1
    return checked


def check_mult_prime_witness_preservation():
    random = Random(20260909)
    checked = 0
    weight_vectors = [
        (27, 9, 3, 1, 1, 1, 1),
        (81, 27, 9, 3, 1, 1, 1),
        (9, 9, 3, 3, 1, 1, 1, 1),
    ]
    for weights in weight_vectors:
        n = sum(weights)
        primes = nonthree_primes(n)
        for _ in range(500):
            values = tuple(F(random.randrange(-1000, 1001)) for _ in weights)
            total = weighted_sum(weights, values)
            # Move the last block to the weighted zero-sum hyperplane.
            values = list(values)
            values[-1] -= total / weights[-1]
            values = tuple(values)
            for prime in primes:
                if not witness(values, prime):
                    continue
                for large, small in combinations(range(len(weights)), 2):
                    if weights[large] < weights[small]:
                        large, small = small, large
                    if weights[large] == weights[small]:
                        continue
                    output = exchange_blocks(weights, values, large, small)
                    assert witness(output, prime)
                    checked += 1
                if 1 in weights:
                    singleton = weights.index(1)
                    for block, weight in enumerate(weights):
                        if weight == 1:
                            continue
                        output, _ = carrier_exchange(weights, values,
                                                     singleton, block)
                        assert witness(output, prime)
                        checked += 1
    return checked


def check_merge_criterion_and_counterexample():
    # Exhaustive residue check for the exact criterion on small weights.
    checked = 0
    weights = (1, 1, 1, 1, 1, 1, 1)
    selected = (0, 1, 2)
    for residues in product(range(7), repeat=len(weights)):
        if not witness(residues, 7):
            continue
        out_weights, out_values, _ = merge_equal_blocks(weights, residues,
                                                         selected)
        expected = witness(out_values, 7)
        assert expected == merge_safe_condition(weights, residues, selected, 7)
        checked += 1

    # A legal G=1 integer state whose equal carry destroys the p=7 witness.
    values = (F(1), F(1), F(5), F(0), F(0), F(0), F(-7))
    assert sum(values, F(0)) == 0
    assert witness(values, 7)
    out_weights, out_values, _ = real_merge_equal_blocks(weights, values,
                                                          selected)
    assert not witness(out_values, 7)
    scaled = [int(value * 3) for value in out_values]
    assert gcd(*(abs(value - scaled[0]) for value in scaled[1:])) == 7
    return checked


def check_chain_transfer():
    weights = (27, 9, 3, 1)
    values = (F(5), F(-4), F(1), F(-102))
    chains = ((0, 1), (2, 3))
    before = chain_sums(weights, values, chains)
    for large, small in ((0, 2), (1, 3), (0, 3)):
        output = exchange_blocks(weights, values, large, small)
        after = chain_sums(weights, output, chains)
        delta = transfer_delta(weights, values, large, small,
                               0 if large in chains[0] else 1,
                               0 if small in chains[0] else 1)
        assert after[0] - before[0] == delta
        assert after[1] - before[1] == -delta
        assert sum(after, F(0)) == 0
    # General chain-square potential identity.
    checked = 0
    random = Random(917)
    for _ in range(1000):
        sums = [F(random.randrange(-20, 21)) for _ in range(4)]
        a, b = 0, 1
        delta = F(random.randrange(-10, 11))
        old = sum(value * value for value in sums)
        new = old + 2 * delta * (sums[a] - sums[b]) + 2 * delta * delta
        changed = list(sums)
        changed[a] += delta
        changed[b] -= delta
        assert new == sum(value * value for value in changed)
        checked += 1
    return checked


if __name__ == "__main__":
    ledgers = check_real_ledgers()
    witnesses = check_mult_prime_witness_preservation()
    merges = check_merge_criterion_and_counterexample()
    transfers = check_chain_transfer()
    print("real exchange/carrier ledgers: PASS", ledgers)
    print("simultaneous p!=3 witness preservation: PASS", witnesses)
    print("equal-carry safety criterion and p=7 counterexample: PASS", merges)
    print("chain-sum transfer identities and potential: PASS", transfers)
