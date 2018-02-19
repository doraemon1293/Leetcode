# coding=utf-8
'''
Created on 2016å¹?11æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x, gx in enumerate(grid):
            for y, gy in enumerate(gx):
                if gy == 1:
                    if x - 1 < 0 or grid[x - 1][y] == 0:ans += 1
                    if x + 1 >= len(grid) or grid[x + 1][y] == 0:ans += 1
                    if y - 1 < 0 or grid[x][y - 1] == 0:ans += 1
                    if y + 1 >= len(gx) or grid[x][y + 1] == 0:ans += 1
        return ans
