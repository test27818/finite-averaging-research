"""Exact four-lift one-stage criterion and an infinite multistep escape family.

The criterion exhausts all integer translations and all possible primitive
cancellations in one M_q return. Complexity is O(p) gcd tests per input; it
does not enumerate a height-dependent translation interval or search words.
"""

from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
from random import Random
import json

from verify_two_prime_neighbour_complete import RecordedPair, replay


def mv(matrix, pair):
    return tuple(sum(a*b for a,b in zip(row,pair)) for row in matrix)


def det(matrix):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]


def audit_prefix_content():
    rng=Random(20260915)
    count=0
    for p in (5,7,11,29):
        m=p+1
        letters=[((1,-1),(0,1)),((-1,-1),(-m,4-m)),
                 ((1,0),(0,-1)),((1,1),(0,1)),((-1,-1),(-m,2*p-m))]
        prefix=((1,0),(0,1))
        prefixes=[]
        for letter in letters:
            prefix=tuple(tuple(sum(letter[i][k]*prefix[k][j] for k in range(2))
                               for j in range(2)) for i in range(2))
            prefixes.append(prefix)
        # m in place of rad(m) is an equally valid, slightly larger modulus.
        modulus=m*lcm(*(abs(det(w)) for w in prefixes))
        for _ in range(80):
            u,v=rng.randrange(-1000,1001),rng.randrange(1,1001)
            if gcd(u,v)!=1:
                continue
            lifted=(u+modulus*rng.randrange(-5,6),v+modulus*rng.randrange(1,6))
            if gcd(*lifted)!=1:
                continue
            for w in prefixes:
                out=mv(w,(u,v))
                out_lifted=mv(w,lifted)
                content=gcd(*out)
                assert abs(det(w))%content==0
                assert content==gcd(*out,abs(det(w)))==gcd(*out_lifted)
                assert (gcd(out[1]//content,m)==1)==(gcd(out_lifted[1]//content,m)==1)
                if out[1]:
                    slope=Fraction(u,v)
                    assert (abs(out[1])<content*v)==(abs(w[1][0]*slope+w[1][1])<content)
                count+=1
    print('fixed-word prefix content and exact slope cells: PASS',count)
    return count


def audit_multiple_terminals():
    count=0
    for p in range(5,80,2):
        for v in range(1,p+3,2):
            if p%v and (p+2)%v:
                continue
            for u in range(v):
                if gcd(u,v)!=1:
                    continue
                exceptions=v==p+2 and u in (2,v-2)
                found=False
                # Bounded normalization: every needed odd lift has |u+k*v|<=v.
                for k in (-1,0,1):
                    a=u+k*v
                    for s in (0,1,2):
                        numerator=(p-(p+1)*s)*a+(p-s)*v
                        if numerator%(2*v)==0 and 0<=numerator//(2*v)<=p-s:
                            found=True
                if exceptions:
                    assert not found
                    # Sign and translation give (p,p+2); M_p sends it to (m,1).
                    out=mv(((-1,-1),(-(p+1),p-1)),(p,p+2))
                    assert out==(-2*(p+1),-2)
                else:
                    assert found
                count+=1
    print('uniform multiple terminal denominator classes: PASS',count)
    return count


def carrier_fixed(ledger,digit):
    p=ledger.p
    assert 1<=digit<=p and digit%2
    j=(p-digit)//2
    first,second=list(ledger.first),list(ledger.second)
    groups=(first[:p-j]+second[:j],first[p-j:]+second[j:])
    u,v=ledger.parameters()
    for group in groups:
        ledger.average(group)
    ledger.first,ledger.second=map(list,groups)
    assert ledger.parameters()==(u,Fraction(digit,p)*v)


def audit_height_preserving_preparation():
    p=29
    conductor=lcm(*range(1,p+1))
    records=[]
    for h in (3,4,11,23,100):
        t=1+conductor*h
        raw=[11*t+conductor]*p+[-3*t-conductor]*p+[-116*t]*2
        ledger=RecordedPair(p,raw,range(p),range(p,2*p),[2*p,2*p+1])
        ledger.execute([('u',1)])
        carrier_fixed(ledger,11)
        prepared=(29*(t+conductor//11),7*t+conductor)
        assert gcd(*prepared)==1
        pu,pv=ledger.parameters()
        assert pu*prepared[1]==pv*prepared[0]
        ledger.execute([('s',0),('u',4),('n',13-15)])
        output=(-3*t-13*conductor//11,t-247*conductor//11)
        assert gcd(*output)==gcd(output[1],p+1)==1
        assert 0<abs(output[1])<7*t+conductor
        pu,pv=ledger.parameters()
        assert pu*output[1]==pv*output[0]
        assert replay(raw,p,ledger.word)==ledger.state
        assert len(ledger.word)==14
        records.append({'h':h,'prepared_uv':prepared,'output_uv':output,
                        'operations':ledger.word})
    print('carrier-fixed height-preserving cone preparation: PASS',len(records))
    return records


def audit_uniform_preparation():
    count=0
    literal=0
    for p in (5,7,11,13,29):
        for v in range(3,44,2):
            if gcd(v,p*(p+1))!=1:
                continue
            for digit in range(1,p+1,2):
                if gcd(digit,v)!=1:
                    continue
                for u in range(1,v):
                    if gcd(u,v)!=1:
                        continue
                    shift=(-u*pow(v,-1,digit))%digit
                    numerator=p*((u+shift*v)//digit)
                    assert gcd(numerator,v)==1
                    assert numerator%v==p*u*pow(digit,-1,v)%v
                    count+=1
            # Include digits sharing factors with m, such as p5, digit3.
        for digit in range(1,p+1,2):
            u,v=4,101
            raw=[u+v]*p+[u-v]*p+[-p*u]*2
            ledger=RecordedPair(p,raw,range(p),range(p,2*p),[2*p,2*p+1])
            shift=(-u*pow(v,-1,digit))%digit
            ledger.execute([('u',shift)])
            carrier_fixed(ledger,digit)
            pu,pv=ledger.parameters()
            numerator=p*((u+shift*v)//digit)
            assert pu*v==pv*numerator
            assert replay(raw,p,ledger.word)==ledger.state
            literal+=1
    print('uniform constant-height preparation arithmetic and physical: PASS',count,literal)
    return {'arithmetic':count,'literal':literal}


def small_height_step(p,u,v):
    m=p+1
    assert 1<v<=m and gcd(u,v)==gcd(v,m)==1
    if gcd(p,v)>1:
        common=gcd(p,v)
        return {'divide':common,'following':(p*u//common,v//common)}
    e=pow(v,-1,m)
    assert 2<=e<=p
    a=(e*v-1)//m
    assert 0<a<v and e*v-m*a==1
    residue=p*u*pow(2*a,-1,v)%v
    sign=1 if residue%2 else -1
    digit=residue if sign>0 else v-residue
    assert 1<=digit<=p and digit%2 and gcd(digit,v)==1
    first_shift=(-sign*u*pow(v,-1,digit))%digit
    prepared=p*((sign*u+first_shift*v)//digit)
    next_shift=(2*a-v-prepared)//v
    assert prepared+next_shift*v==2*a-v
    assert mv(((-1,-1),(-m,2*e-m)),(2*a-v,v))==(-2*a,2)
    return {'sign':sign,'digit':digit,'first_shift':first_shift,
            'next_shift':next_shift,'q':e,'a':a}


def audit_small_height_completion():
    count=0
    for p in range(5,80,2):
        for v in range(3,p+2,2):
            if gcd(v,p+1)!=1:
                continue
            for u in range(1,v):
                if gcd(u,v)==1:
                    small_height_step(p,u,v)
                    count+=1
    records=[]
    for p,u,v in ((5,1,5),(7,3,5),(11,4,7),(29,4,7),(29,5,13),(29,8,17)):
        raw=[u+v]*p+[u-v]*p+[-p*u]*2
        ledger=RecordedPair(p,raw,range(p),range(p,2*p),[2*p,2*p+1])
        initial=(u,v)
        while v>1:
            step=small_height_step(p,u,v)
            if 'divide' in step:
                carrier_fixed(ledger,1)
                u,v=step['following']
            else:
                if step['sign']<0:
                    ledger.execute([('s',0)])
                ledger.execute([('u',step['first_shift'])])
                carrier_fixed(ledger,step['digit'])
                ledger.execute([('u',step['next_shift']),('n',step['q']-(p+1)//2)])
                u,v=-step['a'],1
        ledger.execute([('u',-u)])
        assert ledger.parameters()[0]==0
        ledger.finish()
        assert not any(replay(raw,p,ledger.word))
        records.append({'p':p,'uv':initial,'operations':ledger.word})
    print('uniform all-small-denominator core completion: PASS',count,len(records))
    return {'arithmetic':count,'complete_paths':records}


def four_lifts(p,u,v):
    assert p>=5 and p%2 and v>1 and gcd(u,v)==gcd(v,p+1)==1
    b=u*pow(2,-1,v)%v
    b=min(b,v-b)
    assert 0<2*b<v
    result=[]
    for t in (b,v-b,v+b,2*v-b):
        for q in range(2,p+1):
            common=gcd(t,q)
            if gcd(q//common,p+1)!=1:
                continue
            remainder=q*v-(p+1)*t
            if 0<abs(remainder)<common*v:
                result.append((t,q,common,-t//common,remainder//common))
    return result


def independent_factor_form(p,u,v):
    result=set()
    m=p+1
    for e in range(1,p+1,2):
        if gcd(e,m)!=1:
            continue
        for d in range(1,p//e+1):
            if d*e<2:
                continue
            lo=(e-1)*v//m+1
            hi=((e+1)*v-1)//m
            for a in range(lo,hi+1):
                if gcd(a,e)!=1:
                    continue
                if (2*d*a-u)%v and (2*d*a+u)%v:
                    continue
                result.add((d*a,d*e,d,-a,e*v-m*a))
    return result


def audit_criterion():
    count=0
    for p in (5,7,11,13,17,29,41):
        for v in range(3,72,2):
            if gcd(v,p+1)!=1:
                continue
            for u in range(1,v):
                if gcd(u,v)!=1:
                    continue
                assert set(four_lifts(p,u,v))==independent_factor_form(p,u,v)
                count+=1
    print('four-lift exact one-stage criterion: PASS',count)
    return count


def audit_infinite_family():
    p,m=29,30
    conductor=lcm(*range(1,p+1))
    assert conductor%208==0 and conductor%120==0
    assert not four_lifts(p,4,7)
    # In b/v in (8/30,9/30), failure of each strict inequality depends only
    # on that cell and the t mod q data, not on an input-height cutoff.
    certificate=[]
    for c,sign in ((0,1),(1,-1),(1,1),(2,-1)):
        base_t=7*c+2*sign
        for q in range(2,p+1):
            g=gcd(base_t,q)
            if gcd(q//g,m)!=1:
                certificate.append((c,sign,q,g,'illegal'))
                continue
            # remainder/v = q - 30*(c+sign*x), x in (8/30,9/30).
            endpoints=(q-30*c-8*sign,q-30*c-9*sign)
            low,high=min(endpoints),max(endpoints)
            assert low>=g or high<=-g
            certificate.append((c,sign,q,g,'no-descent'))
    records=[]
    for h in (2,3,5,11,100):
        t=1+conductor*h
        b,v=2*t,7*t+conductor
        assert gcd(b,v)==gcd(v,m)==1 and 8*v<30*b<9*v
        assert 7*b-2*v==-2*conductor
        assert not four_lifts(p,2*b,v)
        raw=[2*b+v]*p+[2*b-v]*p+[-p*(2*b)]*2
        ledger=RecordedPair(p,raw,range(p),range(p,2*p),[2*p,2*p+1])
        plan=[('u',-1),('n',7-15),('s',0),('u',1),('n',26-15)]
        ledger.execute(plan)
        physical_u,physical_v=ledger.parameters()
        expected_u=5*t-7*conductor//2
        expected_v=7*t-14*conductor
        assert expected_v==v-15*conductor and 0<expected_v<v
        assert gcd(expected_u,expected_v)==gcd(expected_v,m)==1
        assert physical_u*expected_v==physical_v*expected_u
        assert len(ledger.word)==8
        assert replay(raw,p,ledger.word)==ledger.state
        records.append({'h':h,'input_uv':[2*b,v],'output_uv':[expected_u,expected_v],
                        'operations':ledger.word,'height_drop':v-expected_v})
    # The base obstruction also has a concrete full solution, not an
    # unreachable example: heights7 ->11 ->7 ->1 ->zero.
    raw=[11]*p+[-3]*p+[-116]*2
    ledger=RecordedPair(p,raw,range(p),range(p,2*p),[2*p,2*p+1])
    plan=[('u',-1),('n',-8),('s',0),('u',1),('n',11),('n',11),('u',3)]
    ledger.execute(plan)
    assert ledger.parameters()[0]==0
    ledger.finish()
    assert not any(replay(raw,p,ledger.word))
    print('infinite no-one-stage cone certificate: PASS',len(certificate))
    print('uniform eight-atom cone escape samples: PASS',len(records))
    print('base multi-prime obstruction full path: PASS',len(ledger.word))
    return {'conductor':conductor,'cone_certificate':certificate,'escape_records':records,
            'base_full_path':ledger.word}


if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Assertions are required.')
    count=audit_criterion()
    data=audit_infinite_family()
    data.update({'one_stage_checks':count,'prefix_content_checks':audit_prefix_content(),
                 'multiple_terminal_checks':audit_multiple_terminals(),
                 'height_preserving_preparation':audit_height_preserving_preparation(),
                 'uniform_constant_height_preparation':audit_uniform_preparation(),
                 'small_denominator_completion':audit_small_height_completion(),
                 'scope':'Exact one-stage criterion, prefix content, terminal classes, '
                 'p29 escape families and constant-height preparation. Uniform complete '
                 'core solution for every odd p>=5 with primitive denominator v<=p+1. '
                 'No general multistage termination or new dimension criterion. '
                 'The external Furstenberg theorem and finite-exception deduction '
                 'are not established by numerical checks.'})
    (Path(__file__).parent/'core_gap_four_lift_records.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print('core gap exact criterion and multistage interface: PASS')
