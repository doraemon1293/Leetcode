# coding=utf-8
'''
Created on 2017å¹?8æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp00 = 1  # P
        dp01 = 1  # L
        dp02 = 0
        dp10 = 1  # A
        dp11 = 0
        dp12 = 0
        for _ in xrange(n - 1):
            dp00, dp01, dp02, dp10, dp11, dp12 = \
            (dp00 + dp01 + dp02) % MOD, \
            (dp00) % MOD, \
            (dp01) % MOD, \
            (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % MOD, \
            (dp10) % MOD, \
            (dp11) % MOD
            # print dp
        return sum([dp00, dp01, dp02, dp10, dp11, dp12]) % MOD


n = 100000
print Solution().checkRecord(n)
