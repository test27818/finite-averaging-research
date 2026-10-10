from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import gcd
import json
from pathlib import Path
if not __debug__:
    raise RuntimeError("Run without -O: all assertions are required.")

FIVE_TABLE = ((0, 0, 5, (0, 2, 2, 2, 2), ('5', '-8', '-8', '-8', '-8')),
 (0, 0, 5, (0, 3, 3, 3, 3), ('5', '-2', '-2', '-2', '-2')),
 (0, 0, 5, (0, 4, 4, 4, 4), ('5', '-7/2', '-7/2', '-7/2', '-7/2')),
 (0, 0, 5, (1, 2, 2, 2, 2), ('-4', '9/2', '9/2', '9/2', '9/2')),
 (0, 0, 5, (1, 3, 3, 3, 3), ('-4', '3', '3', '3', '3')),
 (0, 0, 5, (1, 4, 4, 4, 4), ('-4', '9', '9', '9', '9')),
 (0, 0, 5, (2, 2, 2, 2, 3), ('-3', '-3', '-3', '-3', '8')),
 (0, 0, 5, (2, 2, 2, 2, 4), ('7', '7', '7', '7', '-16')),
 (0, 0, 5, (2, 3, 3, 3, 3), ('12', '-7', '-7', '-7', '-7')),
 (0, 0, 5, (2, 4, 4, 4, 4), ('17', '-6', '-6', '-6', '-6')),
 (0, 0, 5, (3, 3, 3, 3, 4), ('8', '8', '8', '8', '-11')),
 (0, 0, 5, (3, 4, 4, 4, 4), ('-7', '4', '4', '4', '4')),
 (1, 0, 5, (2, 2, 2, 2), ('2', '2', '2', '2')),
 (1, 0, 5, (3, 3, 3, 3), ('4/3', '4/3', '4/3', '4/3')),
 (1, 0, 5, (3, 4, 4, 4), ('-7', '4', '4', '4')),
 (1, 0, 5, (4, 4, 4, 4), ('4', '4', '4', '4')),
 (1, 0, 6, (3, 4, 4, 4, 4), ('-7', '4', '4', '4', '4')),
 (1, 1, 5, (0, 3, 3), ('5', '-7', '-7')),
 (1, 1, 5, (1, 3, 3), ('-4', '8', '8')),
 (2, 0, 5, (2, 2, 2), ('2', '2', '2')),
 (2, 0, 5, (2, 2, 3), ('2', '2', '3')),
 (2, 0, 6, (2, 2, 2, 2), ('2', '2', '2', '2')))

def five_equations(sequence, alpha, beta):
    length = len(sequence)
    for i, residue in enumerate(sequence):
        if residue in (0, 1):
            yield (tuple((int(i == j) for j in range(length))), 5 if residue == 0 else -4)
    for mask in range(1, 1 << length):
        count = mask.bit_count()
        if count > 5:
            continue
        row = tuple((mask >> i & 1 for i in range(length)))
        residue = sum((x * c for x, c in zip(sequence, row))) % 5
        i = -residue % 5
        if i <= min(alpha, 5 - count):
            if 5 - count - i <= beta:
                yield ((0,) * length, 1)
                return
            yield (row, 5 - i)
        j = (residue - count) % 5
        if j <= min(beta, 5 - count):
            yield (row, count + j - 5)

def five_eliminate(rows, width):
    pivots = {}
    original = list(rows)
    for coefficients, rhs in original:
        row = list(map(F, coefficients)) + [F(rhs)]
        for column, pivot in sorted(pivots.items()):
            factor = row[column]
            if factor:
                row = [x - factor * y for x, y in zip(row, pivot)]
        first = next((j for j in range(width) if row[j]), None)
        if first is None:
            if row[-1]:
                return None
        else:
            factor = row[first]
            pivots[first] = [x / factor for x in row]
    assert len(pivots) == width, 'No unchecked positive-dimensional case is allowed.'
    result = [F(0)] * width
    for column, row in sorted(pivots.items(), reverse=True):
        result[column] = row[-1] - sum((row[j] * result[j] for j in range(column + 1, width)))
    assert all((sum((a * x for a, x in zip(row, result))) == rhs for row, rhs in original))
    return tuple(result)

