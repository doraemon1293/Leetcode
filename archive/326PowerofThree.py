# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from math import log10

        return n > 0 and (log10(n) / log10(3)) .is_integer()


print Solution().isPowerOfThree(243)
