# coding=utf-8
'''
Created on 2017å¹?5æœ?28æ—?

@author: Administrator
'''


class Solution(object):

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops:
            min_x = min([x[0] for x in ops])
            min_y = min(x[1] for x in ops)
            return min_x * min_y
        else:
            return m * n


m = n = 3
ops = []

print Solution().maxCount(m, n, ops)
