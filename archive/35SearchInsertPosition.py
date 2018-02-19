# coding=utf-8
'''
Created on 2017å¹?1æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        st, en = 0, len(nums) - 1
        while st < en:
            mid = (st + en) / 2
            if nums[mid] > target:
                en = mid - 1
            elif nums[mid] < target:
                st = mid + 1
            else:
                return mid
        if nums[st] < target:
            st += 1
        return st


nums = [1, 1.5]
target = 0
print Solution().searchInsert(nums, target)
