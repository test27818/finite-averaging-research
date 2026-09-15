from math import gcd


def depth(u, v, limit=10000):
    d = 0
    while d < limit:
        if u + v == 0:
            return d
        if u == 0 or v == 0:
            return None
        if u % 3 == 0 and v % 3:
            q = u // 3
            u, v = v - q, -q
        elif v % 3 == 0 and u % 3:
            q = v // 3
            u, v = u - q, -q
        else:
            return None
        d += 1
    return None


for B in (30, 100, 300, 1000):
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
    print(B, "success", count, "max-depth", mx, "arg", arg, flush=True)
