import string
from pprint import pprint


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.root = self
        self.followers = set()  # Node

    @property
    def size(self):
        return len(self.root.followers) + 1

    def follow(self, node):  # node: Node
        if self.is_connected(node):
            return

        if self != self.root:
            self.root.follow(node)

        for follower in self.followers:
            node.root.followers.add(follower)
            follower.root = node.root
        self.followers = set()

        node.root.followers.add(self)
        self.root = node.root

    def __repr__(self):
        return f"Idx: {self.idx} " \
               f"Root: {self.root.idx} ({', '.join([str(i.idx) for i in self.followers]) if self.followers else ''})"


class UnionFind:
    def __init__(self, length: int):
        self.nodes = [Node(i) for i in range(length)]

    def connect(self, idx1: int, idx2: int):
        print()
        print(f"union_find.connect({idx1}, {idx2})")
        if self.nodes[idx1].is_connected(self.nodes[idx2]):
            return

        if self.nodes[idx1].size <= self.nodes[idx2].size:
            self.nodes[idx1].follow(self.nodes[idx2])
        else:
            self.nodes[idx2].root.follow(self.nodes[idx1].root)

        pprint([(idx, val) for idx, val in enumerate(self.nodes)])


class NonCompressedUnionFind:
    def __init__(self, length: int):
        self.parents = [i for i in range(length)]
        print(self.parents)

    def _find(self, i: int) -> int:
        """find for a non-compressed path"""
        return i if self.parents[i] == i else self._find(self.parents[i])

    # Naive implementation of union()
    def connect(self, x: int, y: int):
        """union for a non-compressed path"""
        xset = self._find(x)
        self.parents[xset] = self._find(y)
        print()
        print([i for i in range(len(self.parents))])
        print(self.parents)


def main():
    lowercase_letters = "abcdefghijk" # list(string.ascii_lowercase)
    union_find = UnionFind(len(lowercase_letters))
    # union_find = NonCompressedUnionFind(len(lowercase_letters))
    # union_find.connect(0, 2)
    # union_find.connect(1, 2)
    # union_find.connect(5, 6)
    # union_find.connect(6, 7)
    # union_find.connect(7, 8)
    # union_find.connect(0, 7)

    for i in range(len(lowercase_letters)-1):
        union_find.connect(i, i+1)


if __name__ == '__main__':
    main()
