# coding=utf-8
'''
Created on 2016å¹?12æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Binary Search
#         if x == 0: return 0
#         if x < 4: return 1
#         lo, hi = 0, x
#         while lo <= hi:
#             mid = (lo + hi) / 2
#             if mid < x / mid:
#                 lo = mid + 1
#             elif mid > x / mid:
#                 hi = mid - 1
#             else:
#                 return mid
#         return hi
        # Newton
        # f(x)=ans^2-x æ±‚f(ans)=0
        # x1=x0-f(x0)/f'(x0)
        if x == 0: return 0
        ans = x
        while ans > x / ans:
            ans = (ans + x / ans) / 2
        return ans


print Solution().mySqrt(0)
