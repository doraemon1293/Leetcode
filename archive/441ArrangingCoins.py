# coding=utf-8
'''
Created on 2016�?11�?8�?

@author: Administrator
'''


class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + (1 + 8 * n) ** 0.5) / 2)
