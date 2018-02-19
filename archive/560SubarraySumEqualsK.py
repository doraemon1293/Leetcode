# coding=utf-8
'''
Created on 2017å¹?5æœ?24æ—?

@author: Administrator
'''
from copy import copy


class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        summ_dict = {0:1}
        summ = 0
        ans = 0
        for num in nums:
            summ += num
            ans += summ_dict.get(summ - k, 0)
            summ_dict.setdefault(summ, 0)
            summ_dict[summ] += 1
        return ans


nums = [1, 1, 1]
k = 2
print Solution().subarraySum(nums, k)

