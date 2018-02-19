# coding=utf-8
'''
Created on 2017å¹?6æœ?7æ—?

@author: Administrator
'''
from random import choice


class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ans = 0
        while nums:
            n = nums.pop()
            st = en = n
            while st - 1 in nums:
                st -= 1
                nums.remove(st)
            while en + 1 in nums:
                en += 1
                nums.remove(en)
            ans = max(ans, en - st + 1)
        return ans

