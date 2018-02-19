# coding=utf-8
'''
Created on 2017å¹?4æœ?12æ—?

@author: Administrator
'''


class Solution:

    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]

        def foo(x, y):
            return int(y + x) - int(x + y)

        nums.sort(cmp = foo)
        return "".join(nums).lstrip("0") or "0"


print Solution().largestNumber([3, 30, 34, 5, 9])
