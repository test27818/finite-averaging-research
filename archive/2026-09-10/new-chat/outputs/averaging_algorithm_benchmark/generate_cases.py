"""Generate fresh structured integer-frozen test inputs. Standard library only."""
import argparse
from math import gcd
from pathlib import Path
from random import Random
import json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p', type=int, default=7)
    parser.add_argument('--count', type=int, default=100)
    parser.add_argument('--bits', type=int, default=64, help='signed lift bound is 2**bits')
    parser.add_argument('--seed', type=int, default=2026091218)
    parser.add_argument('--output', type=Path, default=Path('fresh_cases.json'))
    args = parser.parse_args()
    p = args.p
    if p < 5 or any(p % d == 0 for d in range(2, int(p**0.5)+1)):
        parser.error('p must be prime and at least 5')
    if args.count < 1 or args.bits < 1:
        parser.error('count and bits must be positive')
    rng, cases, seen = Random(args.seed), [], set()
    bound = 1 << args.bits
    while len(cases) < args.count:
        length = rng.randrange(3, min(p-1, 6)+1)
        cuts = sorted(rng.sample(range(1, p-1), length-1))
        residues = [b-a for a, b in zip([0]+cuts, cuts+[p-1])]
        lifts = [rng.randint(-bound, bound) for _ in range(length-1)]
        lifts.append(-3-sum(lifts))
        light = [1+r+p*z for r, z in zip(residues, lifts)]
        if gcd(*(x-1 for x in light)) != 1:
            continue
        values = [1]*(2*p+1-length)+light
        key = tuple(sorted(values))
        if key in seen:
            continue
        seen.add(key)
        assert sum(values) == 0 and sum(residues) == p-1
        cases.append({'id': 'fresh-p%d-%04d' % (p, len(cases)+1),
                      'p': p, 'n': 2*p+1, 'input': list(map(str, values))})
    data = {'schema_version': 1, 'index_base': 1, 'coordinate_encoding': 'exact integer strings',
            'generator': {'p': p, 'count': args.count, 'bits': args.bits, 'seed': args.seed},
            'scope': 'Integer-frozen G=1 inputs; this generator supplies no solution proof.',
            'cases': cases}
    args.output.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print('generated', len(cases), 'cases at', args.output)


if __name__ == '__main__':
    main()
