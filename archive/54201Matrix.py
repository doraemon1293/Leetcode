# coding=utf-8
'''
Created on 2017å¹?6æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        ans = [[float("inf")] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1 if i - 1 >= 0 else float("inf"), ans[i][j - 1] + 1 if j - 1 >= 0 else float("inf"))
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1 if i + 1 < m else float("inf"), ans[i][j + 1] + 1 if j + 1 < n else float("inf"))
        return ans


matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print Solution().updateMatrix(matrix)
