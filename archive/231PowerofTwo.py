# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count("1") == 1
