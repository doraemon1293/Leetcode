# coding=utf-8
'''
Created on 9 Jan 2018

@author: Administrator
'''


class Solution:

    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # da = dict([(x, i) for i, x in enumerate(A)])
        db = dict([(x, i) for i, x in enumerate(B)])
        p = [None] * len(A)
        for i in range(len(A)):
            p[i] = db[A[i]]
        return p


A = [1, 1, 2]
B = [1, 1, 2]
print(Solution().anagramMappings(A, B))
