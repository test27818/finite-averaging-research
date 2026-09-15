"""Look for finite-field obstructions beyond the uniform-residue obstruction."""

from itertools import product

from triple_modp_orbit import orbit_to_zero


def main():
    n = 5
    for p in (2, 5, 7, 11):
        bad = []
        total = p ** (n - 1)
        for prefix in product(range(p), repeat=n - 1):
            state = prefix + ((-sum(prefix)) % p,)
            if len(set(state)) == 1:
                continue
            reachable, _ = orbit_to_zero(state, p)
            if not reachable:
                bad.append(state)
                if len(bad) == 10:
                    break
        print(f"p={p} scanned_at_most={total} nonconstant_bad={bad}", flush=True)


if __name__ == "__main__":
    main()
