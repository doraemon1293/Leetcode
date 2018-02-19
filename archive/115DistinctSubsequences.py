# coding=utf-8
'''
Created on 2017å¹?10æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        len_s = len(s)
        len_t = len(t)
        dp = [[1] + [0] * (len_t) for _ in xrange(len_s + 1)]
        for i in xrange(1, len_s + 1):
            for j in xrange(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


s = "rabbit"
t = "rabit"
print Solution().numDistinct(s, t)
