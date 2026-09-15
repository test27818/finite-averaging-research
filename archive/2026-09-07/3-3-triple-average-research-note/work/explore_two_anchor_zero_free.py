"""Residue-only two-anchor availability diagnostic, not a reachability solver."""

from itertools import combinations_with_replacement
from random import Random


def zero_free(values, p):
    reached, mask = 1, (1 << p)-1
    for value in values:
        shift = value % p
        translated = ((reached << shift) | (reached >> (p-shift))) & mask
        if translated & 1:
            return False
        reached |= translated
    return True


def main():
    checked, failures = 0, []
    for p in (5, 7, 11):
        for alpha in range(1, p-2):
            for beta in range(alpha, p-2-alpha+1):
                length = p-alpha-beta
                for values in combinations_with_replacement(range(2, p), length):
                    checked += 1
                    if zero_free([1]*alpha+list(values), p) and zero_free(
                            [-1]*beta+[x-1 for x in values], p):
                        failures.append((p, alpha, beta, values))
                        break
                if failures:
                    break
            if failures:
                break
        if failures:
            break
    print('bounded exact two-anchor checks:', checked)
    print('two-anchor counterexamples:', failures)
    random = Random(2026091214)
    for p in (13, 17, 23, 31, 43, 61):
        for _ in range(2000):
            alpha = random.randrange(1, p-3)
            beta = random.randrange(1, p-2-alpha)
            values = [random.randrange(2, p) for _ in range(p-alpha-beta)]
            if zero_free([1]*alpha+values, p) and zero_free([-1]*beta+[x-1 for x in values], p):
                failures.append((p, alpha, beta, values))
                break
    print('larger bounded checks counterexamples:', failures)


if __name__ == '__main__':
    main()
