# coding=utf-8
'''
Created on 2016å¹?12æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


s = "Hello, my name is John"
print Solution().countSegments(s)
