"""Exact certificates for B_n forms and the three explicit B12 macros."""

from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt
from itertools import combinations, product
from random import Random


def primitive_form(n):
    m = n - 4
    coefficients = m * (m + 1), 6 * m, 12
    content = gcd(*coefficients)
    return tuple(value // content for value in coefficients)


def reduced_forms(discriminant):
    if discriminant >= 0 or discriminant % 4 not in (0, 1):
        raise ValueError("negative quadratic discriminant required")
    forms = []
    for a in range(1, isqrt((-discriminant) // 3) + 1):
        for b in range(-a, a + 1):
            numerator = b * b - discriminant
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if c < a or gcd(a, gcd(abs(b), c)) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            forms.append((a, b, c))
    return tuple(forms)


def level(form):
    a, b, c = form
    determinant = 4 * a * c - b * b
    for candidate in range(1, determinant + 1):
        # candidate * Gram^-1 must be integral with even diagonal.
        if (candidate * a) % determinant == 0 and (candidate * c) % determinant == 0:
            if (candidate * b) % determinant == 0:
                return candidate
    raise AssertionError("the Gram determinant is always a valid level")


def form_value(form, u, v):
    a, b, c = form
    return a * u * u + b * u * v + c * v * v


def core(u, v):
    state = Counter()
    for value, count in ((u, 8), (v, 3), (tuple(-8*u[i]-3*v[i] for i in (0, 1)), 1)):
        state[value] += count
    return state


def average(state, selected):
    if any(state[value] < count for value, count in Counter(selected).items()):
        raise AssertionError("symbolic macro lacks the required multiplicity")
    mean = tuple(sum(value[i] for value in selected) / 3 for i in (0, 1))
    for value in selected:
        state[value] -= 1
        if not state[value]:
            del state[value]
    state[mean] += 3
    return mean


def verify_macros():
    u, v = (F(1), F(0)), (F(0), F(1))
    w = (F(-8), F(-3))
    state = core(u, v)
    new_v = average(state, (v, v, w))
    assert state == core(u, new_v)
    assert new_v == (F(-8, 3), F(-1, 3))
    matrices = {}
    for name in ("P", "R"):
        state = core(u, v)
        for _ in range(3):
            a = average(state, (u, u, v))
        b = average(state, (u, u, a) if name == "P" else (u, w, a))
        assert state == core(a, b)
        matrices[name] = a, b
    assert matrices["P"] == ((F(2, 3), F(1, 3)), (F(8, 9), F(1, 9)))
    assert matrices["R"] == ((F(2, 3), F(1, 3)), (F(-19, 9), F(-8, 9)))

    # Norm pullback for R in (u,z), z=2u+v, is B/81.
    b11, b12, b22 = 9, 6, 22
    assert 54-b11 > 0 and (54-b11)*(27-b22) - b12*b12 == 189
    assert b11-2 > 0 and (b11-2)*(b22-1) - b12*b12 == 111
    checked = 0
    for u in range(-40, 41):
        for v in range(-40, 41):
            if gcd(abs(u), abs(v)) != 1:
                continue
            x, y = 6*u+3*v, -19*u-8*v
            assert gcd(abs(x), abs(y)) == gcd(9, u-v)
            z = 2*u+v
            new_u, new_z = F(z, 3), -F(3*u+2*z, 9)
            assert 81*(2*new_u**2+new_z**2) == 9*u*u+12*u*z+22*z*z
            if (u-v) % 3:
                assert 2*(3*z)**2+(-3*u-2*z)**2 > 2*u*u+z*z
                assert (25*u+11*v) % 3 != 0
            checked += 1
    print("B12 symbolic A/P/R and norm/content identities: PASS", checked)


def verify_forms():
    expected = {
        12: ((6, 4, 1), -8, 1, "split"),
        15: ((22, 11, 2), -55, 4, "inert"),
        18: ((35, 14, 2), -84, 4, "ramified"),
        21: ((51, 17, 2), -119, 10, "split"),
    }
    for n, (form, discriminant, count, splitting) in expected.items():
        assert primitive_form(n) == form
        a, b, c = form
        assert b*b-4*a*c == discriminant
        assert len(reduced_forms(discriminant)) == count
        assert level(form) == -discriminant
        kind = {0: "ramified", 1: "split", 2: "inert"}[discriminant % 3]
        assert kind == splitting
        for u in range(-10, 11):
            for v in range(-10, 11):
                m = n-4
                energy = m*u*u+3*v*v+(-m*u-3*v)**2
                content = gcd(m*(m+1), 6*m, 12)
                assert energy == content*form_value(form, u, v)
        print(f"n={n} primitive form {form} D={discriminant} "
              f"class number={count} level={-discriminant} p3={kind}")
    print("binary forms, levels, reduced classes, and p3 splitting: PASS")


def verify_carry_family():
    u, v = (F(1), F(0)), (F(0), F(1))
    cases = 0
    for exponent in range(1, 7):
        r = 3 ** exponent
        m = r - 1
        w = (F(-m), F(-3))
        for name in ("P", "R"):
            state = Counter({u: m, v: 3, w: 1})
            current, copies, operations = v, 3, 0
            for _ in range(exponent - 1):
                for _ in range(copies):
                    following = average(state, (u, u, current))
                    operations += 1
                current, copies = following, 3*copies
            a = current
            assert state == Counter({u: 2, a: r, w: 1})
            b = average(state, (u, u, a) if name == "P" else (u, w, a))
            operations += 1
            target = Counter()
            for value, count in ((a, m), (b, 3),
                                 (tuple(-m*a[i]-3*b[i] for i in (0, 1)), 1)):
                target[value] += count
            assert state == target
            assert a == (F(r-3, r), F(3, r))
            expected_b = ((F(r-1, r), F(1, r)) if name == "P"
                          else (F(-r*r+3*r-3, 3*r), F(1-r, r)))
            assert b == expected_b
            det = a[0]*b[1]-a[1]*b[0]
            assert det == (F(-2, r) if name == "P" else F(1, r))
            assert operations == (r-1)//2
            if name == "R":
                difference = tuple(a[i]-b[i] for i in (0, 1))
                assert difference == (
                    F(1, r)+F(r+3, 3)*a[0],
                    -F(1, r)+F(r+3, 3)*a[1],
                )
            cases += 1
    print("carry-repair family symbolic replay k=1..6: PASS", cases)


def verify_pullback_theta():
    f, pullback = (6, 4, 1), (121, 100, 22)
    assert pullback[1]**2-4*pullback[0]*pullback[2] == -648
    assert level(pullback) == 648
    assert len(reduced_forms(-648)) == 6
    for u in range(-12, 13):
        for v in range(-12, 13):
            x, y = 6*u+3*v, -19*u-8*v
            assert form_value(pullback, u, v) == form_value(f, x, y)
            assert (x-3*y) % 9 == 0
            assert ((-8*x-3*y)//9, (19*x+6*y)//9) == (u, v)

    # Independent enumeration of the two lattices through q^180. Bounds
    # follow from completing the square and the smallest Gram eigenvalue.
    cutoff = 180
    restricted, pulled = Counter(), Counter()
    for x in range(-10, 11):
        for z in range(-14, 15):
            y = z-2*x
            energy = form_value(f, x, y)
            if energy <= cutoff and (x-3*y) % 9 == 0:
                restricted[energy] += 1
    # Pullback symmetric form matrix has trace 143 and determinant 162;
    # its smallest eigenvalue exceeds determinant/trace > 1.
    for u in range(-14, 15):
        for v in range(-14, 15):
            energy = form_value(pullback, u, v)
            if energy <= cutoff:
                pulled[energy] += 1
    assert pulled == restricted
    print("B12 index-9 theta pullback and conductor-9 order: PASS")


def verify_safe_carry_patterns():
    checked = 0
    random = Random(90919)
    # Several unequal ternary weight vectors; test only primes dividing n.
    for weights, prime in (((1,)*8, 2), ((1,)*7, 7), ((1,)*6+(9,), 5)):
        t, n = len(weights), sum(weights)
        assert t >= 7 and n % prime == 0
        classes = {}
        for index, weight in enumerate(weights):
            classes.setdefault(weight, []).append(index)
        patterns = set()
        # Translate the unique dominant class to zero. Solve the final
        # exceptional residue from the weighted zero-sum condition.
        for size in (2, 3):
            for support in combinations(range(t), size):
                for nonzero in product(range(1, prime), repeat=size-1):
                    residues = [0] * t
                    for index, value in zip(support, nonzero):
                        residues[index] = value
                    last = support[-1]
                    residues[last] = (-sum(w*x for w, x in zip(weights, residues))
                                      * pow(weights[last], -1, prime)) % prime
                    if residues[last]:
                        patterns.add(tuple(residues))
        for _ in range(80):
            residues = [random.randrange(prime) for _ in range(t-1)] + [0]
            residues[-1] = (-sum(w*x for w, x in zip(weights, residues))
                            * pow(weights[-1], -1, prime)) % prime
            patterns.add(tuple(residues))
        for residues in sorted(patterns):
            assert sum(w*x for w, x in zip(weights, residues)) % prime == 0
            counts = Counter(residues)
            if len(counts) < 2:
                continue
            common, multiplicity = counts.most_common(1)[0]
            exceptions = ({i for i, x in enumerate(residues) if x != common}
                          if multiplicity >= t-3 else None)
            if exceptions is not None:
                assert len(exceptions) in (2, 3)
            for eligible in classes.values():
                h = len(eligible)
                if h < 3:
                    continue
                unsafe = 0
                for triple in combinations(eligible, 3):
                    outside = [x for i, x in enumerate(residues) if i not in triple]
                    after = outside + [sum(residues[i] for i in triple)
                                       * pow(3, -1, prime) % prime]
                    actual_bad = len(set(after)) == 1
                    predicted = exceptions is not None and exceptions <= set(triple)
                    assert actual_bad == predicted
                    unsafe += actual_bad
                assert unsafe <= h-2
                if h*(h-1) > 6:
                    assert unsafe < h*(h-1)*(h-2)//6
            checked += 1
    print("safe equal-weight carry exceptional-set patterns: PASS", checked)


def verify_twelve_macro_family():
    u, v = (F(1), F(0)), (F(0), F(1))
    checked = 0
    for exponent in range(2, 7):
        r, m = 3**exponent, 3**exponent-1
        w = (F(-m), F(-3))
        matrices = {}
        for name in ("B", "C", "D"):
            state = Counter({u: m, v: 3, w: 1})
            operations = 0

            def take(triple):
                nonlocal operations
                operations += 1
                return average(state, triple)

            if name == "B":
                current, copies = take((w, v, v)), 3
                for _ in range(exponent-1):
                    for _ in range(copies):
                        new = take((current, u, u))
                    current, copies = new, 3*copies
                first = current
                middle = take((u, v, first))
                second = take((u, middle, middle))
                expected = (-F(2, r), -F(1, r), F(5*r-4, 9*r), F(2*r-2, 9*r))
                assert operations == (r+3)//2
            else:
                a = take((w, u, u))
                b = take((a, a, v))
                c = take((v, u, u))
                for _ in range(3):
                    current = take((b, c, u))
                copies = 9
                for _ in range(exponent-2):
                    for _ in range(copies):
                        new = take((current, u, u))
                    current, copies = new, 3*copies
                first = current
                second = take((v if name == "C" else a, first, u))
                low = ((F(4*r-6, 9*r), F(1, 3)) if name == "C"
                       else (-F((r-1)*(r-6), 9*r), -F(1, 3)))
                expected = (F(r-6, 3*r), F(0)) + low
                assert operations == (r+5)//2
            target = Counter()
            for value, count in ((first, m), (second, 3),
                                 (tuple(-m*first[i]-3*second[i] for i in (0, 1)), 1)):
                target[value] += count
            assert state == target
            actual = first+second
            assert actual == expected
            matrices[name] = actual
            checked += 1
        a, b, c, d = matrices["B"]
        e, f, g, h = matrices["C"]
        trace = e*a+f*c+g*b+h*d
        determinant = (a*d-b*c)*(e*h-f*g)
        assert trace == F(2*(r-7)*(r-9), 27*r*r)
        assert determinant == F(r-6, 81*r*r)
        assert (trace == 0) == (r == 9)
    print("B/C/D expansion families k=2..6: PASS", checked)


if __name__ == "__main__":
    verify_macros()
    verify_forms()
    verify_carry_family()
    verify_pullback_theta()
    verify_safe_carry_patterns()
    verify_twelve_macro_family()
