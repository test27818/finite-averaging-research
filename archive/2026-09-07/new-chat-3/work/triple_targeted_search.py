from time import perf_counter

from triple_unlabeled_bfs import search


def main():
    for state in [(-3, 0, 1, 1, 1), (-3, -1, 0, 2, 2)]:
        started = perf_counter()
        result = search(state, max_depth=30, max_states=5_000_000)
        print(state, result, "seconds", perf_counter() - started, flush=True)


if __name__ == "__main__":
    main()
