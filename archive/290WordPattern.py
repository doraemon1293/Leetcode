# coding=utf-8
'''
Created on 2016å¹?11æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d_p_s = {}
        d_s_p = {}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        for p, s in zip(pattern, str):
            if p in d_p_s and s != d_p_s[p] or s in d_s_p and p != d_s_p[s]:
                return False
            else:
                d_p_s[p], d_s_p[s] = s, p
        return True

