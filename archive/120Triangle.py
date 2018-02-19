# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''
from random import triangular


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == []: return 0
        dp = triangle[-1]
        for row in xrange(len(triangle) - 2, -1, -1):
            temp = [triangle[row][i] + min(dp[i], dp[i + 1]) for i in xrange(len(triangle[row]))]
            dp = temp
        return dp[0]


triangle = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
print Solution().minimumTotal(triangle)
