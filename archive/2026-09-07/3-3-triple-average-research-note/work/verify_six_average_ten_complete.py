"""Six-averaging n10: genuine G iff criterion via a positive Gamma_0(5).

Four fixed physical macros, exact-scale cycles, an explicit commutator and
six-coset Schreier decomposition. No discovery or word search is called.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd,lcm
from pathlib import Path
from random import Random
import json

from verify_uniform_endpoint_controller import Program, Element, I, SIGMA
from verify_prime_power_endpoint_completion import S,T,mul,inv,bezout
from verify_four_average_nine_complete import FourCompiler,integer_word
from verify_composite_arity_transfer import primitive_center,gap_gcd,independent_replay


class SixProgram(Program):
    def __init__(self):
        # self.p is the physical averaging arity; self.q is the congruence level.
        self.p,self.q=6,5
        self.nodes,self.cache=[],{}
        self.one=Element(self.make(('i',),I,0))
        self.one.back=self.one.node
        self.a=Element(self.make(('a',),(2,-1,0,-1),1))
        self.b=Element(self.make(('b',),(-4,3,-10,9),1))
        self.c=Element(self.make(('c',),(-4,1,-10,1),1))
        self.r=Element(self.make(('r',),(1,-1,5,-3),2))

    def seed(self):
        self.check(self.power(self.r,4),I)
        self.give_inverse(self.r,self.power(self.r,3))
        self.check(self.power(self.mul(self.a,self.r),2),I)
        self.give_inverse(self.a,self.mul(self.r,self.a,self.r))
        ra=self.mul(self.r,self.a)
        self.check(self.power(self.mul(ra,self.c),2),I)
        self.give_inverse(self.c,self.mul(ra,self.c,ra))
        self.swap=self.mul(self.inv(self.c),self.b)
        self.check(self.swap,SIGMA)
        self.give_inverse(self.swap,self.swap)
        self.give_inverse(self.b,self.mul(self.swap,self.inv(self.c)))
        half=self.mul(self.swap,self.a)
        self.check(half,(1,0,0,F(1,2)))
        self.d2=self.inv(half)
        self.uhalf=self.halves(self.d2)
        self.u=self.power(self.uhalf,2)
        self.sign=self.mul(self.swap,self.u)
        self.check(self.sign,(1,0,0,-1))
        self.f=self.mul(self.inv(self.u),self.c)
        self.check(self.f,(1,0,F(-5,3),F(1,6)))
        self.ell=self.mul(self.d2,self.f,self.inv(self.d2),self.inv(self.f))
        self.check(self.ell,(1,0,F(-5,3),1))
        self.lower=self.power(self.ell,-3)
        self.check(self.lower,(1,0,5,1))
        inverse_six=self.mul(self.inv(self.ell),self.f)
        self.check(inverse_six,(1,0,0,F(1,6)))
        self.d3=self.mul(self.inv(inverse_six),self.inv(self.d2))
        self.check(self.d3,(1,0,0,3))


class SixCompiler(FourCompiler):
    def __init__(self):
        self.program=SixProgram()
        self.program.seed()
        self.diagonals={}


REP={j%5:j for j in (0,1,-1,2,-2)}
REPS={**{j:(0,-1,1,j) for j in REP.values()},None:I}


def label(c,d):
    assert gcd(c,d,5)==1
    return REP[d*pow(c,-1,5)%5] if c%5 else None


def edge(key,generator):
    candidate=mul(REPS[key],generator)
    following=label(candidate[2],candidate[3])
    loop=mul(candidate,inv(REPS[following]))
    if generator==S:
        expected=I if key is None else (-1,0,0,-1) if key==0 else (
            -following,-1,key*following+1,key)
    elif key is None:
        expected=generator
    else:
        expected=(1,0,-(key+generator[1]-following),1)
    assert expected==loop and loop[2]%5==0
    return following,loop


def compile_integer(matrix,compiler):
    assert matrix[2]%5==0
    key,result=None,compiler.program.one
    for generator in integer_word(matrix):
        key,loop=edge(key,generator)
        result=compiler.program.mul(result,compiler.gauss(loop))
    assert key is None
    compiler.program.check(result,matrix)
    return result


class Replay:
    def __init__(self,u,v):
        self.state=[F(u)]*6+[F(v)]*3+[F(-6*u-3*v)]
        self.u,self.v,self.w=list(range(6)),list(range(6,9)),9
        self.word=[]

    def average(self,ids):
        assert len(ids)==len(set(ids))==6
        assert all(type(i) is int and 0<=i<10 for i in ids)
        mean=sum(self.state[i] for i in ids)/6
        for i in ids:
            self.state[i]=mean
        self.word.append(ids[:])

    def parameters(self):
        u,v=self.state[self.u[0]],self.state[self.v[0]]
        assert len(self.u)==6 and len(self.v)==3
        assert sorted(self.u+self.v+[self.w])==list(range(10))
        assert all(self.state[i]==u for i in self.u)
        assert all(self.state[i]==v for i in self.v)
        assert self.state[self.w]==-6*u-3*v
        return u,u-v

    def letter(self,key):
        if key==('a',):
            chosen,remaining=self.u[:3]+self.v,self.u[3:]
            self.average(chosen)
            self.u,self.v=chosen,remaining
        elif key==('b',):
            chosen,singleton=self.u[:5]+[self.w],self.u[5]
            self.average(chosen)
            self.u,self.w=chosen,singleton
        elif key==('c',):
            chosen=self.u[:3]+self.v[:2]+[self.w]
            remaining,singleton=self.u[3:],self.v[2]
            self.average(chosen)
            self.u,self.v,self.w=chosen,remaining,singleton
        elif key==('r',):
            # (u^4,v,w) -> t^6 with t=-(u+v)/3; leave two u,two v.
            first=self.u[:4]+self.v[:1]+[self.w]
            leftover_u,leftover_v=self.u[4:],self.v[1:]
            self.average(first)
            second=first[3:]+leftover_u[:1]+leftover_v
            self.average(second)
            self.u,self.v,self.w=second,first[:3],leftover_u[1]
        else:
            raise AssertionError('Unphysical leaf '+str(key))
        self.parameters()

    def finish(self):
        x,y=self.parameters()
        assert x==0
        if y:
            self.average(self.v+[self.w]+self.u[:2])
        assert not any(self.state)


def entry(raw):
    xs=primitive_center(raw)
    assert len(xs)==10 and gap_gcd(xs) in (1,2)
    i,j=next((i,j) for i,j in combinations(range(10),2) if (xs[i]-xs[j])%5)
    outside=[i,j]+[k for k in range(10) if k not in (i,j)][:2]
    first=[i for i in range(10) if i not in outside]
    replay=Replay(0,0)
    replay.state=list(map(F,xs))
    replay.average(first)
    a=replay.state[first[0]]
    residue=a.numerator*pow(a.denominator,-1,5)%5
    singleton=next(i for i in outside if xs[i]%5!=residue)
    second=first[:3]+[i for i in outside if i!=singleton]
    replay.average(second)
    replay.u,replay.v,replay.w=second,first[3:],singleton
    x,y=replay.parameters()
    assert y.numerator%5 and gap_gcd(replay.state) in (1,2)
    return replay


def target_matrix(x,y):
    den=lcm(x.denominator,y.denominator)
    x,y=int(x*den),int(y*den)
    common=gcd(x,y)
    x,y=x//common,y//common
    alpha,beta=bezout(x,y)
    k=-alpha*pow(y,-1,5)%5
    alpha,beta=alpha+k*y,beta-k*x
    assert alpha%5==0
    return y,-x,alpha,beta


def main():
    compiler=SixCompiler()
    program=compiler.program
    a=(F(1),F(-1,2),0,F(-1,2))
    b=tuple(F(x,6) for x in (-4,3,-10,9))
    c=tuple(F(x,6) for x in (-4,1,-10,1))
    r=tuple(F(x,6) for x in (1,-1,5,-3))
    r2=mul(r,r)
    ar=mul(a,r)
    rac=mul(mul(r,a),c)
    assert mul(r2,r2)==(F(-1,324),0,0,F(-1,324))
    assert mul(ar,ar)==(F(1,36),0,0,F(1,36))
    assert mul(rac,rac)==(F(1,216),0,0,F(1,216))
    atom_checks=0
    for name,matrix in (('a',a),('b',b),('c',c),('r',r)):
        for u,v in ((1,0),(0,1)):
            replay=Replay(u,v)
            replay.letter((name,))
            assert replay.parameters()==(matrix[0]*u+matrix[1]*(u-v),
                                        matrix[2]*u+matrix[3]*(u-v))
            assert len(replay.word)==(2 if name=='r' else 1)
            atom_checks+=1
    # The root commutator is also checked without projective normalization.
    f=(F(1),F(0),F(-5,3),F(1,6))
    fi=(F(1),F(0),F(10),F(6))
    actual_ell=mul(mul(mul((1,0,0,2),f),(1,0,0,F(1,2))),fi)
    assert actual_ell==(1,0,F(-5,3),1)
    rows=loops=0
    pivots=set()
    for c0,d0 in product(range(5),repeat=2):
        if gcd(c0,d0,5)==1:
            representative=REPS[label(c0,d0)]
            assert (c0*representative[3]-d0*representative[2])%5==0
            rows+=1
    for key in REPS:
        for generator in (S,T,inv(T)):
            _,loop=edge(key,generator)
            compiler.gauss(loop)
            pivots.add(abs(loop[0]))
            loops+=1
    assert len(REPS)==6 and pivots=={1,2}
    for i,(key,_,_) in enumerate(program.nodes):
        assert key[0] in ('i','a','b','c','r','m')
        if key[0]=='m':
            assert key[1]<i and key[2]<i
    print('six-average n10 actual periods and complete Gamma0(5): PASS',atom_checks,rows,loops,flush=True)
    # Every mod5 residue multiset of length10 with zero total and not constant.
    residue_cases=0
    for a0 in range(11):
        for a1 in range(11-a0):
            for a2 in range(11-a0-a1):
                for a3 in range(11-a0-a1-a2):
                    a4=10-a0-a1-a2-a3
                    counts=(a0,a1,a2,a3,a4)
                    if max(counts)==10 or (a1+2*a2+3*a3+4*a4)%5:
                        continue
                    raw=[r for r,freq in enumerate(counts) for _ in range(freq)]
                    raw[-1]-=sum(raw)
                    entry(raw)
                    residue_cases+=1
    rng=Random(61060912)
    gcounts={1:0,2:0}
    for desired_g in (1,2):
        for _ in range(60):
            while True:
                raw=[rng.randrange(-(1<<80),1<<80) for _ in range(9)]
                if desired_g==2:
                    raw=[2*x+1 for x in raw]
                raw.append(-sum(raw))
                if gap_gcd(raw)==desired_g:
                    break
            replay=entry(raw)
            x,y=replay.parameters()
            matrix=target_matrix(x,y)
            assert matrix[0]*x+matrix[1]*y==0
            assert matrix[0]*matrix[3]-matrix[1]*matrix[2]==1 and matrix[2]%5==0
            gcounts[desired_g]+=1
    print('six-average n10 complete residue entries and both legal G classes: PASS',residue_cases,gcounts[1],gcounts[2],flush=True)
    records=[]
    for desired_g in (1,2):
        for _ in range(3):
            while True:
                raw=[rng.randrange(-2,3) for _ in range(9)]
                if desired_g==2:
                    raw=[2*x+1 for x in raw]
                raw.append(-sum(raw))
                if gap_gcd(raw)==desired_g:
                    break
            replay=entry(raw)
            x,y=replay.parameters()
            word=compile_integer(target_matrix(x,y),compiler)
            for letter in program.letters(word.node):
                replay.letter(letter)
            replay.finish()
            independent_replay(raw,replay.word,6)
            records.append({'input':raw,'G':desired_g,'steps':len(replay.word),
                            'operations':[[i+1 for i in atom] for atom in replay.word]})
    # Exhibit both excluded G values, with invariant nonzero residue mod5.
    rejected=([1]*9+[-9],[1]*6+[6]*3+[-24])
    assert [gap_gcd(x) for x in rejected]==[10,5]
    for xs in rejected:
        assert sum(xs)==0 and gcd(*xs)==1 and {x%5 for x in xs}=={1}
    Path(__file__).with_name('six_average_ten_witnesses.json').write_text(
        json.dumps({'index_base':1,'seed':61060912,'cases':records,
                    'excluded_examples':[{'input':x,'G':gap_gcd(x)} for x in rejected]},indent=2)+'\n',encoding='utf-8')
    print('six-average n10 literal full paths and excluded classes: PASS',len(records),max(x['steps'] for x in records),2,flush=True)
    print('six-average ten-position full G criterion: PASS',flush=True)


if __name__=='__main__':
    main()
