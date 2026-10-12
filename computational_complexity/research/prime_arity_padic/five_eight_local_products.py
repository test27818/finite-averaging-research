"""Exact normal form for ALL local prefixes from two equal exceptions.

The normal form includes local double-exception steps. It reduces a prescribed
local target to a signed multiplicative-language membership question, which is
NOT claimed to be in P. It is not a full consensus decision algorithm.

All states are unscaled (a,b,c,d), meaning (a repeated five times,b,c,d).
"""
from math import gcd
from five_eight_exit_language import encode_singleton_pair, decode_singleton_pair


def valuation(value, prime):
    if value == 0:
        raise ValueError('valuation requires a nonzero integer')
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def source(a, q, length):
    if length < 1 or a % 5 == 0 or q % 5 == 0 or q % 2 == 0 or gcd(a, q) != 1:
        raise ValueError('requires L>=1, 5 not dividing aq, odd q, gcd(a,q)=1')
    u = 5 ** length * q
    return a, a + u, a + u, -7 * a - 2 * u


def return_atom(singletons):
    """A block of singleton steps followed by D: (signed factor, total cost)."""
    singletons = tuple(singletons)
    u, v = encode_singleton_pair(singletons)
    sigma = -u - v
    assert abs(sigma) >= 2 and sigma % 5
    return sigma, len(singletons) + 1


def split_word(word):
    blocks, tail = [], []
    for letter in word:
        if letter in (1, 2):
            tail.append(letter)
        elif letter == 'D':
            blocks.append(tuple(tail))
            tail = []
        else:
            raise ValueError('letters must be 1, 2 or D')
    return tuple(blocks), tuple(tail)


def flatten(blocks, tail):
    return tuple(x for block in blocks for x in tuple(block) + ('D',)) + tuple(tail)


def describe_word(word):
    blocks, tail = split_word(word)
    scalar = 1
    return_cost = 0
    for block in blocks:
        sigma, cost = return_atom(block)
        scalar *= sigma
        return_cost += cost
    return {'scalar': scalar, 'return_cost': return_cost,
            'tail': tail, 'tail_pair': encode_singleton_pair(tail),
            'blocks': blocks, 'length': return_cost + len(tail)}


def realize(a, q, length, blocks, tail):
    """Evaluate a concrete normal-form certificate, including prefix G safety."""
    initial = source(a, q, length)
    description = describe_word(flatten(blocks, tail))
    t, scalar = description['length'], description['scalar']
    if t > length:
        raise ValueError('a local integer prefix cannot exceed initial depth L')
    h1, h2 = description['tail_pair']
    scale = 5 ** (length - t) * q * scalar
    u, v = scale * h1, scale * h2
    common, rem = divmod(-initial[3] - u - v, 7)
    assert rem == 0
    final = (common, common + u, common + v, initial[3])
    safe = valuation(scalar, 2) <= valuation(initial[3], 2)
    return {'state': final, 'all_prefixes_G1': safe, **description}


