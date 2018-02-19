# coding=utf-8
'''
Created on 2017å¹?3æœ?7æ—?

@author: Administrator
'''
from collections import Counter


class Solution(object):

    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        if k == 0:
            counter = Counter(nums)
            return len([x for x in counter.values() if x > 1])
        if k > 0:
            nums_set = set(nums)
            ans = set()
            for num in nums_set:
                if num - k in nums_set:
                    ans.add((num - k, num))
                if num + k in nums_set:
                    ans.add((num, num + k))
            return len(ans)

