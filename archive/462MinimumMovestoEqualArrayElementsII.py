# coding=utf-8
'''
Created on 2016�?11�?21�?

@author: Administrator
'''


class Solution(object):

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            nums.sort()
            m = nums [len(nums) // 2]
            ans = 0
            for num in nums:
                ans += abs(num - m)
            return ans

