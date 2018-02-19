# coding=utf-8
'''
Created on 2017å¹?5æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x_arr = []
        y_arr = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    x_arr.append(i)
                    y_arr.append(j)
        # x_arr.sort()
        y_arr.sort()
        x_median = x_arr[len(x_arr) / 2]
        y_median = y_arr[len(y_arr) / 2]
        return sum(abs(x - x_median) for x in x_arr) + sum(abs(y - y_median) for y in y_arr)


grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
print Solution().minTotalDistance(grid)
