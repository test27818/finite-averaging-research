from math import gcd


def depth(u, v):
    seen = set()
    d = 0
    while True:
        if u + v == 0:
            return d
        key = (u, v)
        if key in seen:
            return None
        seen.add(key)
        if u % 3 == 0 and u != 0 and v % 3:
            u, v = v - u // 3, -u // 3
        elif v % 3 == 0 and v != 0 and u % 3:
            u, v = u - v // 3, -v // 3
        else:
            return None
        d += 1


for B in (30, 100, 300, 1000, 3000):
    mx = 0
    arg = None
    count = 0
    for u in range(-B, B + 1):
        for v in range(-B, B + 1):
            if not u and not v or gcd(u, v) != 1:
                continue
            z = depth(u, v)
            if z is not None:
                count += 1
                if z > mx:
                    mx, arg = z, (u, v)
    print(B, "success", count, "max-depth", mx, "arg", arg)
