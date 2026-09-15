"""Independent exact n9 six-averaging network and universal four-step optimum.

Only Python standard library.  Fixed operators are replayed on every standard
basis; the lower bound checks all possible second six-sets after a fixed first.
The universal mathematical proof is in six_average_nine_fixed_network.md.
"""

from fractions import Fraction as F
from itertools import combinations
from random import Random

WORD = ((1, 2, 3, 4, 5, 6), (1, 2, 3, 7, 8, 9),
        (1, 2, 3, 7, 4, 5), (1, 2, 3, 6, 8, 9))


def replay(raw, word=WORD, consensus=True):
    assert len(raw) == 9
    state = list(map(F, raw))
    mean = sum(state) / 9
    for atom in word:
        assert len(atom) == len(set(atom)) == 6
        assert all(type(i) is int and 1 <= i <= 9 for i in atom)
        value = sum(state[i-1] for i in atom) / 6
        for i in atom:
            state[i-1] = value
    if consensus:
        assert state == [mean]*9
    return state


def main():
    if not __debug__:
        raise RuntimeError('Assertions are required.')
    for j in range(9):
        replay([int(i == j) for i in range(9)])
    print('six-average n9 fixed network exact basis: PASS 9')
    # Symmetry fixes the first operation to WORD[0].  Every remaining matrix
    # row after any second operation is nonuniform; a third operation leaves
    # three such rows unchanged.  This checks the whole finite subclaim.
    rows = 0
    for second in combinations(range(1, 10), 6):
        columns = [replay([int(i == j) for i in range(9)],
                          (WORD[0], second), consensus=False) for j in range(9)]
        for i in range(9):
            row = [column[i] for column in columns]
            assert row != [F(1, 9)]*9
            assert sum(row) == 1 and all(x >= 0 for x in row)
            rows += 1
    print('six-average n9 three-step fixed-network exclusion: PASS', rows)
    rng = Random(60920260912)
    for bits in (3, 12, 48, 128):
        for _ in range(40):
            raw = [F(rng.randrange(-(1 << bits), 1 << bits),
                     rng.randrange(1, 1 << min(bits, 16))) for _ in range(9)]
            replay(raw)
    print('six-average n9 original rational samples: PASS 160')
    print('six-average nine-position universal four-step network: PASS')


if __name__ == '__main__':
    main()
