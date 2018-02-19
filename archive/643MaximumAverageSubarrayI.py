# coding=utf-8
'''
Created on 2017å¹?7æœ?16æ—?

@author: Administrator
'''
from Tkconstants import SOLID


class Solution(object):

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        summ = [0]
        for num in nums:
            summ.append(summ[-1] + num)
        ans = -float("inf")
        for i in xrange(len(summ) - 1, k - 1, -1):
            ans = max(ans, (float(summ[i]) - summ[i - k]) / k)
        return ans


nums = [1, 12, -5, -6, 50, 3]
k = 4
print Solution().findMaxAverage(nums, k)
