"""Exact singleton-entry obstruction with small full-matrix cross-checks."""
from fractions import Fraction as F
from itertools import combinations
from verify_nonsplit_projective_layers import partition,transition,multiply,centered_scalar


def scalar_entry(source,target):
    singles = [b[0] for b in source if len(b)==1]
    i,j = singles[:2]
    block = next(b for b in target if i in b)
    return F(1,len(block)) if j in block else F(0)


def verify():
    count = full = 0
    for p in (5,11,17,23,29,41,47,53,59,71,83):
        base = partition(0,p)
        for c in range(p):
            target = partition(c,p)
            entry = scalar_entry(base,target)
            assert entry == 0 or entry > F(1,p)
            assert (set(base[:2]) == set(target[:2])) == (c==0)
            if p<=17:
                roundtrip = multiply(transition(target,base),transition(base,target))
                lam = centered_scalar(roundtrip,[len(b) for b in base])
                assert lam == (F(1) if c==0 else None)
                full += 1
            count += 1
    # All same-weight partitions on five positions, not only projective layers.
    parts = []
    for pair in combinations(range(5),2):
        triple = tuple(i for i in range(5) if i not in pair)
        parts.append(((pair[0],),(pair[1],),triple))
    for source in parts:
        for target in parts:
            b = multiply(transition(target,source),transition(source,target))
            lam = centered_scalar(b,[1,1,3])
            assert lam == (F(1) if source==target else None)
            full += 1
    print("two-singleton geometric obstruction: PASS",count)
    print("independent full roundtrip cross-checks: PASS",full)
    print("All-prime exclusion follows from the singleton-entry proof, not this sample.")


if __name__ == "__main__":
    verify()
