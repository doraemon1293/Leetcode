# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            # print lo, hi, mid
            if (nums[mid - 1] if mid - 1 >= 0 else -float("inf")) < nums[mid] > (nums[mid + 1] if mid + 1 < len(nums) else -float("inf")):
                return mid
            elif nums[mid] > nums[mid + 1]:
                hi = mid - 1
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1


nums = [1, 2, 3, 1]
print Solution().findPeakElement(nums)
