# coding=utf-8
'''
Created on 2016�?11�?3�?

@author: Administrator
'''


class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)


nums = [3, 2, 2, 3]
val = 3
print Solution().removeElement(nums, val)
print nums
