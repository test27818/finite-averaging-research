"""Falsify a candidate invariant using value types, not averaging-word search."""

from collections import Counter
from functools import cache
from itertools import combinations, combinations_with_replacement
from math import gcd


def good(state):
    divisor = gcd(*state)
    if not divisor:
        return True
    difference = gcd(*(x - state[0] for x in state)) // divisor
    while difference % 3 == 0:
        difference //= 3
    return difference == 1


def invariant(counts):
    return sum(count >= 3 for count in counts.values()) >= 2


@cache
def near_final(state):
    n = len(state)
    if n == 0:
        return True
    power = 1
    while n % 3 == 0:
        power *= 3
        n //= 3
    if power == len(state):
        return sum(state) == 0
    for selected in combinations(range(len(state)), power):
        if sum(state[i] for i in selected):
            continue
        chosen = set(selected)
        if near_final(tuple(x for i, x in enumerate(state) if i not in chosen)):
            return True
    return False


def edges(state):
    counts = Counter(state)
    for triple in combinations_with_replacement(sorted(counts), 3):
        if triple[0] == triple[2] or sum(triple) % 3:
            continue
        used = Counter(triple)
        if any(used[x] > counts[x] for x in used):
            continue
        after = counts - used
        after[sum(triple) // 3] += 3
        result = tuple(sorted(after.elements()))
        yield triple, result, good(result), invariant(after)


def profile(n, bound):
    checked = 0
    # Centering determines the last coordinate; sorted prefixes remove all
    # physical-position permutations before testing the invariant.
    for prefix in combinations_with_replacement(range(-bound, bound + 1), n - 1):
        last = -sum(prefix)
        if not prefix[-1] <= last <= bound:
            continue
        state = prefix + (last,)
        if gcd(*state) != 1 or not invariant(Counter(state)) or not good(state):
            continue
        if near_final(state):
            continue
        checked += 1
        choices = list(edges(state))
        if not any(arithmetic and (repeated or near_final(after))
                   for _, after, arithmetic, repeated in choices):
            print('CANDIDATE_FAILS', n, bound, 'checked', checked, 'state', state, flush=True)
            for choice in choices:
                print(choice, flush=True)
            return state
    print('NO_FAILURE_IN_RANGE', n, bound, 'checked', checked, flush=True)
    return None


if __name__ == '__main__':
    for n, bound in ((7, 5), (11, 5), (13, 4)):
        profile(n, bound)
