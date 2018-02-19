# coding=utf-8
'''
Created on 2017å¹?1æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = set()
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                ans.add(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return list(ans)

