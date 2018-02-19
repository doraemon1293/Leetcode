# coding=utf-8
'''
Created on 2017å¹?6æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []: return 0
        m, n = len(grid), len(grid[0])
        col = [0] * n
        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                if j == 0 or grid[i][j - 1] == "W":
                    row = 0
                    k = j
                    while k < n and grid[i][k] != "W":
                        row += grid[i][k] == "E"
                        k += 1
                if i == 0 or grid[i - 1][j] == "W":
                    col[j] = 0
                    k = i
                    while k < m and grid[k][j] != "W":
                        col[j] += grid[k][j] == "E"
                        k += 1
                if grid[i][j] == "0":
                    ans = max(ans, row + col[j])
        return ans


grid = ["0E00", "E0WE", "0E00"]
print Solution().maxKilledEnemies(grid)
