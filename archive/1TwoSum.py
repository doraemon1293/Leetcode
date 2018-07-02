# coding=utf-8
'''
Created on 2016�?10�?26�?

@author: Administrator
'''


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in d and i != d[target - nums[i]]:
                return [i, d[target - nums[i]]]


print (Solution().twoSum([2, 7, 11, 15], 9))
