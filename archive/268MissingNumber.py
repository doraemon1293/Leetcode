# coding=utf-8
'''
Created on 2016�?11�?17�?

@author: Administrator
'''


class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) + 1) * len(nums) / 2 - sum(nums)


nums = [0]
print Solution().missingNumber(nums)
