# coding=utf-8
'''
Created on 2016�?12�?13�?

@author: Administrator
'''


class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def foo(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return foo(n / 2) + 1
            else:
                return min(foo((n + 1)), foo((n - 1))) + 1

        return foo(n)


print Solution().integerReplacement(3)
