# coding=utf-8
'''
Created on 2017å¹?7æœ?5æ—?

@author: Administrator
'''


class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 0 or n == 1: return 0
        nbr = [set() for _ in xrange(n)]
        for a, b in edges:
            nbr[a].add(b)
            nbr[b].add(a)
        leaves = [i for i in xrange(n) if len(nbr[i]) == 1]
        while n > 2:
            newLeaves = []
            for leave in leaves:
                newLeave = nbr[leave].pop()
                nbr[newLeave].remove(leave)
                if len(nbr[newLeave]) == 1:
                    newLeaves.append(newLeave)
            n -= len(leaves)
            leaves = newLeaves
        return leaves


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
print Solution().findMinHeightTrees(n, edges)
