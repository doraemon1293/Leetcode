# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float("inf")
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


prices = [7, 6, 4, 3, 1]
print Solution().maxProfit(prices)

