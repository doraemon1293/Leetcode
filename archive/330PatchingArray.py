# coding=utf-8
'''
Created on 2017å¹?6æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        reach = 0
        i = 0
        added = 0
        while reach < n:
            if i < len(nums) and reach + 1 >= nums[i]:
                reach += nums[i]
                i += 1
            else:
                added += 1
                reach += reach + 1
        return added


nums = [1, 3]
n = 6
nums = [1, 5, 10]
n = 20
nums = []
n = 50
print Solution().minPatches(nums, n)
