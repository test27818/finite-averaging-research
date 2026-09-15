"""Exact bounded three-factor screening; no expanding group-word ball."""
from time import perf_counter
from compile_bn_integer_templates import compile_returns
from explore_b17_integral_return_cover import mul
from verify_twenty_five_arithmetic_group import finite_order
from verify_bn_integer_templates import replay


def search():
    start = perf_counter()
    rows,_ = compile_returns(59,True,True,True)
    keys = sorted(rows)
    dets = [a*d-b*c for a,b,c,d in keys]
    hits = []
    checked = 0
    for i,a in enumerate(keys):
        for j,b in enumerate(keys):
            pair = mul(b,a)
            x,y,z,w = pair
            pairdet = dets[i]*dets[j]
            # Trace is cyclic, so require the first index to be minimal.
            for k in range(i,len(keys)):
                if j < i:
                    continue
                c = keys[k]
                trace = c[0]*x+c[1]*z+c[2]*y+c[3]*w
                det = pairdet*dets[k]
                checked += 1
                if trace != 0 and (det <= 0 or trace*trace not in
                                                   (det,2*det,3*det,4*det)):
                    continue
                order = finite_order(mul(c,pair))
                if order:
                    hits.append((a,b,c,order))
    for m in {m for hit in hits for m in hit[:3]}:
        replay(59,rows[m])
    print("templates",len(keys),"cyclic-screen comparisons",checked,
          "cycles",len(hits),"seconds",round(perf_counter()-start,3))
    for hit in hits[:8]:
        print(hit)
    print("Absence only concerns this finite template grammar and word length.")


if __name__ == "__main__":
    search()
