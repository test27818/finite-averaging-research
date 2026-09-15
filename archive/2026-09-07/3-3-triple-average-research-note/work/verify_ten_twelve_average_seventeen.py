"""Full G criterion at n17 for ten- and twelve-averaging.

Fixed physical templates, exact cycles and root identities; no discovery
generator is imported. All reported words are replayed on original inputs.
"""
from fractions import Fraction as F
from itertools import combinations,product
from math import gcd,lcm
from pathlib import Path
from random import Random
import json

from verify_uniform_endpoint_controller import Program,Element,I,SIGMA
from verify_prime_power_endpoint_completion import Compiler,S,T,mul,inv,bezout
from verify_four_average_nine_complete import integer_word
from verify_composite_arity_transfer import primitive_center,gap_gcd,independent_replay


# First-operation type (number of u, number of v, includes carrier), then
# preserve r copies of its newly averaged value, leave the given singleton
# type, and average the complement. A/B are separately defined one-atom maps.
TEMPLATES={
    10:{'R':(5,4,1,'u'),'P':(7,2,1,'u'),'H':(4,5,1,'u'),
        'S':(8,1,1,'v'),'E':(8,2,0,'u')},
    12:{'R':(9,2,1,'u'),'P':(11,0,1,'u'),'H':(8,3,1,'u'),'S':(10,1,1,'v')}
}
MATRICES={
    10:{'R':tuple(F(x,50) for x in (16,-6,51,-16)),
        'P':tuple(F(x,50) for x in (16,-12,51,-32)),
        'H':tuple(F(x,50) for x in (16,-3,51,-8)),
        'S':tuple(F(x,50) for x in (16,-10,51,-35)),
        'E':tuple(F(x,50) for x in (-35,6,-85,16)),
        'B':tuple(F(x,10) for x in (-7,6,-17,16))},
    12:{'R':tuple(F(x,36) for x in (2,-2,17,-8)),
        'P':tuple(F(x,36) for x in (2,-4,17,-16)),
        'H':tuple(F(x,36) for x in (2,-1,17,-4)),
        'S':tuple(F(x,36) for x in (2,0,17,-9)),
        'A':(F(1),F(-1,3),F(0),F(-1,3))}
}


def rational_to_int(m):
    den=lcm(*(x.denominator for x in m))
    return tuple(int(x*den) for x in m)


