from collections import Counter

from triple_unlabeled_bfs import canonical, successors


def main():
    state = canonical((-3, 0, 1, 1, 1))
    seen = {state}
    frontier = {state}
    for depth in range(15):
        profile = Counter(sum(value == 0 for value in item) for item in frontier)
        support = Counter(sum(value != 0 for value in item) for item in frontier)
        print(f"depth={depth} frontier={len(frontier)} seen={len(seen)} zeros={dict(profile)} support={dict(support)}")
        next_frontier = set()
        for item in frontier:
            for child in successors(item):
                if child not in seen:
                    seen.add(child)
                    next_frontier.add(child)
        frontier = next_frontier


if __name__ == '__main__':
    main()
