# coding=utf-8
'''
Created on 2016å¹?11æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while 1:
            squar_sum = 0
            while n:
                squar_sum += (n % 10) ** 2
                n /= 10
            if squar_sum == 1:
                return True
            else:
                if squar_sum in s:
                    return False
                else:
                    s.add(squar_sum)
                    n = squar_sum
            print squar_sum


print Solution().isHappy(88)

