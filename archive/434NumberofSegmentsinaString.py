# coding=utf-8
'''
Created on 2016�?12�?5�?

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
