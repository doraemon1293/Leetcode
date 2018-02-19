# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Union Find
        if n == 0 or len(edges) != n - 1: return False
        parents = range(n)
        for a, b in edges:
            while a != parents[a]: a = parents[a]
            while b != parents[b]: b = parents[b]
            if a != b:  # a!=b means onr set will be deleted
                parents[b] = a
                n -= 1
        return n == 1


n = 4
edges = [[0, 1], [2, 3], [1, 2]]
print Solution().validTree(n, edges)
