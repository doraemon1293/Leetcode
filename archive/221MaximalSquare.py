# coding=utf-8
'''
Created on 2017å¹?9æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in xrange(m)]
        ans = 0
        for x in xrange(m):
            for y in xrange(n):
                if x == 0 or y == 0:
                    dp[x][y] = int(matrix[x][y])
                elif int(matrix[x][y]):
                    dp[x][y] = min(dp[x - 1][y], dp[x - 1][y - 1], dp[x][y - 1]) + 1
                ans = max(ans, dp[x][y])
        return ans ** 2
