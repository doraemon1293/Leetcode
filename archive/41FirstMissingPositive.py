# coding=utf-8
'''
Created on 2017å¹?6æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 1
        n = len(nums)
        for i in xrange(n):
            while 1 <= nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


nums = [3, 4, -1, 1]
nums = []
nums = [1]
nums = [1, 1]
print Solution().firstMissingPositive(nums)

