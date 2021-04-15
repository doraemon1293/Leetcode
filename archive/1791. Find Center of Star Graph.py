from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {}
        N = len(edges) + 1
        for u, v in edges:
            degree.setdefault(u, 0)
            degree.setdefault(v, 0)
            degree[u] += 1
            degree[v] += 1
        return [k for k in degree if degree[k] == N - 1][0]
