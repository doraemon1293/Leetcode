# coding=utf-8
'''
Created on 2016�?11�?16�?

@author: Administrator
'''


class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output


Solution().productExceptSelf([1, 2, 3, 4])

