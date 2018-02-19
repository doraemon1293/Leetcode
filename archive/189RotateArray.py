# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''
from copy import copy


class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
# space O(n)
#         nums_copy = copy(nums)
#         for i in xrange(len(nums)):
#             nums[(i + k) % len(nums)] = nums_copy[i]

# spcae O(1)
#         n = len(nums)
#         k %= n
#         start = cur = 0
#         temp = nums[cur]
#         for _ in xrange(n):
#             cur = (cur - k) % n
#             nums[cur], temp = temp, nums[cur]
#             if cur == start:
#                 start = (start + 1) % n
#                 cur = start
#                 temp = nums[cur]

# space O(1) Reverse
        def reverse(nums, s, e):
            for i in xrange(0, (e - s + 1) / 2):
                nums[s + i], nums[e - i] = nums[e - i], nums[s + i]

        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 2
Solution().rotate(nums, k)
print nums
