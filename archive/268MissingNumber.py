# coding=utf-8
'''
Created on 2016å¹?11æœ?17æ—?

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
