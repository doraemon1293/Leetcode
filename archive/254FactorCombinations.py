# coding=utf-8
'''
Created on 2017å¹?6æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def foo(n, st):
            return [[i] + x  for i in range(st, int(n ** 0.5) + 1) if n % i == 0 for x in foo(n / i, i)] + [[n]]

        return foo(n, 2)[:-1]


print Solution().getFactors(32)
