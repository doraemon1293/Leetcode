class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0])
        flag = True
        minutes = 0
        while flag:
            flag = False
            new_grid = [[grid[i][j] for j in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if new_grid[i][j] == 1:
                        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                            if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 2:
                                new_grid[i][j] = 2
                                flag = True
                                break
            if flag:
                minutes += 1
                grid = new_grid
            #print(grid, new_grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))
