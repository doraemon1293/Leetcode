from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:

        M = len(grid)
        N = len(grid[0])

        def legit(dp, i, j):
            if dp == set():
                return set()
            if grid[i][j] == "(":
                return set([x + 1 for x in dp])
            else:
                return set([x - 1 for x in dp if x != 0])

        for i in range(M):
            dp = [0] * N
            for j in range(N):
                if i == 0:
                    if j == 0:
                        dp[j] = legit([0], i, j)
                    else:
                        dp[j] = legit(dp[j - 1], i, j)
                else:
                    if j == 0:
                        dp[j] = legit(last_dp[j], i, j)
                    else:
                        dp[j] = legit(last_dp[j] | dp[j - 1], i, j)
            last_dp = dp
        return 0 in dp[N - 1]
