# coding=utf-8
'''
Created on 2016å¹?10æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            t1 = max(nums[0], nums[1])
            t2 = nums[0]
        for i in range(3, n + 1):
            ans = max(t1, t2 + nums[i - 1])
            t2 = t1
            t1 = ans
        return ans

