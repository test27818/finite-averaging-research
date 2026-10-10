from fractions import Fraction as F
from collections import deque
from itertools import combinations_with_replacement

def op(x, i, j):
    y = list(x)
    m = (x[i] + 2*x[j])/3
    y[i] = y[j] = m
    return tuple(sorted(y))

def find(x, depth):
    x = tuple(sorted(map(F, x)))
    q = deque([(x, 0)])
    seen = {x}
    while q:
        z, d = q.popleft()
        if len(set(z)) == 1:
            return d
        if d == depth:
            continue
        for i in range(len(x)):
            for j in range(len(x)):
                if i == j: continue
                y = op(z, i, j)
                if y not in seen:
                    seen.add(y)
                    q.append((y, d+1))
    return None

for x in combinations_with_replacement(range(5), 5):
    print(x, find(x, 5))
