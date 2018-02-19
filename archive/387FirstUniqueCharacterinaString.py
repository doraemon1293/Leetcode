# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        temp = Counter(s)
        for i, c in enumerate(s):
            if temp[c] == 1:
                return i
        return -1
