# coding=utf-8
'''
Created on 2016�?11�?15�?

@author: Administrator
'''


class Solution(object):

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        temp = 9 * (10 ** (i - 1)) * i
        while n >= temp:
            n -= temp
            i += 1
            temp = 9 * (10 ** (i - 1)) * i
        print temp
        length = i
        print length
        if n == 0:
            return 9
        return int(str(10 ** (length - 1) + (n - 1) / length)[(n - 1) % length])


print Solution().findNthDigit(3)

