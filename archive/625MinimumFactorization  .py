# coding=utf-8
'''
Created on 2017å¹?6æœ?18æ—?

@author: Administrator
'''


class Solution(object):

    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a == 1: return 1
        factors = []
        n = 9
        while a != 1 and n >= 2:
            if a % n == 0:
                a /= n
                factors.append(n)
            else:
                n -= 1
        if a != 1: return 0
        factors.reverse()
        ans = int("".join([str(x) for x in factors]))
        if ans > 2 ** 31 - 1:
            return 0
        else:
            return ans


print Solution().smallestFactorization(1)
