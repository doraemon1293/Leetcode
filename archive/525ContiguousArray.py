# coding=utf-8
'''
Created on 2017å¹?5æœ?31æ—?

@author: Administrator
'''


class Solution(object):

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {0:-1}
        sub = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i]:
                sub += 1
            else:
                sub -= 1
            d.setdefault(sub, i)
            if sub in d and i - d[sub] > maxi:
                maxi = i - d[sub]
        print d
        return maxi


nums = [0, 0, 1, 0, 0, 0, 1, 1]

print Solution().findMaxLength(nums)

