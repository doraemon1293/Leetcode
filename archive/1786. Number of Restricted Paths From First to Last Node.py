from typing import List
import heapq
import functools
import bisect


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        shortest = [float("inf")] * n
        edges_dict = {}
        for u, v, w in edges:
            edges_dict.setdefault(u - 1, [])
            edges_dict.setdefault(v - 1, [])
            edges_dict[u - 1].append((w, v - 1))
            edges_dict[v - 1].append((w, u - 1))
        h = [(0, n - 1)]
        while h:
            dis, node = heapq.heappop(h)
            if dis < shortest[node]:
                shortest[node] = dis
                for w, node1 in edges_dict[node]:
                    heapq.heappush(h, (dis + w, node1))

        @functools.lru_cache(None)
        def foo(node):
            if node == n - 1:
                return 1
            res = 0
            for w, node1 in edges_dict[node]:
                if shortest[node1] < shortest[node]:
                    res += foo(node1)
                    res %= MOD
            return res

        return foo(0)


print(Solution().countRestrictedPaths(n=5, edges=[[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1],
                                                  [5, 4, 10]]))
