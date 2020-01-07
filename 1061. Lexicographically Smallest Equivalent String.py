class Union_find:
    def __init__(self):
        self.parent = {}

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        px, py = min(px, py), max(px, py)
        self.parent[py] = px

    def find(self, x):
        path = []
        self.parent.setdefault(x, x)
        temp = x
        while temp != self.parent[temp]:
            path.append(temp)
            temp = self.parent[temp]
        root = temp
        for temp in path:
            self.parent[temp] = root
        return root


class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        uf = Union_find()
        for a, b in zip(A, B):
            uf.union(a, b)
        return "".join([uf.find(ch) for ch in S])
