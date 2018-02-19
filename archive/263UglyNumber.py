# coding=utf-8
'''
Created on 2016å¹?11æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num <= 0:
            return False
        else:
            for i in (2, 3, 5):
                while num % i == 0:
                    num /= i
            if num == 1:
                return True
            else:
                return False


print Solution().isUgly(-14)
