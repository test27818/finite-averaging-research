"""Permutation shadows and the shared determinant character at two levels.

The old n91 automaton stays unchanged as a historical coarse container.
This verifier proves its equality with the macro group is impossible.
"""

from fractions import Fraction as F
from collections import Counter, deque
from itertools import product
from math import gcd
from random import Random

from verify_flat_star_arithmetic import identity, inverse, multiply


def reduce_fraction(value,modulus):
    value = F(value)
    return value.numerator*pow(value.denominator,-1,modulus) % modulus


def transpose(a):
    return list(map(list,zip(*a)))


def verify_permutation_shadows():
    checked = 0
    for exponents in ((0,1,2),(0,2,4),(1,4,7),(0,1,1,3),(2,4,8,10)):
        weights = [3**k for k in exponents]
        rank = len(weights)
        step = gcd(*(abs(k-exponents[0]) for k in exponents))
        modulus = 3**step-1
        gram = [[F(weights[i]) if i == j else F(0) for j in range(rank)]
                for i in range(rank)]
        for i in range(rank):
            for j in range(rank):
                if weights[i] <= weights[j]:
                    continue
                ratio = F(weights[j],weights[i])
                exchange = identity(rank)
                exchange[i][i],exchange[i][j] = 1-ratio,ratio
                exchange[j][i],exchange[j][j] = F(1),F(0)
                image = multiply(multiply(transpose(exchange),gram),exchange)
                coefficient = weights[j]*(1-ratio)
                difference = [[gram[a][b]-image[a][b] for b in range(rank)] for a in range(rank)]
                expected = [[coefficient*(int(a==i)-int(a==j))*(int(b==i)-int(b==j))
                             for b in range(rank)] for a in range(rank)]
                assert difference == expected
                permutation = identity(rank)
                permutation[i],permutation[j] = permutation[j],permutation[i]
                assert [[reduce_fraction(x,modulus) for x in row] for row in exchange] == permutation
                checked += 1
    print('weighted variance defects and exact permutation shadows: PASS',checked)


def matrix_tuple(a,modulus):
    return tuple(reduce_fraction(x,modulus) for row in a for x in row)


def mul_mod(a,b,modulus):
    x,y,z,w = a
    p,q,r,s = b
    return ((x*p+y*r)%modulus,(x*q+y*s)%modulus,
            (z*p+w*r)%modulus,(z*q+w*s)%modulus)


def character_data(root):
    s = root*root
    n = s*s+s+1
    modulus = s-1
    multiplier = {}
    for j in range(6):
        for sign in (-1,1):
            value = sign*pow(root,j,n) % n
            assert value not in multiplier
            multiplier[value] = j % 2
    c = (0,1,-1,-1)
    cycle = [(1,0,0,1),tuple(x % modulus for x in c),mul_mod(c,c,modulus)]
    local = {}
    for j in range(2):
        for sign in (-1,1):
            for matrix in cycle:
                value = tuple(sign*root**j*x % modulus for x in matrix)
                assert value not in local
                local[value] = j
    assert len(multiplier) == len(local) == 12
    for a,ca in multiplier.items():
        for b,cb in multiplier.items():
            assert multiplier[a*b%n] == ca ^ cb
    for a,ca in local.items():
        for b,cb in local.items():
            assert local[mul_mod(a,b,modulus)] == ca ^ cb
    return n,modulus,multiplier,local


def coupled_characters(matrix,root):
    n,modulus,multipliers,local = character_data(root)
    a,b,c,d = matrix
    lam = (a-c) % n
    assert (b-d) % n == -lam % n
    return multipliers[lam],local[tuple(x % modulus for x in matrix)]


def verify_joint_words():
    random = Random(9181)
    checked = 0
    for root in (3,9,27):
        s = root*root
        n,modulus,multipliers,local = character_data(root)
        combined = n*modulus
        generators = [
            [[F(root),F(0)],[F(-root**3),F(-1,root)]],
            [[F(s-1,root),F(1,root)],[F(root),F(0)]],
            [[F(-1,s),F(-1)],[F(0),F(s)]],
        ]
        choices = [(matrix_tuple(g,combined),degree) for g,degree in zip(generators,(1,1,2))]
        choices += [(matrix_tuple(inverse(g),combined),-degree) for g,degree in zip(generators,(1,1,2))]
        for _ in range(80):
            matrix = (1,0,0,1)
            degree = 0
            for _ in range(2*random.randrange(1,13)):
                generator,step = random.choice(choices)
                matrix = mul_mod(generator,matrix,combined)
                degree += step
            a,b,c,d = matrix
            assert (a*d-b*c) % combined == 1
            lam = (a-c) % n
            assert (b-d) % n == -lam % n
            assert lam == pow(root,-degree,n)
            assert multipliers[lam] == local[tuple(x % modulus for x in matrix)] == degree % 2
            checked += 1
    print('shared determinant character on normalized cyclotomic words: PASS',checked)


