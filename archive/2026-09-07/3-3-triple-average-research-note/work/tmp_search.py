from itertools import combinations
from random import Random

def safe(vals,p):
    n=len(vals)
    for S in combinations(range(n),3):
        if sum(vals[i] for i in S)%3: continue
        if len({vals[i] for i in S})==1: continue
        rem=[vals[i]%p for i in range(n) if i not in S]
        if len(set(rem))>=2:
            return S
    return None
for p in [7,11,13,17,19,23]:
    rnd=Random(1)
    best=0; bestv=None
    # random values mod 3p with p residue diversity and zero sum mod p maybe not necessary
    for _ in range(200000):
        vals=[rnd.randrange(3*p) for _ in range(p)]
        # ensure G mod p not all same
        if len({v%p for v in vals})==1: continue
        if safe(vals,p) is None:
            mm=max(vals.count(v) for v in set(vals))
            if mm>best: best=mm;bestv=vals
            if mm < p-4:
                print('counter',p,mm,vals);break
    print('p',p,'best',best,bestv)