class CoreProgram(Program):
    def __init__(self,arity):
        self.arity,self.p,self.q=arity,arity,17
        self.nodes,self.cache=[],{}
        self.one=Element(self.make(('i',),I,0))
        self.one.back=self.one.node
        self.atoms={name:Element(self.make((name,),rational_to_int(matrix),
                                         1 if name in ('A','B') else 2))
                    for name,matrix in MATRICES[arity].items()}

    def seed(self):
        a=self.atoms
        r=a['R']
        order=2 if self.arity==10 else 4
        self.check(self.power(r,order),I)
        self.give_inverse(r,self.power(r,order-1))
        twice=self.mul(self.inv(r),a['P'])
        half=self.mul(self.inv(r),a['H'])
        self.check(twice,(1,0,0,2))
        self.check(half,(1,0,0,F(1,2)))
        self.give_inverse(twice,half)
        self.give_inverse(half,twice)
        self.d2=twice
        self.swap=self.mul(self.inv(r),a['S'])
        self.check(self.swap,SIGMA)
        self.give_inverse(self.swap,self.swap)
        self.uhalf=self.halves(self.d2)
        self.u=self.power(self.uhalf,2)
        self.sign=self.mul(self.swap,self.u)
        self.check(self.sign,(1,0,0,-1))
        if self.arity==10:
            e=a['E']
            self.check(self.power(self.mul(r,e),2),I)
            self.give_inverse(e,self.mul(r,e,r))
            upper=self.mul(self.power(self.d2,3),self.power(self.u,-3),self.power(self.d2,-3))
            self.check(upper,(1,F(-3,8),0,1))
            f=self.mul(upper,e)
            self.check(f,(1,0,F(136,5),F(-128,25)))
            ell=self.mul(self.d2,f,self.inv(self.d2),self.inv(f))
            self.check(ell,(1,0,F(136,5),1))
            self.lower=self.mul(self.power(self.d2,-3),self.power(ell,5),self.power(self.d2,3))
            self.check(self.lower,(1,0,17,1))
            ratio=self.mul(self.sign,self.inv(ell),f)
            self.check(ratio,(1,0,0,F(128,25)))
            square=self.mul(self.inv(ratio),self.power(self.d2,7))
            self.check(square,(1,0,0,25))
            self.dother=self.mul(self.inv(e),a['B'])
            self.check(self.dother,(1,0,0,5))
            self.give_inverse(self.dother,self.mul(self.inv(square),self.dother))
            self.other_prime=5
        else:
            upper=self.mul(self.power(self.d2,2),self.inv(self.u),self.power(self.d2,-2))
            self.check(upper,(1,F(-1,4),0,1))
            f=self.mul(upper,r)
            self.check(f,(1,0,F(-68,9),F(32,9)))
            ell=self.mul(self.d2,f,self.inv(self.d2),self.inv(f))
            self.check(ell,(1,0,F(-68,9),1))
            self.lower=self.mul(self.power(self.d2,-2),self.power(ell,-9),self.power(self.d2,2))
            self.check(self.lower,(1,0,17,1))
            ratio=self.mul(self.inv(ell),f)
            self.check(ratio,(1,0,0,F(32,9)))
            square=self.mul(self.inv(ratio),self.power(self.d2,5))
            self.check(square,(1,0,0,9))
            third=self.mul(self.swap,a['A'])
            self.check(third,(1,0,0,F(1,3)))
            self.dother=self.mul(square,third)
            self.check(self.dother,(1,0,0,3))
            self.give_inverse(self.dother,third)
            self.other_prime=3


class CoreCompiler(Compiler):
    def __init__(self,arity):
        self.program=CoreProgram(arity)
        self.program.seed()
        self.diagonals={}

    def diagonal(self,value):
        value=F(value)
        assert value
        if value in self.diagonals:return self.diagonals[value]
        p=self.program
        result=p.sign if value<0 else p.one
        numerator,denominator=abs(value.numerator),value.denominator
        for prime,element in ((2,p.d2),(p.other_prime,p.dother)):
            exponent=0
            while numerator%prime==0:numerator//=prime;exponent+=1
            while denominator%prime==0:denominator//=prime;exponent-=1
            result=p.mul(result,p.power(element,exponent))
        assert numerator==denominator==1,value
        p.check(result,(1,0,0,value))
        self.diagonals[value]=result
        return result


def representatives(arity):
    prime=5 if arity==10 else 3
    candidates=sorted({sign*2**a*prime**b for a,b in product(range(7),repeat=2)
                       for sign in (1,-1)},key=lambda x:(abs(x),x<0))
    choices={0:0}
    for x in candidates:
        choices.setdefault(x%17,x)
        if len(choices)==17:break
    assert len(choices)==17
    return {**{j:(0,-1,1,j) for j in choices.values()},None:I},choices


def edge(key,generator,reps,choices):
    image=mul(reps[key],generator)
    c,d=image[2:]
    target=choices[d*pow(c,-1,17)%17] if c%17 else None
    loop=mul(image,inv(reps[target]))
    assert loop[0]*loop[3]-loop[1]*loop[2]==1 and loop[2]%17==0
    return target,loop


def compile_integer(matrix,compiler):
    reps,choices=representatives(compiler.program.arity)
    key,result=None,compiler.program.one
    for generator in integer_word(matrix):
        key,loop=edge(key,generator,reps,choices)
        result=compiler.program.mul(result,compiler.gauss(loop))
    assert key is None
    compiler.program.check(result,matrix)
    return result


