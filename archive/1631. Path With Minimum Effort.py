from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        min_eff = {(0, 0): 0}
        M, N = len(heights), len(heights[0])
        while heap:
            eff, x, y = heapq.heappop(heap)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xt, yt = x + dx, y + dy
                if 0 <= xt < M and 0 <= yt < N:
                    eff_t = max(eff, abs(heights[xt][yt] - heights[x][y]))
                    if eff_t < min_eff.get((xt, yt), float("inf")):
                        min_eff[xt, yt] = eff_t
                        heapq.heappush(heap, (eff_t, xt, yt))
        print(min_eff)
        return min_eff[M - 1, N - 1]

heights=[[1,10,6,7,9,10,4,9]]
print(Solution().minimumEffortPath(heights))
