# coding=utf-8
'''
Created on 2017å¹?9æœ?14æ—?

@author: Administrator
'''
from collections import defaultdict


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s) + 1) for _ in xrange(len(p) + 1)]
        dp[0][0] = True
        i = 1
        while i <= len(p) and p[i - 1] == "*":
            dp[i][0] = True
            i += 1

        for i in xrange(1, len(p) + 1):
            for j in xrange(1, len(s) + 1):
                if dp[i][j] == False:
                    if p[i - 1] == s[j - 1] or p[i - 1] == "?":
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[i - 1] == "*":
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[len(p)][len(s)]


s = "a"
p = ""
print Solution().isMatch(s, p)

#         lens, lenp = len(s), len(p)
#         if lenp == 0:
#             if s == "":
#                 return True
#             else:
#                 return False
#         dp = defaultdict(bool)
#         dp[-1, -1] = True
#         if p[0] == "*":
#             dp[0, -1] = True
#         for i in xrange(lenp):
#             for j in xrange(lens):
#                 if p[i] == "*":
#                     dp[i, j] = dp[i - 1, j - 1] or dp[i - 1, j] or dp[i, j - 1]
#                 elif p[i] == "?" or p[i] == s[j]:
#                     dp[i, j] = dp[i - 1, j - 1]
#         print dp
#         return dp[lenp - 1, lens - 1]

#         memo = {(len(p), len(s)):True}
#         def foo(i, j):
#             print i, j
#             if (i, j) in memo:
#                 return memo[(i, j)]
#             if i >= len(p) or j >= len(s):
#                 return False
#             if p[i] == s[j] or p[i] == "?":
#                 res = foo(i + 1, j + 1)
#                 memo[(i, j)] = res
#             elif p[i] == "*":
#                 res = False
#                 for k in xrange(j, len(s) + 1):
#                     res = res or foo(i + 1, k)
#                     if res:
#                         break
#                 memo[(i, j)] = res
#             else:
#                 memo[(i, j)] = False
#             return memo[(i, j)]
#         foo(0, 0)
#         print memo
#         return memo[(0, 0)]

