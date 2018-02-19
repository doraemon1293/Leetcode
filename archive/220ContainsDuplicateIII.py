# coding=utf-8
'''
Created on 2016å¹?11æœ?2æ—?

@author: Administrator
'''


class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        d = {}
        for i, num in enumerate(nums):
            bucket = num / t if t else num
            for temp in (bucket - 1, bucket, bucket + 1):
                if temp in d:
                    if abs(d[temp][0] - i) <= k and abs(d[temp][1] - num) <= t:
                        return True
            d[bucket] = (i, num)
        return False


print Solution().containsNearbyAlmostDuplicate([0], 0, 0)
