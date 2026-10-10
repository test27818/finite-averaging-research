from fractions import Fraction
from random import sample, seed

def op(M, i, j):
    n = len(M)
    out = [list(row) for row in M]
    row = [(M[i][k] + 2 * M[j][k]) / 3 for k in range(n)]
    out[i] = row
    out[j] = row
    return tuple(tuple(r) for r in out)

def rank(M):
    A = [list(r) for r in M]
    n, m = len(A), len(A[0])
    rr = 0
    for c in range(m):
        piv = next((r for r in range(rr, n) if A[r][c]), None)
        if piv is None: continue
        A[rr], A[piv] = A[piv], A[rr]
        q = A[rr][c]
        A[rr] = [x/q for x in A[rr]]
        for r in range(n):
            if r != rr and A[r][c]:
                q = A[r][c]
                A[r] = [a-q*b for a,b in zip(A[r], A[rr])]
        rr += 1
    return rr

def trial(n, steps, repeats):
    I = tuple(tuple(Fraction(i == j) for j in range(n)) for i in range(n))
    best = n
    bestw = None
    for _ in range(repeats):
        M, word = I, []
        for t in range(steps):
            i,j = sample(range(n), 2)
            M = op(M,i,j); word.append((i,j))
            r = rank(M)
            if r < best:
                best, bestw = r, word[:]
            if r == 1: return best, bestw
    return best, bestw

if __name__ == '__main__':
    seed(4)
    for n in range(3, 9):
        print(n, trial(n, 150, 500))
