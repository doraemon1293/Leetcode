# coding=utf-8
'''
Created on 2017�?6�?26�?

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

