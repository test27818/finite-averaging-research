"""Exact macro replay, local scheduling, and the quadratic norm identities.

The surrounding universal lattice lemma and infinite identities are proved
in the companion document. Subproblem calls use existing 13/14/15 theorems.
"""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt

from explore_b17_guarded_returns import generate as guarded_rows, primitive, height
from explore_b17_nine_thirteen_bridges import at, projective, points
from explore_b17_universal_subblocks import generate, row_lattice_contains
from verify_fifteen_via_subblocks import centered_g, is_three_power, actual_average
from verify_thirteen_arithmetic_group import average_block
from b17_universal_atomic_words import apply as apply_atomic, certificates


A = (F(1), F(0), F(-13, 3), F(-1, 3))
B = (F(7, 9), F(2, 9), F(-11, 3), F(-1))
B_INTEGER = (7, 2, -33, -9)
SCHEDULE = {(1, 4): '', (1, 0): 'A', (1, 2): 'B',
            (1, 1): 'AB', (1, 3): 'BA', (0, 1): 'BBA'}
FOURTEEN_WORDS = (
    ('BABB', 'BBB', 'BBA'), ('BBBB', 'BBABB', 'BBBA'),
    ('BBAB', 'ABBAB', 'BBAA'), ('BBBBBB', 'BAB', 'BAA'),
    ('AB', 'BBBBB', 'AA'), ('ABBABB', 'ABBBB', 'ABBBA'),
    ('ABAB', 'B', 'A'), ('BB', 'ABB', 'BA'),
)


def core(u, v):
    return Counter([u]*13+[v]*3+[-13*u-3*v])


def expand(block, pair):
    return [at(value, pair) for value, count in block for _ in range(count)]


def contract(state, values, power=False):
    size = len(values)
    if power:
        physical = values.copy()
        count = average_block(physical, list(range(size)))
        assert count == {3: 1, 9: 6}[size]
        assert len(set(physical)) == 1
    else:
        assert size in (13, 14, 15)
        local_g = centered_g(values)
        assert local_g == 0 or is_three_power(local_g)
    result = state.copy()
    for value, count in Counter(values).items():
        assert result[value] >= count
        result[value] -= count
        if not result[value]:
            del result[value]
    mean = sum(values, F(0))/size
    assert is_three_power(mean.denominator)
    result[mean] += size
    return result, mean


def replay(row, pair):
    pair = tuple(map(F, pair))
    state, _ = contract(core(*pair), expand(row['first_block'], pair), power=True)
    state, _ = contract(state, expand(row['block'], pair))
    state = actual_average(state, expand(row['triple'], pair))
    output = at(row['matrix'][:2], pair), at(row['matrix'][2:], pair)
    assert state == core(*output)
    assert sum(state.values()) == 17 and sum(x*c for x,c in state.items()) == 0
    return output


def norm(u, v):
    return u*u+2*(4*u+v)**2


def verify_lattice():
    cases = [
        ([(2, 0), (0, 5)], (2, 5), True),
        ([(2, 0), (0, 5)], (1, 5), False),
        ([(3, 0), (0, 9)], (1, 1), True),
        ([(2, 0), (9, 0)], (F(5, 3), 0), True),
        ([(2, 0), (10, 0)], (1, 0), False),
        ([(2, 0), (10, 0)], (2, 1), False),
        ([(2, 2), (9, 9)], (F(5, 3), F(5, 3)), True),
        ([(0, 0)], (1, 0), False),
        ([(0, 0)], (0, 0), True),
        ([(1, 0), (0, 1)], (F(1, 5), 0), False),
    ]
    for rows, target, expected in cases:
        assert row_lattice_contains(rows, target) == expected
    assert centered_g([F(0)]*3+[F(1)]*8+[F(9)]*2) == 1
    assert centered_g([F(0)]*6+[F(2)]*8+[F(9)]) == 3
    print('localized row-lattice and fixed coefficient patterns: PASS')


