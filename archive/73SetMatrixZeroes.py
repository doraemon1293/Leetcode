# coding=utf-8
'''
Created on 2017å¹?5æœ?24æ—?

@author: Administrator
'''


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_0 = 0 in matrix[0]
        col_0 = 0 in [x[0] for x in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        if row_0:
            matrix[0] = [0] * len(matrix[0])
        if col_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

