from triple_unlabeled_bfs import canonical, successors


def main():
    frontier = {canonical((-3, 0, 1, 1, 1))}
    seen = set(frontier)
    for depth in range(5):
        print("DEPTH", depth, "COUNT", len(frontier))
        for state in sorted(frontier)[:20]:
            triples = [triple for triple in __import__('itertools').combinations(range(5), 3) if sum(state[i] for i in triple) == 0]
            print(state, "zero_triples", triples)
        next_frontier = set()
        for state in frontier:
            for child in successors(state):
                if child not in seen:
                    seen.add(child)
                    next_frontier.add(child)
        frontier = next_frontier


if __name__ == '__main__':
    main()
