# coding=utf-8
'''
Created on 2016å¹?12æœ?14æ—?

@author: Administrator
'''
from collections import Counter


class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        for i in xrange(0, len(nums) - 3):
            for j in xrange(i + 1, len(nums) - 2):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    temp = nums[i] + nums[j] + nums[k] + nums[l]
                    if temp > target:
                        l -= 1
                    elif temp < target:
                        k += 1
                    else:
                        ans.add(tuple(sorted(nums[i], nums[j], nums[k], nums[l])))
                        k += 1
                        l -= 1
        return list(ans)

