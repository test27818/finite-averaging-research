"""Exact identities and already-certified B59 affine specialization."""
import json
from pathlib import Path
from fractions import Fraction as F
from verify_diagonal_resource_reduction import product,lower
from verify_b53_inverse_closure import inverse


def affine(b,d):
    return (F(1),F(0),F(b),F(d))


def verify():
    count = 0
    for b in (F(-3),F(0),F(7,9)):
        for c in (F(-5,2),F(1),F(0)):
            for d in (F(-1),F(1),F(2,3)):
                for e in (F(-3,7),F(1),F(4)):
                    a,h = affine(b,d),affine(c,e)
                    t = (1-e)*b+(d-1)*c
                    assert product(a,h,inverse(a),inverse(h)) == lower(t)
                    assert product(a,lower(t),inverse(a)) == lower(d*t)
                    if d != 1:
                        assert (t==0) == (c==(1-e)*b/(1-d))
                    count += 1
    path = Path(__file__).with_name("b59_expanded_inverse_closure_certificate.json")
    nodes = json.loads(path.read_text(encoding="utf-8"))["nodes"]
    ms = [tuple(map(F,n["matrix"])) for n in nodes]
    normalize = lambda a: tuple(x/a[0] for x in a)
    a = normalize(product(ms[0],ms[5]))
    h = normalize(product(ms[0],inverse(ms[12])))
    assert a == affine(24,F(16,7))
    assert h == affine(F(-936,19),F(-48,19))
    t = F(59*48,133)
    assert product(a,h,inverse(a),inverse(h)) == lower(t)
    assert t/59 == F(48,133)
    print("affine commutator, conjugation and fixed-point identities: PASS",count)
    print("B59 exact commutator ideal generator: PASS",t)
    print("All-prime physical seed and primitive-ideal existence remain open.")


if __name__ == "__main__":
    verify()
