# coding=utf-8
'''
Created on 2017å¹?6æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0: return 0
        dp = [0] * n
        summ = 0
        for i in xrange(m - 1, -1, -1):
            new_dp = [0] * n
            for j in xrange(n - 1, -1, -1):
                new_dp[j] = (min((dp[j] if i != m - 1 else float("inf")),
                               (new_dp[j + 1] if j != n - 1 else float("inf"))
                            ) if i != m - 1 or j != n - 1 else 0) + grid[i][j]
            dp = new_dp
        return dp[0]


grid = [[1, 2], [3, 4]]
print Solution().minPathSum(grid)

