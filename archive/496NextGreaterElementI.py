# coding=utf-8
'''
Created on 2017å¹?2æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        d = {}
        for num in nums:
            while s != [] and s[-1] < num:
                x = s.pop()
                d[x] = num
            s.append(num)
        return [d.get(num, -1) for num in findNums]


findNums = [4, 1, 2]
nums = [1, 3, 4, 2]
print Solution().nextGreaterElement(findNums, nums)
