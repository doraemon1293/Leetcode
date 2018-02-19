# coding=utf-8
'''
Created on 2017å¹?6æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # é€’å½’
#         memo = {}
#         def dp(st, en):
#             if (st, en) in memo:
#                 return memo[st, en]
#             if st >= en:
#                 memo[(st, en)] = 0
#                 return 0
#             if st + 1 == en:
#                 memo[(st, en)] = st
#                 return st
#             mini = min([max(dp(st, x - 1), dp(x + 1, en)) + x for x in range(st, en + 1)])
#             memo[(st, en)] = mini
#             return mini
#         return dp(1, n)
        # é€’æŽ¨
        dp = [[0] * (n + 2) for _ in xrange(n + 2)]

        for step in xrange(2, n + 1):
            for st in xrange(1, n - step + 2):
                en = st + step - 1
                dp[st][en] = min(max(dp[st][x - 1], dp[x + 1][en]) + x for x in xrange(st, en + 1))
        return dp[1][n]


n = 60
print Solution().getMoneyAmount(n)

