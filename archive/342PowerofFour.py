# coding=utf-8
'''
Created on 2016å¹?11æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def isPowerOfThree(self, num):
        """
        :type n: int
        :rtype: bool
        """
        from math import log10

        return num > 0 and (log10(num) / log10(4)) .is_integer()


print Solution().isPowerOfThree(243)
