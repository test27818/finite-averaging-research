"""Seven-averaging n15: a two-prime entry and full dyadic Gamma_0(15).

Reuses the proved all-odd-arity positive seed; no averaging-word discovery.
Four exceptional Schreier loops are handled by exact dyadic Gauss pivots.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import gcd,lcm
from pathlib import Path
from random import Random
import json

from verify_uniform_endpoint_controller import Program, Replay, I
from verify_prime_power_endpoint_completion import S,T,mul,inv,bezout
from verify_four_average_nine_complete import FourCompiler,integer_word
from verify_composite_arity_transfer import primitive_center,gap_gcd,independent_replay


REPS={**{('a',j):(0,-1,1,j) for j in range(-7,8)},
      **{('b',t):(1,0,t,1) for t in (-6,-5,-3,0,3,5,6)},
      ('c',0):(-1,-2,3,5),('d',0):(2,1,5,3)}


def local_label(c,d,p):
    assert gcd(c,d,p)==1
    return (1,d*pow(c,-1,p)%p) if c%p else (0,1)


LABELS={(local_label(r[2],r[3],3),local_label(r[2],r[3],5)):key
        for key,r in REPS.items()}


def label(c,d):
    return LABELS[(local_label(c,d,3),local_label(c,d,5))]


def edge(key,generator):
    candidate=mul(REPS[key],generator)
    following=label(candidate[2],candidate[3])
    loop=mul(candidate,inv(REPS[following]))
    assert loop[0]*loop[3]-loop[1]*loop[2]==1 and loop[2]%15==0
    return following,loop


def dyadic_unit(x):
    x=F(x)
    if not x:
        return False
    a,b=abs(x.numerator),x.denominator
    return a&(a-1)==0 and b&(b-1)==0


class FifteenCompiler(FourCompiler):
    def __init__(self):
        self.program=Program(7)
        self.program.seed()
        self.program.d2=self.program.d(2)
        self.diagonals={}

    def decompose(self,matrix):
        p=self.program
        a,b,c,d=map(F,matrix)
        assert a*d-b*c==1 and c/15==int(c/15)
        if dyadic_unit(a):
            result=self.gauss(matrix)
        elif dyadic_unit(d):
            # U(b/d) diag(1/d,d) L(c/d), projective diagonal Delta(d^2).
            result=p.mul(self.upper(b/d),self.diagonal(d*d),self.lower(c/d))
        else:
            assert matrix in ((-11,4,30,-11),(11,4,30,11)),matrix
            t=F(1,2) if a<0 else F(-1,2)
            adjusted=mul((1,t,0,1),matrix)
            assert abs(adjusted[0])==4
            result=p.mul(self.upper(-t),self.gauss(adjusted))
        p.check(result,matrix)
        assert result.back is not None
        return result


def compile_integer(matrix,compiler):
    assert matrix[2]%15==0
    key,result=('b',0),compiler.program.one
    for generator in integer_word(matrix):
        key,loop=edge(key,generator)
        result=compiler.program.mul(result,compiler.decompose(loop))
    assert key==('b',0)
    compiler.program.check(result,matrix)
    return result


def residue(x,p):
    x=F(x)
    return x.numerator*pow(x.denominator,-1,p)%p


class OriginalReplay(Replay):
    def __init__(self,raw):
        super().__init__(7,0,0)
        self.state=list(map(F,raw))
        self.word=[]

    def average(self,ids):
        assert len(ids)==len(set(ids))==7
        assert all(type(i) is int and 0<=i<15 for i in ids)
        super().average(ids)
        self.word.append(ids[:])


def entry(raw):
    xs=primitive_center(raw)
    assert len(xs)==15 and gap_gcd(xs)==1
    protected=set()
    for p in (3,5):
        i,j=next((i,j) for i,j in combinations(range(15),2) if (xs[i]-xs[j])%p)
        protected.update((i,j))
    block=[i for i in range(15) if i not in protected][:7]
    singles=[i for i in range(15) if i not in block]
    replay=OriginalReplay(xs)
    replay.average(block)
    return finish_entry(replay,block,singles)


def finish_entry(replay,block,singles):
    assert len(block)==7 and len(singles)==8
    a=replay.state[block[0]]
    assert all(replay.state[i]==a for i in block)
    assert gap_gcd(replay.state)==1
    def unit(i):
        return all(residue(replay.state[i]-a,p) for p in (3,5))
    suitable=[i for i in singles if unit(i)]
    repaired=False
    if not suitable:
        i=next(i for i in singles if residue(replay.state[i]-a,3)==0
               and residue(replay.state[i]-a,5)!=0)
        j=next(j for j in singles if residue(replay.state[j]-a,5)==0
               and residue(replay.state[j]-a,3)!=0)
        old=block[-1]
        selected=block[:-1]+[i]
        replay.average(selected)
        block=selected
        singles.remove(i)
        singles.append(old)
        a=replay.state[block[0]]
        assert unit(j)
        suitable=[j]
        repaired=True
    singleton=suitable[0]
    second=[i for i in singles if i!=singleton]
    replay.average(second)
    replay.a,replay.b,replay.w=block,second,singleton
    x,y=replay.parameters()
    assert gcd(y.numerator,15)==1 and gap_gcd(replay.state)==1
    assert len(replay.word)==2+repaired
    return replay,repaired


def target_matrix(x,y):
    den=lcm(x.denominator,y.denominator)
    x,y=int(x*den),int(y*den)
    common=gcd(x,y)
    x,y=x//common,y//common
    assert gcd(y,15)==1
    alpha,beta=bezout(x,y)
    k=-alpha*pow(y,-1,15)%15
    alpha,beta=alpha+k*y,beta-k*x
    assert alpha%15==0
    return y,-x,alpha,beta


def verify_entry_logic():
    # Every ordered complementary local-type pair, with arbitrary local block mean.
    combinations_checked=0
    for a in range(15):
        for first,second in product(range(15),repeat=2):
            if first%3 or first%5==0 or second%5 or second%3==0:
                continue
            # First difference is 0 only at3; second is0 only at5.
            updated=(second-first*pow(7,-1,15))%15
            assert gcd(updated,15)==1
            for extra in range(15):
                aa=((6*a+(a+first))*pow(7,-1,15))%15
                selected_singleton=a
                assert (7*aa+selected_singleton-(7*a+a+first))%15==0
                assert (a+second-aa)%15==updated
                # The untouched coordinate may have any residue: block-singleton
                # exchange preserves simultaneous constancy at each prime.
                for p in (3,5):
                    old_constant=len({a%p,(a+first)%p,extra%p})==1
                    new_constant=len({aa%p,selected_singleton%p,extra%p})==1
                    assert old_constant==new_constant
                combinations_checked+=1
    return combinations_checked


def main():
    assert len(REPS)==len(LABELS)==24
    compiler=FifteenCompiler()
    program=compiler.program
    rows=loops=ordinary=lowerpivot=shifted=0
    for c,d in product(range(15),repeat=2):
        if gcd(c,d,15)==1:
            representative=REPS[label(c,d)]
            assert (c*representative[3]-d*representative[2])%15==0
            rows+=1
    exceptions=[]
    for key in REPS:
        for generator in (S,T,inv(T)):
            following,loop=edge(key,generator)
            if dyadic_unit(loop[0]):
                ordinary+=1
            elif dyadic_unit(loop[3]):
                lowerpivot+=1
            else:
                shifted+=1
                exceptions.append(loop)
            compiler.decompose(loop)
            loops+=1
    assert ordinary==62 and lowerpivot==8 and shifted==2
    assert set(exceptions)=={(-11,4,30,-11),(11,4,30,11)}
    leaves=0
    for i,(key,_,_) in enumerate(program.nodes):
        if key[0]=='m':
            assert key[1]<i and key[2]<i
        elif key[0] in ('t','f'):
            for a,b in ((1,0),(0,1)):
                replay=Replay(7,a,b)
                replay.letter(key)
                x,y=replay.parameters()
                if key[0]=='t':
                    j=key[1]
                    assert (x,y)==(F(-8*a+j*(a-b),7),F(-15*a+2*j*(a-b),7))
                else:
                    r=key[1]
                    assert (x,y)==(a+F(r-7,14)*(a-b),F(r,7)*(a-b))
                leaves+=1
    print('seven-average n15 complete CRT cosets and positive pivots: PASS',rows,loops,ordinary,lowerpivot,shifted,leaves,flush=True)
    local=verify_entry_logic()
    rng=Random(71560912)
    samples=repairs=0
    for _ in range(160):
        while True:
            raw=[rng.randrange(-(1<<96),1<<96) for _ in range(15)]
            if gap_gcd(raw)==1:
                break
        replay,repaired=entry(raw)
        repairs+=repaired
        x,y=replay.parameters()
        matrix=target_matrix(x,y)
        assert matrix[0]*x+matrix[1]*y==0
        assert matrix[0]*matrix[3]-matrix[1]*matrix[2]==1
        samples+=1
    forced_cases=[]
    for a in range(-4,5):
        for e,f in product((3,6,9,12),(5,10)):
            e+=15*rng.randrange(-1000,1001)
            f+=15*rng.randrange(-1000,1001)
            diffs=[e,-e,f,-f,0,0,0,-15*a]
            raw=[a]*7+[a+t for t in diffs]
            assert sum(raw)==0 and gap_gcd(raw)==1
            replay=OriginalReplay(raw)
            replay.average(list(range(7)))
            replay,repaired=finish_entry(replay,list(range(7)),list(range(7,15)))
            assert repaired and len(replay.word)==3
            result=independent_replay(raw,replay.word,7,require_consensus=False)
            assert result==replay.state and gap_gcd(result)==1
            forced_cases.append(raw)
    print('seven-average n15 two-prime entry logic and large inputs: PASS',local,samples,len(forced_cases),flush=True)
    records=[]
    # Include the general integer-freeze family Z7 and several independent draws.
    targets=[[1]*12+[-5,-4,-3]]
    for _ in range(5):
        while True:
            raw=[rng.randrange(-2,3) for _ in range(14)]
            raw.append(-sum(raw))
            if gap_gcd(raw)==1:
                break
        targets.append(raw)
    for raw in targets:
        replay,repaired=entry(raw)
        x,y=replay.parameters()
        result=compile_integer(target_matrix(x,y),compiler)
        # The expression DAG proves all-word existence; these small cases also
        # expand the actual original-position atoms and are separately replayed.
        for letter in program.letters(result.node):
            replay.letter(letter)
        assert replay.parameters()[0]==0
        replay.finish()
        independent_replay(raw,replay.word,7)
        records.append({'input':raw,'G':1,'entry_steps':2+repaired,'steps':len(replay.word),
                        'operations':[[i+1 for i in atom] for atom in replay.word]})
    raw=[0]*7+[3,-3,5,-5,0,0,0,0]
    replay=OriginalReplay(raw)
    replay.average(list(range(7)))
    replay,repaired=finish_entry(replay,list(range(7)),list(range(7,15)))
    assert repaired
    result=compile_integer(target_matrix(*replay.parameters()),compiler)
    for letter in program.letters(result.node):
        replay.letter(letter)
    replay.finish()
    independent_replay(raw,replay.word,7)
    records.append({'input':raw,'G':1,'entry_steps':3,'steps':len(replay.word),
                    'operations':[[i+1 for i in atom] for atom in replay.word]})
    excluded=([1]*14+[-14],[1]*13+[4,-17],[1]*13+[6,-19])
    assert sorted(gap_gcd(raw) for raw in excluded)==[3,5,15]
    Path(__file__).with_name('seven_average_fifteen_witnesses.json').write_text(
        json.dumps({'index_base':1,'seed':71560912,'cases':records,
                    'forced_entry_inputs':forced_cases,
                    'excluded_examples':[{'input':raw,'G':gap_gcd(raw)} for raw in excluded]},indent=2)+'\n',encoding='utf-8')
    print('seven-average n15 literal full paths and excluded G: PASS',len(records),max(x['steps'] for x in records),3,flush=True)
    print('seven-average fifteen-position full G criterion: PASS',flush=True)


if __name__=='__main__':
    main()
