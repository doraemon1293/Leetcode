# coding=utf-8
'''
Created on 2017å¹?2æœ?1æ—?

@author: Administrator
'''


class Solution(object):

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums) - 1):
            if i % 2 == 0 and nums[i] > nums[i + 1] or i % 2 == 1 and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

