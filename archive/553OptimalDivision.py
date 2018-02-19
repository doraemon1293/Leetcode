# coding=utf-8
'''
Created on 2017å¹?4æœ?18æ—?

@author: Administrator
'''


# The expression A[0] / ( A[1] / A[2] / ... / A[N-1] ) has every element in the numerator except A[1], and it is impossible for A[1] to be in the numerator,
class Solution(object):

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        if len(nums) <= 2:
            return "/".join(nums)
        else:
            return nums[0] + "/(" + "/".join(nums[1:]) + ")"

