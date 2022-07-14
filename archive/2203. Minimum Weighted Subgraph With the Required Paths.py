import collections
from typing import List
import heapq


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        G1 = collections.defaultdict(dict)
        G2 = collections.defaultdict(dict)  # G2 reverted Graph
        for a, b, w in edges:
            G1.setdefault(a, {})
            G2.setdefault(b, {})
            G1[a][b] = w
            G2[b][a] = w

        def dijkstra(g, source):
            q = [(0, source)]
            costs = {}
            while q:
                cost, node = heapq.heappop(q)
                if node not in costs:
                    costs[node] = cost
                    for node1 in g[node]:
                        heapq.heappush(q, (g[node][node1] + cost, node1))
            return costs

        costs_s1 = dijkstra(G1, src1)
        costs_s2 = dijkstra(G1, src2)
        costs_dest_reverted = dijkstra(G2, dest)
        ans = float("inf")
        for i in range(n):
            ans = min(ans, costs_s1.get(i, float("inf")) + costs_s2.get(i, float("inf")) + \
                      costs_dest_reverted.get(i,float("inf")))
        return -1 if ans==float("inf") else ans
