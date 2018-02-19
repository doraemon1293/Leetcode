# coding=utf-8
'''
Created on 2017å¹?5æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter
        c1 = Counter(s1)
        len1 = len(s1)
        c2 = Counter(s2[:len1])
        if c1 == c2: return True
        for i in range(1, len(s2) - len1 + 1):
            c2[s2[i - 1]] -= 1
            if c2[s2[i - 1]] == 0:
                del c2[s2[i - 1]]
            c2.setdefault(s2[i + len1 - 1], 0)
            c2[s2[i + len1 - 1]] += 1
            if c1 == c2:
                return True
        return False

        for
        c2 = Counter(s2[])
        for i in range(len(s2)):
            c2 = Counter(s2[i:i + len(s1)])
            if c1 == c2:
                return True
        return False
