class Solution:
    def pathsWithMaxScore(self, board: list) -> list:
        M, N = len(board), len(board[0])
        dp = [[(-1, 0)] * M for _ in range(N)]
        MOD = 10 ** 9 + 7

        dp[M - 1][N - 1] = (0, 1)
        for x in range(M - 1, -1, -1):
            for y in range(N - 1, -1, -1):
                if board[x][y] != "X" and board[x][y] != "S":
                    for x1, y1 in ((x + 1, y), (x, y + 1), (x + 1, y + 1)):
                        if 0 <= x1 < M and 0 <= y1 < N and dp[x1][y1][0] != -1:
                            temp = dp[x1][y1][0] + (0 if board[x][y] == "E" else int(board[x][y]))
                            if temp > dp[x][y][0]:
                                dp[x][y] = (temp, dp[x1][y1][1])
                            elif temp == dp[x][y][0]:
                                dp[x][y] = (temp, (dp[x][y][1] + dp[x1][y1][1]) % MOD)
        print(dp)
        if dp[0][0][0] >= 0:
            return dp[0][0]
        else:
            return [0, 0]


board = ["E23", "2X2", "12S"]
# board = ["E11", "XXX", "11S"]
print(Solution().pathsWithMaxScore(board))
