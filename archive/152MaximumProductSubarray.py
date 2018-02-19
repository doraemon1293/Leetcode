# coding=utf-8
'''
Created on 2017å¹?2æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = maxi = mini = nums[0]
        for num in nums[1:]:
            new_maxi, new_mini = maxi, mini
            new_maxi = max(maxi * num, mini * num, num)
            new_mini = min(maxi * num, mini * num, num)
            maxi, mini = new_maxi, new_mini
            ans = max(maxi, ans)
        return ans


nums = [-4, -3, -2]
print Solution().maxProduct(nums)

