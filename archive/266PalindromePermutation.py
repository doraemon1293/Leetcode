# coding=utf-8
'''
Created on 2016�?12�?1�?

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
