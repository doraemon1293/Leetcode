# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

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