def verify_five():
    expected = {(a, b, c, s): tuple(map(F, v)) for a, b, c, s, v in FIVE_TABLE}
    observed, systems = ({}, 0)
    for alpha, beta in ((0, 0), (1, 0), (1, 1), (2, 0)):
        for capacity in (5, 6, 7, 8):
            length = capacity - alpha - beta
            for sequence in combinations_with_replacement(range(5), length):
                frequencies = Counter(sequence)
                if max(frequencies.values()) >= 5 or frequencies[0] > 1 or frequencies[1] > 1:
                    continue
                systems += 1
                solution = five_eliminate(five_equations(sequence, alpha, beta), length)
                if solution is not None:
                    assert all((x.denominator % 5 and x.numerator * pow(x.denominator, -1, 5) % 5 == r for x, r in zip(solution, sequence)))
                    observed[alpha, beta, capacity, sequence] = solution
    assert observed == expected and systems == 903
    for (alpha, beta, capacity, sequence), values in expected.items():
        assert capacity in (5, 6)
        if capacity == 6:
            assert all((x.denominator == 1 for x in values))
            assert 5 + alpha + sum(values) == 15
        elif any((x.denominator % 2 == 0 for x in values)):
            assert alpha == beta == 0
            assert sum((x.denominator == 2 for x in values)) == 4
            assert all((x.denominator in (1, 2) for x in values))
        else:
            assert all((x.denominator % 2 for x in values))
        if capacity == 5:
            assert (5 + alpha + sum(values)).denominator % 2 == 1
    return (systems, len(expected))

SEVEN_TABLE = ((1, 2, 0, (2,), (6,), (2,)),
 (1, 3, 0, (2,), (5,), (2,)),
 (1, 3, 0, (2, 3), (4, 1), (2, 3)),
 (1, 4, 0, (2,), (4,), (2,)),
 (1, 4, 0, (2, 3), (3, 1), (2, 3)),
 (1, 4, 0, (2, 4), (3, 1), (2, 4)),
 (1, 4, 0, (2, 3), (2, 2), (2, 3)),
 (2, 3, 0, (2,), (6,), (2,)),
 (2, 4, 0, (2,), (5,), (2,)),
 (2, 4, 0, (2, 3), (4, 1), (2, 3)),
 (3, 4, 0, (2,), (6,), (2,)))

def seven_equations(alpha, beta, residues, frequencies):
    for j, r in enumerate(residues):
        if r in (0, 1):
            yield (tuple((int(i == j) for i in range(len(residues)))), 7 if r == 0 else -6)
    for counts in product(*(range(f + 1) for f in frequencies)):
        size = sum(counts)
        if not 1 <= size <= 7:
            continue
        residue = sum((r * k for r, k in zip(residues, counts))) % 7
        i = -residue % 7
        if i <= min(alpha, 7 - size):
            if 7 - size - i <= beta:
                yield ((0,) * len(residues), 1)
                return
            yield (counts, 7 - i)
        j = (residue - size) % 7
        if j <= min(beta, 7 - size):
            yield (counts, size + j - 7)

