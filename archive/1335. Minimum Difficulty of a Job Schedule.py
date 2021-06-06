from typing import List
import functools

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        D = d
        dp = [[0] * N for _ in range(D)]  # list dp(d,job) job schedule d-th day finish job-th job N*d

        @functools.lru_cache(None)
        def get_max(i,j):
            return max(jobDifficulty[i:j+1])

        for d in range(D):
            for job in range(N):
                if d == 0:
                    dp[d][job] = get_max(0,job)
                else:
                    mini = float("inf")
                    for i in range(d - 1, job):
                        mini = min(dp[d - 1][i] + get_max(i+1,job), mini)
                    dp[d][job]=mini

        return dp[D-1][N-1]
