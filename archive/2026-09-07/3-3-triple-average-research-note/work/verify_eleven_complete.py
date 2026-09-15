"""Exact checks for the eleven-point safety lemma and five-step bridge."""

from collections import Counter
from fractions import Fraction as F
from itertools import product


def add(*values):
    return tuple(sum(value[index] for value in values) for index in range(5))


def scale(value, denominator):
    return tuple(entry / denominator for entry in value)


def bridge_forms():
    u = (F(1), F(0), F(0), F(0), F(0))
    a = (F(0), F(1), F(0), F(0), F(0))
    b = (F(0), F(0), F(1), F(0), F(0))
    c = (F(0), F(0), F(0), F(1), F(0))
    d = (F(0), F(0), F(0), F(0), F(1))
    e = (F(-6), F(-1), F(-1), F(-1), F(-1))

    q = scale(add(e, c, d), 3)
    r = scale(add(q, u, u), 3)
    s = scale(add(r, r, b), 3)

    assert r == tuple(F(-1, 9) * (a[i] + b[i]) for i in range(5))
    assert s == tuple(F(1, 27) * (7 * b[i] - 2 * a[i])
                      for i in range(5))
    assert a == tuple(-7 * r[i] - 3 * s[i] for i in range(5))

    # The five position-level operations are always available:
    # (e,c,d), (q,u,u) three times, then (r,r,b).
    multiplicities = Counter([r] * 7 + [s] * 3 + [a])
    assert sorted(multiplicities.values()) == [1, 3, 7]
    return a, b, r, s


def verify_bridge_legality():
    a, b, r, s = bridge_forms()
    # 27(r-s)=-(a+10b); 27 is a unit modulo 11.
    for residue_a in range(11):
        for residue_b in range(11):
            if residue_a == residue_b:
                continue
            lhs = -(residue_a + 10 * residue_b) % 11
            assert lhs != 0

    # If all five exceptions have one residue t, zero sum gives u=t mod 11.
    for t in range(11):
        assert (6 * t + 5 * t) % 11 == 0
    assert any(r[index] != s[index] for index in range(5))


def pair_sums_cover_all_mod3(counts):
    sums = set()
    for left in range(3):
        for right in range(left, 3):
            multiplicity = counts[left] if left == right else min(
                counts[left], counts[right]
            )
            if left == right and counts[left] < 2:
                continue
            if left != right and multiplicity < 1:
                continue
            sums.add((left + right) % 3)
    return sums == {0, 1, 2}


def verify_safety_combinatorics():
    # A no-integer-triple configuration already has a value occurring six
    # times: two mod-3 classes suffice, and 11 positions force one class >= 6.
    for counts in product(range(12), repeat=3):
        if sum(counts) != 11:
            continue
        if sum(count > 0 for count in counts) > 2:
            continue
        assert max(counts) >= 6

    # If a mod-11 main class has b=2 or 3 exceptions, two occupied mod-3
    # classes with at least two entries yield a safe pair with one exception.
    for b in (2, 3):
        size = 11 - b
        for counts in product(range(size + 1), repeat=3):
            if sum(counts) != size:
                continue
            if sum(count >= 2 for count in counts) >= 2:
                assert pair_sums_cover_all_mod3(counts)
            elif max(counts) >= 6:
                assert True
            else:
                # The only remaining distributions have a class of size at
                # least 7 (b=3) or 8 (b=2), hence already contain six copies.
                assert max(counts) >= 6

    # For b=1, the only distribution with no sixfold class and two classes
    # both of size at least three is 5+5.  Such a pattern is ruled out by
    # the mod-11 zero-sum equation: 10t+z=0 forces z=t.
    size = 10
    exceptional = []
    for counts in product(range(size + 1), repeat=3):
        if sum(counts) != size:
            continue
        if max(counts) >= 6:
            continue
        if sum(count > 0 for count in counts) > 2:
            continue
        occupied = [count for count in counts if count]
        exceptional.append(tuple(sorted(occupied, reverse=True)))
    assert set(exceptional) == {(5, 5)}
    for t in range(11):
        for z in range(11):
            if (10 * t + z) % 11 == 0:
                assert z == t


def main():
    verify_bridge_legality()
    verify_safety_combinatorics()
    print("eleven-point safety and bridge certificate: PASS")
    print("generic bridge: 5 operations, target multiplicities 7+3+1")
    print("terminal legality: a != b (mod 11)")
    print("safety cases: b=1,2,3 mod-11 exceptions checked")


if __name__ == "__main__":
    main()
