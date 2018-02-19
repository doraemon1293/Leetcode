# coding=utf-8
'''
Created on 2017å¹?4æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return max(len(a), len(b)) if a != b else -1
