# coding=utf-8
'''
Created on 2017å¹?8æœ?20æ—?

@author: Administrator
'''


class Solution(object):

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        arr = [[0] * len(M[0]) for _ in xrange(len(M))]
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                temp = [M[i + dir[0]][j + dir[1]] for dir in dirs if 0 <= i + dir[0] < len(M) and 0 <= j + dir[1] < len(M[0])]
                arr[i][j] = sum(temp) / len(temp)
        return arr


M = [[1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]
print Solution().imageSmoother(M)
