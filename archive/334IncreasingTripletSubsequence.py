# coding=utf-8
'''
Created on 2017�?6�?22�?

@author: Administrator
'''


class Solution(object):

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
