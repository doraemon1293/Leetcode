# coding=utf-8
'''
Created on 2017å¹?6æœ?6æ—?

@author: Administrator
'''


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix:
            m, n = len(matrix), len(matrix[0])
            self.summ = [[0] * n for _ in xrange(m)]
            print self.summ
            self.summ[0][0] = matrix[0][0]
            for i in xrange(1, n):
                self.summ[0][i] = self.summ[0][i - 1] + matrix[0][i]
            for i in xrange(1, m):
                self.summ[i][0] = self.summ[i - 1][0] + matrix[i][0]
            for i in xrange(1, m):
                for j in xrange(1, n):
                    self.summ[i][j] = matrix[i][j] + self.summ[i][j - 1] + self.summ[i - 1][j] - self.summ[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1 -= 1
        col1 -= 1
        return self.summ[row2][col2] - (self.summ[row1][col2] if row1 >= 0 else 0) - (self.summ[row2][col1] if col1 >= 0 else 0) + (self.summ[row1][col1] if row1 >= 0 and col1 >= 0 else 0)


matrix = [[-1]]
row1, col1, row2, col2 = 0, 0, 0, 0
numMatrix = NumMatrix(matrix)
for x in numMatrix.summ:
    print x
print numMatrix.sumRegion(row1, col1, row2, col2)
# for row1, col1, row2, col2 in [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]:
#     print numMatrix.sumRegion(row1, col1, row2, col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
