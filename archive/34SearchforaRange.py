# coding=utf-8
'''
Created on 2017å¹?3æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def divide_and_conquer(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) / 2
                l_range = divide_and_conquer(lo, mid)
                r_range = divide_and_conquer(mid + 1, hi)
                if l_range == [-1, -1] and r_range == [-1, -1]:
                    return [-1, -1]
                elif l_range == [-1, -1]:
                    return r_range
                elif r_range == [-1, -1]:
                    return l_range
                else:
                    return [l_range[0], r_range[1]]
            return [-1, -1]

        if nums:
            return divide_and_conquer(0, len(nums) - 1)
        else:
            return [-1, -1]


nums = []
print Solution().searchRange(nums, 0)
