"""Shared first-row buckets avoid a growing projective word ball."""
import json
import argparse
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from verify_diagonal_resource_reduction import product


def inverse(m):
    a,b,c,d = m
    det = a*d-b*c
    return (d/det,-b/det,-c/det,a/det)


def search(certificate="b53_inverse_closure_certificate.json"):
    data = json.loads(Path(__file__).with_name(certificate)
                      .read_text(encoding="utf-8"))
    buckets = defaultdict(list)
    for i,node in enumerate(data["nodes"]):
        m = tuple(map(F,node["matrix"]))
        for sign,mat in ((1,m),(-1,inverse(m))):
            a,b = mat[:2]
            key = (F(1),b/a) if a else (F(0),F(1))
            buckets[key].append((i,sign,mat))
    affines = {}
    for entries in buckets.values():
        for i,si,m in entries:
            for j,sj,n in entries:
                z = product(m,inverse(n))
                z = tuple(x/z[0] for x in z)
                assert z[:2] == (1,0)
                affines.setdefault(z,((j,-sj),(i,si)))
    by_slope = defaultdict(list)
    for m,word in affines.items():
        by_slope[m[3]].append((m,word))
    print("row buckets",len(buckets),"affines",len(affines))
    for slope,entries in by_slope.items():
        for m,word in entries:
            for n,other in entries:
                if m[2] == n[2]:
                    continue
                root = product(m,inverse(n))
                assert root == (1,0,m[2]-n[2],1)
                print("root",root,"words",word,other,"slope",slope)
                return
    print("No matching slopes; this is only a bounded candidate family.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate",default="b53_inverse_closure_certificate.json")
    search(parser.parse_args().certificate)
