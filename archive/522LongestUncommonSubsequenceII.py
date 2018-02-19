# coding=utf-8
'''
Created on 2017å¹?7æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key = len, reverse = True)

        def isSubseq(a, b):
            i = 0
            for ch in  b:
                if i < len(a) and a[i] == ch:
                    i += 1
                if i == len(a):
                    break
            return i == len(a)

        for i, a in enumerate(strs):
            if all(not isSubseq(a, b) for j, b in enumerate(strs) if i != j):
                return len(a)
        return -1

