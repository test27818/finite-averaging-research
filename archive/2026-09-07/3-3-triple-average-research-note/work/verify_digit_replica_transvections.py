"""Uniform digit-averaging cycles and balanced transvections on three copies.

These are real 3n-position words, not proofs of n-position cancellation.
Integer sparse identities establish the operator formulas independently
of the finite physical coefficient replays.
"""

from fractions import Fraction as F
from math import gcd
from random import Random


def digit_order(n,arity=3):
    assert gcd(n,arity) == 1
    value = arity % n
    exponent = 1
    while value != 1:
        value = arity*value % n
        exponent += 1
        assert exponent <= n
    return exponent


def order_three(n):
    return digit_order(n)


def digit_matrix(n,arity=3):
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for digit in range(arity):
            matrix[i][(arity*i+digit) % n] += 1
    return matrix


def digit_counts(n,length,arity=3):
    counts = [1]+[0]*(n-1)
    for _ in range(length):
        following = [0]*n
        for i,count in enumerate(counts):
            for digit in range(arity):
                following[(arity*i+digit) % n] += count
        counts = following
    return counts


def transvection_data(n,arity=3):
    assert n >= 5 and gcd(n,arity) == 1 and arity % n not in (1,n-1)
    inverse = pow(arity,-1,n)
    g = [0]*n
    for position in range(inverse):
        g[position] += 1
        g[(position+inverse)%n] -= 1
    i,j = inverse-1,inverse
    h = g.copy()
    h[i] -= 1
    h[j] += 1
    k = next(position for position,value in enumerate(h) if value == 1)
    ell = next(position for position,value in enumerate(h)
               if value == 0 and position not in (i,j))
    assert len({i,j,k,ell}) == 4
    assert h[i] == h[j] == 0 and h[k] == 1 and h[ell] == 0
    return i,j,k,ell,g,h


def verify_integer_identities():
    tested = 0
    for n in range(5,101):
        if n % 3 == 0:
            continue
        K = digit_matrix(n)
        assert all(sum(row) == 3 for row in K)
        assert all(sum(K[i][j] for i in range(n)) == 3 for j in range(n))
        for i in range(n):
            # K(I-S)=(I-S)F, with (Fx)_i=x_(3i).
            left = [0]*n
            for j,c in enumerate(K[i]):
                left[j] += c
                left[(j+1)%n] -= c
            right = [0]*n
            right[3*i%n] += 1
            right[3*(i+1)%n] -= 1
            assert left == right
        period = order_three(n)
        q = (3**period-1)//n
        assert digit_counts(n,period) == [q+1]+[q]*(n-1)
        i,j,k,ell,g,h = transvection_data(n)
        assert [K[z][0]-K[z][1] for z in range(n)] == [int(z==i)-int(z==j) for z in range(n)]
        assert [sum(g[z]*K[z][w] for z in range(n)) for w in range(n)] == [int(w==0)-int(w==1) for w in range(n)]
        swapped = h.copy()
        swapped[k],swapped[ell] = swapped[ell],swapped[k]
        assert [a-b for a,b in zip(h,swapped)] == [int(z==k)-int(z==ell) for z in range(n)]
        tested += 1
    print('digit intertwiner, scalar periods and balanced transvection identities: PASS',tested)


def physical_transvection(n,arity=3):
    period = digit_order(n,arity)
    i,j,k,ell,_,_ = transvection_data(n,arity)
    width = n-1
    inputs = [tuple(F(int(a==b)) for b in range(width)) for a in range(width)]
    inputs.append(tuple(F(-1) for _ in range(width)))
    state = [value for value in inputs for _ in range(arity)]
    groups = [list(range(arity*a,arity*(a+1))) for a in range(n)]
    operations = 0
    def digit_layer():
        nonlocal groups,operations
        unused = [group.copy() for group in groups]
        following = []
        for a in range(n):
            selected = [unused[(arity*a+d)%n].pop() for d in range(arity)]
            assert len(set(selected)) == arity
            average = tuple(sum(state[position][b] for position in selected)/arity for b in range(width))
            for position in selected:
                state[position] = average
            following.append(selected)
            operations += 1
        assert all(not group for group in unused)
        groups = following
    V = [('P',None)]*(period-1)+[('swap',(0,1)),('P',None),('swap',(i,j))]
    V_inverse = [('swap',(i,j))]+[('P',None)]*(period-1)+[('swap',(0,1)),('P',None)]
    word = [('swap',(k,ell))]+V_inverse+[('swap',(k,ell))]+V
    for name,pair in word:
        if name == 'P':
            digit_layer()
        else:
            a,b = pair
            groups[a],groups[b] = groups[b],groups[a]
    scale = F(1,arity**(2*period))
    for a,group in enumerate(groups):
        sign = int(a==i)-int(a==j)
        expected = tuple(scale*(inputs[a][b]+sign*(inputs[k][b]-inputs[ell][b])) for b in range(width))
        assert all(state[position] == expected for position in group)
    assert operations == 2*n*period
    return operations


