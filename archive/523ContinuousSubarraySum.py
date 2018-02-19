# coding=utf-8
'''
Created on 2017å¹?5æœ?24æ—?

@author: Administrator
'''


class Solution(object):

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        summ_dict = {0:-1}
        summ = 0
        for i, num in enumerate(nums):
            summ = (summ + num) % k if k != 0 else summ + num
            # print num, summ, summ_dict
            if summ in summ_dict and i - summ_dict[summ] > 1:
                return True
            summ_dict.setdefault(summ, i)
        return False


nums = [0, 0, 0]
k = 0
print Solution().checkSubarraySum(nums, k)
