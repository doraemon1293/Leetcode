# coding=utf-8
'''
Created on 2016å¹?10æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")
