# coding=utf-8
'''
Created on 2017å¹?6æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        step = 1
        left_to_right = True
        while n != 1:
            if left_to_right or n % 2 == 1:
                first += step
            n /= 2
            step *= 2
            left_to_right = not left_to_right
        return first
