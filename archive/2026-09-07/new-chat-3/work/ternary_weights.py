from itertools import product


def first_weights(e, max_k=8):
    n = len(e)
    for k in range(max_k + 1):
        total = 3**k
        for prefix in product(range(total + 1), repeat=n - 1):
            used = sum(prefix)
            if used > total:
                continue
            weights = prefix + (total - used,)
            if sum(a * b for a, b in zip(e, weights)) == 0:
                return k, weights
    return None


def main():
    for e in [(-3, 0, 1, 1, 1), (-3, -1, 0, 2, 2), (-2, -1, 1, 2)]:
        print(e, first_weights(e, 5))


if __name__ == '__main__':
    main()
