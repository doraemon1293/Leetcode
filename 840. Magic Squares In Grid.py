class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0
        for x in range(N - 2):
            for y in range(N - 2):
                if set(grid[x][y:y+3]+grid[x+1][y:y+3]+grid[x+2][y:y+3])==set(range(1,10)):
                    r1 = sum(grid[x][y:y + 3])
                    r2 = sum(grid[x + 1][y:y + 3])
                    r3 = sum(grid[x + 2][y:y + 3])
                    c1 = grid[x][y] + grid[x + 1][y]+grid[x + 2][y]
                    c2 = grid[x][y + 1] + grid[x + 1][y + 1] + grid[x + 2][y + 1]
                    c3 = grid[x][y + 2] + grid[x + 1][y + 2] + grid[x + 2][y + 2]
                    d1 = grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2]
                    d2 = grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y]
                    if r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2:
                        ans += 1
        return ans


grid = [[10,3,5],[1,6,11],[7,9,2]]
print(Solution().numMagicSquaresInside(grid))
