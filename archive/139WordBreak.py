# coding=utf-8
'''
Created on 2016å¹?12æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        flag = [False] * len(s)
        for i in xrange(len(s)):
            for j in xrange(i + 1):
                if (j == 0 or flag[j - 1]) and s[j :i + 1] in wordDict:
                    flag[i] = True
        return flag[len(s) - 1]


s = "leetcode"
wordDict = ["leet", "code"]

print Solution().wordBreak(s, wordDict)

