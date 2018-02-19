# coding=utf-8
'''
Created on 2017å¹?6æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         for k transactions
#         f[k, ii] represents the max profit up until prices[ii] using at most k transactions.
#         f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj+1] + f[k-1, jj]) { jj in range of [0, ii-2] }
#                  = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj+1]))
#         f[0, ii] = 0; 0 times transation makes 0 profit
#         f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
        if len(prices) == 0: return 0
        f = []
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            f.append(max_profit)
        print f
        max_profit = [0]
        ans = max(f)
        maxi = -prices[0]
        for i in xrange(1, len(prices)):
            max_profit.append(max(max_profit[-1], prices[i] + maxi))
            maxi = max(maxi, f[i - 1] - prices[i])
            ans = max(ans, max_profit[-1])
        print max_profit
        return ans


prices = [2, 1, 2, 0, 1]
prices = [1, 2, 1, 5, 100]
# prices = [2, 0, 1]
print Solution().maxProfit(prices)

