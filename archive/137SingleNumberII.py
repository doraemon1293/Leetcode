# coding=utf-8
'''
Created on 2017å¹?5æœ?30æ—?

@author: Administrator
'''


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            if i == 31:
                if (count % 3):
                    ans -= (2 ** 31)
            else:
                ans |= (count % 3) << i
        return ans


nums = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
# nums = [1000, 1000, 1000, 1]
print Solution().singleNumber(nums)
