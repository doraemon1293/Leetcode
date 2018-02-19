# coding=utf-8
'''
Created on 2016å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums)) == len(nums)
