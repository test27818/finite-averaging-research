"""Exact identities for the formal equal-carrier zero-leaf theorem.

Formal inverses are explicit in this file.  The checks prove algebraic
interfaces used by the accompanying theorem; they do not turn those inverses
into positive triple-average words.
"""

from fractions import Fraction as F
from math import gcd


def identity(size):
    return [[F(row == column) for column in range(size)]
            for row in range(size)]


def multiply(left, right):
    return [[sum(left[row][index] * right[index][column]
                 for index in range(len(right)))
             for column in range(len(right[0]))]
            for row in range(len(left))]


def product(*matrices):
    result = identity(len(matrices[0]))
    for matrix in reversed(matrices):
        result = multiply(matrix, result)
    return result


def inverse(matrix):
    size = len(matrix)
    work = [list(map(F, row)) + unit
            for row, unit in zip(matrix, identity(size))]
    for column in range(size):
        pivot = next(row for row in range(column, size)
                     if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(size):
            if row == column:
                continue
            value = work[row][column]
            work[row] = [left - value * right
                         for left, right in zip(work[row], work[column])]
    return [row[size:] for row in work]


def commutator(left, right):
    return product(left, right, inverse(left), inverse(right))


def rank_one(center, covector, coefficient=1):
    size = len(center)
    return [[F(row == column)
             + coefficient * center[row] * covector[column]
             for column in range(size)] for row in range(size)]


def equal_carrier_exchange(rank, index):
    result = identity(rank)
    result[index] = [F(-2, 3) if column == index else F(-1)
                     for column in range(rank)]
    return result


def verify_balanced_shears():
    checked = 0
    for rank in range(5, 13):
        for i, j, k, ell in ((0, 1, 2, 3),
                             (rank - 1, rank - 2, 0, 1)):
            si, sj, sk, sell = (equal_carrier_exchange(rank, index)
                                for index in (i, j, k, ell))
            first = product(si, sj, inverse(si))
            second = product(sj, si, inverse(sj))
            root = product(first, inverse(second))

            center = [F(index == j) - F(index == i)
                      for index in range(rank)]
            covector = [F(1) + F(1, 3) * (int(index == i)
                                           + int(index == j))
                        for index in range(rank)]
            assert root == rank_one(center, covector)

            balanced = product(commutator(root, sk),
                               inverse(commutator(root, sell)))
            source = [F(index == k) - F(index == ell)
                      for index in range(rank)]
            assert balanced == rank_one(center, source)

            row_shear = commutator(si, balanced)
            unit = [F(index == i) for index in range(rank)]
            assert row_shear == rank_one(unit, source, F(2, 3))
            integral = product(inverse(si), row_shear, si)
            assert integral == rank_one(unit, source, -1)
            checked += 1
    print("equal-carrier integral balanced shears: PASS", checked)


def verify_q_basis_interface():
    checked = 0
    for rank in range(5, 13):
        dimension = rank - 1
        q = identity(rank)
        for row in range(dimension):
            q[row][-1] = 1
        q_inverse = inverse(q)
        for i, k in ((0, 1), (dimension - 1, 0)):
            source = [F(index == k) - F(index == rank - 1)
                      for index in range(rank)]
            center = [F(index == i) for index in range(rank)]
            shear = rank_one(center, source, -1)
            transformed = product(q_inverse, shear, q)
            expected = identity(rank)
            expected[i][k] -= 1
            assert transformed == expected

        last = product(q_inverse,
                       equal_carrier_exchange(rank, rank - 1), q)
        n = 3 * rank + 2
        expected = identity(rank)
        for row in range(dimension):
            for column in range(dimension):
                expected[row][column] += 1
            expected[row][-1] = F(n, 3)
        expected[-1] = [F(-1)] * dimension + [F(3 - n, 3)]
        assert last == expected
        checked += 1
    print("equal-carrier Q-basis and SL block interface: PASS", checked)


def verify_prime_gcd_step():
    checked = 0
    primes = (17, 23, 29, 41, 47, 53, 59, 71, 83, 89, 101, 107)
    for prime in primes:
        rank = (prime - 2) // 3
        assert 3 * rank + 2 == prime
        for g in range(1, 3 * prime + 1):
            if g % prime == 0:
                continue
            for t in range(-prime, prime + 1):
                tail = 3 * g + prime * t
                first = 6 * g + prime * t
                new_t = -3 * g + (3 - prime) * t
                divisor = gcd(abs(first), abs(tail))
                assert divisor == gcd(3 * g, prime * t)
                assert new_t % divisor == 0
                checked += 1
    print("prime formal SL-exchange-SL gcd step: PASS", checked)
    print("equal-carrier formal zero-leaf theorem: PASS")


def verify():
    verify_balanced_shears()
    verify_q_basis_interface()
    verify_prime_gcd_step()


if __name__ == "__main__":
    verify()
