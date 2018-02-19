# coding=utf-8
'''
Created on 2017å¹?7æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix[0] == []: return False
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo > hi: return False
        lo, hi = 0, len(matrix[row]) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo > hi: return False
