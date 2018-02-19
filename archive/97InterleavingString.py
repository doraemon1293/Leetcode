# coding=utf-8
'''
Created on 2017å¹?10æœ?25æ—?

@author: Administrator
'''


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # dp[i][j] s1[:i] s2[:j] æ˜¯å¦åŒ¹é…s3[:i+j]
        # dp[i][j]= dp[i-1][j] if s1[i-1]==s3[i+j-1] or
        #           dp[i][j-1] if s2[j-1]==s3[i+j-1]
        # dp[0][0]=True
        # dp[0][j]= dp[0][j-1] and s2[j-1]==s3[j-1]
        # dp[i][0]= dp[i-1][0] and s1[i-1]==s3[i-1]
        # 0<=i<=len(s1) 0<=j<=len(s2)
        if len(s3) != len(s2) + len(s1): return False
        dp = [[False] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]
        dp[0][0] = True
        for i in xrange(0, len(s1) + 1):
            for j in xrange(0, len(s2) + 1):
                if i != 0 or j != 0:
                    if i == 0:
                        dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
        return dp[-1][-1]


s1 = "a"
s2 = ""
s3 = "a"
print Solution().isInterleave(s1, s2, s3)
