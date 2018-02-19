# coding=utf-8
'''
Created on 2016å¹?11æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_a = sum(A)
        f = 0
        for i, a in enumerate(A):
            f += i * a
        max_f = f
        for i in xrange(1, len(A)):
            temp = f - sum_a + A[i - 1] * len(A)
            f = temp
            # print temp, i
            if temp > max_f:
                max_f = temp
        return max_f

