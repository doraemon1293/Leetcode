# coding=utf-8
'''
Created on 2017�?4�?10�?

@author: Administrator
'''


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        " ".join([word[::-1] for word in s.split()])
