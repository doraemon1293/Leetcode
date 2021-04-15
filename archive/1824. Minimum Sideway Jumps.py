from typing import List
from collections import deque


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        N = len(obstacles)
        dp = {(-1, 2): 0}
        for point in range(0, N):
            min_cost, min_lane = min([(dp[point - 1, lane], lane) for lane in range(1, 4) if
                                      (point - 1, lane) in dp and obstacles[point] != lane])
            dp[point, min_lane] = min_cost
            for lane in range(1, 4):
                if lane != obstacles[point]:
                    if (point, lane) not in dp:
                        dp[point, lane] = min(dp.get((point - 1, lane), float("inf")), min_cost + 1)
        return min(dp[N - 1, lane] for lane in range(1, 4) if (N - 1, lane) in dp)




