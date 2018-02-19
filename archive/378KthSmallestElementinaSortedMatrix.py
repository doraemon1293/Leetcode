# coding=utf-8
'''
Created on 2016�?11�?17�?

@author: Administrator
'''


class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from itertools import chain
        import heapq

        arr = list(chain(matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix))))
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)[-1]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print (Solution().kthSmallest(matrix, k))