class Replay:
    def __init__(self,q,u,v):
        self.q,self.r=q,16-q
        self.state=[F(u)]*q+[F(v)]*self.r+[F(-q*u-self.r*v)]
        self.u,self.v,self.w=list(range(q)),list(range(q,16)),16
        self.word=[]

    def average(self,ids):
        assert len(ids)==len(set(ids))==self.q
        assert all(type(i) is int and 0<=i<17 for i in ids)
        m=sum(self.state[i] for i in ids)/self.q
        for i in ids:self.state[i]=m
        self.word.append(ids[:])

    def parameters(self):
        u,v=self.state[self.u[0]],self.state[self.v[0]]
        assert len(self.u)==self.q and len(self.v)==self.r
        assert sorted(self.u+self.v+[self.w])==list(range(17))
        assert all(self.state[i]==u for i in self.u)
        assert all(self.state[i]==v for i in self.v)
        assert self.state[self.w]==-self.q*u-self.r*v
        return u,u-v

    def letter(self,key):
        name,=key
        if name=='A':
            chosen=self.u[:self.q-self.r]+self.v
            remaining=self.u[self.q-self.r:]
            self.average(chosen)
            self.u,self.v=chosen,remaining
        elif name=='B':
            chosen=self.u[:-1]+[self.w]
            singleton=self.u[-1]
            self.average(chosen)
            self.u,self.w=chosen,singleton
        else:
            cu,cv,cw,leave=TEMPLATES[self.q][name]
            first=self.u[:cu]+self.v[:cv]+([self.w] if cw else [])
            old_u=self.u[cu:]
            old_v=self.v[cv:]
            singleton=(old_u if leave=='u' else old_v)[0]
            remaining=first[:self.r]
            self.average(first)
            second=[i for i in range(17) if i not in remaining+[singleton]]
            self.average(second)
            self.u,self.v,self.w=second,remaining,singleton
        self.parameters()

    def finish(self):
        x,y=self.parameters()
        assert x==0
        if y:self.average(self.v+[self.w]+self.u[:self.q-self.r-1])
        assert not any(self.state)


def entry(raw,q):
    xs=primitive_center(raw)
    assert len(xs)==17 and gap_gcd(xs)==1
    i,j=next((i,j) for i,j in combinations(range(17),2) if (xs[i]-xs[j])%17)
    outside=[i,j]+[k for k in range(17) if k not in (i,j)][:15-q]
    first=[k for k in range(17) if k not in outside]
    replay=Replay(q,0,0)
    replay.state=list(map(F,xs))
    replay.average(first)
    a=replay.state[first[0]]
    amod=a.numerator*pow(a.denominator,-1,17)%17
    w=next(k for k in outside if xs[k]%17!=amod)
    second=first[:q-replay.r]+[k for k in outside if k!=w]
    remaining=first[q-replay.r:]
    replay.average(second)
    replay.u,replay.v,replay.w=second,remaining,w
    x,y=replay.parameters()
    assert y.numerator%17 and gap_gcd(replay.state)==1
    return replay


def target_matrix(x,y):
    den=lcm(x.denominator,y.denominator)
    x,y=int(x*den),int(y*den)
    g=gcd(x,y)
    x,y=x//g,y//g
    alpha,beta=bezout(x,y)
    k=-alpha*pow(y,-1,17)%17
    alpha,beta=alpha+k*y,beta-k*x
    assert alpha%17==0
    return y,-x,alpha,beta


