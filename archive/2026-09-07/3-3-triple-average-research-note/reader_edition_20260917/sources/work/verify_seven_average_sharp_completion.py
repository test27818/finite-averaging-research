"""Complete fixed certificates for seven-averaging in dimensions20 and22.

Positive inverse words come from the fixed scalar cycles written below.
There is no seed discovery search in this verifier. Finite quotients use
unit cosets as well as projective directions. General group containment
uses the previously proved deep lemma and its stated external dependencies.
"""

from collections import deque
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from random import Random
import json

from verify_four_prime_entry_and_band import Ledger, factors, is_legal
from verify_uniform_odd_middle_cores import mm, invq, residue, bezout, normalize_pair
from verify_upper_band_six_unit_completion import modular_matrix_power
from verify_upper_band_descent_boundary import apply_return as upper_return
from verify_upper_band_three_value_reduction import upper_reduce
from verify_uniform_two_block_entry import uniform_entry
from verify_prime_arity_zero_trigger_bridge import GlobalReplay

if not __debug__:
    raise RuntimeError('Assertions are required.')

ROOT = Path(__file__).parent
I = (1, 0, 0, 1)
CASES = {
    20: {
        'm': 1, 'r': 6, 'modulus': 1600, 'ring_primes': (3, 7),
        'macros': {'P': (-4, 23, -1, 0), 'Q': (-2, -3, -1, 0),
                   'F': (3, 12, 0, 7), 'S': (-1, 6, 0, 1)},
        'rows': {'P': ('A', 5, 1), 'Q': ('A', 3, 3), 'F': ('C', 2, 0)},
        'cycle': ['F', 'Q', 'P']*2, 'scalar': 1449,
        'graph_letters': ('S', 'Q', 'q', 'F', 'f'),
    },
    22: {
        'm': 2, 'r': 1, 'modulus': 1936, 'ring_primes': (5, 7),
        'macros': {'A': (4, 1, -1, 0), 'F': (1, 2, 0, 7), 'J': (1, 2, 2, -1)},
        'rows': {'A': ('A', 1, 0), 'F': ('C', 2, 0), 'J': ('B', 2, 0)},
        'cycle': ['A', 'A', 'F']*2, 'scalar': -7,
        'graph_letters': ('A', 'a', 'F', 'f', 'J'),
    },
}


