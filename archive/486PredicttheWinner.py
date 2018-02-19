# coding=utf-8
'''
Created on 2017å¹?8æœ?10æ—?

@author: Administrator
'''


class Solution(object):

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def check(nums, left, right, turn):
            if left - right >= summ - left - right:
                return True
            if right - left > summ - left - right:
                return False
            if len(nums) == 0:
                return left >= right
            if turn == 0:  # left's turn
                return check(nums[1:], left + nums[0], right, 1) or check(nums[:-1], left + nums[-1], right, 1)
            else:
                return check(nums[1:], left , right + nums[0], 0) and check(nums[:-1], left, right + nums[-1], 0)

        summ = sum(nums)
        return check(nums, 0, 0, 0)


nums = [1, 5, 233, 7]
nums = [1, 5, 2]
print Solution().PredictTheWinner(nums)

