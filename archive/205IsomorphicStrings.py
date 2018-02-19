# coding=utf-8
'''
Created on 2016å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            d = {}  # characters
            for i in range(len(s)):
                if s[i] in d:
                    if t[i] != d[s[i]]:
                        return False
                elif t[i] in d.values():
                        return False
                else:
                    d[s[i]] = t[i]
        return True


s = "ab"
t = "ca"
print Solution().isIsomorphic(s, t)

# print zip(s, t)
