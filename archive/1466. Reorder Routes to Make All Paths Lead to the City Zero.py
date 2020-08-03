from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(list)
        for a, b in connections:
            d[a].append(b)
            d[b].append(-a)
        self.ans = 0
        visited = set()

        def dfs(root):
            for node in d[root]:
                if abs(node) not in visited:
                    if node > 0:
                        self.ans += 1
                    visited.add(abs(node))
                    dfs(abs(node))

        dfs(0)
        return self.ans


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(Solution().minReorder(n, connections))
