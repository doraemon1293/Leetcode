# coding=utf-8
'''
Created on 2016�?11�?2�?

@author: Administrator
'''


class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums)) == len(nums)
