class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        N = len(A[0])
        dp = [1] * N
        for i in range(N - 1, -1, -1):
            for j in range(i-1, -1, -1):
                if all(row[i] >= row[j] for row in A):
                    dp[j] = max(dp[j], 1 + dp[i])
        return N - max(dp)


A = ["babca", "bbazb"]
print(Solution().minDeletionSize(A))
