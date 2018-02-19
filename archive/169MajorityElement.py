# coding=utf-8
'''
Created on 2016å¹?10æœ?27æ—?

@author: Administrator
'''


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         from collections import Counter
#         c = Counter(nums)
#         return c.most_common(1)[0][0]

        # Boyer-Moore Majority Vote algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count > len(nums) / 2:
            return candidate


print Solution().majorityElement([1])
