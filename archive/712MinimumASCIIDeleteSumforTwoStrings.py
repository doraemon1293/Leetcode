# coding=utf-8
'''
Created on 2017å¹?10æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in xrange(m + 1)]
        for i in xrange(m):
            for j in xrange(n):
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], ord(s1[i]) + dp[i][j] if s1[i] == s2[j] else 0)
        return sum([ord(ch) for ch in s1]) + sum([ord(ch) for ch in s2]) - 2 * dp[-1][-1]


s1 = 'ABCBDAB'
s2 = 'BDCABA'
s1 = ""
s2 = ""
print Solution().minimumDeleteSum(s1, s2)

