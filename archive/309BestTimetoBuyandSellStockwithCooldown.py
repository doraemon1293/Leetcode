# coding=utf-8
'''
Created on 2017�?7�?5�?

@author: Administrator
'''


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        sell = [-float("inf")] * n
        ans = sell[0] = 0
        buy = [-float("inf")] * n
        buy[0] = -prices[0]
        for i in xrange(1, n):
            sell[i] = max(sell[i - 1] + prices[i] - prices[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1] - prices[i] + prices[i - 1])
            ans = max(ans, sell[i])
        return ans
