# coding=utf-8
'''
Created on 2017�?4�?24�?

@author: Administrator
'''


class Solution(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([num for i, num in enumerate(nums) if i % 2 == 0])
