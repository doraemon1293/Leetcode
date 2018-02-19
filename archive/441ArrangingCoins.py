# coding=utf-8
'''
Created on 2016å¹?11æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1 + (1 + 8 * n) ** 0.5) / 2)
