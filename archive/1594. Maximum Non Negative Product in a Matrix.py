from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = {}
        if grid[0][0] > 0:
            dp[0, 0] = [0, grid[0][0]]
            dp[0, 0] = [grid[0][0], 0]
        M, N = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7
        for i in range(M):
            for j in range(N):
                if i == j == 0:
                    dp[i, j] = (grid[i][j], grid[i][j])
                else:
                    max1, min1 = dp[i - 1, j] if i - 1 >= 0 else (-float("inf"), float("inf"))
                    max2, min2 = dp[i, j - 1] if j - 1 >= 0 else (-float("inf"), float("inf"))
                    max_ = max(max(max1, max2) * grid[i][j], min(min1, min2) * grid[i][j])
                    min_ = min(max(max1, max2) * grid[i][j], min(min1, min2) * grid[i][j])
                    dp[i, j] = [max_, min_]
        return (dp[M - 1, N - 1][0]) % MOD if dp[M - 1, N - 1][0] >= 0 else -1