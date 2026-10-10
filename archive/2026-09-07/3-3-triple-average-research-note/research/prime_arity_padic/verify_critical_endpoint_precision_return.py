"""Exact audits of five-step one-digit returns; no orbit search over inputs.

The only exhaustive part enumerates three remaining type selections for p=3,5,7,
with exact p-adic congruence pruning. Larger primes use derived formulas.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from pathlib import Path
import argparse
import json

HERE = Path(__file__).resolve().parent
RECORD = HERE / 'critical_endpoint_precision_return_verification.json'


def primes(bound):
    sieve = bytearray(b'\x01') * (bound + 1)
    sieve[:2] = b'\x00\x00'
    for a in range(2, int(bound ** .5) + 1):
        if sieve[a]:
            sieve[a*a:bound+1:a] = b'\x00' * ((bound-a*a)//a + 1)
    return [i for i in range(2, bound + 1) if sieve[i]]


def parameters(p):
    u = 2 * ((p + 1) // 4) - 1
    v = p + 1 - u
    k = (pow(v, -1, u) - 1) % u
    l = (p + v * k) // u
    assert 2 <= u < p and 2 <= v < p and gcd(u, v) == 1
    assert 1 <= k < u and 1 <= l < v
    assert u*l - v*k == p
    assert 2 <= k+l <= p-1
    return u, v, k, l


def row_mean(rows, counts, p):
    return tuple(sum(count * row[j] for row, count in zip(rows, counts)) / p
                 for j in range(2))


@lru_cache(None)
def choices(bounds, total):
    if len(bounds) == 1:
        return ((total,),) if 0 <= total <= bounds[0] else ()
    lower = max(0, total - sum(bounds[1:]))
    return tuple((i,) + tail
                 for i in range(lower, min(bounds[0], total) + 1)
                 for tail in choices(bounds[1:], total-i))


def residue_constraint(row, p, allowed_depth, domain):
    """Intersect t == r (mod p**e) with row(1,t) in p^-depth Z_p."""
    den = max(row[0].denominator, row[1].denominator)
    exp = 0
    while den % p == 0:
        den //= p
        exp += 1
    assert den == 1
    exp -= allowed_depth
    if exp <= 0:
        return domain
    scale = p ** (exp + allowed_depth)
    a, b = int(row[0]*scale), int(row[1]*scale)
    modulus = p ** exp
    common = gcd(b, modulus)
    if a % common:
        return None
    modulus //= common
    if modulus == 1:
        return domain
    residue = (-a // common * pow(b // common, -1, modulus)) % modulus
    new_exp = 0
    temp = modulus
    while temp > 1:
        temp //= p
        new_exp += 1
    old_residue, old_exp = domain
    if (old_residue-residue) % (p ** min(old_exp, new_exp)):
        return None
    return (residue, new_exp) if new_exp > old_exp else domain


def integral_on_domain(row, p, domain):
    r, e = domain
    return ((row[0] + row[1]*r).denominator == 1
            and (row[1]*p**e).denominator == 1)


def state_after(state, counts, mean, p):
    out = Counter({row: count-take for (row, count), take in zip(state, counts)
                   if count > take})
    out[mean] += p
    return tuple(sorted(out.items()))


def exhaustive_cleanup(p):
    """All type choices after the two initial fractional blocks, modulo units."""
    U, V, C = (F(1,p), F(0)), (F(0), F(1,p)), (F(-1), F(-1))
    start = tuple(sorted(((U,p), (V,p), (C,1))))
    nodes = [(start, (r,1), ()) for r in range(1,p)]
    layer_sizes = []
    finals = 0
    rank_one = 0
    for stage in range(3):
        following = []
        for state, domain, history in nodes:
            rows = tuple(row for row, count in state)
            for counts in choices(tuple(count for row,count in state), p):
                if sum(c > 0 for c in counts) == 1:
                    continue  # An identical-value average cannot be in a minimal excursion.
                mean = row_mean(rows, counts, p)
                nxt_domain = residue_constraint(mean, p, 1, domain)
                if nxt_domain is None:
                    continue
                nxt = state_after(state, counts, mean, p)
                record = (dict(zip(rows, counts)), mean)
                hist = history + (record,)
                if stage < 2:
                    following.append((nxt, nxt_domain, hist))
                    continue
                for row, count in nxt:
                    nxt_domain = residue_constraint(row, p, 0, nxt_domain)
                    if nxt_domain is None:
                        break
                if nxt_domain is None:
                    continue
                finals += 1
                assert all(integral_on_domain(mean_row, p, nxt_domain)
                           for _, mean_row in hist)
                first, D = hist[0]
                assert first.get(C, 0) == 1
                u, v = p-first.get(U,0), p-first.get(V,0)
                assert 2 <= u < p and 2 <= v < p and u+v == p+1
                second, E = hist[1]
                k, l = second.get(U,0), second.get(V,0)
                assert 1 <= k < u and 1 <= l < v
                q = k+l
                assert 2 <= q < p and second.get(D,0) == p-q
                third, final_mean = hist[2]
                s = q-third.get(D,0)
                assert 1 <= s <= q
                assert third.get(U,0) == u-k and third.get(V,0) == v-l
                assert third.get(E,0) == s-1
                delta = u*l-v*k
                assert delta % p == 0
                det = D[0]*E[1]-D[1]*E[0]
                assert det == F(-delta,p**4)
                if p in (3,5):
                    assert delta == 0  # Exact small-prime obstruction.
                rank_one += int(delta == 0)
        layer_sizes.append(len(following) if stage < 2 else finals)
        nodes = following
    if p == 7:
        assert finals > rank_one
    return {'p':p, 'layers':layer_sizes,
            'admissible_histories':finals, 'rank_one_histories':rank_one,
            'rank_two_histories':finals-rank_one}


def non_p_G(state, p):
    if not any(state):
        return 1
    denominator = 1
    for x in state:
        denominator = denominator*x.denominator // gcd(denominator,x.denominator)
    nums = [int(x*denominator) for x in state]
    content = gcd(*nums)
    primitive = [x//content for x in nums]
    value = gcd(*(x-primitive[0] for x in primitive))
    while value and value % p == 0:
        value //= p
    return value


def physical_path(p, D=1, E=2):
    u,v,k,l = parameters(p)
    q = k+l
    A = (v*(p-q)-p*l)*D-p*v*E
    B = (p*k-u*(p-q))*D+p*u*E
    assert A % p and B % p
    assert (2*D+(p-1)*E) % p == 0
    final_mean = -(2*D+(p-1)*E)//p
    def block(total):
        a, remainder = divmod(total,p)
        return [F(a)]*(p-1) + [F(a+remainder)]
    state = block(A)+block(B)+[F(-A-B)]
    first, second = list(range(p)), list(range(p,2*p))
    third = first[:p-u]+second[:p-v]+[2*p]
    left_U, left_V = first[p-u:], second[p-v:]
    fourth = left_U[:k]+left_V[:l]+third[:p-q]
    left_D = third[p-q:]
    fifth = left_U[k:]+left_V[l:]+left_D[:q-2]+fourth[:1]
    actions = [first, second, third, fourth, fifth]
    obs = [non_p_G(state,p)]
    for index, selected in enumerate(actions):
        assert len(selected) == p and len(set(selected)) == p
        mean = sum(state[i] for i in selected)/p
        if index < 2:
            assert mean.denominator == p
        else:
            assert mean.denominator == 1
        old_energy = sum(x*x for x in state)
        for i in selected:
            state[i] = mean
        assert sum(x*x for x in state) < old_energy
        assert sum(state) == 0
        assert all(p % x.denominator == 0 for x in state)
        obs.append(non_p_G(state,p))
    expected = [F(D)]*2+[F(E)]*(p-1)+[F(final_mean)]*p
    assert sorted(state) == sorted(expected)
    assert len(set(obs[2:])) == 1  # The three-step block map preserves the full non-p obstruction.
    if D == 1 and E == 2:
        assert set(obs) == {1}
        # Independent integer-only completion of the common nonzero endpoint.
        selected = ([i for i,x in enumerate(state) if x == 1][:2]
                    +[i for i,x in enumerate(state) if x == 2][:(p-3)//2]
                    +[i for i,x in enumerate(state) if x == -2][:(p-1)//2])
        assert len(selected) == p and sum(state[i] for i in selected) == 0
        for i in selected:
            state[i] = F(0)
        while any(state):
            pos = next(i for i,x in enumerate(state) if x == 2)
            neg = next(i for i,x in enumerate(state) if x == -2)
            zeros = [i for i,x in enumerate(state) if x == 0][:p-2]
            assert len(zeros) == p-2
            for i in [pos,neg]+zeros:
                state[i] = F(0)
    return {'p':p, 'counts':[u,v,k,l], 'sums':[A,B], 'start_obstruction':obs[0]}


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def frozen_family_audit(bound=499):
    stats = [0,0,0,0]
    cases = 0
    first_thirds = []
    for p in primes(bound):
        if p < 3:
            continue
        cases += 1
        counts, values = [p+2,p-2,1], [1,2,2-3*p]
        thirds = fourths = returns = 0
        for ci,c in enumerate(values):
            pool = counts.copy()
            pool[ci] -= 1
            for bad in range(pool[2]+1):
                for twos in range(pool[1]+1):
                    ones = p-bad-twos
                    if not 0 <= ones <= pool[0]:
                        continue
                    A = ones+2*twos+bad*values[2]
                    B = -c-A
                    if A > B or A % p == 0 or B % p == 0 or (A-B) % p == 0:
                        continue
                    stats[0] += 1
                    u = (-(p+1)*B*pow(A-B,-1,p*p)) % (p*p)
                    v = p+1-u
                    if not 2 <= u < p or not 2 <= v < p:
                        continue
                    thirds += 1
                    D = -(u*A+v*B)//(p*p)
                    inv_u = pow(u,-1,p)
                    for k in range(1,u):
                        l = v*k*inv_u % p
                        q = k+l
                        if not 1 <= l < v or q >= p:
                            continue
                        numerator = k*A+l*B+p*(p-q)*D
                        if numerator % (p*p):
                            continue
                        fourths += 1
                        E = numerator//(p*p)
                        returns += sum((s*D+(p+1-s)*E) % p == 0
                                       for s in range(1,q+1))
        stats[1] += thirds
        stats[2] += fourths
        stats[3] += returns
        if p == 7:
            assert thirds == returns == 0
        if thirds and len(first_thirds) < 6:
            first_thirds.append([p,thirds,fourths,returns])
    assert stats[3] == 0
    return {'prime_bound':bound, 'primes':cases,
            'first_partitions':stats[0], 'integral_third_steps':stats[1],
            'integral_fourth_steps':stats[2], 'five_step_returns':stats[3],
            'first_nonempty_third_layers':first_thirds,
            'status':'Finite diagnostic; only p=7 has the additional general exclusion proof in this note.'}


def block_matrix(p,u,v,k,l,s):
    q = k+l
    D = [F(p-u,p),F(p-v,p),F(1,p)]
    E = [F(k,p)+(p-q)*D[0]/p,
         F(l,p)+(p-q)*D[1]/p,(p-q)*D[2]/p]
    Frow = [F(u-k,p)+(q-s)*D[0]/p+(s-1)*E[0]/p,
            F(v-l,p)+(q-s)*D[1]/p+(s-1)*E[1]/p,
            (q-s)*D[2]/p+(s-1)*E[2]/p]
    return [D,E,Frow]


def formula_checks():
    count = 0
    for p in primes(311):
        if p < 7:
            continue
        u,v,k,l = parameters(p)
        q = k+l
        for s in (1,2,q):
            M = block_matrix(p,u,v,k,l,s)
            assert all(sum(row) == 1 for row in M)
            assert all(x >= 0 for row in M for x in row)
            assert [sum(w*M[i][j] for i,w in enumerate((s,p+1-s,p)))
                    for j in range(3)] == [p,p,1]
            assert det3(M) == F(-1,p*p)
            count += 1
    huge = []
    for p in (2147483647,2305843009213693951):
        u,v,k,l = parameters(p)
        M = block_matrix(p,u,v,k,l,2)
        assert det3(M) == F(-1,p*p)
        huge.append({'p':p,'counts':[u,v,k,l]})
    return count,huge


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    small = [exhaustive_cleanup(p) for p in (3,5,7)]
    formulas, huge = formula_checks()
    paths = []
    extra = 0
    for p in primes(97):
        if p < 7:
            continue
        paths.append(physical_path(p))
        for D in (-2,-1,1,2):
            for t in (-2,-1,0,1,2):
                physical_path(p,D,2*D+p*t)
                extra += 1
    result = {'status':'PASS','small_prime_complete_congruence_audits':small,
              'full_three_value_matrix_checks':formulas,'large_parameter_checks':huge,
              'physical_five_step_paths':len(paths)+extra,
              'complete_integer_tails':len(paths),'examples':paths[:4],
              'frozen_family_diagnostic':frozen_family_audit(),
              'scope':'Exact identities and finite congruence/type audits; general theorems are proved in the note. No all-input precision theorem.'}
    if args.write:
        RECORD.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    elif RECORD.exists():
        assert result == json.loads(RECORD.read_text(encoding='utf-8'))
    print(json.dumps(result,ensure_ascii=False))


if __name__ == '__main__':
    main()