def seven_eliminate(rows, width):
    pivots = {}
    for coefficients, rhs in rows:
        row = tuple(coefficients) + (rhs,)
        for j, pivot in sorted(pivots.items()):
            if row[j]:
                a, b = (pivot[j], row[j])
                row = tuple((a * x - b * y for x, y in zip(row, pivot)))
                common = gcd(*row)
                if common:
                    row = tuple((x // common for x in row))
        j = next((i for i in range(width) if row[i]), None)
        if j is None:
            if row[-1]:
                return None
        else:
            pivots[j] = row
    assert len(pivots) == width
    values = [F(0)] * width
    for j, row in sorted(pivots.items(), reverse=True):
        values[j] = (F(row[-1]) - sum((row[k] * values[k] for k in range(j + 1, width)))) / row[j]
    return tuple(values)

def verify_seven():
    expected = {(e, a, b, r, f): tuple(map(F, v)) for e, a, b, r, f, v in SEVEN_TABLE}
    observed, systems = ({}, 0)
    for extra in range(1, 6):
        for alpha in range(5):
            for beta in range(min(alpha, 4 - alpha) + 1):
                length = 7 + extra - alpha - beta
                for sequence in combinations_with_replacement(range(7), length):
                    bins = Counter(sequence)
                    if max(bins.values()) >= 7 or bins[0] > 1 or bins[1] > 1:
                        continue
                    residues, frequencies = (tuple(bins), tuple(bins.values()))
                    result = seven_eliminate(seven_equations(alpha, beta, residues, frequencies), len(bins))
                    systems += 1
                    if result is None:
                        continue
                    rows = list(seven_equations(alpha, beta, residues, frequencies))
                    assert all((sum((x * k for x, k in zip(result, row))) == rhs for row, rhs in rows))
                    for j, f in enumerate(frequencies):
                        assert f == 1 or any((0 < row[j] < f for row, rhs in rows))
                    assert all((x.denominator == 1 and x % 7 == r for x, r in zip(result, residues)))
                    mass = 7 + alpha + sum((x * f for x, f in zip(result, frequencies)))
                    assert 0 < mass < 21 + extra and mass.denominator == 1
                    observed[extra, alpha, beta, residues, frequencies] = result
    assert observed == expected and systems == 57026
    return (systems, len(observed))

def mm(A, B, modulus):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%modulus,(a*f+b*h)%modulus,
            (c*e+d*g)%modulus,(c*f+d*h)%modulus)

def power(A,k,m):
    out=(1,0,0,1)
    while k:
        if k&1: out=mm(A,out,m)
        A=mm(A,A,m); k//=2
    return out

def closure(generators, modulus):
    I=(1,0,0,1); seen={I}; queue=deque([I])
    while queue:
        A=queue.popleft()
        for B in generators:
            C=mm(B,A,modulus)
            if C not in seen: seen.add(C); queue.append(C)
    return seen

def verify_twenty_two():
    m=1936
    A=(4,1,-1,0); Fm=(1,2,0,7)
    X=tuple(t*pow(7,-1,m)%m for t in mm(Fm,Fm,m))
    assert power(A,440,m)==power(X,440,m)==(1,0,0,1)
    X9=tuple(t*pow(7,-1,9)%9 for t in mm(Fm,Fm,9))
    group=closure([power(A,440,9),power(X9,440,9)],9)
    assert len(group)==648
    assert all((a*d-b*c)%9==1 for a,b,c,d in group)
    units={1}; queue=deque([1])
    while queue:
        u=queue.popleft()
        for f in (-1,5,7):
            v=u*f%m
            if v not in units: units.add(v); queue.append(v)
    all_units={u for u in range(m) if gcd(u,m)==1}
    assert len(units)==440 and len(all_units)==880
    other={3*u%m for u in units}
    assert units.isdisjoint(other) and units|other==all_units
    chi={u:0 for u in units}; chi.update({u:1 for u in other})
    # Matrices in the (z,y) chart; inverse representatives are adjugates.
    matrices=[(7,-1,22,-3),(7,0,44,1),(-15,2,-110,15)]
    matrices += [(d,-b,-c,a) for a,b,c,d in matrices[:2]]
    seen={(0,0):0}; queue=deque([(0,0)])
    while queue:
        x,e=point=queue.popleft()
        for a,b,c,d in matrices:
            denominator=(c*x+d)%m
            assert denominator in all_units
            out=((a*x+b)*pow(denominator,-1,m)%m,e^chi[denominator])
            if out not in seen:
                seen[out]=seen[point]+1; queue.append(out)
    assert len(seen)==3872 and max(seen.values())==8
    return {'auxiliary_group':len(group),'unit_image':len(units),
            'marked_states':len(seen),'maximum_depth':max(seen.values())}

if __name__ == '__main__':
    report={'five':verify_five(),'seven':verify_seven(),
            'twenty_two':verify_twenty_two()}
    Path(__file__).with_name('finite_checks_result.json').write_text(
        json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
