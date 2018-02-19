# coding=utf-8
'''
Created on 2016�?11�?17�?

@author: Administrator
'''


class Solution(object):

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "": return True
        if t == "": return False
        i = 0
        for x in s:
            while i < len(t) and t[i] != x:
                i += 1
            if i >= len(t):
                return False
            i += 1
        return True

