# coding=utf-8
'''
Created on 2016å¹?11æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        c1 = Counter(s)
        c1.subtract(Counter(t))
        return [k for k, v in c1.items() if v != 0][0]


s = "abcd"
t = "abcda"
print Solution().findTheDifference(s, t)
