"""Shallow word survey to conjecture a uniform small-support identity."""
from verify_nonsplit_reynolds_words import tau,shift,compose,power


def support(permutation):
    return tuple(i for i,x in enumerate(permutation) if i!=x)


def search(depth=9):
    primes=(11,17,23,29)
    generators={}
    for p in primes:
        a=tau(p);b=shift(p,1)
        generators[p]={'a':a,'A':power(a,2),'b':b,'B':power(b,p-1)}
    states={p:{tuple(range(p)):''} for p in primes}
    frontier={p:[tuple(range(p))] for p in primes}
    common={''}
    words={'':{p:tuple(range(p)) for p in primes}}
    for level in range(1,depth+1):
        next_words={}
        for word,data in words.items():
            for letter in 'aAbB':
                if word and word[-1].swapcase()==letter:
                    continue
                candidate=word+letter
                result={p:compose(generators[p][letter],data[p]) for p in primes}
                next_words[candidate]=result
                if all(len(support(result[p]))==3 for p in primes):
                    print('common 3-cycle word',candidate,
                          [support(result[p]) for p in primes])
                    return
        print('depth',level,'words',len(next_words))
        words=next_words
    print('No common short word; this is not a group-theoretic exclusion.')


if __name__=='__main__':
    search()
