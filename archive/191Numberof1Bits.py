# coding=utf-8
'''
Created on 2016�?10�?31�?

@author: Administrator
'''


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")