def verify_macros():
    rows = generate()
    expected = {(-1, 0, 0, -1), (-3, 0, 13, 1), (-9, 0, 26, -1),
                (-21, -6, -26, -1), (-7, -2, 33, 9), (-21, -6, 100, 26),
                (-66, -15, -65, -16), (-66, -15, 307, 71)}
    assert {row['integer'] for row in rows} == expected
    special = [(F(1, 9), F(14, 9)), (F(2, 3), F(-25, 9)),
               (1, 1+13*27), (1, 1+5*27), (2, 2+5**3*13**2)]
    parameters = [(u, v) for u in range(-5, 6) for v in range(-5, 6)] + special
    for row in rows:
        matrix = row['integer']
        assert (matrix[0]*matrix[3]-matrix[1]*matrix[2]) % 17
        assert (matrix[0]+matrix[1]-matrix[2]-matrix[3]) % 17 == 0
        for pair in parameters:
            replay(row, pair)
    print('B17 universal macro exact interfaces: PASS', len(rows)*len(parameters))
    names = {(-21, -6, -26, -1): 'R', (-7, -2, 33, 9): 'B',
             (-21, -6, 100, 26): 'C', (-66, -15, -65, -16): 'D',
             (-66, -15, 307, 71): 'E'}
    assert {name: len(word) for name, (word, _) in certificates().items()} == {
        'R': 17, 'B': 17, 'C': 17, 'D': 19, 'E': 19}
    for row in rows:
        if row['integer'] not in names:
            continue
        for pair in parameters:
            x,y = at(row['matrix'][:2], pair), at(row['matrix'][2:], pair)
            actual = apply_atomic(names[row['integer']], *pair)
            assert actual == tuple([x]*13+[y]*3+[-13*x-3*y])
    print('B17 fixed atomic certificates (17,17,17,19,19 steps): PASS', 5*len(parameters))
    return next(row for row in rows if row['integer'] == (-7, -2, 33, 9))


def verify_scheduler(b_row):
    expected_cycle = [(1, 0), (1, 1), (1, 2), (1, 4), (0, 1), (1, 3)]
    current = (1, 0)
    cycle = []
    for _ in range(6):
        cycle.append(current)
        current = projective((at(B[:2], current), at(B[2:], current)), 5)
    assert cycle == expected_cycle and current == cycle[0]
    for point in points(5):
        current = point
        assert len(SCHEDULE[point]) <= 3
        for letter in SCHEDULE[point]:
            matrix = A if letter == 'A' else B
            current = projective((at(matrix[:2], current), at(matrix[2:], current)), 5)
        assert current == (1, 4)
    row15 = next(row for row in guarded_rows() if row['matrix'] == (-3, -3, 13, -2))
    checked = 0
    histogram = Counter()
    for u in range(25):
        for v in range(-24, 25):
            if gcd(u, v) != 1 or (u-v) % 17 == 0:
                continue
            pair = tuple(map(F, (u, v)))
            initial_point = projective(pair, 5)
            histogram[initial_point] += 1
            for letter in SCHEDULE[initial_point]:
                if letter == 'B':
                    pair = replay(b_row, pair)
                else:
                    state = actual_average(core(*pair), (-13*pair[0]-3*pair[1], pair[1], pair[1]))
                    pair = pair[0], -(13*pair[0]+pair[1])/3
                    assert state == core(*pair)
            assert projective(pair, 5) == (1, 4)
            state, _ = contract(core(*pair), [pair[0]]*12+[pair[1]]*2+[-13*pair[0]-3*pair[1]])
            state = actual_average(state, [at(value, pair) for value in row15['triple']])
            pair = at(row15['actual'][:2], pair), at(row15['actual'][2:], pair)
            assert state == core(*pair)
            local_g = centered_g(list(state.elements()))
            assert local_g == 0 or is_three_power(local_g)
            checked += 1
    assert set(histogram) == set(points(5))
    print('B17 six local directions reach a legal 15-call in <=3 returns: PASS', checked)


