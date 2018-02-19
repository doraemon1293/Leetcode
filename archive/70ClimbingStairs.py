# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a1 = 1
            a2 = 2
            for _ in xrange(3, n + 1):
                a3 = a1 + a2
                a1, a2 = a2, a3
            return a3


print Solution().climbStairs(5)

