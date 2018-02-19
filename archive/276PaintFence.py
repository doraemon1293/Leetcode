# coding=utf-8
'''
Created on 2016å¹?12æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k * 1
        diff = k * (k - 1)
        for i in range(3, n + 1):
            same, diff = diff * 1, same * (k - 1) + diff * (k - 1)
        return same + diff
