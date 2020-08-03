class Solution:
    def countSquares(self, matrix: list) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [x[:] for x in matrix]
        ans = 0
        for x in range(0, M):
            for y in range(0, N):
                if x==0 or y==0:
                    dp[x][y]=matrix[x][y]
                elif matrix[x][y]:
                    dp[x][y] = min(dp[x - 1][y], dp[x][y - 1], dp[x - 1][y - 1]) + 1
                else:
                    dp[x][y] = 0
                ans += dp[x][y]

        return ans


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
print(Solution().countSquares(matrix))
