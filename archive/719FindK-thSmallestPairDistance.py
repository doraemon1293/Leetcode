# coding=utf-8
'''
Created on 2017å¹?10æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import bisect

        def numberOfPairsLessThan(nums, mid):
            res = 0
            for i in xrange(len(nums)):
                res += bisect.bisect_right(nums, nums[i] + mid) - i - 1
            return res

        nums.sort()
        lo = float("inf")
        hi = nums[-1] - nums[0]
        for i in xrange(len(nums) - 1):
            lo = min(lo, abs(nums[i] - nums[i + 1]))
        while lo < hi:
            mid = (lo + hi) / 2
            if numberOfPairsLessThan(nums, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
