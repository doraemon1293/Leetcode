# coding=utf-8
'''
Created on 2017å¹?5æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        if matrix == []: return []
        delta = [(-1, 1), (1, -1)]
        x = y = 0
        ans = []
        direction = 0
        m, n = len(matrix), len(matrix[0])
        while True:
            ans.append(matrix[x][y])
            if valid(x + delta[direction][0], y + delta[direction][1]):
                x = x + delta[direction][0]
                y = y + delta[direction][1]
            else:
                if direction == 0:
                    if valid(x, y + 1):
                        y += 1
                    elif valid(x + 1, y):
                        x += 1
                    else:
                        return ans
                if direction == 1:
                    if valid(x + 1, y):
                        x += 1
                    elif valid(x, y + 1):
                        y += 1
                    else:
                        return ans
                direction = (direction + 1) % 2


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print Solution().findDiagonalOrder(matrix)

