# coding=utf-8
'''
Created on 2017å¹?9æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        ans = 0
        for row in xrange(m):
            for col in xrange(n):
                if matrix[row][col] == "0":
                    heights[col] = 0
                else:
                    heights[col] += 1
            stack = []
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


matrix = ["10100", "10111", "11111", "10010"]
print Solution().maximalRectangle(matrix)

