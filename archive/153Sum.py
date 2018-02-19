# coding=utf-8
'''
Created on 2016å¹?12æœ?14æ—?

@author: Administrator
'''
from collections import Counter


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freqs = Counter(nums)
        ans = set()
        for i in freqs:
            freqs[i] -= 1
            for j in freqs:
                if freqs[j] > 0:
                    freqs[j] -= 1
                    if freqs.get(-(i + j), 0) != 0:
                        ans.add(tuple(sorted([i, j, -(i + j)])))
                    freqs[j] += 1
            freqs[i] += 1
        return list(ans)


nums = [-1, 0, 1, 2, -1, -4]
print Solution().threeSum(nums)

