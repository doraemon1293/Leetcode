# coding=utf-8
'''
Created on 2017å¹?4æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        " ".join([word[::-1] for word in s.split()])
