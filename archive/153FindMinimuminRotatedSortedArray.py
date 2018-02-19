# coding=utf-8
'''
Created on 2016�?12�?22�?

@author: Administrator
'''


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums)
        while s < e:
            if nums[s] < nums[e]:
                return nums[s]
            mid = (s + e) / 2
            if nums[mid] >= nums[s]:
                s = mid + 1
            else:
                e = mid
        return nums[s]
