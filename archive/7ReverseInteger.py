# coding=utf-8
'''
Created on 2016�?10�?26�?

@author: Administrator
'''


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = -1 * int(str(-1 * x)[::-1])
        if (-1) * 2 ** 31 >= ans or ans >= (2 ** 31 - 1):
            ans = 0
        return ans


print Solution().reverse(123)

