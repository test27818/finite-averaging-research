import math

A = ((0, -3), (1, -1))
B = ((1, -1), (0, -3))


def mul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))


level = {((1, 0), (0, 1))}
for d in range(1, 13):
    level = {mul(M, X) for X in level for M in (A, B)}
    best = None
    for M in level:
        tr = M[0][0] + M[1][1]
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        disc = tr * tr - 4 * det
        if disc >= 0:
            roots = [abs((tr + math.sqrt(disc)) / 2), abs((tr - math.sqrt(disc)) / 2)]
        else:
            roots = [math.sqrt(det)] * 2
        rho = max(roots)
        if best is None or rho < best[0]:
            best = (rho, M, tr, det)
    print(d, len(level), best)
