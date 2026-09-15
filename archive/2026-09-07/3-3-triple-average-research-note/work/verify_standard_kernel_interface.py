"""Exact regression checks for the executable standard-kernel interface."""

from fractions import Fraction as F
from math import gcd
from random import Random

from standard_kernel_interface import (
    KernelInterfaceCertificate,
    PowerBlockKernel,
    TerminalPartitionCertificate,
    nonthree_prime_divisors,
    replay_value_word,
    safe_equal_weight_carry,
)
from verify_power_partition_compression import (
    good_partition,
    power_partition,
)


def equalize_with_word(state, indices, operations):
    if len(indices) == 1:
        return
    third = len(indices) // 3
    chunks = [indices[offset * third:(offset + 1) * third] for offset in range(3)]
    for chunk in chunks:
        equalize_with_word(state, chunk, operations)
    for offset in range(third):
        selected_indices = [chunk[offset] for chunk in chunks]
        selected = tuple(state[index] for index in selected_indices)
        operations.append(selected)
        mean = sum(selected, F(0)) / 3
        for index in selected_indices:
            state[index] = mean


def primitive_zero_sum(random, n):
    values = [random.randrange(-10**5, 10**5) for _ in range(n - 1)]
    values.append(-sum(values))
    content = gcd(*(abs(value) for value in values))
    if content:
        values = [value // content for value in values]
    return values


def verify():
    random = Random(120915)
    checked = 0
    for n in list(range(7, 50)) + [91, 105, 210]:
        weights = power_partition(n)
        for _ in range(5):
            source = primitive_zero_sum(random, n)
            if any(
                all((value - source[0]) % prime == 0 for value in source[1:])
                for prime in nonthree_prime_divisors(n)
            ):
                continue
            blocks = good_partition(source, weights)
            state = list(map(F, source))
            operations = []
            values = []
            for block in blocks:
                equalize_with_word(state, block, operations)
                values.append(state[block[0]])
                assert all(state[index] == values[-1] for index in block)
            kernel = PowerBlockKernel(tuple(weights), tuple(values))
            certificate = KernelInterfaceCertificate(
                tuple(map(F, source)), tuple(operations), kernel
            )
            summary = certificate.verify()
            assert summary["blocks"] == len(weights)
            assert summary["operations"] == sum(
                _power_exponent(weight) * weight // 3 for weight in weights
            )
            checked += 1
    return checked


def verify_parser_failures():
    # Repeated entries represent separate copies, not an overwrite.
    duplicated = ((F(-1), 1), (F(-1), 1), (F(2), 1))
    certificate = TerminalPartitionCertificate(duplicated, (duplicated,))
    assert certificate.verify() == (3,)
    invalid = [
        lambda: TerminalPartitionCertificate(((0, 0),), ()).verify(),
        lambda: TerminalPartitionCertificate(((0, True),), ()).verify(),
        lambda: TerminalPartitionCertificate(((0, 3),), (((0, -1), (0, 4)),)).verify(),
        lambda: TerminalPartitionCertificate(((0, 3),), (((0, 2),),)).verify(),
        lambda: TerminalPartitionCertificate(((1, 3),), (((1, 3),),)).verify(),
        lambda: TerminalPartitionCertificate(((0, 3),), (((0, 9),),)).verify(),
        lambda: PowerBlockKernel((F(3, 2),), (F(0),)),
        lambda: replay_value_word((0, 1, -1), ((1, 1, -1),)),
        lambda: PowerBlockKernel((3, 3, 1), (1, 1, -6)).local_witnesses(),
    ]
    for case in invalid:
        try:
            case()
        except ValueError:
            pass
        else:
            raise AssertionError("malformed certificate was accepted")
    zero = PowerBlockKernel((3, 3, 1), (0, 0, 0))
    assert KernelInterfaceCertificate((F(0),) * 7, (), zero).verify()["operations"] == 0
    return len(invalid)


def verify_carry_interface():
    checked = 0
    for weight in (1, 3, 9, 27):
        source_kernel = PowerBlockKernel(
            (weight,) * 7, (F(-2), F(-1), F(-1), F(1), F(1), F(1), F(1))
        )
        output, operations = safe_equal_weight_carry(source_kernel)
        source = tuple(source_kernel.expanded_state().elements())
        summary = KernelInterfaceCertificate(source, operations, output).verify()
        assert summary["blocks"] == 5
        assert summary["operations"] == weight
        checked += 1
    print("safe carry concrete interface replay: PASS", checked)


def _power_exponent(value):
    exponent = 0
    while value > 1:
        assert value % 3 == 0
        value //= 3
        exponent += 1
    return exponent


if __name__ == "__main__":
    print("interface malformed certificate rejection: PASS", verify_parser_failures())
    print("standard kernel interface certificates: PASS", verify())
    verify_carry_interface()
