class Solution:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        dp = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            maxi=A[i-1]
            for k in range(1, min(K+1, i+1)):
                maxi=max(maxi,A[i-k])
                dp[i] = max(dp[i], dp[i - k] + maxi * k)
        return dp[-1]


A = [1, 15, 7, 9, 2, 5, 10]
K = 3
print(Solution().maxSumAfterPartitioning(A, K))
