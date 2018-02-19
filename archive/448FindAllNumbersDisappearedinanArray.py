# coding=utf-8
'''
Created on 2017å¹?1æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            num = abs(nums[i]) - 1
            nums[num] = -abs(nums[num])
        return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print Solution().findDisappearedNumbers(nums)
