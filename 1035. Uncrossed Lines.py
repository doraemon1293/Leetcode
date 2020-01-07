class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            for j in range(len(B) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif A[i-1] != B[j-1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        print(dp)
        return dp[-1][-1]


A = [1, 3, 7, 1, 7, 5]
B = [1, 9, 2, 5, 1]
Solution().maxUncrossedLines(A, B)
