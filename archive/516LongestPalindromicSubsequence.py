# coding=utf-8
'''
Created on 2017å¹?7æœ?24æ—?

@author: Administrator
'''


class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j] the longest subsequence between s[i] and s[j]
        # dp[i][j]=dp[i+1][j-1]+2 if s[i]==s[j]
        # dp[i-1][j+1]=max(dp[i][j+1],dp[i-1][j] if s[i-1]!=s[j+1]
# 1st solution  dp by length
#         if s==s[::-1]: return len(s)
#         n = len(s)
#         dp = [[1] * n for _ in xrange(n)]
#         for length in xrange(1, n):
#             for i in xrange(n):
#                 if (i + length) < n:
#                     if length == 1:
#                         dp[i][i + length] = 2 if s[i] == s[i + length] else 1
#                     else:
#                         if s[i] == s[i + length]:
#                             dp[i][i + length] = dp[i + 1][i + length - 1] + 2
#                         else:
#                             dp[i][i + length] = max(dp[i + 1][i + length], dp[i][i + length - 1])
#                 else:
#                     break
#         return dp[0][n - 1]

# 2nd solution dp from end to begin
# not neccesary to remember start index(i) so memory can be reduce to O(n)
        n = len(s)
        dp = [0] * n
        dp[-1] = 1  # dp[i] the longest for s[:i+1]
        for i in xrange(n - 1, -1, -1):
            new_dp = dp[:]
            new_dp[i] = 1
            for j in xrange(i + 1, n):
                if s[i] == s[j]:
                    new_dp[j] = dp[j - 1] + 2
                else:
                    new_dp[j] = max(dp[j], new_dp[j - 1])
            dp = new_dp
        return dp[n - 1]


s = "aaa"

print Solution().longestPalindromeSubseq(s)
