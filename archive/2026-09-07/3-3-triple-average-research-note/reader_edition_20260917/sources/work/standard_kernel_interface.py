"""Executable certificate contract between compression and controllers."""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd
from itertools import combinations


def is_power_three(value):
    if type(value) is not int or value < 1:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def denominator_is_power_three(value):
    return is_power_three(F(value).denominator)


def nonthree_prime_divisors(value):
    if type(value) is not int or value < 1:
        raise ValueError("size must be a positive integer")
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
    return tuple(result)


def rational_mod(value, prime):
    value = F(value)
    if value.denominator % prime == 0:
        raise ValueError("denominator is not invertible modulo the prime")
    return value.numerator * pow(value.denominator, -1, prime) % prime


def state_key(state):
    return tuple(sorted((F(value), count) for value, count in state.items() if count))


def replay_value_word(start, operations):
    state = Counter(F(value) for value in start)
    for selected in operations:
        if len(selected) != 3:
            raise ValueError("every operation must select exactly three values")
        selected = tuple(map(F, selected))
        required = Counter(selected)
        if any(state[value] < count for value, count in required.items()):
            raise ValueError(f"operation lacks multiplicity: {selected}")
        mean = sum(selected, F(0)) / 3
        for value in selected:
            state[value] -= 1
            if state[value] == 0:
                del state[value]
        state[mean] += 3
    return +state


@dataclass(frozen=True)
class PowerBlockKernel:
    weights: tuple[int, ...]
    values: tuple[F, ...]

    def __post_init__(self):
        object.__setattr__(self, "values", tuple(map(F, self.values)))
        if len(self.weights) != len(self.values) or not self.weights:
            raise ValueError("weights and values must have the same positive length")
        if not all(is_power_three(weight) for weight in self.weights):
            raise ValueError("every block weight must be a power of three")
        if not all(denominator_is_power_three(value) for value in self.values):
            raise ValueError("block values may only have powers of three in denominators")
        if sum(
            weight * value for weight, value in zip(self.weights, self.values)
        ) != 0:
            raise ValueError("kernel must satisfy weighted zero sum")

    @property
    def size(self):
        return sum(self.weights)

    def expanded_state(self):
        state = Counter()
        for weight, value in zip(self.weights, self.values):
            state[value] += weight
        return +state

    def local_witnesses(self):
        if not any(self.values):
            return {}
        witnesses = {}
        for prime in nonthree_prime_divisors(self.size):
            residues = [rational_mod(value, prime) for value in self.values]
            pair = next(
                (
                    (left, right)
                    for left in range(len(residues))
                    for right in range(left + 1, len(residues))
                    if residues[left] != residues[right]
                ),
                None,
            )
            if pair is None:
                raise ValueError(f"kernel loses the local witness modulo {prime}")
            witnesses[prime] = pair
        return witnesses


@dataclass(frozen=True)
class KernelInterfaceCertificate:
    source: tuple[F, ...]
    operations: tuple[tuple[F, F, F], ...]
    kernel: PowerBlockKernel

    def verify(self):
        source = tuple(map(F, self.source))
        if len(source) != self.kernel.size or sum(source, F(0)) != 0:
            raise ValueError("source size or zero-sum condition is invalid")
        if not all(denominator_is_power_three(value) for value in source):
            raise ValueError("source must lie in Z[1/3]")
        result = replay_value_word(source, self.operations)
        if state_key(result) != state_key(self.kernel.expanded_state()):
            raise ValueError("operation word does not produce the declared kernel")
        witnesses = self.kernel.local_witnesses()
        return {
            "size": self.kernel.size,
            "blocks": len(self.kernel.weights),
            "operations": len(self.operations),
            "local_witnesses": witnesses,
        }


@dataclass(frozen=True)
class TerminalPartitionCertificate:
    state: tuple[tuple[F, int], ...]
    blocks: tuple[tuple[tuple[F, int], ...], ...]

    def verify(self):
        state = Counter()
        for value, count in self.state:
            if type(count) is not int or count <= 0:
                raise ValueError("state multiplicities must be positive integers")
            state[F(value)] += count
        used = Counter()
        sizes = []
        for block in self.blocks:
            block_counter = Counter()
            for value, count in block:
                if type(count) is not int or count <= 0:
                    raise ValueError("block multiplicities must be positive integers")
                block_counter[F(value)] += count
            size = sum(block_counter.values())
            if not is_power_three(size):
                raise ValueError("terminal block size is not a power of three")
            if sum(value * count for value, count in block_counter.items()) != 0:
                raise ValueError("terminal block is not zero sum")
            sizes.append(size)
            used.update(block_counter)
        if used != state:
            raise ValueError("terminal blocks do not partition the state")
        return tuple(sorted(sizes))


def safe_equal_weight_carry(kernel):
    """Return (output kernel, value word) using cached exceptional sets.

    None means this selector found no equal-weight triple. It is not an
    obstruction to other averaging paths. The proof applies with t >= 7.
    """
    t = len(kernel.weights)
    if t < 7:
        return None
    kernel.local_witnesses()
    forbidden_supports = []
    for prime in nonthree_prime_divisors(kernel.size):
        residues = [rational_mod(value, prime) for value in kernel.values]
        common, multiplicity = Counter(residues).most_common(1)[0]
        if multiplicity >= t - 3:
            support = frozenset(i for i, residue in enumerate(residues)
                                if residue != common)
            if support:
                forbidden_supports.append(support)
    groups = {}
    for index, weight in enumerate(kernel.weights):
        groups.setdefault(weight, []).append(index)
    for weight, indices in groups.items():
        for selected in combinations(indices, 3):
            selected_set = frozenset(selected)
            if any(support <= selected_set for support in forbidden_supports):
                continue
            triple = tuple(kernel.values[index] for index in selected)
            new_weights = tuple(w for i, w in enumerate(kernel.weights)
                                if i not in selected_set) + (3 * weight,)
            new_values = tuple(v for i, v in enumerate(kernel.values)
                               if i not in selected_set) + (sum(triple, F(0))/3,)
            output = PowerBlockKernel(new_weights, new_values)
            output.local_witnesses()
            return output, (triple,) * weight
    return None
