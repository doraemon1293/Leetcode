# coding=utf-8
'''
Created on 2017å¹?7æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 >= len(nums) or nums[mid] != nums[mid + 1]):
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    lo = mid + 1
                else:
                    hi = mid - 1


nums = [3, 3, 7, 7, 10, 11, 11]
nums = [0]
print Solution().singleNonDuplicate(nums)

