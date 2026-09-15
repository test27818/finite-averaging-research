"""Exact finite subgroup folding inside PSL(2,Z) = C2 * C3."""

from explore_thirteen_group import (A, R, IDENTITY, determinant, inverse,
                                    multiply, primitive)

B = (1, 3, 0, -9)
S = (0, -1, 1, 0)
U = (0, -1, 1, 1)


def modular_word(matrix):
    assert determinant(matrix) == 1
    a, b, c, d = matrix
    output = []

    def translation(power):
        output.extend("su" * power if power >= 0 else "Us" * -power)

    while c:
        q = a // c
        translation(q)
        output.append("s")
        a, b, c, d = -c, -d, a - q * c, b - q * d
    assert a == d and abs(a) == 1
    translation(b // d)
    word = "".join(output)
    check = IDENTITY
    for letter in word:
        check = multiply(check, {"s": S, "u": U, "U": inverse(U)}[letter])
    assert check == primitive(matrix)
    return word


class Fold:
    def __init__(self):
        self.parent = []
        self.edges = []
        self.new()

    def new(self):
        value = len(self.parent)
        self.parent.append(value)
        return value

    def root(self, value):
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def merge(self, left, right):
        left, right = self.root(left), self.root(right)
        if left == right:
            return False
        self.parent[max(left, right)] = min(left, right)
        return True

    def edge(self, start, letter, end):
        if letter == "U":
            start, end = end, start
            letter = "u"
        self.edges.append((start, letter, end))
        if letter == "s":
            self.edges.append((end, letter, start))

    def loop(self, word):
        position = 0
        for offset, letter in enumerate(word):
            following = 0 if offset == len(word) - 1 else self.new()
            self.edge(position, letter, following)
            position = following

    def contains(self, word, table):
        backward = {(end, letter): start for (start, letter), end in table.items()}
        position = self.root(0)
        for letter in word:
            if letter == "U":
                position = backward.get((position, "u"))
            else:
                position = table.get((position, letter))
            if position is None:
                return False
        return position == self.root(0)

    def close(self):
        while True:
            changed = False
            table = {}
            back = {}
            for start, letter, end in self.edges:
                start, end = self.root(start), self.root(end)
                key = (start, letter)
                if key in table:
                    changed |= self.merge(end, table[key])
                else:
                    table[key] = end
                key = (end, letter)
                if key in back:
                    changed |= self.merge(start, back[key])
                else:
                    back[key] = start
            if changed:
                continue
            additions = []
            for (start, letter), middle in table.items():
                if letter == "u" and (middle, "u") in table:
                    end = table[middle, "u"]
                    if (end, "u") in table:
                        changed |= self.merge(start, table[end, "u"])
                    else:
                        additions.append((end, "u", start))
            if additions:
                self.edges.extend(additions)
                changed = True
            if not changed:
                return table


def generators(depth):
    basic = {"A": A, "R": R, "B": B,
             "a": inverse(A), "r": inverse(R), "b": inverse(B)}
    seen = {IDENTITY: ""}
    frontier = [IDENTITY]
    integral = {}
    for _ in range(depth):
        following = []
        for matrix in frontier:
            for letter, generator in basic.items():
                result = multiply(generator, matrix)
                if result in seen:
                    continue
                word = seen[matrix] + letter
                seen[result] = word
                following.append(result)
                if determinant(result) == 1:
                    integral[result] = word
        frontier = following
    return integral


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=6)
    arguments = parser.parse_args()
    fold = Fold()
    integral = generators(arguments.depth)
    retained = []
    previous = None
    table = fold.close()
    for matrix, word in integral.items():
        word_modular = modular_word(matrix)
        if fold.contains(word_modular, table):
            continue
        fold.loop(word_modular)
        table = fold.close()
        nodes = {fold.root(value) for value in range(len(fold.parent))}
        incomplete = sum((node, letter) not in table
                         for node in nodes for letter in "su")
        signature = (len(nodes), incomplete)
        if signature != previous:
            retained.append((word, matrix, signature))
        previous = signature
        if incomplete == 0:
            print("COMPLETE index", len(nodes), "last", word, flush=True)
            break
    print("integral matrices", len(integral), "final", previous)
    print("progress", retained)


if __name__ == "__main__":
    main()
