# coding=utf-8
'''
Created on 2016å¹?12æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            temp_sum = max(num, temp_sum + num)
            ans = max(ans, temp_sum)
        return ans

