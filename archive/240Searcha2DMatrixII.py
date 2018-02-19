# coding=utf-8
'''
Created on 2016å¹?11æœ?23æ—?

@author: Administrator
'''


# binary search
class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        from bisect import bisect
        for row in matrix:
            i = bisect(row, target)
            print i
            if i - 1 >= 0 and row[i - 1] == target:
                return True
        return False


# o(n+m)
class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

