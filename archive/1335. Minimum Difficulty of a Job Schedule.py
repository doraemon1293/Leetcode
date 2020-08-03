import collections


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        dp = collections.defaultdict(lambda: float("inf"))
        n=len(jobDifficulty)
        def foo(i, d):
            if (i, d) in dp:
                return dp[i, d]
            if d == 1:
                dp[i, d] = max(jobDifficulty[i:])
                return dp[i, d]
            max_d = -1
            res = float("inf")
            for j in range(i, n - d + 1):
                max_d = max(jobDifficulty[j], max_d)
                res = min(res, max_d + foo(j + 1, d - 1))
            dp[i,d]=res
            return res

        ans=foo(0,d)
        if ans==float("inf"):
            return -1
        else:
            return ans
