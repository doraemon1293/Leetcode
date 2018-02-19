# coding=utf-8
'''
Created on 2017å¹?10æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur_pro = 1
        st = 0
        end = 0
        ans = 0
        while st < len(nums):
            while end < len(nums) and cur_pro * nums[end] < k:
                cur_pro *= nums[end]
                end += 1
            ans += end - st
            cur_pro = max(cur_pro / nums[st], 1)
            st += 1
            end = max(st, end)
        return ans


nums = [1] * 47220
nums[867] = 8
nums[12808] = 6
nums[21913] = 9
nums[24832] = 7
k = 5
nums = [1, 1, 1, 6, 1, 7, 1]
k = 5
# nums = [10, 5, 2, 6]
# k = 100
print Solution().numSubarrayProductLessThanK(nums, k)

