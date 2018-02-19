# coding=utf-8
'''
Created on 2017å¹?7æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            one_diff = False
            for i in xrange(len(s)):
                if s[i] != t[i]:
                    if one_diff == False:
                        one_diff = True
                    else:
                        return False
            return one_diff
        elif len(s) == len(t) + 1:
            for i in xrange(len(s)):
                if i == len(t) or s[i] != t[i]:
                    break
            # print i
            return s[:i] + s[i + 1:] == t
        elif len(s) + 1 == len(t) :
            for i in xrange(len(t)):
                if i == len(s) or s[i] != t[i]:
                    break
            return t[:i] + t[i + 1:] == s
        else:
            return False


s = "ab"
t = "abc"
print Solution().isOneEditDistance(s, t)
