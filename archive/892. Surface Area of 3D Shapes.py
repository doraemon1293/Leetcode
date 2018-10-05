class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0
        for x in range(N):
            for y in range(N):
                temp = 2 if grid[x][y]!=0 else 0
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < N and 0 <= ty < N:
                        temp += max(grid[x][y] - grid[tx][ty], 0)
                    else:
                        temp += grid[x][y]
                ans += temp
                #print(x,y,temp)
        return ans
grid=[[1,0],[0,2]]
print(Solution().surfaceArea(grid))