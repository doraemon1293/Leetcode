class Solution:
    def largest1BorderedSquare(self, grid: list) -> int:
        M, N = len(grid), len(grid[0])
        rows = [[0] * N for _ in range(M)]
        cols = [[0] * N for _ in range(M)]

        for x in range(M):
            for y in range(N - 1, -1, -1):
                if grid[x][y] == 1:
                    rows[x][y] = rows[x][y + 1] + 1 if y != N - 1 else 1
                else:
                    rows[x][y] = 0
        for y in range(N):
            for x in range(M - 1, -1, -1):
                if grid[x][y] == 1:
                    cols[x][y] = cols[x + 1][y] + 1 if x != M - 1 else 1
                else:
                    cols[x][y] = 0
        ans = 0
        for x in range(M):
            for y in range(N):
                length = min(rows[x][y], cols[x][y])
                for _len in range(length, 0, -1):
                    if rows[x + _len - 1][y] >= _len and cols[x][y + _len - 1] >= _len:
                        ans = max(ans, _len**2)
                        break
        return ans


grid = [[1, 1, 0, 0]]
grid=[[1,1,0,1,1,1,1,0],
      [0,1,1,0,0,0,1,1],
      [1,0,1,1,1,1,1,1],
      [1,1,1,0,0,1,1,1],
      [1,0,1,0,1,1,1,0],
      [1,1,1,1,1,1,1,1],
      [0,1,1,1,0,1,1,1],
      [0,1,1,0,1,1,0,1]]
print(Solution().largest1BorderedSquare(grid))
