# coding=utf-8
'''
Created on 2017å¹?9æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        d = [[0] * (l2 + 1) for _ in xrange(l1 + 1)]
        for i in xrange(l1 + 1):
            for j in xrange(l2 + 1):
                if i == 0 or j == 0:
                    d[i][j] = i or j
                elif word1[i - 1] == word2[j - 1]:
                    d[i][j] = min(d[i - 1][j - 1], d[i - 1][j] + 1, d[i][j - 1] + 1)
                else:
                    d[i][j] = min(d[i - 1][j - 1] + 1, d[i - 1][j] + 1, d[i][j - 1] + 1)
        return d[l1][l2]


word1 = "a"
word2 = ""
print Solution().minDistance(word1, word2)
