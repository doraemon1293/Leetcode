# coding=utf-8
'''
Created on 2016�?11�?7�?

@author: Administrator
'''


class Solution(object):

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
