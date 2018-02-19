# coding=utf-8
'''
Created on 2017å¹?6æœ?27æ—?

@author: Administrator
'''


# https://discuss.leetcode.com/topic/67881/single-pass-c-o-n-space-and-time-solution-8-lines-with-detailed-explanation
class Solution(object):

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = -float("inf")
        s = []
        for num in nums[::-1]:
            if num < s3:
                return True
            else:
                while s and num > s[-1]:
                    s3 = max(s3, s.pop())
            s.append(num)
        return False


nums = [1, 0, 1, 4, 3]
print Solution().find132pattern(nums)
