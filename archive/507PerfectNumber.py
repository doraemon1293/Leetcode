# coding=utf-8
'''
Created on 2017å¹?3æœ?28æ—?

@author: Administrator
'''


class Solution(object):

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (sum([(x if x != num else 0) + (num / x if x != num / x and x != 1 else 0) for x in range(1, int(num ** 0.5) + 1) if num % x == 0]) == num) if num > 0 else False


print Solution().checkPerfectNumber(28)
