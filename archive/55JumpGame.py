# coding=utf-8
'''
Created on 2017�?3�?7�?

@author: Administrator
'''


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mini_true = len(nums) - 1
        for i in xrange(len(nums) - 1, -1, -1):
            if nums[i] >= (mini_true - i):
                mini_true = i
        return mini_true == 0

