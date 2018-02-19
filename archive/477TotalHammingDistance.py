# coding=utf-8
'''
Created on 2017å¹?5æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(x.count("0") * x.count("1") for x in zip(*map(lambda num:bin(num)[2:].zfill(32), nums)))


nums = [4, 14, 2]
print Solution().totalHammingDistance(nums)
