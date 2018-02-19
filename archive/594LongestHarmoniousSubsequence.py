# coding=utf-8
'''
Created on 2017å¹?5æœ?21æ—?

@author: Administrator
'''


class Solution(object):

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        ans = 0
        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])
            if num - 1 in count:
                ans = max(ans, count[num] + count[num - 1])
        return ans

