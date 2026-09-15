from collections import deque
from math import gcd

A=((3,0),(0,-1))
R=((-1,1),(39,9))
def mm(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def norm(M):
    g=0
    for row in M:
        for x in row:g=gcd(g,abs(x))
    return tuple(tuple(x//g for x in row) for row in M)
def det(M):return M[0][0]*M[1][1]-M[0][1]*M[1][0]
q=deque([(((1,0),(0,1)),())]);seen={((1,0),(0,1))}
for _ in range(7):
    nq=deque()
    while q:
        M,p=q.popleft()
        for name,N in [('A',A),('R',R)]:
            K=norm(mm(N,M))
            if K not in seen:
                seen.add(K);nq.append((K,p+(name,)))
                d=det(K)
                if K[0][1]==0 and K[1][0]==0:print('diag',p+(name,),K)
                if K[0][0]==K[1][1] or K[0][1]==0 or K[1][0]==0:
                    print('special',p+(name,),K,'det',d)
                if (K[0][0],K[1][1]) in [(1,1),(-1,-1)] and K[0][1] != 0 and K[1][0] == 0:
                    print('shear',p+(name,),K)
    q=nq
print('maps',len(seen))
