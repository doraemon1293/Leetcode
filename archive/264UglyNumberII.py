# coding=utf-8
'''
Created on 2017å¹?6æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2 = p3 = p5 = 0
        nums = [1]
        for i in xrange(1, n):
            temp = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            nums.append(temp)
            if temp == nums[p2] * 2: p2 += 1
            if temp == nums[p3] * 3: p3 += 1
            if temp == nums[p5] * 5: p5 += 1
        return nums[-1]
