# coding=utf-8
'''
Created on 2017å¹?6æœ?16æ—?

@author: Administrator
'''


class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        steps = [0] * len(nums)
        max_reach = 0
        for i in xrange(0, len(nums)):
            temp = nums[i] + i
            if temp > max_reach:
                for j in xrange(i + 1, min(temp + 1, len(nums))):
                    if steps[j] == 0 or steps[i] + 1 < steps[j]:
                        steps[j] = steps[i] + 1
                max_reach = temp
            print steps, max_reach
            if max_reach >= len(nums) - 1:
                break

        return steps[-1]


nums = [3, 4, 3, 2, 5, 4, 3]
print Solution().jump(nums)
