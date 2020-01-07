import heapq


class Solution:
    def maximumMinimumPath(self, A: list) -> int:
        R, C = len(A), len(A[0])
        heap = [(-A[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        while heap:
            v, x, y = heapq.heappop(heap)
            if (x, y) == (R - 1, C - 1):
                return -v
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < R and 0 <= y1 < C and (x1, y1) not in visited:
                    heapq.heappush(heap, (max(v, -A[x1][y1]),x1,y1))
                    visited.add((x1, y1))
        return -1
