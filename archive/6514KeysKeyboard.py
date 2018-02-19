# coding=utf-8
'''
Created on 2017å¹?7æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {}

        def f(N):
            if N <= 6: return N
            if N in d:
                return d[N]
            else:
                d[N] = max([(N - n - 1) * f(b) for b in xrange(N - 3, 0, -1)])
                return d[N]

        return f(N)

        if N <= 15:
            return (0, 1, 2, 3, 4, 5, 6, 9, 12, 16, 20, 27, 36, 48, 64, 81)[N]
        e3 = (4 - N) % 5
        e4 = N // 5 - e3
        return 4 * (4 ** e4) * (3 ** e3)
