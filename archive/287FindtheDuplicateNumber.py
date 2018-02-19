# coding=utf-8
'''
Created on 2016å¹?12æœ?19æ—?

@author: Administrator
'''


class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# O(n) explaination http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
#         # The "tortoise and hare" step.  We start at the end of the array and try
#         # to find an intersection point in the cycle.
#         slow = 0
#         fast = 0
#
#         # Keep advancing 'slow' by one step and 'fast' by two steps until they
#         # meet inside the loop.
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#
#             if slow == fast:
#                 break
#
#         # Start up another pointer from the end of the array and march it forward
#         # until it hits the pointer inside the array.
#         finder = 0
#         while True:
#             slow   = nums[slow]
#             finder = nums[finder]
#
#             # If the two hit, the intersection index is the duplicate element.
#             if slow == finder:
#                 return slow

        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            temp = len([x for x in nums if x <= mid])
            if temp <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo


nums = [1, 1, 3]
print Solution().findDuplicate(nums)
