# coding=utf-8
'''
Created on 2017å¹?10æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        path = [[False] * len(s) for _ in xrange(len(s))]
        for mid in xrange(len(s)):
            st = end = mid
            while st >= 0 and end < len(s) and s[st] == s[end]:
                path[st][end] = True
                st -= 1
                end += 1
            st, end = mid, mid + 1
            while st >= 0 and end < len(s) and s[st] == s[end]:
                path[st][end] = True
                st -= 1
                end += 1
        dp = [float("inf")] * len(s)
        # dp[-1]=1
        for i in xrange(len(s) - 1, -1, -1):
            if path[i][len(s) - 1]:
                dp[i] = 0
            else:
                for j in xrange(i + 1, len(s)):
                    if path[i][j - 1]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]


s = "aab"
print Solution().minCut(s)

