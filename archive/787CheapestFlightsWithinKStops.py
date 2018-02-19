# coding=utf-8


class Solution:

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        import heapq
        edges = {}
        for s, d, cost in flights:
            edges.setdefault(s, [])
            edges[s].append((cost, d))
        q = [(0, src, -1)]  # (cost,vertex,stops)
        visited = set()
        while q:
            cost, v1, stops = heapq.heappop(q)
            if v1 not in visited:
                visited.add(v1)
                if v1 == dst:
                    return cost
                for c, v2 in edges.get(v1, ()):
                    if v2 not in visited:
                        if stops + 1 <= K:
                            heapq.heappush(q, (cost + c, v2, stops + 1))

        return -1


n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 0
print(Solution().findCheapestPrice(n, flights, src, dst, K))
