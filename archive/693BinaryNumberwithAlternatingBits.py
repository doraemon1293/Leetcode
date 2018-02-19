# coding=utf-8
'''
Created on 2017å¹?10æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last_bit = n % 2
        n /= 2
        while n:
            cur_bit = n % 2
            if cur_bit == last_bit:
                return False
            n /= 2
            print cur_bit, last_bit
            last_bit = cur_bit
        return True


n = 1
print Solution().hasAlternatingBits(n)
