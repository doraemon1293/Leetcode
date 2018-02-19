# coding=utf-8
'''
Created on 2016å¹?12æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_delta = float("inf")
        nums.sort()
        for i in xrange(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if abs(nums[i] + nums[j] + nums[k] - target) < min_delta:
                    min_delta = abs(nums[i] + nums[j] + nums[k] - target)
                    ans = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] - target > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] - target < 0:
                    j += 1
                else:
                    return ans
        return ans


nums = [1, 1, 1, 0]
target = 100
print Solution().threeSumClosest(nums, target)

