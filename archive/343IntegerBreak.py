# coding=utf-8
'''
Created on 2016�?11�?17�?

@author: Administrator
'''


class Solution(object):

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 1
        if n == 3: return 2
        if n % 3 == 0: return 3 ** (n / 3)
        if n % 3 == 1: return 2 * 2 * (3 ** ((n - 4) / 3))
        if n % 3 == 2: return 2 * (3 ** ((n - 2) / 3))


print Solution().integerBreak(4)