def normalize_matrix(matrix):
    common = gcd(*matrix)
    assert common
    matrix = tuple(value//common for value in matrix)
    if next(value for value in matrix if value) < 0:
        matrix = tuple(-value for value in matrix)
    return matrix


def adjugate(matrix):
    a, b, c, d = matrix
    return d, -b, -c, a


def word_matrix(word, matrices):
    result = I
    for letter in word:
        result = mm(matrices[letter], result)
    return result


def inverse_words(case):
    cycle = case['cycle']
    result = {}
    for letter in set(cycle):
        index = cycle.index(letter)
        rotated = cycle[index:]+cycle[:index]
        result[letter.lower()] = rotated[1:]
    for letter in ('S', 'J'):
        if letter in case['macros']:
            result[letter.lower()] = [letter]
    return result


def physical_atom(ledger, groups, case, letter):
    p, m, r = 7, case['m'], case['r']
    if letter == 'S':
        assert m == 1
        return [groups[1], groups[0], groups[2]]
    carrier, j, s = case['rows'][letter]
    if m == 2:
        return upper_return(ledger, groups, carrier, j, s)
    aa, bb, cc = [list(group) for group in groups]
    i = p-j-s
    if carrier == 'A':
        kept, aa = aa[-r:], aa[:-r]
    elif carrier == 'B':
        kept, bb = bb[-r:], bb[:-r]
    else:
        assert carrier == 'C' and s == 0
        kept, cc = cc, []
    first = aa[:i]+bb[:j]+cc[:s]
    second = aa[i:]+bb[j:]+cc[s:]
    ledger.average(first)
    ledger.average(second)
    return [first, second, kept]


def physical_word(n, word, a, z):
    case = CASES[n]
    m, r = case['m'], case['r']
    raw = [F(a)]*(m*7)+[-m*F(a)+r*z]*7+[-7*F(z)]*r
    ledger = Ledger(raw, 7)
    groups = [list(range(m*7)), list(range(m*7, (m+1)*7)), list(range((m+1)*7, n))]
    inverse = inverse_words(case)
    for letter in word:
        expanded = [letter] if letter.isupper() else inverse[letter]
        for positive in expanded:
            groups = physical_atom(ledger, groups, case, positive)
    state = list(raw)
    for group in ledger.word:
        assert len(group) == len(set(group)) == 7
        assert all(0 <= index < n for index in group)
        value = sum(state[index] for index in group)/7
        for index in group:
            state[index] = value
        assert sum(state) == 0 and is_legal(state, factors(n))
    assert state == ledger.state
    ap, zp = state[groups[0][0]], -state[groups[2][0]]/7
    assert all(state[index] == value for group, value in zip(groups, (ap, -m*ap+r*zp, -7*zp))
               for index in group)
    return (ap, zp), len(ledger.word)


def verify_cycles_and_roots():
    replays = 0
    for n, case in CASES.items():
        matrices = dict(case['macros'])
        assert word_matrix(case['cycle'], matrices) == tuple(case['scalar']*x for x in I)
        for letter, positive in inverse_words(case).items():
            product = mm(word_matrix(positive, matrices), matrices[letter.upper()])
            assert product[1] == product[2] == 0 and product[0] == product[3] != 0
        words = [case['cycle']]
        for letter in matrices:
            words += [[letter], [letter, letter.lower()]]
        if n == 20:
            P, Q, Fm, S = [matrices[x] for x in ('P', 'Q', 'F', 'S')]
            chart = (3, 1, 1, 0)  # (u,v) -> (a,z), u=z, v=a-3z.
            p, q, f, s = [mm(mm(invq(chart), x), chart) for x in (P, Q, Fm, S)]
            assert (p, q, f, s) == ((-3,-1,20,-1),(-3,-1,0,1),(7,0,0,3),(1,0,0,-1))
            h = mm(p, invq(q))
            assert h == (1, 0, F(-20,3), F(-23,3))
            upper = mm(mm(mm(s,q),s),invq(q))
            lower = mm(mm(mm(s,h),s),invq(h))
            assert upper == (1,2,0,1) and lower == (1,0,F(40,3),1)
            assert mm(mm(f, upper), invq(f)) == (1,F(14,3),0,1)
            assert mm(mm(f, lower), invq(f)) == (1,0,F(40,7),1)
            words += [list('qSQS'), list('pQSqPS')]
            formal = dict(matrices)
            formal.update({name.lower(): invq(value) for name,value in matrices.items()})
            assert mm(mm(invq(chart),word_matrix(words[-2],formal)),chart) == upper
            assert mm(mm(invq(chart),word_matrix(words[-1],formal)),chart) == lower
        else:
            A, Fm, J = [matrices[x] for x in ('A','F','J')]
            h = mm(mm(mm(A,Fm),J),invq(A))
            assert h == (-7,-62,0,5)
            upper = mm(mm(mm(Fm,h),invq(Fm)),invq(h))
            assert upper == (1,F(396,35),0,1)
            chart = (1,4,0,-1)
            assert mm(mm(chart, upper),chart) == (1,F(-396,35),0,1)
            conjugate = mm(mm(A,upper),invq(A))
            assert mm(mm(chart,conjugate),chart) == (1,0,F(396,35),1)
            # Product left-to-right is F H F^-1 H^-1.
            words += [list('afjAfaJFAF')]
            formal = dict(matrices)
            formal.update({name.lower(): invq(value) for name,value in matrices.items()})
            assert word_matrix(words[-1],formal) == upper
        for word in words:
            expanded = []
            for letter in word:
                expanded += [letter] if letter.isupper() else inverse_words(case)[letter]
            expected = word_matrix(expanded, matrices)
            for a, z in ((1,0),(0,1)):
                actual, _ = physical_word(n, word, a, z)
                target = (expected[0]*a+expected[1]*z, expected[2]*a+expected[3]*z)
                assert actual[0]*target[1] == actual[1]*target[0]
                assert any(actual) and any(target)
                replays += 1
        for a, z in ((1,0),(0,1)):
            actual, atom_count = physical_word(n, case['cycle'], a, z)
            assert atom_count == (12 if n == 20 else 18)
            scale = F(case['scalar'], 7**6)
            assert actual == (scale*a, scale*z)
    print('seven-average fixed scalar cycles and inverse/root replays: PASS', replays)
    return replays


def remove_auxiliary_three():
    n, modulus, exponent = 22, 1936, 440
    A, Fm = CASES[n]['macros']['A'], CASES[n]['macros']['F']
    X = tuple(F(value,7) for value in mm(Fm,Fm))
    assert X[0]*X[3]-X[1]*X[2] == 1
    for matrix in (A,X):
        assert modular_matrix_power(tuple(residue(x,modulus) for x in matrix),exponent,modulus) == I
    generators = [modular_matrix_power(tuple(residue(x,9) for x in matrix),exponent,9)
                  for matrix in (A,X)]
    forest, queue = {I: None}, deque([I])
    while queue:
        matrix = queue.popleft()
        for index, generator in enumerate(generators):
            image = tuple(x%9 for x in mm(generator,matrix))
            if image not in forest:
                forest[image] = (matrix,index)
                queue.append(image)
    assert len(forest) == 648
    assert all((a*d-b*c)%9==1 for a,b,c,d in forest)
    for tangent in ((0,1,0,0),(0,0,1,0),(1,0,0,-1)):
        matrix = tuple((x+3*t)%9 for x,t in zip(I,tangent))
        assert matrix in forest
    assert 396**2 == modulus*3**4
    print('twenty-two auxiliary3 removal: PASS', len(forest), exponent)
    return {'exponent':exponent,'generators_mod9':generators,
            'forest_mod9': [[list(key),value] for key,value in forest.items()]}


def unit_forest(modulus, primes):
    forest, queue = {1: None}, deque([1])
    while queue:
        current = queue.popleft()
        for factor in (-1, *primes):
            image = current*factor%modulus
            if image not in forest:
                forest[image] = (current,factor)
                queue.append(image)
    return forest


def finite_case(n):
    case = CASES[n]
    modulus, primes = case['modulus'],case['ring_primes']
    units = unit_forest(modulus,primes)
    inverses = {x:pow(x,-1,modulus) for x in range(modulus) if gcd(x,modulus)==1}
    if n==20:
        assert set(units)==set(inverses) and len(units)==640
        representatives=[1]
    else:
        assert len(units)==440 and len(inverses)==880
        assert 3 not in units and {3*x%modulus for x in units} == set(inverses)-set(units)
        representatives=[1,3]
    labels={x:0 for x in units}
    if len(representatives)==2:
        labels.update({3*x%modulus:1 for x in units})
    chart=(0,1,1,7)
    matrices={}
    for letter in case['graph_letters']:
        raw=case['macros'][letter.upper()]
        matrices[letter]=raw if letter.isupper() else adjugate(raw)
    chart_matrices={letter:tuple(residue(x,modulus) for x in mm(mm(chart,raw),invq(chart)))
                    for letter,raw in matrices.items()}
    root=(0,0)
    forest={root:(None,None,0)}
    lifts={root:I}
    queue=deque([root])
    while queue:
        x,scale=point=queue.popleft()
        for letter,(a,b,c,d) in chart_matrices.items():
            denominator=(c*x+d)%modulus
            assert denominator in inverses
            image=((a*x+b)*inverses[denominator]%modulus,scale^labels[denominator])
            if image not in forest:
                forest[image]=(point,letter,forest[point][2]+1)
                lifts[image]=normalize_matrix(mm(matrices[letter],lifts[point]))
                queue.append(image)
    assert len(forest)==modulus*len(representatives)
    for point,(parent,letter,depth) in forest.items():
        lift=lifts[point]
        a,z=lift[0],lift[2]
        y=a+7*z
        assert y%modulus in inverses
        assert (z*inverses[y%modulus]%modulus,labels[y%modulus])==point
        if parent is not None:
            assert forest[parent][2]==depth-1
        # Exhaust all edges, not just first arrivals.
        x,scale=point
        for mat in chart_matrices.values():
            aa,b,c,d=mat
            denominator=(c*x+d)%modulus
            image=((aa*x+b)*inverses[denominator]%modulus,scale^labels[denominator])
            assert image in forest
    print('seven-average complete finite direction/scale quotient: PASS',n,len(units),len(forest),
          max(record[2] for record in forest.values()))
    return units,forest,lifts,representatives


def unit_lift(value,forest):
    result=1
    while value!=1:
        value,factor=forest[value]
        result*=factor
    return result


def primitive_lift(x,scale,modulus):
    z=scale*x
    if not z:
        return scale,modulus
    a=scale-7*z
    conditions=[q for q in factors(abs(z)) if modulus%q]
    radical=1
    for q in conditions:
        radical*=q
    k=0
    for q in conditions:
        selected=1 if a%q==0 else 0
        k+=selected*(radical//q)*pow(radical//q,-1,q)
    k%=radical
    a+=modulus*k
    assert gcd(a,z)==1 and (a+7*z)%modulus==scale%modulus
    return a,z


def exact_transport(n,units,forest,lifts,representatives):
    case=CASES[n]
    modulus=case['modulus']
    checked=0
    for (x,scale),lift in lifts.items():
        a,z=primitive_lift(x,representatives[scale],modulus)
        inverse=adjugate(lift)
        a,z=normalize_pair(inverse[0]*a+inverse[1]*z,inverse[2]*a+inverse[3]*z)
        assert gcd(a,z)==1 and z%modulus==0 and a%modulus in units
        target=unit_lift(a%modulus,units)
        _,alpha,beta=bezout(a,z)
        alpha,beta=target*alpha,target*beta
        adjust=residue(beta,modulus)*pow(a,-1,modulus)%modulus
        alpha,beta=alpha+adjust*z,beta-adjust*a
        h=(alpha,beta,F(-z,target),F(a,target))
        assert h[0]*h[3]-h[1]*h[2]==1
        assert all(residue(value-delta,modulus)==0 for value,delta in zip(h,I))
        assert (h[0]*a+h[1]*z,h[2]*a+h[3]*z)==(target,0)
        assert all(set(factors(F(value).denominator))<=set(case['ring_primes']) for value in h)
        checked+=1
    print('seven-average exact principal terminal lifts: PASS',n,checked)
    return checked


def verify_entries_and_tails():
    rng=Random(2026091451)
    records=[]
    for n in (20,22):
        for _ in range(48):
            while True:
                raw=[rng.randrange(-(1<<50),1<<50) for _ in range(n-1)]
                raw.append(-sum(raw))
                if gcd(*raw)==1 and is_legal(raw,factors(n)):
                    break
            records.append(uniform_entry(raw,7,6) if n==20 else upper_reduce(raw,7))
        m,r=CASES[n]['m'],CASES[n]['r']
        raw=[1]*(m*7)+[-m]*7+[0]*r
        replay=GlobalReplay(raw,7)
        j,s=divmod(7,m+1)
        group=list(range(m*j))+list(range(m*7,m*7+j))+list(range((m+1)*7,(m+1)*7+s))
        replay.average(group)
        if n<=21:
            replay.small_tail()
        else:
            replay.three_p_tail()
        assert not any(replay.state)
    forbidden=[-7]+[0]*6+[1]*7
    assert sum(forbidden)==0 and gcd(*forbidden)==1
    assert gcd(*(x-forbidden[0] for x in forbidden))==1
    print('seven-average full-input entries and literal tails: PASS',len(records),2)
    print('seven-average known14-dimensional lower-bound input: PASS')
    return records


def verify_parameter_scope():
    """Check the two natural continuations exactly in Q[p], not by samples."""
    def add(a,b):
        out=tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                  for i in range(max(len(a),len(b))))
        while len(out)>1 and out[-1]==0:
            out=out[:-1]
        return out
    def multiply(a,b):
        out=[F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                out[i+j]+=x*y
        while len(out)>1 and out[-1]==0:
            out.pop()
        return tuple(out)
    def product(a,b):
        return tuple(add(multiply(a[2*i],b[j]),multiply(a[2*i+1],b[2+j]))
                     for i in range(2) for j in range(2))
    zero,minus_one=(F(0),),(F(-1),)
    # n=3p-1: P=A(p-2,1), Q=A((p-1)/2,(p-1)/2), F=C((p-1)/3,0).
    pmat=((F(3),F(-1)),(F(2),F(-4),F(1)),minus_one,zero)
    qmat=((F(3,2),F(-1,2)),(F(1,2),F(-1,2)),minus_one,zero)
    fmat=((F(2,3),F(1,3)),(F(1,3),F(-2,3),F(1,3)),zero,(F(0),F(1)))
    word=product(product(pmat,qmat),fmat)
    expected=multiply((F(7,6),F(-1,6)),(F(1),F(2)))
    assert add(word[0],word[3])==expected
    # n=3p+1: A=A((p-1)/6,0), F=C((p-1)/3,0).
    amat=((F(1,2),F(1,2)),(F(-1,6),F(1,6)),minus_one,zero)
    fmat=((F(1),),(F(-1,3),F(1,3)),zero,(F(0),F(1)))
    word=product(product(fmat,amat),amat)
    expected=multiply((F(1),F(1)),(F(7,12),F(-1,12)))
    assert add(word[0],word[3])==expected
    print('seven-average natural cycles have isolated p7 trace zero: PASS 2')


def main():
    verify_parameter_scope()
    replays=verify_cycles_and_roots()
    remove_three=remove_auxiliary_three()
    cases=[]
    for n in (20,22):
        units,forest,lifts,reps=finite_case(n)
        checks=exact_transport(n,units,forest,lifts,reps)
        cases.append({'n':n,'modulus':CASES[n]['modulus'],'ring_primes':CASES[n]['ring_primes'],
                      'unit_forest':[[key,value] for key,value in sorted(units.items())],
                      'state_forest':[[list(key),value] for key,value in sorted(forest.items())],
                      'unit_coset_representatives':reps,'exact_target_lifts':checks})
    entries=verify_entries_and_tails()
    record={'scope':'Complete fixed finite quotients with unit scales and literal scalar-cycle inverses. '
                    'Infinite containment uses the stated arithmetic-group theorems and deep lemma. '
                    'General principal group elements are not expanded into full averaging words.',
            'claim':'Seven-averaging has the sharp final threshold N(7)=15, using previous completed dimensions.',
            'physical_replays':replays,'three_removal':remove_three,'cases':cases,'input_entries':entries}
    (ROOT/'seven_average_sharp_completion_records.json').write_text(
        json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print('seven-average dimensions20 and22 complete; N7=15: PASS')


if __name__=='__main__':
    main()