def sl2_order(modulus):
    result = modulus**3
    value = modulus
    prime = 2
    while prime*prime <= value:
        if value % prime == 0:
            result = result//(prime*prime)*(prime*prime-1)
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        result = result//(value*value)*(value*value-1)
    return result


def verify_n91_strict_refinement():
    from cyclotomic_congruence import macro_local_orientation_image
    from analyze_cyclotomic_local_images import canonical
    n,modulus,multipliers,local = character_data(3)
    witness = (547,728,74256,98827)
    a,b,c,d = witness
    assert a*d-b*c == 1
    assert tuple(x % n for x in witness) == (1,0,0,1)
    assert tuple(x % modulus for x in witness) == (3,0,0,3)
    assert canonical(witness,modulus) in macro_local_orientation_image(9,modulus)
    assert coupled_characters(witness,3) == (0,1)
    global_size = len(multipliers)*n
    local_size = len(local)
    fiber_size = sum(1 for lam in multipliers for _ in range(n)
                     for matrix in local if multipliers[lam] == local[matrix])
    total = sl2_order(n)*sl2_order(modulus)
    assert total//(global_size*local_size) == 21504
    assert total//fiber_size == 43008
    assert sum((a*d-b*c) % 8 == 1 for a,b,c,d in product(range(8),repeat=4)) == sl2_order(8)
    print('n91 old-container strict witness and coupled index: PASS 21504 43008')


def verify_coupled_schreier_cover():
    from cyclotomic_congruence import congruence_automaton
    from explore_thirteen_modular import S,U
    labels,old,base,_,_ = congruence_automaton(9)
    n,modulus,multipliers,local = character_data(3)
    combined = n*modulus
    generators = {'s':S,'u':U}
    representatives = {base:(1,0,0,1)}
    queue = deque([base])
    while queue:
        node = queue.popleft()
        for letter,generator in generators.items():
            target = old[node,letter]
            if target not in representatives:
                representatives[target] = mul_mod(representatives[node],generator,combined)
                queue.append(target)
    assert len(representatives) == 21504
    new = {}
    for node,representative in representatives.items():
        for letter,generator in generators.items():
            target = old[node,letter]
            a,b,c,d = representatives[target]
            target_inverse = d,-b,-c,a
            loop = mul_mod(mul_mod(representative,generator,combined),target_inverse,combined)
            a,b,c,d = loop
            lam = (a-c) % n
            assert (b-d) % n == -lam % n
            character = multipliers[lam] ^ local[tuple(x % modulus for x in loop)]
            for bit in (0,1):
                new[2*node+bit,letter] = 2*target+(bit ^ character)
    start = 2*base
    reached = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for letter in 'su':
            target = new[node,letter]
            if target not in reached:
                reached.add(target)
                queue.append(target)
    assert len(reached) == 43008
    assert all(new[new[node,'s'],'s'] == node for node in reached)
    assert all(new[new[new[node,'u'],'u'],'u'] == node for node in reached)
    e2 = sum(new[node,'s'] == node for node in reached)
    e3 = sum(new[node,'u'] == node for node in reached)
    unused = set(reached)
    widths = Counter()
    legal = 0
    while unused:
        initial = next(iter(unused))
        node = initial
        length = 0
        while node in unused:
            unused.remove(node)
            length += 1
            node = new[new[node,'s'],'u']
        assert node == initial
        widths[length] += 1
        legal += gcd(labels[initial//2][0][0],n) == 1
    cusps = sum(widths.values())
    genus = 1+len(reached)//12-e2//4-e3//3-cusps//2
    assert (e2,e3,cusps,legal,genus) == (0,48,192,48,3473)
    assert widths == {8:48,56:48,104:48,728:48}
    assert genus == 2*1737-1
    print('n91 coupled Schreier cover and unramified genus check: PASS 43008 192 48 3473')


def verify():
    verify_permutation_shadows()
    verify_joint_words()
    verify_n91_strict_refinement()
    verify_coupled_schreier_cover()


if __name__ == '__main__':
    verify()
