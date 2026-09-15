"""Bounded exact projective search; absence is not group nonmembership."""
from compile_bn_integer_templates import primitive_matrix
from explore_b17_integral_return_cover import mul


def search(depth=9):
    a = (-26,-1,433,17)
    b = (-229,-14,3816,234)
    generators = dict(A=a,B=b,a=(a[3],-a[1],-a[2],a[0]),
                      b=(b[3],-b[1],-b[2],b[0]))
    identity = primitive_matrix((1,0,0,1))
    seen = {identity: ""}
    frontier = [identity]
    for level in range(1,depth+1):
        following = []
        for matrix in frontier:
            for letter,g in generators.items():
                word = seen[matrix]+letter
                if len(word)>1 and word[-2] == letter.swapcase():
                    continue
                result = primitive_matrix(mul(g,matrix))
                if result in seen:
                    continue
                seen[result] = word
                following.append(result)
                x,y,z,w = result
                if (x+w)**2 == 4*(x*w-y*z):
                    print("exact parabolic",word,result)
                    return word,result
        print("depth",level,"new",len(following),"total",len(seen),flush=True)
        frontier = following
    print("No parabolic in the stated finite ball; no infinite-group claim.")


if __name__ == "__main__":
    search()
