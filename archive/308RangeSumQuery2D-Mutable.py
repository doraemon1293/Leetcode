# coding=utf-8
'''
Created on 2017å¹?11æœ?7æ—?

@author: Administrator
'''

# coding=utf-8
'''
Created on 2017å¹?8æœ?18æ—?

@author: Administrator
'''


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        if self.m == 0: return
        self.n = len(matrix[0])
        self.matrix = [[0] * self.n for _ in xrange(self.m)]
        self.tree = [[0] * (self.n + 1) for _ in xrange(self.m + 1)]
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += (j & -j)
            i += (i & -i)
        self.matrix[row][col] = val

    def sum(self, row, col):
        res = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                res += self.tree[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum(row2 + 1, col2 + 1) + self.sum(row1, col1) - \
               self.sum(row1, col2 + 1) - self.sum(row2 + 1, col1)

