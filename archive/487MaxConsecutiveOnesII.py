# coding=utf-8
'''
Created on 2017å¹?5æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        before = 0
        for i, num in enumerate(nums):
            if num:
                if i == len(nums) - 1: return len(nums)
                before += 1
            else:
                break
        after = 0
        for num in nums[i + 1:]:
            if num:
                after += 1
            else:
                ans = max(ans, before + after + 1)
                before = after
                after = 0
        ans = max(ans, before + after + 1)
        return ans


nums = [0]

print Solution().findMaxConsecutiveOnes(nums)

