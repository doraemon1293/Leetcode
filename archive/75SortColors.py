# coding=utf-8
'''
Created on 2017å¹?6æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i] = nums[zero]
                nums[zero] = 0
                zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[two]
                nums[two] = 2
                two -= 1


nums = [2, 1]
nums = [0, 2, 1]

print Solution().sortColors(nums)

