import collections


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        memo = {}
        for x, y in edges:
            d[x].add(y)
            d[y].add(x)
        self.ans = 0

        def dfs(n, pre):
            temp = sorted([dfs(i, n) for i in d[n] if i != pre], reverse=True)
            diameter = sum([x + 1 for x in temp[:2]])
            self.ans = max(self.ans, diameter)
            return temp[0] + 1 if temp else 0

        dfs(0, None)
        return self.ans