def reduce_target(a, q, length, target):
    """Reduce exact local-target membership to one scalar and one cost.

    'no' rejects an impossible target. 'yes' covers the zero-return-cost
    case. 'scalar_membership' is UNRESOLVED: it requires a product of return
    atoms with the returned scalar and exact total cost. No factorization
    algorithm or P guarantee for that subproblem is being asserted.
    """
    initial = source(a, q, length)
    A, B, C, d = tuple(target)
    if d != initial[3] or 5*A + B + C + d:
        return {'status': 'no', 'reason': 'outside value or total sum mismatch'}
    u, v = B - A, C - A
    content = gcd(u, v)
    if not content:
        return {'status': 'no', 'reason': 'local difference pair cannot vanish'}
    e = valuation(content, 5)
    t = length - e
    if t < 0:
        return {'status': 'no', 'reason': 'local depth cannot grow from equal exceptions'}
    scale = 5 ** e * q
    if content % scale:
        return {'status': 'no', 'reason': 'source content does not divide target content'}
    if valuation(content, 2) > valuation(d, 2):
        return {'status': 'no', 'reason': 'primitive G obstruction'}
    matches = []
    for sign in (1, -1):
        h = (sign*u//content, sign*v//content)
        tail = decode_singleton_pair(*h)
        if tail is not None:
            matches.append((sign*content//scale, tail))
    assert len(matches) <= 1
    if not matches:
        return {'status': 'no', 'reason': 'primitive tail is not a singleton orbit point'}
    scalar, tail = matches[0]
    cost = t - len(tail)
    if cost < 0:
        return {'status': 'no', 'reason': 'decoded tail exceeds elapsed depth'}
    if cost == 0:
        return {'status': 'yes', 'word': tail} if scalar == 1 else {
            'status': 'no', 'reason': 'zero return cost requires scalar one'}
    if abs(scalar) < 2:
        return {'status': 'no', 'reason': 'every nonempty return has absolute factor at least two'}
    return {'status': 'scalar_membership', 'scalar': scalar, 'return_cost': cost,
            'tail': tail, 'elapsed_steps': t, 'two_adic_budget': valuation(d, 2)}


def first_exits(state):
    """All G-safe, nonidentity integer outside moves from a fixed local state.

    This lists up to four exits of this ONE state, not all states represented
    by an unresolved scalar-membership query.
    """
    a, b, c, d = state
    choices = (
        ('E0', (a,a,a,a,d), (a,b,c)),
        ('E1', (a,a,a,b,d), (a,a,c)),
        ('E2', (a,a,a,c,d), (a,a,b)),
        ('E12', (a,a,b,c,d), (a,a,a)),
    )
    result = []
    for letter, selected, rest in choices:
        if len(set(selected)) == 1 or sum(selected) % 5:
            continue
        next_state = (sum(selected)//5,) + rest
        scale = gcd(*next_state)
        if not scale:
            result.append((letter, next_state))
            continue
        pstate = tuple(x//scale for x in next_state)
        if gcd(*(x-pstate[0] for x in pstate[1:])) == 1:
            result.append((letter, next_state))
    return tuple(result)


def analyze_scalar(scalar, cost):
    """Sound polynomial filters and a constructive power-of-two slice of M(R,c).

    cost is measured in unary, as it is bounded by the original local depth.
    'unresolved' has NO truth-value implication. In particular, powers of two
    with cost > 4*v2(abs(scalar)) are not rejected solely for that reason.
    """
    if not isinstance(scalar, int) or not isinstance(cost, int) or cost < 0:
        raise ValueError('an integer scalar and nonnegative integer cost are required')
    if cost == 0:
        return {'status':'yes','blocks':()} if scalar == 1 else {
            'status':'no','reason':'empty product'}
    if abs(scalar) < 2 or scalar % 5 == 0:
        return {'status':'no','reason':'nonempty products have nonunit size and are 5-adic units'}
    if scalar % 7 != pow(5,cost,7):
        return {'status':'no','reason':'cost residue modulo seven'}
    b = valuation(scalar,2)
    if b == 0 and scalar % 4 != 1:
        return {'status':'no','reason':'every odd return factor is one modulo four'}
    odd_part = abs(scalar) >> b
    maximum_odd = 0
    power = 1
    while 3*power <= odd_part:
        power *= 3
        maximum_odd += 1
    maximum_returns = min(cost,b+maximum_odd,(cost+b)//2)
    residue = next(s for s in range(4) if pow(2,s,5) == scalar * (-1 if cost % 2 else 1) % 5)
    first_count = b + (residue-b) % 4
    first_count = max(first_count, residue if residue else 4)  # A nonempty product has at least one factor.
    if first_count > maximum_returns:
        return {'status':'no','reason':'no possible number of return factors',
                'minimum_even_returns':b,'maximum_returns':maximum_returns,'return_count_mod4':residue}
    if odd_part == 1 and b <= cost <= 4*b and (cost-b) % 3 == 0:
        long_count = (cost-b)//3
        blocks = ((1,2,1),)*long_count + ((),)*(b-long_count)
        actual_scalar = 1
        actual_cost = 0
        for block in blocks:
            factor,length = return_atom(block)
            actual_scalar *= factor
            actual_cost += length
        assert (actual_scalar,actual_cost) == (scalar,cost)
        return {'status':'yes','blocks':blocks}
    return {'status':'unresolved','minimum_even_returns':b,
            'maximum_returns':maximum_returns,'return_count_mod4':residue}


def decide_local_target(a, q, length, target):
    """Partial local decision with explicit unresolved outcomes; not full consensus."""
    reduced = reduce_target(a,q,length,target)
    if reduced['status'] != 'scalar_membership':
        return reduced
    scalar_result = analyze_scalar(reduced['scalar'],reduced['return_cost'])
    if scalar_result['status'] == 'no':
        return scalar_result
    if scalar_result['status'] == 'unresolved':
        return {**reduced,'scalar_analysis':scalar_result}
    blocks = scalar_result['blocks']
    checked = realize(a,q,length,blocks,reduced['tail'])
    assert checked['state'] == tuple(target) and checked['all_prefixes_G1']
    return {'status':'yes','word':flatten(blocks,reduced['tail'])}
