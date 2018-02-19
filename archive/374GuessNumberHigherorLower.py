# coding=utf-8
'''
Created on 2016å¹?11æœ?11æ—?

@author: Administrator
'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    n = 10
    if num > n:
        return -1
    elif num < n:
        return 1
    else:
        return 0


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1, p2 = 1, n
        x = p1 + (p2 - p1) / 2
        while guess(x):
            if guess(x) == -1:
                p2 = x - 1
            else:
                p1 = x + 1
            x = (p1 + p2) / 2
        return x


print Solution().guessNumber(10)
