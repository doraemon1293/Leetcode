# coding=utf-8
'''
Created on 2017�?4�?10�?

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
