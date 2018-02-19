# coding=utf-8
'''
Created on 2016å¹?11æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
