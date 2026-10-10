"""Exact checks for norm towers; all-exponent claims have written proofs.

Shell enumeration is complete for each stated norm, using its positive-definite
square identity. Prior oracle outputs and frozen files are never rewritten.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import json

from verify_subcritical_complement_dynamics import core_distance, atom


def norm(q, u, v):
    a, b, c = q
    return a*u*u+b*u*v+c*v*v


def strip3(n):
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return n, k


def shell(q, target):
    """All primitive integer representations, including both common signs."""
    a, b, c = q
    delta = 4*a*c-b*b
    assert delta > 0 and target > 0
    solutions = set()
    bound = isqrt(4*a*target//delta)
    for v in range(-bound, bound+1):
        square = 4*a*target-delta*v*v
        root = isqrt(square)
        if root*root != square:
            continue
        for signed in {root, -root}:
            numerator = signed-b*v
            if numerator % (2*a):
                continue
            u = numerator//(2*a)
            if gcd(u, v) == 1:
                assert norm(q, u, v) == target
                solutions.add((u, v))
    return sorted(solutions)


def norm11_prediction(u, v):
    m, k = strip3(norm((1, -1, 3), u, v))
    if (u+v) % 5 or (k and u % 3):
        return None
    if m == 5:
        return k+1
    if m == 25:
        return k+2
    if m == 55:
        return k+4
    if m == 115:
        r = u*pow(v, -1, m) % m
        assert r in (19, 74)
        return k+(3 if r == 19 else 4)
    if m == 235:
        return k+3 if (u-21*v) % 47 == 0 else None
    assert m in (125, 155, 185)
    return None


def norm59_prediction(u, v, k):
    if (u+v) % 5 or (k and u % 3):
        return None
    assert k % 3 != 2
    return k+1+int(k % 3 == 1)


def generalized_strip_checks():
    checked = 0
    successes = 0
    for u in range(-240, 241):
        for v in range(-240, 241):
            if gcd(u, v) != 1:
                continue
            m, k = strip3(norm((1, -1, 3), u, v))
            if not k:
                continue
            answer = core_distance(3, u, v)
            if u % 3:
                assert answer is None
            else:
                a, b = u, v
                for _ in range(k):
                    assert a % 3 == 0
                    a, b = b-a//3, -a//3
                    assert gcd(a, b) == 1
                assert norm((1, -1, 3), a, b) == m
                assert gcd(v, m) == gcd(b, m) == 1
                assert (u*b-v*a) % m == 0
                base_answer = core_distance(3, a, b)
                assert (answer is None) == (base_answer is None)
                if answer is not None:
                    assert answer == k+base_answer
                    successes += 1
            checked += 1
    return {'primitive_nonzero_exponent_pairs': checked, 'solvable_pairs': successes,
            'coordinate_box': [-240, 240]}


def root_label_checks():
    represented = collisions = 0
    for m in range(1, 501):
        if m % 3 == 0:
            continue
        roots = {r for r in range(m) if (r*r-r+3) % m == 0}
        reps = shell((1, -1, 3), m)
        by_root = {}
        for u, v in reps:
            assert gcd(v, m) == 1
            r = u*pow(v, -1, m) % m
            if r in by_root:
                assert (u, v) == tuple(-z for z in by_root[r])
                collisions += 1
            else:
                by_root[r] = (u, v)
            represented += 1
        assert set(by_root) == roots, m
    return {'moduli_through': 500, 'primitive_representations': represented,
            'only_common_sign_collisions': collisions}


def full_towers():
    shells11 = []
    bases11 = []
    for m in (5, 25, 55, 115, 125, 155, 185, 235):
        base = [{'pair': (u, v), 'root': u*pow(v, -1, m) % m,
                 'distance': core_distance(3, u, v)}
                for u, v in shell((1, -1, 3), m) if u > 0 and (u+v) % 5 == 0]
        bases11.append({'m': m, 'all_G_legal_representatives_up_to_sign': base})
        for k in range(13):
            reps = shell((1, -1, 3), m*3**k)
            accepted = 0
            for u, v in reps:
                predicted = norm11_prediction(u, v)
                assert predicted == core_distance(3, u, v), (m, k, u, v)
                accepted += predicted is not None
            shells11.append({'m': m, 'k': k, 'primitive_representations': len(reps),
                             'accepted': accepted})
    shells59 = []
    bases59 = []
    for k in range(19):
        reps = shell((1, -7, 27), 35*3**k)
        accepted = 0
        for u, v in reps:
            predicted = norm59_prediction(u, v, k)
            assert predicted == core_distance(3, u, v), (k, u, v)
            accepted += predicted is not None
        shells59.append({'k': k, 'primitive_representations': len(reps), 'accepted': accepted})
        if k < 3:
            bases59.append({'norm': 35*3**k,
                            'all_G_legal_representatives_up_to_sign': [
                                (u, v) for u, v in reps if u > 0 and (u+v) % 5 == 0]})
    return {'minus11_base_table': bases11, 'minus11_complete_shells': shells11,
            'minus59_base_table': bases59, 'minus59_complete_shells': shells59}


def physical_three_step_checks():
    checked = 0
    for a in range(-20, 21):
        for v in range(-40, 41):
            u = 27*a
            if not u or gcd(u, v) != 1 or (u+v) % 5:
                continue
            center = F(-u-v, 5)
            state = (center, center, center, center+u, center+v)
            for _ in range(3):
                updated = atom(state, (0, 1, 3))
                state = (updated[0], updated[1], updated[3], updated[2], updated[4])
                assert all(x.denominator == 1 for x in state)
            # Swap exception roles after the three physical steps, without an extra operation.
            state = state[:3]+(state[4], state[3])
            aa, bb = v-7*a, -a
            cc = F(-aa-bb, 5)
            assert state == (cc, cc, cc, cc+aa, cc+bb)
            assert norm((1, -7, 27), u, v) == 27*norm((1, -7, 27), aa, bb)
            checked += 1
    return checked


def general_prime_slices():
    records = []
    for p in (3, 5, 7, 11, 13, 17, 31):
        checked = accepted = 0
        for k in range(7):
            for u, v in shell((1, -1, p), (p+2)*p**k):
                predicted = (u+v) % (p+2) == 0 and (k == 0 or u % p == 0)
                actual = core_distance(p, u, v)
                assert predicted == (actual is not None), (p, k, u, v)
                if predicted:
                    assert actual == k+1
                    accepted += 1
                checked += 1
        records.append({'p': p, 'exponents': [0, 6], 'checked': checked, 'accepted': accepted})
    return records


def global_norm_restriction():
    checked = accepted = 0
    for u in range(-180, 181):
        for v in range(-180, 181):
            if gcd(u, v) != 1:
                continue
            answer = core_distance(3, u, v)
            m, _ = strip3(norm((1, -1, 3), u, v))
            if answer is not None:
                assert m == 5 or m % 30 == 25, (u, v, m)
                accepted += 1
            if m != 5 and m % 3 == 2:
                assert answer is None
            checked += 1
    assert norm((1, -1, 3), 41, 9) == 1555
    assert norm((1, -1, 3), 38, -3) == 1585
    assert core_distance(3, 41, 9) == 9 and core_distance(3, 38, -3) == 8
    return {'primitive_pairs': checked, 'solvable_pairs': accepted,
            'coordinate_box': [-180, 180], 'necessary_condition': 'm=5 or m=25 mod 30',
            'nonmonotone_successful_step': {'from': [41, 9], 'to': [38, -3],
                                           'm_before': 1555, 'm_after': 1585}}


def forced_trace(u, v):
    assert gcd(u, v) == 1
    path = [(u, v)]
    letters = []
    while u+v:
        if u and u % 3 == 0:
            u, v = -u//3, v-u//3
            letters.append('A')
        elif v and v % 3 == 0:
            u, v = u-v//3, -v//3
            letters.append('B')
        else:
            return {'path': path, 'letters': ''.join(letters), 'distance': None}
        path.append((u, v))
    return {'path': path, 'letters': ''.join(letters), 'distance': len(letters)+1}


def root_couplings():
    records = []
    for m, p, q in ((9145, 31, 59), (21235, 31, 137)):
        rows = []
        for u, v in shell((1, -1, 3), m):
            if u <= 0 or (u+v) % 5:
                continue
            trace = forced_trace(u, v)
            assert trace['distance'] == core_distance(3, u, v)
            label = (u*pow(v, -1, p) % p, u*pow(v, -1, q) % q)
            rows.append({'pair': (u, v), 'root_labels': label, **trace})
        assert len(rows) == 4 and len({tuple(row['root_labels']) for row in rows}) == 4
        accepted = {tuple(row['root_labels']) for row in rows if row['distance'] is not None}
        assert len(accepted) < len({a for a, b in accepted})*len({b for a, b in accepted})
        if m == 21235:
            assert len(accepted) == 3  # Cannot be a subgroup coset of (C_2)^2.
        else:
            assert len(accepted) == 2
        records.append({'m': m, 'varying_primes': (p, q), 'all_G_legal_representations': rows})
    return records


def mm(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return a*e+b*g, a*f+b*h, c*e+d*g, c*f+d*h


def mv(t, x):
    a, b, c, d = t
    u, v = x
    return a*u+b*v, c*u+d*v


def make_macro(word):
    t = (1, 0, 0, 1)
    for letter in word:
        t = mm(t, (-3, 0, -1, 1) if letter == 'A' else (1, -1, 0, -3))
    swap = len(word) % 2
    if swap:
        t = mm(t, (0, 1, 1, 0))
    a, b, c, d = t
    determinant = a*d-b*c
    assert determinant == 3**len(word)
    if (a+d)**2 >= 4*determinant:
        return None
    content = gcd(c, gcd(d-a, b))
    form = (c//content, (d-a)//content, -b//content)
    if form[0] < 0:
        form = tuple(-value for value in form)
    return t, form, swap


def literal_macro_replay(word, swap, t, seed):
    u, v = mv(t, seed)
    assert gcd(u, v) == 1 and (u+v) % 5 == 0
    center = F(-u-v, 5)
    state = (center, center, center, center+u, center+v)
    for letter in word:
        if letter == 'A':
            changed = atom(state, (0, 1, 3))
            state = (changed[0], changed[1], changed[3], changed[2], changed[4])
        else:
            changed = atom(state, (0, 1, 4))
            state = (changed[0], changed[1], changed[4], changed[3], changed[2])
        assert all(z.denominator == 1 for z in state)
    if swap:
        state = state[:3]+(state[4], state[3])
    a, b = seed
    c = F(-a-b, 5)
    assert state == (c, c, c, c+a, c+b)
    assert core_distance(3, u, v) == len(word)+core_distance(3, a, b)


def generic_elliptic_macros():
    macros = classes = roots = replays = 0
    for length in range(1, 8):
        for letters in product('AB', repeat=length):
            word = ''.join(letters)
            result = make_macro(word)
            if result is None:
                continue
            t, form, swap = result
            a, b, c, d = t
            qa, qb, qc = form
            modulus = 3**length
            assert (a+d) % 3 and (qb*qb-4*qa*qc) % 3
            transformed = (qa*a*a+qb*a*c+qc*c*c,
                           2*qa*a*b+qb*(a*d+b*c)+2*qc*c*d,
                           qa*b*b+qb*b*d+qc*d*d)
            assert transformed == tuple(modulus*q for q in form)
            local_roots = 0
            # These two disjoint charts exhaust P^1(Z/3^length Z).
            projective = [(1, v) for v in range(modulus)]
            projective += [(u, 1) for u in range(0, modulus, 3)]
            for u, v in projective:
                if (u-v) % 3 == 0:
                    continue
                norm_divisible = norm(form, u, v) % modulus == 0
                inverse_integral = ((d*u-b*v) % modulus == 0 and
                                    (-c*u+a*v) % modulus == 0)
                assert norm_divisible == inverse_integral, (word, u, v)
                classes += 1
                local_roots += norm_divisible
            assert local_roots == 1
            roots += local_roots
            macros += 1
            for seed in ((1, -1), (2, 3), (7, 3)):
                literal_macro_replay(word, swap, t, seed)
                replays += 1
    return {'all_word_lengths': [1, 7], 'elliptic_macros': macros,
            'complete_admissible_projective_classes': classes, 'unique_integrality_roots': roots,
            'independent_physical_macro_replays': replays,
            'scope': 'All lengths beyond 7 are covered by the written Z_3 eigenlattice proof, '
                     'not by this finite enumeration.'}


def minus971_shells():
    t, form, swap = make_macro('AABAA')
    assert t == (-9, 63, -5, 8) and form == (5, -17, 63) and swap == 1
    records = []
    for k in range(19):
        reps = shell(form, 85*3**k)
        accepted = 0
        for u, v in reps:
            predicted = (u+v) % 5 == 0 and (k == 0 or u % 3 == 0)
            actual = core_distance(3, u, v)
            assert predicted == (actual is not None), (k, u, v)
            if predicted:
                assert k % 5 == 0 and actual == k+1
                accepted += 1
        if k == 0:
            assert set(reps) == {(1, -1), (-1, 1)}
        elif k < 5:
            assert not reps
        records.append({'k': k, 'primitive_representations': len(reps), 'accepted': accepted})
    # Coordinate identity for multiplication by conjugate zeta on (5, zeta-8).
    for u in range(-8, 9):
        for v in range(-8, 9):
            alpha = (5*u-8*v, v)
            # zeta^2 + zeta + 243 = 0, conjugate zeta = -1-zeta.
            aa, bb = alpha
            multiplied = (-aa+243*bb, -aa)
            uu, vv = mv(t, (u, v))
            assert multiplied == (5*uu-8*vv, vv)
            assert aa*aa-aa*bb+243*bb*bb == 5*norm(form, u, v)
    return records


def run():
    towers = full_towers()
    for r in range(1, 16):
        a = (-3)**r
        b = (a-1)//4
        positive = a < 0 and b*b+4*a < 0
        assert positive == (r in (1, 3))
        for u, v in ((1, -1), (2, 3), (-7, 9)):
            q = (1, b, -a)
            assert norm(q, a*v, u+b*v) == (-a)*norm(q, u, v)
    return {'status': 'PASS', 'general_strip': generalized_strip_checks(),
            'root_labels': root_label_checks(), **towers,
            'independent_physical_three_step_replays': physical_three_step_checks(),
            'general_prime_slices': general_prime_slices(),
            'global_norm_restriction': global_norm_restriction(),
            'root_couplings': root_couplings(),
            'generic_elliptic_macros': generic_elliptic_macros(),
            'minus971_complete_shells': minus971_shells(),
            'scope': 'All listed integer norm shells are completely enumerated. Finite exponent '
                     'checks and the prior exact oracle detect mistakes; all-exponent claims, '
                     'root-label uniqueness, Euclideanity and the ideal-class interpretation '
                     'are proved in the accompanying note. No all-five-entry static criterion claimed.'}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    result = run()
    Path(__file__).with_name('five_quadratic_norm_towers_verification.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    brief = {k: v for k, v in result.items() if k not in
             ('minus11_complete_shells', 'minus59_complete_shells',
              'minus971_complete_shells', 'root_couplings')}
    brief['minus11_complete_shell_count'] = len(result['minus11_complete_shells'])
    brief['minus59_complete_shell_count'] = len(result['minus59_complete_shells'])
    brief['minus971_complete_shell_count'] = len(result['minus971_complete_shells'])
    brief['complete_root_coupling_moduli'] = [item['m'] for item in result['root_couplings']]
    print(json.dumps(brief, ensure_ascii=False, indent=2))
