# coding=utf-8
'''
Created on 2017å¹?8æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """

        # 1+x+...+x^m=n => x<n^(1/m)
        # 1+x+...+x^m=n<(1+x)^m => n^(1/m)-1<x
        # so x=int(n^(1/m))
        # m<=log(n,2)
        import math
        n = int(n)
        for m in xrange(int(math.log(n, 2)), 1, -1):
            x = int(n ** (1.0 / m))
            if (x ** (m + 1) - 1) / (x - 1) == n:
                return str(x)
        return str(n - 1)


n = "14919921443713777"
print Solution().smallestGoodBase(n)

