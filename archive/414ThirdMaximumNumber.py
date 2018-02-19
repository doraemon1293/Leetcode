# coding=utf-8
'''
Created on 2016å¹?11æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            import bisect
            temp_list = []
            for x in nums:
                if len(temp_list) < 3:
                    bisect.insort(temp_list, x)
                else:
                    bisect.insort(temp_list, x)
                    del temp_list[0]
            return temp_list[0]

