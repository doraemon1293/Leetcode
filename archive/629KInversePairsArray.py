# coding=utf-8
'''
Created on 2017å¹?6æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if k > n * (n - 1) / 2: return 0
        dp = [0] * (k + 1)
        for i in xrange(1, n + 1):
            new_dp = [1]  # k==0
            for j in xrange(1, min(i * (i - 1) / 2 + 1, k + 1)):
                new_dp.append((new_dp[j - 1] + (dp[j] if j < len(dp) else 0) - (dp[j - i] if j >= i else 0)) % (10 ** 9 + 7))
            dp = new_dp
#         for i in xrange(1, n + 1):
#             for j in xrange(0, k + 1):
#                 print i, j, dp[i, j]
        return dp[k]


n = 1000
k = 1000
print Solution().kInversePairs(n, k)
