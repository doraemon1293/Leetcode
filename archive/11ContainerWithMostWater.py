# coding=utf-8
'''
Created on 2016å¹?12æœ?14æ—?

@author: Administrator
'''


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            h = min(height[i], height[j])
            if h * (j - i) > ans:
                ans = h * (j - i)
            while height[i] <= h and i < j: i += 1
            while height[j] <= h and i < j: j -= 1
        return ans
