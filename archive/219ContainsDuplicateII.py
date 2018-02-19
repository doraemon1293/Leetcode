# coding=utf-8
'''
Created on 2016å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        d = {}
        for i, num in enumerate(nums):
            if num in d:
                if abs(i - d[num]) <= k:
                    return True
            d[num] = i
        return False


print Solution().containsNearbyDuplicate([-1, -1], 3)
