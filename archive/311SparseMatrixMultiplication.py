# coding=utf-8
'''
Created on 2017å¹?2æœ?13æ—?

@author: Administrator
'''


class Solution(object):

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [ [0] * len(B[0]) for _ in xrange(len(A)) ]
        for i in xrange(len(A)):
            for k in xrange(len(A[0])):
                if A[i][k] != 0:
                    for j in xrange(len(B[0])):
                        if B[k][j] != 0:
                            ans[i][j] += A[i][k] * B[k][j]

        return ans