def verify_norm_theta():
    for u, v in ((1, 0), (0, 1), (1, 1)):
        assert norm(7*u+2*v, -33*u-9*v) == 3*norm(u, v)
    branches = Counter()
    for u in range(-24, 25):
        for v in range(-24, 25):
            if gcd(u, v) != 1:
                continue
            x, y = 7*u+2*v, -33*u-9*v
            content = gcd(x, y)
            assert content in (1, 3)
            assert (content == 3) == ((u-v) % 3 == 0)
            assert norm(x//content, y//content)*content*content == 3*norm(u, v)
            branches[content] += 1
    assert set(branches) == {1, 3}

    bound = 600
    coefficients = [0]*(bound+1)
    selected = [0]*(bound+1)
    conjugate = [0]*(bound+1)
    for x in range(-isqrt(bound), isqrt(bound)+1):
        for y in range(-isqrt(bound//2), isqrt(bound//2)+1):
            value = x*x+2*y*y
            if value <= bound:
                coefficients[value] += 1
                selected[value] += (x-y) % 3 == 0
                conjugate[value] += (x+y) % 3 == 0
    character = {0: 0, 1: 1, 2: 0, 3: 1, 4: 0, 5: -1, 6: 0, 7: -1}
    for value in range(bound+1):
        theta3 = coefficients[value//3] if value % 3 == 0 else 0
        theta9 = coefficients[value//9] if value % 9 == 0 else 0
        assert selected[value] == conjugate[value] == theta3
        assert (coefficients[value] if value % 3 == 0 else 0) == 2*theta3-theta9
        if value:
            assert coefficients[value] == 2*sum(character[d % 8] for d in range(1, value+1) if value % d == 0)
    print('B17 norm-3 similarity and primitive branches: PASS', sum(branches.values()))
    print('discriminant -8 theta and split-prime branch identities: PASS', bound)


def verify_positive_inverse_obstruction():
    axes = {(1, 0), (0, 1)}
    for row in generate():
        a,b,c,d = row['integer']
        for x,y in axes:
            assert projective((a*x+b*y, c*x+d*y), 3) in axes
    conjugate = (-9, -2, 33, 7)
    assert gcd(*conjugate) == 1
    assert projective((conjugate[0], conjugate[2]), 3) is None
    # Every integer product stays nonzero on e1 mod 3; an integer multiple
    # of this primitive conjugate matrix annihilates e1 mod 3.
    print('B17 original universal semigroup has no fixed positive B inverse: PASS')


def fourteen_scheduler():
    states = list(product(points(2), points(7), ((1, 0), (0, 1))))
    goals = {((0, 1), (1, 3), (0, 1)): (-3, -6, 13, 12),
             ((1, 0), (1, 5), (1, 0)): (-6, -3, 12, 13)}
    matrices = {'A': (3, 0, -13, -1), 'B': B_INTEGER}
    reverse = {state: [] for state in states}
    for state in states:
        for letter, (a,b,c,d) in matrices.items():
            target = tuple(projective((a*x+b*y, c*x+d*y), prime)
                           for (x,y), prime in zip(state, (2,7,3)))
            reverse[target].append((state, letter))
    schedule = {state: ('', matrix) for state, matrix in goals.items()}
    queue = deque(goals)
    while queue:
        target = queue.popleft()
        for state, letter in reverse[target]:
            if state not in schedule:
                word, matrix = schedule[target]
                schedule[state] = letter+word, matrix
                queue.append(state)
    assert len(schedule) == len(states) == 48
    assert max(len(word) for word, _ in schedule.values()) == 6
    # Independently check the compact 24-word table printed in the proof.
    for state in states:
        row = points(7).index(state[1])
        column = points(2).index(state[0])
        word = FOURTEEN_WORDS[row][column]
        target = state
        for letter in word:
            a,b,c,d = matrices[letter]
            target = tuple(projective((a*x+b*y, c*x+d*y), prime)
                           for (x,y), prime in zip(target, (2,7,3)))
        assert target in goals
        schedule[state] = word, goals[target]
    return schedule


def verify_fourteen_scheduler():
    schedule = fourteen_scheduler()
    rows = {row['matrix']: row for row in guarded_rows()}
    for signature, (word, matrix) in schedule.items():
        u0 = next(u for u in range(42) if all(u % p == pt[0] for p,pt in zip((2,7,3), signature)))
        v0 = next(v for v in range(42) if all(v % p == pt[1] for p,pt in zip((2,7,3), signature)))
        pair = next(z for k in range(18) if (z := primitive(u0, v0+42*k))[0] != z[1]
                    and (z[0]-z[1]) % 17)
        for letter in word:
            u,v = pair
            pair = (3*u, -13*u-v) if letter == 'A' else (7*u+2*v, -33*u-9*v)
            assert gcd(*pair) == 1
        row = rows[matrix]
        a,b,modulus = row['guard']
        assert (a*pair[0]+b*pair[1]) % modulus == 0
        u,v = map(F, pair)
        state, _ = contract(core(u,v), [u]*row['alpha']+[v]*row['beta']+[-13*u-3*v])
        state = actual_average(state, [at(value, pair) for value in row['triple']])
        x,y = at(row['actual'][:2], pair), at(row['actual'][2:], pair)
        assert x.denominator == y.denominator == 1
        assert state == core(x,y)
        output = primitive(int(x), int(y))
        assert height(output) < height(pair)
        assert (output[0]-output[1]) % 17
    print('B17 mod-(2,7,3) scheduling into an integral 14-return: PASS 48 maxdepth 6')


def verify():
    verify_lattice()
    b_row = verify_macros()
    verify_scheduler(b_row)
    verify_norm_theta()
    verify_positive_inverse_obstruction()
    verify_fourteen_scheduler()


if __name__ == '__main__':
    verify()
