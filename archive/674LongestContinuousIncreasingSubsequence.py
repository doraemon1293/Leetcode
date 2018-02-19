# coding=utf-8
'''
Created on 2017å¹?9æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        ans = 1
        temp = 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 1
        ans = max(temp, ans)
        return ans


nums = [1, 3, 5, 7]
# nums = [2, 2, 2]
print Solution().findLengthOfLCIS(nums)
