# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        cur = lower
        for num in nums:
            if num == cur:
                cur += 1
            elif num > cur:
                if num == cur + 1:
                    ans.append(str(cur))
                else:
                    ans.append(str(cur) + "->" + str(num - 1))
                cur = num + 1
        if cur == upper:
            ans.append(str(cur))
        elif cur < upper:
            ans.append(str(cur) + "->" + str(upper))
        return ans


nums = [1, 1, 1]
lower = 1
upper = 1

print Solution().findMissingRanges(nums, lower, upper)
