from fractions import Fraction as F
from collections import deque

def run(vals, depth):
    n=len(vals); x=tuple(vals); q=deque([(x,[])]) ; seen={x}
    while q:
        z,w=q.popleft()
        if len(set(z))==1:return w,z,len(seen)
        if len(w)==depth:continue
        for i in range(n):
            for j in range(n):
                if i==j:continue
                y=list(z);m=(z[i]+2*z[j])/3;y[i]=y[j]=m;y=tuple(y)
                if y not in seen:seen.add(y);q.append((y,w+[(i,j)]))
    return None,None,len(seen)
for x in [(F(0),F(0),F(1)),(F(0),F(1),F(2)),(F(0),F(1),F(3))]:
    print(x,run(x,14))
