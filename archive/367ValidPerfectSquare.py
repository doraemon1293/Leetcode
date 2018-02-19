# coding=utf-8
'''
Created on 2016å¹?11æœ?23æ—?

@author: Administrator
'''


# binary search
class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) / 2
            if mid ** 2 < num:
                lo = mid + 1
            elif mid ** 2 > num:
                hi = mid - 1
            else:
                return True
        return False

# 1+3+5+7+9...(2n-1)=(1+(2n-1)*n)/2=n^2


class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = 0
        for i in xrange(1, 2 * num + 1, 2):
            s += i
            if s == num: return True
            if s > num: return False
