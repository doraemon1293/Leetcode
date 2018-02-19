# coding=utf-8
'''
Created on 2016å¹?11æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        i = 0
        for x in g:
            while i < len(s) and s[i] < x:
                i += 1
            ans += 1
            i += 1
            if i >= len(s):
                break
        return ans

