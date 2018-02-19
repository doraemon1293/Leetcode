# coding=utf-8
'''
Created on 2017å¹?11æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        set1, set2 = set(s1), set(s2)
        l1, l2 = len(s1), len(s2)
        if not set2 <= set1: return 0
        x1 = x2 = 0
        dp = {}
        while x1 < l1 * n1:
            while s1[x1 % l1] != s2[x2 % l2]:
                x1 += 1
            if x1 >= l1 * n1:
                break
            y1, y2 = x1 % l1, x2 % l2
            if (y1, y2) in dp:
                dx1, dx2 = dp[y1, y2]
                round = (l1 * n1 - dx1) / (x1 - dx1)
                x1 = dx1 + round * (x1 - dx1)
                x2 = dx2 + round * (x2 - dx2)
            else:
                dp[y1, y2] = (x1, x2)
            if x1 < l1 * n1:
                x1 += 1
                x2 += 1
        return x2 / (n2 * l2)

