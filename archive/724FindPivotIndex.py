# coding=utf-8
'''
Created on 2017å¹?11æœ?12æ—?

@author: Administrator
'''


class Solution(object):

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = [0]
        for num in nums:
            summ.append(summ[-1] + num)
        for i in xrange(len(nums)):
            left = summ[i]
            right = summ[len(nums)] - summ[i + 1]
            if left == right:
                return i
        return -1


nums = [1, 7, 3, 6, 5, 6]
nums = []
print Solution().pivotIndex(nums)
