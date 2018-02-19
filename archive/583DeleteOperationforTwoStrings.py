# coding=utf-8
'''
Created on 2017å¹?5æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        c = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i > 0 and j > 0:
                    if word1[i - 1] == word2[j - 1]:
                        c[i][j] = c[i - 1][j - 1] + 1
                    else:
                        c[i][j] = max(c[i - 1][j], c[i][j - 1])
        # print c
        return len(word1) + len(word2) - 2 * c[len(word1)][len(word2)]


word1, word2 = "sea", "eat"
print Solution().minDistance(word1, word2)
