"""Scan existing B_p return libraries for a second q=3 Hecke reflection.

The projective condition for eigenvalue ratio -3 is
3 trace(M)^2 + 4 det(M) = 0.  It is checked directly on primitive integer
matrices.  Independent prime libraries are compiled in separate processes.
"""

from concurrent.futures import ProcessPoolExecutor
import os

from compile_bn_integer_templates import compile_returns


CASES = (
    (17, False, False, False),
    (19, True, False, False),
    (23, True, False, False),
    (29, True, False, False),
    (41, True, True, True),
    (47, True, True, True),
    (53, True, True, True),
    (59, True, True, True),
)


def hecke_reflection(matrix):
    a, b, c, d = matrix
    return 3 * (a + d) ** 2 + 4 * (a * d - b * c) == 0


def inspect(case):
    prime, include_six, current_library, expanded_first = case
    rows, _ = compile_returns(prime, include_six, current_library,
                              expanded_first)
    hits = tuple(matrix for matrix in rows if hecke_reflection(matrix))
    return prime, len(rows), hits


def main():
    workers = min(os.cpu_count() or 1, len(CASES))
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = sorted(executor.map(inspect, CASES))
    for result in results:
        print("B_p Hecke reflection inventory", result, flush=True)
    print("existing return-library Hecke reflection scan: PASS",
          sum(size for _, size, _ in results),
          sum(len(hits) for _, _, hits in results), flush=True)


if __name__ == "__main__":
    main()
