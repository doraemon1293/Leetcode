# coding=utf-8
'''
Created on 2017å¹?6æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums) - 1
        while s < e:
            if nums[s] < nums[e]:
                return nums[s]
            mid = (s + e) / 2
            if nums[mid] > nums[s]:
                s = mid + 1
            elif nums[mid] < nums[s]:
                e = mid
            else:
                if nums[mid] > nums[e]:
                    s = mid + 1
                else:
                    e -= 1
        return nums[s]


nums = []
print Solution().findMin(nums)
