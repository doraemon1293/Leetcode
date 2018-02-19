# coding=utf-8
'''
Created on 2017å¹?8æœ?29æ—?

@author: Administrator
'''


class Solution(object):

    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lo, hi = 1, m * n + 1
        while lo < hi:
            mid = (lo + hi) / 2
            c = sum([min(mid / i, n) for i in xrange(1, m + 1)])
            if c < k:
                lo = mid + 1
            else:
                hi = mid
        return hi


print Solution().findKthNumber(45, 12, 471)
print Solution().findKthNumber(3, 3, 5)
