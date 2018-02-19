# coding=utf-8
'''
Created on 2017å¹?2æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0

        def dfs(i, j):
            grid[i][j] = "."
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            if i + 1 < len(grid) and grid[i + 1][j] == "1":
                dfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                dfs(i, j - 1)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1":
                dfs(i, j + 1)

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans


grid = ["111", "010", "111"]

print Solution().numIslands(grid)

