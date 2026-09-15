from math import gcd


def norm(u, v):
    d = gcd(abs(u), abs(v))
    return u // d, v // d


def solve(u, v):
    u, v = norm(u, v)
    word = []
    while u + v:
        if u == 0 or v == 0:
            return None
        if u % 3 == 0 and v % 3:
            word.append("A")
            u, v = norm(v - u // 3, -u // 3)
        elif v % 3 == 0 and u % 3:
            word.append("B")
            u, v = norm(u - v // 3, -v // 3)
        else:
            return None
    return "".join(word), (u, v)


for pair in [(-23,18), (-97,-48), (-883,783), (3,2), (-4,-1), (1,0)]:
    print(pair, solve(*pair))
