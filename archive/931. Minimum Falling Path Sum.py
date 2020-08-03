class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        N = len(A)
        dp = A[-1]
        for i in range(N - 2, -1, -1):
            for j in range(N):
                new_dp = A[i]
                new_dp[j] += min(dp[j - 1] if j - 1 >= 0 else float("inf"), dp[j],
                                 dp[j + 1] if j + 1 < N else float("inf"))
            dp = new_dp
        return min(dp)


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().minFallingPathSum(A))
