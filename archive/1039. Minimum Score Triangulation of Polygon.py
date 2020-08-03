class Solution:
    def minScoreTriangulation(self, A) -> int:
        dp = {}

        def solve(A):
            if len(A) < 3:
                return 0
            if len(A) == 3:
                return A[0] * A[1] * A[2]
            if A in dp:
                return dp[A]

            mini = float("inf")
            for i in range(1, len(A) - 1):
                A1 = tuple(A[:i + 1])
                A2 = tuple(A[i:])
                temp = A[i] * A[0] * A[len(A) - 1] + solve(A1) + solve(A2)
                if temp < mini:
                    mini = temp
            dp[A] = mini
            return mini

        A = tuple(A)
        return solve(A)
