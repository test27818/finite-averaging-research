"""Polynomial decision of the first outside interaction, not full averaging.

A state (a,b,c,d) denotes (a repeated five times,b,c,d), with d the
distinguished outside position. All local prefixes and the final outside
operation must be integral, nonidentity, and have primitive G=1 (or be zero).
The entry domain is a zero-sum core with primitive G=1 and nonzero d. An
interaction means selecting d in a nonidentity operation, not necessarily
changing d's own value immediately. A negative answer certifies full
nonreachability; a positive answer does not imply full consensus.
"""
from collections import Counter
from functools import lru_cache
from math import gcd

LOCAL=('S1','S2','D')
EXTERNAL=('E0','E1','E2','E12')


def primitive(state):
    g=gcd(*state)
    return tuple(x//g for x in state) if g else (0,0,0,0)


def good_g(state):
    a,b,c,d=primitive(state)
    return not any((a,b,c,d)) or gcd(b-a,c-a,d-a)==1


def valuation(x):
    assert x
    e=0
    while x%5==0:x//=5;e+=1
    return e


def depth(state):
    a,b,c,d=state
    g=gcd(b-a,c-a)
    return None if g==0 else valuation(g)


def step(state,letter):
    a,b,c,d=state
    if letter=='S1':selected=(a,a,a,a,b);rest=(a,c,d)
    elif letter=='S2':selected=(a,a,a,a,c);rest=(b,a,d)
    elif letter=='D':selected=(a,a,a,b,c);rest=(a,a,d)
    elif letter=='E0':selected=(a,a,a,a,d);rest=(a,b,c)
    elif letter=='E1':selected=(a,a,a,b,d);rest=(a,a,c)
    elif letter=='E2':selected=(a,a,a,c,d);rest=(a,a,b)
    elif letter=='E12':selected=(a,a,b,c,d);rest=(a,a,a)
    else:raise ValueError(letter)
    if len(set(selected))==1 or sum(selected)%5:return None
    result=primitive((sum(selected)//5,)+rest)
    assert 5*result[0]+sum(result[1:])==0
    return result if good_g(result) else None


def follow(state,word):
    for letter in word:
        state=step(state,letter)
        if state is None:return None
    return state


def deep_escape(state):
    """Construct a safe nonidentity outside singleton after a deep local run."""
    source=state=primitive(state);prefix=[]
    a,b,c,d=state
    e=depth(state)
    assert good_g(state) and d%5 and e is not None
    if b!=c:
        assert e>=8
        u,v=b-a,c-a
        first=('D',) if (u+v)%2 else ('S1','D')
        for letter in first:
            state=step(state,letter)
            assert state is not None
        prefix.extend(first)
    a,b,c,d=state
    assert b==c
    u=b-a;L=valuation(u);q=u//5**L
    assert L>=6 and u%2 and a%5
    beta=(-3*a*pow(q,-1,5))%5
    sign=1 if L%2 else -1
    s=next(s for s in range(4) if sign*pow(2,s,5)%5==beta)
    word=('S1','D')*s+('S1',)*(L-2*s)
    for letter in word:
        state=step(state,letter)
        assert state is not None
    # If the tail length is odd, common and outside have different parity.
    # If even, they differ modulo 4. Thus this outside move is not an identity.
    assert state[0]!=state[3]
    end=step(state,'E0')
    assert end is not None
    answer=tuple(prefix)+word+('E0',)
    assert follow(source,answer)==end
    return answer


class FirstEscape:
    def __init__(self):
        self.stats=Counter()
        self.search=lru_cache(None)(self._search)

    def _search(self,state):
        prefix=[];state=primitive(state)
        while True:
            self.stats['visited_nodes']+=1
            assert good_g(state) and state[3]
            for letter in EXTERNAL:
                if step(state,letter) is not None:
                    self.stats['direct_outside_exits']+=1
                    return tuple(prefix)+(letter,)
            e=depth(state)
            if e is None:
                return None # a nonzero two-value trap cannot be G=1
            if e:assert state[3]%5
            if e>=8 or (state[1]==state[2] and e>=6):
                self.stats['deep_constructions']+=1
                return tuple(prefix)+deep_escape(state)
            lower=[];continuation=[]
            for letter in LOCAL:
                child=step(state,letter)
                if child is None:continue
                f=depth(child)
                assert f is not None
                if f<e:lower.append((letter,child))
                else:continuation.append((letter,child))
            assert len(continuation)<=1
            # Each lower child is in the cone where every further local
            # operation lowers depth by exactly one. Here e<=7, so its full
            # local tree has constant depth, independently of input height.
            for letter,child in lower:
                suffix=self.search(child)
                if suffix is not None:return tuple(prefix)+(letter,)+suffix
            if not continuation:return None
            letter,state=continuation[0]
            prefix.append(letter);self.stats['spine_steps']+=1

    def decide(self,state):
        state=primitive(tuple(state))
        a,b,c,d=state
        if 5*a+b+c+d:raise ValueError('a zero-sum weighted core is required')
        if not d:raise ValueError('the distinguished outside value must be nonzero')
        if not good_g(state):return {'possible':False,'word':None,'stats':dict(self.stats)}
        word=self.search(state)
        return {'possible':word is not None,'word':word,'stats':dict(self.stats)}
