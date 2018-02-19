# coding=utf-8
'''
Created on 2016å¹?11æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([prices[i + 1] - prices[i] for i in xrange(len(prices) - 1) if prices[i + 1] - prices[i] > 0])
