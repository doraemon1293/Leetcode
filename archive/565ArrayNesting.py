# coding=utf-8
'''
Created on 2017å¹?5æœ?28æ—?

@author: Administrator
'''


class Solution(object):

    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        maxi = 0
        for i, num in enumerate(nums):
            if i not in visited:
                start = i
                next = num
                cur = 1
                visited.add(start)
                while next != start:
                    next = nums[next]
                    cur += 1
                    visited.add(next)
                if cur > maxi:
                    maxi = cur
        return maxi


nums = [5, 4, 0, 3, 1, 6, 2]
print Solution().arrayNesting(nums)

