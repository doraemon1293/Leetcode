class DSU:
    def __init__(self):
        self.weights = {}
        self.parents = {}

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.weights[x] = 1
            return x
        else:
            path = [x]
            while self.parents[path[-1]] != path[-1]:
                path.append(self.parents[path[-1]])
            root = path[-1]
            for node in path:
                self.parents[node] = root
            return root

    def union(self, x, y):
        roots = [self.find(x), self.find(y)]
        heaviest = float("-inf")
        for root in roots:
            if self.weights[root] > heaviest:
                heaviest = self.weights[root]
                heaviest_root = root

        for root in roots:
            if root != heaviest_root:
                self.weights[heaviest_root] += self.weights[root]
                self.parents[root] = heaviest_root


class Solution(object):
    def removeStones(self, stones):
        dsu = DSU()
        for x, y in stones:
            dsu.union((x, None), (None, y))
        return len(stones) - len({dsu.find((x, None)) for x, y in stones})


print(Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
