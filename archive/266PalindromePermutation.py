# coding=utf-8
'''
Created on 2016å¹?12æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        return len([x for x in Counter(s).values() if x % 2]) <= 1
