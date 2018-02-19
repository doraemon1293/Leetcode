# coding=utf-8
'''
Created on 2016å¹?11æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        import operator

        def permutation(m, n):
            return reduce(operator.mul, range(n, n - m, -1))

        if n > 10 :n = 10
        if n == 0: return 1
        return sum([permutation(i, 10) for i in range(1, n + 1)]) - sum([permutation(i, 9) for i in range(1, n)])


print Solution().countNumbersWithUniqueDigits(10)
