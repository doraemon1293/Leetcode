# coding=utf-8
'''
Created on 2017å¹?9æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # forwrd DP TLE
#         n = len(s)
#         memo = [[] for i in xrange(n)]
#         for i in xrange(n):
#             for j in xrange(i + 1):
#                 if s[j:i + 1] in wordDict:
#                     for pre in memo[j - 1] if j != 0 else [[]]:
#                         memo[i].append(pre + [s[j:i + 1]])
#         print memo
#         return [" ".join(x) for x in memo[-1]]

        memo = {len(s):[[]]}
        wordDict = set(wordDict)

        def foo(ind):
            if ind in memo:
                return memo[ind]
            else:
                memo[ind] = []
                for i in xrange(ind, len(s)):
                    if s[ind:i + 1] in wordDict:
                        memo[ind] += [[s[ind:i + 1]] + tail for tail in foo(i + 1)]
                return memo[ind]

        foo(0)
        return [" ".join(x) for x in memo[0]]


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print Solution().wordBreak(s, wordDict)
