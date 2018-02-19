# coding=utf-8
# https://en.wikipedia.org/wiki/Digital_root
# æ•°æ ¹çš„o(1)ç®—æ³•
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return num - (num - 1) / 9 * 9


print Solution().addDigits(0)

