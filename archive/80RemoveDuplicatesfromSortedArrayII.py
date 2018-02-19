# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            ans = 1
            dup = 1
            i = 1
            while i < len(nums):
                last_num = nums[i - 1]
                if nums[i] == last_num:
                    if dup > 0:
                        dup -= 1
                        i += 1
                    else:
                        del nums[i]
                else:
                    dup = 1
                    i += 1
        return len(nums)


nums = [1, 1, 1, 2, 2, 2, 3]
print Solution().removeDuplicates(nums)
print nums

