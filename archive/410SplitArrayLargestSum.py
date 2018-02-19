# coding=utf-8
'''
Created on 2017å¹?9æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # Solution 1 DP time complexity(m*n^2)
        # dp[j,m]=min( max(dp[i,m-1],sum[j]-sum[i]) m-1<=i<=j-1 )
#         n = len(nums)
#         temp = 0
#         summ = []
#         for num in nums:
#             temp += num
#             summ.append(temp)
#         dp0 = summ[:]  # åˆ†æˆ1ä»?
#         for mx in xrange(2, m + 1):
#             dp1 = [float("inf")] * n
#             for j in xrange(mx - 1, n):
#                 for i in xrange(mx - 2, j):
#                     dp1[j] = min(dp1[j], max(dp0[i], summ[j] - summ[i]))
#             dp0 = dp1
#         return dp0[n - 1]

        # solution bi-search complexity(mlog(i-lo))
        lo = max(sum(nums) / m, max(nums))
        hi = sum(nums)

        def valid(nums, m, mid):
            summ = 0
            for num in nums:
                if summ + num > mid:
                    summ = num
                    m -= 1
                    if m == 0:
                        return False
                else:
                    summ += num
            return True

        while lo < hi:
            mid = (lo + hi) / 2
            if valid(nums, m, mid):
                hi = mid
            else:
                lo = mid + 1
        return hi


nums = [1, 2, 3, 4, 5]
m = 2
print Solution().splitArray(nums, m)

