# coding=utf-8
'''
Created on 2016�?10�?26�?

@author: Administrator
'''


class Solution(object):

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True

