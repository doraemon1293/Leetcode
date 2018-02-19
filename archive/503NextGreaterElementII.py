# coding=utf-8
'''
Created on 2017å¹?2æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        ans = [-1] * len(nums)
        for i in range(len(nums) * 2):
            num = nums[i % len(nums)]
            while s != [] and s[-1][1] < num:
                ans[s.pop()[0]] = num
            if i < len(nums):
                s.append((i, num))

        return ans


nums = [1, 2, 1]
print Solution().nextGreaterElements(nums)

