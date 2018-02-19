# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n / 5
            n /= 5
        return ans

