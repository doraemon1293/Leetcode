# coding=utf-8
'''
Created on 2017å¹?5æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        i = 0
        while i < len(nums) and nums[i] == sort_nums[i]:
            i += 1
        j = len(nums) - 1
        while j >= i and nums[j] == sort_nums[j]:
            j -= 1
        return j - i + 1


# nums = [2, 6, 4, 8, 10, 9, 15]
nums = []
print Solution().findUnsortedSubarray(nums)
