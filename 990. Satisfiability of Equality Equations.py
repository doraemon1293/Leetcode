class DSU:
    def __init__(self):
        self.parents = {}

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            return x
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)


class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        eqs = DSU()
        not_eqs = []
        for equation in equations:
            a, b = equation[0], equation[3]
            ch = equation[1]
            if ch == "=":
                eqs.union(a, b)
            else:
                not_eqs.append((a, b))
        for a, b in not_eqs:
            if eqs.find(a) == eqs.find(b):
                return False
        return True
