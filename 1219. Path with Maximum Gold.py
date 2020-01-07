class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])

        def validate(x, y):
            return 0 <= x < M and 0 <= y < N and grid[x][y] != 0

        def dfs(grid, x, y):
            temp = grid[x][y]
            grid[x][y] = 0
            maxi = 0
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if validate(x + dx, y + dy):
                    maxi = max(maxi, dfs(grid, x + dx, y + dy))
            grid[x][y] = temp
            return temp + maxi

        ans = 0
        for x in range(M):
            for y in range(N):
                if validate(x, y):
                    ans = max(ans, dfs(grid, x, y))
        return ans

