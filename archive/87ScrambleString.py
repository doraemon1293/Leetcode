# coding=utf-8
'''
Created on 2017å¹?7æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def foo(s1, s2):
            if len(s1) != len(s2):
                return False
            if sorted(s1) != sorted(s2):
                return False
            if len(s1) == 1: return True
            for i in xrange(1, len(s1)):
                if foo(s1[:i], s2[:i]) and foo(s1[i:], s2[i:]) or foo(s1[:i], s2[-i:]) and foo(s1[i:], s2[:-i]):
                    return True
            return False

        return foo(s1, s2)

