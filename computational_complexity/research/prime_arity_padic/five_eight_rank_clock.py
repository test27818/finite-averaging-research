"""Symbolic rank, p-adic clock, and image-plane decoding for p+3 cores.

Theorems assume a fixed prime p >= 5. A proper operation selects one or two
of the three exceptions. These tools inspect symbolic words or matrices;
they DO NOT decide whether an input has a successful averaging word.
"""
from math import gcd


def primitive(v):
    d = gcd(*v)
    if not d:
        return tuple(v)
    v = tuple(x//d for x in v)
    return tuple(-x for x in v) if next(x for x in v if x) < 0 else v


def valuation(x,p):
    if not x:
        raise ValueError('nonzero input required')
    k = 0
    while x % p == 0:
        x //= p
        k += 1
    return k


def embedding(pair=(0,1)):
    pair = frozenset(pair)
    if len(pair) != 2 or not pair <= {0,1,2}:
        raise ValueError('a pair of distinct indices from 0,1,2 is required')
    return tuple((1,0) if i in pair else (0,1) for i in range(3))


def step_matrix(matrix,mask,p=5):
    if mask not in (1,2,3,4,5,6):
        raise ValueError('only nonempty proper subsets of three exceptions are allowed')
    width = len(matrix[0])
    selected_sum = tuple(sum(matrix[i][j] for i in range(3) if mask>>i&1)
                         for j in range(width))
    return tuple(tuple(-selected_sum[j] if mask>>i&1 else p*matrix[i][j]-selected_sum[j]
                       for j in range(width)) for i in range(3))


def wedge(matrix):
    a,b,c = matrix
    return (b[0]*c[1]-b[1]*c[0],
            c[0]*a[1]-c[1]*a[0],
            a[0]*b[1]-a[1]*b[0])


def clock(matrix,p=5):
    minors = wedge(matrix)
    content = gcd(*minors)
    if not content:
        raise ValueError('matrix does not have rank two')
    return valuation(content,p)


def plane_update(normal,index,p=5):
    total = sum(normal)
    return tuple(-(p-1)*x-total if i==index else x for i,x in enumerate(normal))


def decode_plane(normal,p=5):
    """Recover the unique nonstationary singleton suffix of an image plane.

    The missing index of the pair can be repeated arbitrarily at the root
    without changing the plane. The returned word omits only that initial
    stationary run. None means this plane is not in the claimed orbit.
    """
    if p < 5 or p % 2 == 0:
        raise ValueError('the theorem assumes a prime p >= 5')
    g = primitive(tuple(normal))
    residues = tuple(x%p for x in g)
    if sorted(residues) != [0,1,p-1]:
        return None
    root = tuple(0 if x==0 else 1 if x==1 else -1 for x in residues)
    missing = residues.index(0)
    reverse_runs = []
    while g != root:
        total = sum(g)
        if total % p:
            return None
        candidates = [i for i in range(3) if (total+p*g[i]) % (p*p) == 0]
        if len(candidates) != 1:
            return None
        i = candidates[0]
        d = total+p*g[i]
        if not d:
            return None  # A stationary point cannot be reached nontrivially from the root.
        count = valuation(d,p)-1
        other_sum = total-g[i]
        new_value,rem = divmod((-1)**count*(d//p**count)-other_sum,p+1)
        assert not rem
        g = tuple(new_value if j==i else x for j,x in enumerate(g))
        assert gcd(*g)==1 and tuple(x%p for x in g)==residues
        reverse_runs.append((i,count))
    word = tuple(i for i,count in reversed(reverse_runs) for _ in range(count))
    return {'pair':tuple(i for i in range(3) if i!=missing),
            'stationary_index':missing,'word':word,'runs':tuple(reversed(reverse_runs))}


def kernel_row(matrix,p=5):
    """Canonical projective row defining integrality modulo p**clock.

    Returns pivot-normalized coefficients and modulus. A matching row for two
    histories only identifies their modular kernel, NOT their future behavior.
    """
    t = clock(matrix,p)
    if t == 0:
        return {'clock':0,'modulus':1,'row':(0,0)}
    modulus = p**t
    row = matrix[0]
    pivot = next(i for i in (0,1) if row[i]%p)
    inverse = pow(row[pivot],-1,modulus)
    return {'clock':t,'modulus':modulus,
            'row':tuple(x*inverse%modulus for x in row)}


def strip_singleton(matrix,index,p=5):
    """Exact inverse on a symbolic matrix, only when all divisions are integral."""
    old = []
    for i,row in enumerate(matrix):
        if i == index:
            old.append(tuple(-x for x in row))
        else:
            nums = tuple(x-y for x,y in zip(row,matrix[index]))
            if any(x%p for x in nums):
                return None
            old.append(tuple(x//p for x in nums))
    return tuple(old)
