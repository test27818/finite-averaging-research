"""Independent exact verifier for the 512-case disjoint-blocker bridge."""

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from math import gcd, lcm

from verify_even_kernel_halving import bridge as halve_b_kernel


def local_g(values):
    mean = sum(values, F(0))/len(values)
    denominator = lcm(*(F(x-mean).denominator for x in values))
    integers = [int((x-mean)*denominator) for x in values]
    content = gcd(*integers)
    if not content:
        return 0
    return gcd(*((x-integers[0])//content for x in integers))


def residue(value, modulus):
    value = F(value)
    return value.numerator*pow(value.denominator, -1, modulus) % modulus


def label(value, main, delta):
    mod8 = residue(value, 8)
    mod7 = (residue(value, 7)-main)*pow(delta, -1, 7) % 7
    # Independent CRT implementation: unique integer in 0..55.
    return next(i for i in range(56) if i % 8 == mod8 and i % 7 == mod7)


def positions_for(labels, selected):
    unused = set(range(len(labels)))
    indices = []
    for value in selected:
        index = next(i for i in sorted(unused) if labels[i] == value)
        unused.remove(index)
        indices.append(index)
    return indices


def replay(row, values):
    u = values[0]
    main, delta = residue(u, 7), residue(values[12]-u, 7)
    assert delta
    initial = tuple(residue(values[i], 8) for i in (0,10,11,12,13))
    assert initial == tuple(row["pattern"])
    values = list(map(F, values))
    assert sum(values) == 0 and local_g(values) == 1
    for selected in row["path"]:
        assert len(selected) == 3
        labels = [label(value, main, delta) for value in values]
        indices = positions_for(labels, selected)
        mean = sum(values[i] for i in indices)/3
        for i in indices:
            values[i] = mean
        assert sum(values) == 0
    labels = [label(value, main, delta) for value in values]
    left, right = positions_for(labels, row["omitted"])
    x, y = values[left], values[right]
    assert residue(x-y, 7)
    assert residue(5*x+y, 8) == 4
    selected = [i for i in range(14) if i not in (left, right)]
    block = [values[i] for i in selected]
    assert {residue(value, 2) for value in block} == {0, 1}
    assert local_g(block) in (1, 3)
    mu = sum(block)/12
    assert mu == -(x+y)/12
    assert residue(mu-x, 2) == 1 and residue(mu-x, 7)

    # This contraction invokes the independently proved n=12 theorem.
    for i in selected:
        values[i] = mu
    indices = selected[:2]+[left]
    new_v = sum(values[i] for i in indices)/3
    for i in indices:
        values[i] = new_v
    target = Counter([mu]*10+[new_v]*3+[y])
    assert Counter(values) == target and local_g(values) == 1
    denominator = lcm(mu.denominator, new_v.denominator)
    a, b = int(mu*denominator), int(new_v*denominator)
    content = gcd(a, b)
    assert content
    halve_b_kernel(14, a//content, b//content)


def verify():
    work = Path(__file__).resolve().parent
    data = json.loads((work/"fourteen_blocker_depth2.json").read_text(encoding="utf-8"))
    assert data["depth"] == 2 and not data["missing"]
    expected = {
        row for row in product(range(8), repeat=5)
        if (10*row[0]+sum(row[1:])) % 8 == 0
        and all((row[i]-row[0]) % 2 for i in (1,2))
        and all((row[i]-row[0]) % 2 == 0 for i in (3,4))
    }
    rows = {tuple(row["pattern"]): row for row in data["certificates"]}
    assert set(rows) == expected and len(rows) == len(data["certificates"]) == 512
    histogram = Counter()
    for pattern, row in rows.items():
        assert all(type(x) is int and 0 <= x < 8 for x in pattern)
        assert len(row["omitted"]) == 2
        assert all(type(x) is int and 0 <= x < 56 for x in row["omitted"])
        assert all(len(triple) == 3 and all(type(x) is int and 0 <= x < 56
                                           for x in triple)
                   for triple in row["path"])
        u8, b8, bp8, c8, cp8 = pattern

        def lift(a, b):
            return next(i for i in range(56) if i % 8 == a and i % 7 == b)

        u, b, bp, c = lift(u8,1), lift(b8,1), lift(bp8,1), lift(c8,2)
        cp = -10*u-b-bp-c
        values = [u]*10+[b,bp,c,cp]
        replay(row, values)
        assert len(row["path"]) <= 2
        histogram[len(row["path"])] += 1
    assert histogram == Counter({0:296, 1:112, 2:104})
    # Replay a genuinely no-safe-integer-move example, not just CRT lifts.
    example = [1]*10+[8,-34,5,11]
    pattern = tuple(x % 8 for x in (1,8,-34,5,11))
    replay(rows[pattern], example)
    two_step = [8]*10+[1,1,16,-98]
    pattern = tuple(x % 8 for x in (8,1,1,16,-98))
    assert len(rows[pattern]["path"]) == 2
    replay(rows[pattern], two_step)
    print("B14 disjoint-blocker residue coverage: PASS 512")
    print("B14 prelude histogram", dict(sorted(histogram.items())))
    print("B14 twelve-subproblem and halving interfaces: PASS 514")


if __name__ == "__main__":
    verify()
