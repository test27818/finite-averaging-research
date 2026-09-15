"""Exact interfaces for positive modular control and the two-exception core.

The general finite-ring generation proof is in the accompanying document.
Only the small mod5 field image is enumerated; no large state BFS is used.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd
from random import Random
from itertools import combinations

from verify_flat_star_arithmetic import identity, inverse, multiply, product, rank_one
from verify_fifteen_via_subblocks import centered_g
from verify_general_lifting import primitive,prime_divisors,equalize_power_of_three


def coefficient(value,modulus):
    value = F(value)
    return value.numerator*pow(value.denominator,-1,modulus) % modulus


def mod_matrix(matrix,modulus):
    return tuple(tuple(coefficient(x,modulus) for x in row) for row in matrix)


def mod_image(matrix,x,modulus):
    return tuple(sum(a*b for a,b in zip(row,x)) % modulus for row in matrix)


def carrier(r,index,which):
    # Parameters are (u_0,...,u_(r-1),w), with z=-3 sum(u)-w.
    matrix = identity(r+1)
    if which == 'w':
        matrix[index] = [F(2,3)*int(j==index)+F(1,3)*int(j==r) for j in range(r+1)]
        matrix[r] = [F(j==index) for j in range(r+1)]
    else:
        assert which == 'z'
        matrix[index] = [F(-1)+F(2,3)*int(j==index) for j in range(r)]+[F(-1,3)]
    return matrix


def natural_lift(r,matrix,which):
    # A local zero-mean block with mass a is complemented by its own mean.
    a = 3*r+1
    cols = []
    for j in range(r+1):
        values = [F(k==j) for k in range(r+1)]
        u,w = values[:r],values[r]
        z = -3*sum(u)-w
        fixed = z if which == 'w' else w
        mean = -fixed/a
        deviations = [v-mean for v in u]
        output = [sum(c*v for c,v in zip(row,deviations))+mean for row in matrix]
        moving = -fixed-3*sum(output)
        cols.append(output+[moving if which == 'w' else fixed])
    return [list(row) for row in zip(*cols)]


def verify_two_levi_gluing():
    checked = 0
    for r in range(4,13):
        a,n = 3*r+1,3*r+2
        size = r+1
        # B-coordinates: natural u=x+t*1, w=-a*t.
        q = identity(size)
        q[-1][-1] = -a
        for j in range(r):
            q[j][-1] = 1
        qi = inverse(q)
        i,j,k = 0,1,2
        v = [F(t==i)-F(t==j) for t in range(r)]+[F(0)]
        source = [F(t==k) for t in range(r)]+[F(n)]
        upper = rank_one(v,source)
        natural = product(q,upper,qi)
        assert natural[-1] == identity(size)[-1]
        constant_a = [F(1)]*(r+1)
        assert [sum(c*x for c,x in zip(row,constant_a)) for row in natural] == constant_a
        # Local A fixes z and fixes its local constant vector.
        zrow = [F(-3)]*r+[F(-1)]
        assert [sum(zrow[t]*natural[t][col] for t in range(size)) for col in range(size)] == zrow
        top = rank_one(v,[F(t==k) for t in range(size)])
        extracted = product(inverse(top),upper)
        assert extracted == rank_one(v,[F(t==r) for t in range(size)],n)

        f = [F(t==1)-F(t==2) for t in range(size)]
        center = [F(t==i)-F(3,a) for t in range(r)]+[F(3,a)]
        lower = rank_one(center,f)
        natural = product(q,lower,qi)
        assert natural == rank_one([F(t==i)-3*F(t==r) for t in range(size)],f)
        top = rank_one(center[:-1]+[F(0)],f)
        assert product(inverse(top),lower) == rank_one([F(t==r) for t in range(size)],f,F(3,a))
        # No division by r is needed, including moduli dividing r.
        for modulus in (5,7,25,35):
            if gcd(modulus,6*a*n) != 1:
                continue
            assert gcd(n,modulus) == gcd(a,modulus) == 1
            mod_matrix(extracted,modulus)
            mod_matrix(lower,modulus)
        checked += 1
    print('two-carrier finite-ring Levi gluing without division by r: PASS',checked)


def verify_local_principal_lifts():
    checked = 0
    for p in (17,23,29,41,47,53,59,71,83,89,35,65,95,119,143,185,209):
        r = (p-2)//3
        a = p-1
        m = r
        while m % 3 == 0:
            m //= 3
        level = (192*a)**2
        assert gcd(m,level*p) == 1
        for which in ('w','z'):
            local = identity(r)
            local[0][1] = level*p
            lifted = natural_lift(r,local,which)
            assert all(x.denominator == 1 for row in lifted for x in row)
            assert mod_matrix(lifted,p) == mod_matrix(identity(r+1),p)
            if m > 1:
                assert mod_matrix(lifted,m) != mod_matrix(identity(r+1),m)
            checked += 1
    print('principal local words lift integrally and protect modp: PASS',checked)


def mixed_partition(values):
    n = len(values)
    r = (n-2)//3
    assert n >= 17 and n % 6 == 5
    blocks = [list(range(3*i,3*i+3)) for i in range(r)]+[[n-2],[n-1]]
    protected = []
    repairs = 0
    def means(prime):
        return [sum(values[i] for i in block)*pow(len(block),-1,prime) % prime for block in blocks]
    for prime in prime_divisors(n):
        residues = means(prime)
        if len(set(residues)) > 1:
            protected.append(prime)
            continue
        found = False
        for left,right in combinations(range(len(blocks)),2):
            for i in range(len(blocks[left])):
                for j in range(len(blocks[right])):
                    a,b = blocks[left][i],blocks[right][j]
                    if (values[a]-values[b]) % prime == 0:
                        continue
                    blocks[left][i],blocks[right][j] = b,a
                    if all(len(set(means(q))) > 1 for q in protected):
                        found = True
                        repairs += 1
                        break
                    blocks[left][i],blocks[right][j] = a,b
                if found:break
            if found:break
        assert found
        protected.append(prime)
    return blocks,repairs


def verify_mixed_partitions():
    random = Random(455017)
    checked = repairs = 0
    for n in (17,29,35,41,65,95,119,143,185,209,455):
        cases = [[1,-1,0]*((n-2)//3)+[0,0]]
        for _ in range(14):
            x = [random.randrange(-100,101) for _ in range(n-1)]
            x.append(-sum(x))
            cases.append(list(primitive(x)))
        for x in cases:
            if centered_g(list(map(F,x))) != 1:
                continue
            blocks,count = mixed_partition(x)
            assert sorted(i for block in blocks for i in block) == list(range(n))
            out = [F(0)]*n
            for block in blocks:
                mean = sum(F(x[i]) for i in block)/len(block)
                for i in block:out[i] = mean
            assert centered_g(out) == 1 and sum(out) == 0
            checked += 1
            repairs += count
    print('mixed triple-and-singleton simultaneous partitions: PASS',checked,repairs)


def verify_small_positive_orbit():
    p,r,modulus = 17,5,5
    generators = [mod_matrix(carrier(r,i,which),modulus)
                  for i in range(r) for which in ('w','z')]
    start = (1,)+(0,)*r
    seen = {start}
    queue = deque([start])
    while queue:
        values = queue.popleft()
        for matrix in generators:
            target = mod_image(matrix,values,modulus)
            if target not in seen:
                seen.add(target)
                queue.append(target)
    assert len(seen) == modulus**(r+1)-1
    target = (1,-1,0,0,0,0)
    assert tuple(x % modulus for x in target) in seen
    for i in range(r):
        for which in ('w','z'):
            matrix = carrier(r,i,which)
            power = identity(r+1)
            order = 0
            while True:
                order += 1
                power = multiply(matrix,power)
                if mod_matrix(power,modulus) == mod_matrix(identity(r+1),modulus):
                    break
                assert order < 100
            assert mod_matrix(multiply(matrix,inverse(matrix)),modulus) == mod_matrix(identity(r+1),modulus)
    print('positive carrier orbit modulo5 on p17 parameters: PASS',len(seen))


def verify_finite_inverse_formula():
    checked = 0
    for modulus in (5,7,11,17,25,35,55,85,125,455):
        scalar = -pow(3,-1,modulus) % modulus
        value,order = scalar,1
        while value != 1:
            value = value*scalar % modulus
            order += 1
        assert order < modulus
        for which in ('w','z'):
            t = carrier(5,0,which)
            projector = [[F(-3,4)*(x-int(i==j)) for j,x in enumerate(row)] for i,row in enumerate(t)]
            assert multiply(projector,projector) == projector
            power = identity(6)
            for _ in range(order):
                power = [[F(x) for x in row] for row in mod_matrix(multiply(t,power),modulus)]
            assert mod_matrix(power,modulus) == mod_matrix(identity(6),modulus)
            checked += 1
    print('uniform positive modular inverse exponent formula: PASS',checked)


def verify_physical_modular_schedules():
    total = 0
    for n in (17,29,35,41,65):
        r = (n-2)//3
        m = r
        while m % 3 == 0:m //= 3
        modulus = n*m
        scalar = -pow(3,-1,modulus) % modulus
        value,order = scalar,1
        while value != 1:
            value = value*scalar % modulus
            order += 1
        w = crt(0,m,1,n)
        leaf_values = [F(1),F(-1)]+[F(0)]*(r-2)
        state = [x for value in leaf_values for x in [value]*3]+[F(w),F(-w)]
        groups = [list(range(3*i,3*i+3)) for i in range(r)]
        carriers = [n-2,n-1]
        def step(index,which):
            old = groups[index]
            selected = old[:2]+[carriers[which]]
            mean = sum(state[i] for i in selected)/3
            for i in selected:state[i] = mean
            groups[index] = selected
            carriers[which] = old[2]
        scramble = ((0,0),(1,1),(2,0),(r-1,1))
        for index,which in scramble:step(index,which)
        assert centered_g(state) == 1
        for index,which in reversed(scramble):
            for _ in range(order-1):
                step(index,which)
                total += 1
        u = [state[group[0]] for group in groups]
        assert all(state[i] == u[j] for j,group in enumerate(groups) for i in group)
        target = [1,-1]+[0]*(r-2)
        assert [coefficient(value,modulus) for value in u] == [x % modulus for x in target]
        assert [coefficient(state[i],modulus) for i in carriers] == [w % modulus,-w % modulus]
        indices = [i for group in groups for i in group]
        child = [state[i] for i in indices]
        assert is_power_three(centered_g(child))
        mean = sum(child)/len(child)
        assert coefficient(mean,n) == 0
        assert centered_g([mean]*(n-2)+[state[i] for i in carriers]) == 1
        if n == 29:
            operations = []
            result = equalize_power_of_three(tuple(state),indices,operations)
            assert all(result[i] == mean for i in indices)
            assert len(operations) == 27 and centered_g(result) == 1
            total += len(operations)
    print('fixed-position positive modular schedules and n29 physical child: PASS 5',total)


def crt(a,m,b,p):
    return a+m*((b-a)*pow(m,-1,p) % p)


def verify_child_bridge():
    random = Random(41470910)
    checked = 0
    for p in (17,23,29,41,47,53,59,71,83,89,101,107,113,35,65,95,119,143,185,209):
        r = (p-2)//3
        m = r
        while m % 3 == 0:
            m //= 3
        for _ in range(24):
            desired = [1,-1]+[0]*(r-2)
            # Over modp keep carriers w=1,z=-1 and nonconstant leaves.
            residue_p = [1,-1]+[0]*(r-2)
            u = [crt(x,m,y,p)+m*p*random.randrange(-10,11) for x,y in zip(desired,residue_p)]
            w = crt(0,m,1,p)+m*p*random.randrange(-10,11)
            z = -3*sum(u)-w
            leaves = [F(x) for x in u for _ in range(3)]
            assert centered_g(leaves) == 1 or is_power_three(centered_g(leaves))
            mu = sum(leaves)/len(leaves)
            assert is_power_three(mu.denominator)
            state = leaves+[F(w),F(z)]
            result = [mu]*(p-2)+[F(w),F(z)]
            assert centered_g(state) == centered_g(result) == 1
            assert (w-z) % p == 2
            checked += 1
    print('legal p-minus-two child and preserved prime two-exception output: PASS',checked)


def is_power_three(value):
    if value < 1:
        return False
    while value % 3 == 0:
        value //= 3
    return value == 1


def verify_core_call_boundary():
    checked = 0
    for p in (17,23,41,47,53,59,71,89):
        size = p-2
        nonthree = size
        while nonthree % 3 == 0:
            nonthree //= 3
        assert nonthree > 1
        for u in range(-2,3):
            for a in range(-4,5):
                b = -(p-2)*u-a
                state = [F(u)]*(p-2)+[F(a),F(b)]
                if len(set(state)) < 3 or centered_g(state) != 1:
                    continue
                # Omitting one carrier and a background entry leaves a
                # two-value child with just one exceptional coordinate.
                for exceptional in (a,b):
                    child = [F(u)]*(p-3)+[F(exceptional)]
                    g = centered_g(child)
                    while g % 3 == 0:
                        g //= 3
                    assert g == nonthree
                # Omitting two background values gives only two values
                # after formal equalization, hence an illegal nonzero state.
                child = [F(u)]*(p-4)+[F(a),F(b)]
                mean = sum(child)/size
                output = [mean]*size+[F(u),F(u)]
                if u:
                    assert centered_g(output) == p
                else:
                    assert mean == 0 and not any(output)
                checked += 1
    state = [F(5)]*15+[F(1),F(-76)]
    child = [F(5)]*13+[F(1),F(-76)]
    assert centered_g(state) == 1 and is_power_three(centered_g(child))
    assert centered_g([sum(child)/15]*15+[F(5),F(5)]) == 17
    print('two-exception full-child call boundary away from terminal: PASS',checked)


def verify_diagonal_core():
    checked = 0
    for n in (17,29,35,41,65,95,119,143):
        for u in range(-4,5):
            for a in range(-5,6):
                if gcd(u,a) != 1:continue
                b = -(n-2)*u-a
                y = a-b
                state = [F(u)]*(n-2)+[F(a),F(b)]
                assert 2*sum(x*x for x in state) == n*(n-2)*u*u+y*y
                assert centered_g(state) == gcd(y,n)
                if gcd(y,n) != 1:continue
                v = F(a+2*u,3)
                output = [F(u)]*(n-4)+[v]*3+[F(b)]
                assert centered_g(output) == 1 and sum(output) == 0
                assert (n-4)*u+4*v == F(n*u+2*y,3)
                checked += 1
    print('two-exception norm form and globally safe standard B-core entry: PASS',checked)


def verify():
    verify_mixed_partitions()
    verify_two_levi_gluing()
    verify_local_principal_lifts()
    verify_small_positive_orbit()
    verify_finite_inverse_formula()
    verify_physical_modular_schedules()
    verify_child_bridge()
    verify_core_call_boundary()
    verify_diagonal_core()


if __name__ == '__main__':
    verify()