def verify_general_arity():
    checked = 0
    for arity in range(2,13):
        for n in range(max(5,arity+2),46):
            if gcd(n,arity) != 1:
                continue
            K = digit_matrix(n,arity)
            i,j,k,ell,g,h = transvection_data(n,arity)
            assert [K[z][0]-K[z][1] for z in range(n)] == [int(z==i)-int(z==j) for z in range(n)]
            assert [sum(g[z]*K[z][w] for z in range(n)) for w in range(n)] == [int(w==0)-int(w==1) for w in range(n)]
            period = digit_order(n,arity)
            quotient = (arity**period-1)//n
            assert digit_counts(n,period,arity) == [quotient+1]+[quotient]*(n-1)
            checked += 1
    operations = sum(physical_transvection(n,arity)
                     for n,arity in ((5,2),(7,4),(7,5),(11,6)))
    print('general q-averaging interval identity and replica transvections: PASS',checked,operations)


def difference_gcd(values):
    return gcd(*(x-values[0] for x in values))


def balanced_normal_form(values):
    x = list(values)
    n = len(x)
    total = sum(x)
    assert n >= 5 and difference_gcd(x) == 1
    word = []
    def take(i,j,k,ell,q):
        assert len({i,j,k,ell}) == 4
        if q:
            delta = q*(x[k]-x[ell])
            x[i] += delta
            x[j] -= delta
            word.append((i,j,k,ell,q))
    def shortest():
        ordered = sorted((value,i) for i,value in enumerate(x))
        return min((a-b,i,j) for (b,j),(a,i) in zip(ordered,ordered[1:]) if a != b)
    def reduce_outside(a,b,d):
        outside = [i for i in range(n) if i not in (a,b)]
        ell = outside[0]
        i = next((i for i in outside if (x[i]-x[ell]) % d),None)
        if i is None:
            return False
        j = next(j for j in outside if j not in (i,ell))
        q = -((x[i]-x[ell]+d//2)//d)
        take(i,j,a,b,q)
        assert 0 < abs(x[i]-x[ell]) <= d//2
        return True
    initial_d,_,_ = shortest()
    iterations = 0
    while True:
        d,a,b = shortest()
        if d == 1:
            break
        if not reduce_outside(a,b,d):
            outside = [i for i in range(n) if i not in (a,b)]
            i,ell,j = outside[:3]
            assert (x[a]-x[i]) % d
            assert (x[i]-x[ell]) % d == 0
            take(i,j,a,b,(d-x[i]+x[ell])//d)
            assert x[i]-x[ell] == d
            assert reduce_outside(i,ell,d)
        assert shortest()[0] <= d//2 and difference_gcd(x) == 1
        iterations += 1
    buffer = next(i for i in range(n) if i not in (a,b))
    zeros = [i for i in range(n) if i not in (a,b,buffer)]
    for i in zeros:
        take(i,buffer,a,b,-x[i])
        assert x[i] == 0
    k,ell = zeros[:2]
    take(k,buffer,a,b,1)
    assert x[k] == 1 and x[ell] == 0
    take(a,buffer,k,ell,-x[a])
    take(b,buffer,k,ell,-x[b])
    assert x == [int(i==k)+(total-1)*int(i==buffer) for i in range(n)]
    assert len(word) <= 2*initial_d.bit_length()+n
    return tuple(x),tuple(word),iterations


def balanced_reduce(values):
    assert sum(values) == 0
    return balanced_normal_form(values)


def physical_balanced_word(values,word):
    n = len(values)
    period = order_three(n)
    ci,cj,ck,cl,_,_ = transvection_data(n)
    state = [F(x) for x in values for _ in range(3)]
    groups = [list(range(3*i,3*i+3)) for i in range(n)]
    operations = 0
    def triple(indices):
        nonlocal operations
        average = sum((state[i] for i in indices),F(0))/3
        for i in indices:
            state[i] = average
        operations += 1
    def digit_layer():
        nonlocal groups
        available = [group.copy() for group in groups]
        output = []
        for i in range(n):
            indices = [available[(3*i+d)%n].pop() for d in range(3)]
            triple(indices)
            output.append(indices)
        assert all(not row for row in available)
        groups = output
    V = [('P',None)]*(period-1)+[('swap',(0,1)),('P',None),('swap',(ci,cj))]
    V_inverse = [('swap',(ci,cj))]+[('P',None)]*(period-1)+[('swap',(0,1)),('P',None)]
    unit_word = [('swap',(ck,cl))]+V_inverse+[('swap',(ck,cl))]+V
    abstract = list(values)
    scale = F(1)
    for i,j,k,ell,q in word:
        permutation = [None]*n
        targets = (i,j,k,ell) if q > 0 else (i,j,ell,k)
        for source,target in zip((ci,cj,ck,cl),targets):
            permutation[source] = target
        unused = iter(target for target in range(n) if target not in targets)
        for source in range(n):
            if permutation[source] is None:
                permutation[source] = next(unused)
        for _ in range(abs(q)):
            groups = [groups[target] for target in permutation]
            for name,pair in unit_word:
                if name == 'P':
                    digit_layer()
                else:
                    a,b = pair
                    groups[a],groups[b] = groups[b],groups[a]
            restored = [None]*n
            for source,target in enumerate(permutation):
                restored[target] = groups[source]
            groups = restored
            scale /= 3**(2*period)
        delta = q*(abstract[k]-abstract[ell])
        abstract[i] += delta
        abstract[j] -= delta
        assert all(state[position] == scale*abstract[a] for a,group in enumerate(groups) for position in group)
    positive = abstract.index(1)
    negative = abstract.index(-1)
    zero = abstract.index(0)
    for copy in range(3):
        triple((groups[positive][copy],groups[negative][copy],groups[zero][copy]))
    assert not any(state)
    assert operations == 2*n*period*sum(abs(step[-1]) for step in word)+3
    return operations


def verify_balanced_euclid():
    random = Random(20260910)
    checked = 0
    max_descent = 0
    for n in range(5,25):
        for _ in range(80):
            x = [random.randrange(-10000,10001) for _ in range(n-1)]
            x.append(-sum(x))
            if difference_gcd(x) != 1:
                continue
            _,word,iterations = balanced_reduce(x)
            max_descent = max(max_descent,iterations)
            checked += 1
    operations = 0
    for x in ((-2,-1,0,1,2),(-3,-1,0,0,1,1,2)):
        _,word,_ = balanced_reduce(x)
        operations += physical_balanced_word(x,word)
    print('balanced Euclidean reduction to a root: PASS',checked,'maximum gcd stages',max_descent)
    print('complete three-copy zeroing words independently replayed: PASS',operations)


def verify_affine_orbits():
    random = Random(7625)
    checked = 0
    for n in range(5,21):
        for _ in range(30):
            y = [random.randrange(-100,101) for _ in range(n)]
            if difference_gcd(y) != 1:
                continue
            d = random.randrange(1,20)
            c = random.randrange(d)
            x = [c+d*value for value in y]
            total = sum(x)
            final,word,_ = balanced_normal_form(y)
            for i,j,k,ell,q in word:
                delta = q*(x[k]-x[ell])
                x[i] += delta
                x[j] -= delta
                assert sum(x) == total and difference_gcd(x) == d
                assert x[0] % d == c
            assert x == [c+d*value for value in final]
            assert sorted(x) == sorted([c]*(n-2)+[c+d,c+d*(sum(y)-1)])
            for i,j,k,ell,q in reversed(word):
                delta = q*(x[k]-x[ell])
                x[i] -= delta
                x[j] += delta
            assert x == [c+d*value for value in y]
            checked += 1
    print('full integer affine-lattice orbit normal forms: PASS',checked)


def verify_three_divisible_integration():
    from compile_bn_integer_templates import certificate_size, solved_size
    from verify_general_lifting import (
        equalize_power_of_three, good_simultaneous_partition,
        prime_divisors, primitive,
    )
    random = Random(8729)
    checked = 0
    largest = 0
    for m in (5,7,11,29,31,35,58,145,203):
        for r in (3,9):
            n = m*r
            cases = [[1,-1,0]*(n//3)]
            for _ in range(5):
                values = [random.randrange(-50,51) for _ in range(n-1)]
                values.append(-sum(values))
                cases.append(list(primitive(values)))
            for values in cases:
                if any(difference_gcd(values) % p == 0 for p in prime_divisors(m)):
                    continue
                blocks,sums = good_simultaneous_partition(values,m,r)
                assert sorted(i for block in blocks for i in block) == list(range(n))
                assert all(len(block) == r for block in blocks)
                quotient = primitive(sums)
                assert sum(quotient) == 0 and difference_gcd(quotient) == 1
                final,word,_ = balanced_reduce(quotient)
                replay = list(quotient)
                for i,j,k,ell,q in word:
                    delta = q*(replay[k]-replay[ell])
                    replay[i] += delta
                    replay[j] -= delta
                assert tuple(replay) == final and sorted(final) == [-1]+[0]*(m-2)+[1]
                if m == 29 and r == 3:
                    physical = tuple(map(F,values))
                    operations = []
                    for block in blocks:
                        physical = equalize_power_of_three(physical,block,operations)
                    assert all(physical[i] == F(total,r)
                               for block,total in zip(blocks,sums) for i in block)
                assert solved_size(n)
                largest = max(largest,n)
                checked += 1
    assert solved_size(87) and not certificate_size(87)
    assert solved_size(53) and solved_size(59)
    assert not solved_size(71) and not solved_size(6)
    print('three-divisible partition and replica-controller integration: PASS',checked,'largest N',largest)


def verify_level_boundary():
    checked = 0
    for p in (5,7,11,13):
        for exponent in (2,3,4):
            modulus = p**exponent
            # [[1,0],[p,1]] preserves u-v!=0 modp in both directions,
            # but does not preserve [1:1] modp^exponent.
            assert p % modulus != 0
            for u in range(p):
                for v in range(p):
                    assert (u-v) % p == (u-(p*u+v)) % p
                    assert (u-v) % p == (u-(-p*u+v)) % p
            checked += 1
    print('legal-domain level-p versus universal-operator level-p^k boundary: PASS',checked)


def verify_ordered_braid_boundary():
    def path(weights,word):
        weights = list(weights)
        matrix = [list(row) for row in ((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)))]
        for i in word:
            a,b = weights[i:i+2]
            u,v = matrix[i:i+2]
            if a>b:
                matrix[i],matrix[i+1] = u,[(1-F(b,a))*x+F(b,a)*y for x,y in zip(u,v)]
            else:
                matrix[i],matrix[i+1] = [(1-F(a,b))*y+F(a,b)*x for x,y in zip(u,v)],v
            weights[i],weights[i+1] = b,a
        return matrix
    assert path((27,3,1),(0,1,0)) == path((27,3,1),(1,0,1))
    assert path((27,1,3),(0,1,0)) != path((27,1,3),(1,0,1))
    print('unequal-weight braid groupoid extrapolation boundary: PASS')


def verify_flat_carrier_artin():
    def identity(n):
        return [[F(i==j) for j in range(n)] for i in range(n)]
    def multiply(a,b):
        return [[sum(a[i][k]*b[k][j] for k in range(len(a)))
                 for j in range(len(a))] for i in range(len(a))]
    def alternating(a,b,length):
        result = identity(len(a))
        for step in range(length):
            result = multiply(a if step % 2 == 0 else b,result)
        return result
    checked = 0
    for m in range(2,7):
        generators = []
        for selected in range(m):
            matrix = identity(m)
            for row in range(m):
                matrix[row][selected] = F(-1,3) if row == selected else F(-1)
            generators.append(matrix)
        for i in range(m):
            for j in range(i+1,m):
                left = alternating(generators[i],generators[j],6)
                assert left == alternating(generators[j],generators[i],6)
                assert multiply(left,generators[i]) == multiply(generators[i],left)
                checked += 1
        if m >= 3:
            center = alternating(generators[0],generators[1],6)
            assert multiply(center,generators[2]) != multiply(generators[2],center)
    operations = 0
    for m in (2,3,5):
        width = m+1
        inputs = [tuple(F(i==j) for j in range(width)) for i in range(width)]
        state = [value for value in inputs[:-1] for _ in range(3)]+[inputs[-1]]
        groups = [list(range(3*i,3*i+3)) for i in range(m)]
        carrier = 3*m
        for selected in (0,1,0,1,0,1):
            leaf = groups[selected]
            indices = [carrier,leaf[0],leaf[1]]
            mean = tuple(sum(state[i][j] for i in indices)/3 for j in range(width))
            for i in indices:
                state[i] = mean
            carrier = leaf[2]
            groups[selected] = indices
            operations += 1
        local_mean = tuple((3*inputs[0][j]+3*inputs[1][j]+inputs[-1][j])/7
                           for j in range(width))
        for i,positions in enumerate(groups+[[carrier]]):
            expected = inputs[i]
            if i in (0,1,m):
                expected = tuple(mu-(value-mu)/27 for mu,value in zip(local_mean,expected))
            assert all(state[position] == expected for position in positions)
    # For (3,1,1), the determinant-one normalization has nonintegral
    # rational trace -5/3, ruling out finite projective order.
    small0 = [[F(-1,3),F(0)],[F(-1,3),F(1)]]
    small1 = [[F(1),F(-1,3)],[F(0),F(-1,3)]]
    product = multiply(small0,small1)
    assert 3*(product[0][0]+product[1][1]) == F(-5,3)
    print('flat triple-block Artin-six relations and centered carrier replay: PASS',checked,operations)


def verify_number_field_boundaries():
    # Quadratic values are exact coefficient pairs, not floating embeddings.
    def multiply(x,y,d):
        return x[0]*y[0]+d*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
    values = [(1,0)]*5+[(1,1),(-6,-1)]
    assert tuple(sum(x[j] for x in values) for j in (0,1)) == (0,0)
    assert all(x[0] % 7 == 1 for x in values)
    alpha = (0,1)
    assert multiply(alpha,(0,-1),-1) == (1,0)
    square = multiply(alpha,alpha,-2)
    assert (-4*square[0]-7,-4*square[1]) == (1,0)
    # Difference Z[1/3]-module has index7 in the coordinate module,
    # although its O_K-span is the unit ideal in both quadratic fields.
    differences = [(0,1),(-7,-1)]
    assert abs(differences[0][0]*differences[1][1]-differences[0][1]*differences[1][0]) == 7
    # In Q(sqrt(-10)), (2,sqrt(-10)) is a nonprincipal norm2 ideal;
    # 3 is inert, so inverting the prime above3 cannot remove its class.
    zeroable = ((2,0),(0,1),(-2,-1))
    assert tuple(sum(x[j] for x in zeroable) for j in (0,1)) == (0,0)
    assert all((x*x+10) % 3 for x in range(3))
    assert all(x*x+10*y*y != 2 for x in range(-2,3) for y in range(-1,2))
    print('number-field content/class and local-ideal counterexamples: PASS')


def verify():
    verify_integer_identities()
    verify_general_arity()
    operations = sum(physical_transvection(n) for n in (5,7,11,13))
    print('three-copy balanced transvection full coefficient replay: PASS',operations)
    print('prime29 three-copy transvection coefficient replay: PASS',physical_transvection(29))
    verify_level_boundary()
    verify_ordered_braid_boundary()
    verify_flat_carrier_artin()
    verify_balanced_euclid()
    verify_affine_orbits()
    verify_three_divisible_integration()
    verify_number_field_boundaries()


if __name__ == '__main__':
    verify()
