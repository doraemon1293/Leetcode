# coding=utf-8
'''
Created on 2017å¹?11æœ?2æ—?

@author: Administrator
'''
import bisect


class Solution(object):

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans = -float("inf")
        m, n = len(matrix), len(matrix[0])
        if m < n:
            M, N = m, n
        else:
            M, N = n, m
        for x in xrange(M):
            summ = [0] * (N + 1)
            for y in xrange(x, M):
                sumList = [0]
                preSum = 0
                for z in xrange(N):
                    summ[z + 1] += matrix[y][z] if m < n else matrix[z][y]
                    preSum += summ[z + 1]
                    ind = bisect.bisect_left(sumList, preSum - k)
                    if ind != len(sumList):
                        ans = max(ans, preSum - sumList[ind])
                    bisect.insort(sumList, preSum)
        return ans if ans != float("-inf") else 0


matrix = [[1, 0, 1],
          [0, -2, 3]]
k = 2
print Solution().maxSumSubmatrix(matrix, k)
