# coding=utf-8
'''
Created on 2016å¹?10æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x ** n

        # x^n=(x^2)^(n/2)*(x if n is odd else 1)

        # iterative
#         if n < 0:
#             x = 1 / x
#             n = -n
#         ans = 1
#         while n:
#             if n % 2 == 1:
#                 ans *= x
#             x *= x
#             n /= 2
#         return ans

        # recursive
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0: return 1
        return self.myPow(x * x, n / 2) if n % 2 == 0 else x * self.myPow(x * x, n / 2)


print Solution().myPow(3.13, 10)
