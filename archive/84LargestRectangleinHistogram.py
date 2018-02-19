# coding=utf-8
'''
Created on 2017å¹?9æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            if stack == [] or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                while stack and stack[-1][1] > h:
                    _, top_h = stack.pop()
                    if stack:
                        ans = max(ans, (i - stack[-1][0] - 1) * top_h)
                    else:
                        ans = max(ans, i * top_h)
                stack.append((i, h))
        return ans


heights = [2, 1, 2]
print Solution().largestRectangleArea(heights)
