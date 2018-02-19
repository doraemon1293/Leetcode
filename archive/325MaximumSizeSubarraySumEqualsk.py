# coding=utf-8
'''
Created on 2017å¹?5æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:-1}
        summ = 0
        maxi = 0
        for i in range(len(nums)):
            summ += nums[i]
            d.setdefault(summ, i)
            if (summ - k) in d and i - d[(summ - k)] > maxi:
                maxi = i - d[(summ - k)]
        return maxi
