class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        self.ans = 0
        self.blocks = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] == 0:
                    self.blocks += 1

        def dfs(x, y):
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                xt, yt = x + dx, y + dy
                if 0 <= xt < M and 0 <= yt < N:
                    if grid[xt][yt] == 2 and self.blocks == 0:
                        self.ans += 1
                    if grid[xt][yt] == 0:
                        self.blocks -= 1
                        grid[xt][yt] = -1
                        dfs(xt, yt)
                        grid[xt][yt] = 0
                        self.blocks += 1

        dfs(x,y)
        return self.ans

grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
grid= [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(Solution().uniquePathsIII(grid))