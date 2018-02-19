# coding=utf-8
'''
Created on 2017�?10�?22�?

@author: Administrator
'''


class Solution(object):

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp_buy = [0] * len(prices)
        dp_buy[0] = -prices[0]
        dp_not_buy = [0] * len(prices)
        for i in xrange(1, len(prices)):
            dp_buy[i] = max(dp_buy[i - 1], dp_not_buy[i - 1] - prices[i])
            dp_not_buy[i] = max(dp_not_buy[i - 1], dp_buy[i - 1] + prices[i] - fee)
        return dp_not_buy[-1]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print Solution().maxProfit(prices, fee)
