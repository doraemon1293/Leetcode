# coding=utf-8
'''
Created on 2016å¹?12æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        symbol = (dividend < 0) == (divisor < 0)
        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        temp, i = divisor, 1
        while dividend >= divisor:
            while dividend >= temp << 1:
                temp <<= 1
                i <<= 1
            dividend -= temp
            ans += i
            while temp > dividend:
                temp >>= 1
                i >>= 1

        ans = -ans if not symbol else ans
        return min(max(-2147483648, ans), 2147483647)


dividend = 10
divisor = 3
print Solution().divide(dividend, divisor)
