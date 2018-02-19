# coding=utf-8
'''
Created on 2016å¹?12æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in xrange(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                else:
                    ans += k - j
                    j += 1
        return ans


nums = [3, 2, -2, 6, 2, -2, 6, -2, -4, 2, 3, 0, 4, 4, 1]
target = 3
print Solution().threeSumSmaller(nums, target)
