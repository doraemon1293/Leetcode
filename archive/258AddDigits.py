# coding=utf-8
# https://en.wikipedia.org/wiki/Digital_root
# 数根的o(1)算法
'''
Created on 2016�?10�?26�?

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

