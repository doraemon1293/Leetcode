# coding=utf-8
'''
Created on 2016�?10�?26�?

@author: Administrator
'''


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return x == int(str(x)[::-1])

