"""Check the B_(2*3^k) -> legal 12-block -> paired ternary network reduction.

Equalizing the selected twelve positions invokes the proved n12-complete
theorem. This program checks its input hypotheses; it does not substitute
a one-step 12-average for an unproved primitive operation.
"""

from collections import Counter
from fractions import Fraction as F
from math import gcd

from verify_thirteen_arithmetic_group import average_block


def selected_block(n, u, v):
    if n < 18 or n % 4 != 2:
        raise ValueError("this reduction requires n=2 mod 4 and n>=18")
    if gcd(u, v) != 1 or (u-v) % 2 != 1:
        raise ValueError("primitive integer pair with opposite parity required")
    m = n-4
    b = 3 if u % 2 == 0 else 1
    a = 11-b
    values = (u,)*a+(v,)*b+(-m*u-3*v,)
    mean = F(sum(values), 12)
    remaining = Counter()
    for value, count in ((u, m-a), (v, 3-b), (mean, 12)):
        if count:
            remaining[F(value)] += count
    return values, mean, remaining


def local_gcd(values):
    mean = F(sum(values), len(values))
    denominator = mean.denominator
    centered = [int((value-mean)*denominator) for value in values]
    content = gcd(*(abs(value) for value in centered))
    assert content
    primitive = [value//content for value in centered]
    return gcd(*(abs(value-primitive[0]) for value in primitive))


def verify():
    checked, tails = 0, 0
    for k in range(2, 7):
        n = 2*3**k
        samples = []
        for u in range(-30, 31):
            for v in range(-30, 31):
                if gcd(u, v) != 1 or (u-v) % 2 == 0:
                    continue
                values, mean, after = selected_block(n, u, v)
                assert len(values) == 12
                assert mean.denominator in (1, 3)
                assert local_gcd(values) in (1, 3)
                assert sum(after.values()) == n
                assert sum(value*count for value, count in after.items()) == 0
                assert all(count % 2 == 0 for count in after.values())
                checked += 1
                if k <= 4 and len(samples) < 8:
                    samples.append(after)
        # Lift the fixed 3^k network twice, preserving exact values.
        for after in samples:
            compressed = [value for value, count in after.items()
                          for _ in range(count//2)]
            assert len(compressed) == 3**k
            physical = [value for value in compressed for _ in range(2)]
            operations = 0
            for copy in (0, 1):
                indices = list(range(copy, len(physical), 2))
                operations += average_block(physical, indices)
            assert not any(physical)
            assert operations == 2*k*3**(k-1)
            tails += 1
    print("B_(2*3^k) legal twelve-block interfaces k=2..6: PASS", checked)
    print("paired ternary-network physical tails: PASS", tails)


if __name__ == "__main__":
    verify()
