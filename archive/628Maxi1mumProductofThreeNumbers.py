# coding=utf-8
'''
Created on 2017å¹?6æœ?26æ—?

@author: Administrator
'''


# coding=utf-8
class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

