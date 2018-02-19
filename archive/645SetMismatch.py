# coding=utf-8
'''
Created on 2017å¹?7æœ?23æ—?

@author: Administrator
'''


class Solution(object):

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        ans = [None, None]
        for num in nums:
            if num in s:
                ans[0] = num
            s.add(num)
        ans[1] = (set(range(1, len(nums) + 1)) - s).pop()
        return ans


nums = [1, 2, 2, 4]
print Solution().findErrorNums(nums)