def automatic_B_table():
    # Independent small arithmetic enumeration of the old B formula.
    def factor(n):
        result={}
        p=2
        while p*p<=n:
            while n%p==0:result[p]=result.get(p,0)+1;n//=p
            p+=1
        if n>1:result[n]=result.get(n,0)+1
        return result
    result=[]
    for q in range(2,201):
        qf=factor(q)
        s=max(p**((a+1)//2) for p,a in qf.items())
        boundary=q+s
        b=boundary+(not set(factor(boundary))<=set(qf))
        if set(factor(b))<=set(qf):
            result.append([q,b,factor(b)])
    assert [x[:2] for x in result]==[[2,4],[6,9],[10,16],[12,16],[20,25],[30,36],
        [42,49],[54,64],[56,64],[75,81],[90,96],[110,121],[120,125],[132,144],
        [138,162],[156,169],[182,196]]
    return result


def main():
    rng=Random(10121760912)
    automatic=automatic_B_table()
    print('old B automatic-G arities through200: PASS',len(automatic),flush=True)
    records=[]
    for q in (10,12):
        compiler=CoreCompiler(q)
        program=compiler.program
        matrices=MATRICES[q]
        r=matrices['R']
        if q==10:
            assert mul(r,r)==tuple(F(x) for x in (F(-1,50),0,0,F(-1,50)))
            re=mul(r,matrices['E'])
            assert mul(re,re)==(F(1,2500),0,0,F(1,2500))
        else:
            r2=mul(r,r)
            assert mul(r2,r2)==(F(-1,5184),0,0,F(-1,5184))
        leaves=0
        for name,m in matrices.items():
            for u,v in ((1,0),(0,1)):
                replay=Replay(q,u,v)
                replay.letter((name,))
                assert replay.parameters()==(m[0]*u+m[1]*(u-v),m[2]*u+m[3]*(u-v))
                leaves+=1
        reps,choices=representatives(q)
        rows=loops=0
        for c,d in product(range(17),repeat=2):
            if c==d==0:continue
            target=choices[d*pow(c,-1,17)%17] if c else None
            rep=reps[target]
            assert (c*rep[3]-d*rep[2])%17==0
            rows+=1
        for key in reps:
            for generator in (S,T,inv(T)):
                _,loop=edge(key,generator,reps,choices)
                compiler.gauss(loop)
                loops+=1
        for i,(key,_,_) in enumerate(program.nodes):
            assert key[0] in set(matrices)|{'i','m'}
            if key[0]=='m':assert key[1]<i and key[2]<i
        print('arity',q,'n17 physical macros and full Gamma0(17): PASS',leaves,rows,loops,flush=True)
        for _ in range(60):
            while True:
                raw=[rng.randrange(-(1<<72),1<<72) for _ in range(16)]
                raw.append(-sum(raw))
                if gap_gcd(raw)==1:break
            replay=entry(raw,q)
            x,y=replay.parameters()
            h=target_matrix(x,y)
            assert h[0]*x+h[1]*y==0
        print('arity',q,'n17 large-coordinate entry and transport: PASS 60',flush=True)
        accepted=0
        attempts=0
        while accepted<3:
            attempts+=1
            assert attempts<=300
            while True:
                raw=[rng.randrange(-2,3) for _ in range(17)]
                if gap_gcd(raw)==1:break
            replay=entry(raw,q)
            element=compile_integer(target_matrix(*replay.parameters()),compiler)
            if program.nodes[element.node][2]>5000:continue
            for letter in program.letters(element.node):replay.letter(letter)
            replay.finish()
            independent_replay(raw,replay.word,q)
            records.append({'arity':q,'input':raw,'G':1,'steps':len(replay.word),
                            'operations':[[i+1 for i in atom] for atom in replay.word]})
            accepted+=1
        print('arity',q,'n17 literal full paths: PASS',3,max(r['steps'] for r in records if r['arity']==q),flush=True)
    rejected=[1]*16+[-16]
    assert gap_gcd(rejected)==17 and {x%17 for x in rejected}=={1}
    Path(__file__).with_name('ten_twelve_seventeen_witnesses.json').write_text(
        json.dumps({'index_base':1,'seed':10121760912,
                    'sampling':'Random candidate inputs, additionally selected for compiled words under5000 atoms; not performance statistics',
                    'cases':records,'automatic_B_q2_through200':automatic,
                    'excluded_input':rejected},indent=2)+'\n',encoding='utf-8')
    print('ten and twelve averaging seventeen-position G criteria: PASS',flush=True)


if __name__=='__main__':main()
