# coding=utf-8
'''
Created on 2017å¹?2æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        from collections import defaultdict

        last_sums = defaultdict(int)
        last_sums[0] = 1
        for num in nums:
            sums = defaultdict(int)
            for k, v in last_sums.items():
                sums[k + num] += v
                sums[k - num] += v
            last_sums = sums

        return sums[S]


nums = [1, 1, 1, 1, 1]
S = 3
print Solution().findTargetSumWays(nums, S)
