# coding=utf-8
'''
Created on 2017å¹?9æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Edge(i,j) should be removed if
        # j is a child of another node ( j != root[j] )
        # i and j form a ring ( root[i] == root[j] )
        union = {}
        parent = {}

        def connect(s, t):
            path = []
            union[t] = s
            while t != union[t]:
                path.append(t)
                t = union[t]
            for node in path:
                union[node] = t

        def find(t):
            path = []
            while t != union[t]:
                path.append(t)
                t = union[t]
            for node in path:
                union[node] = t
            return t

        for s, t in edges:
            if t in parent:
                return [s, t]
            parent[t] = s
            union.setdefault(s, s)
            union.setdefault(t, t)
            if find(s) == find(t):
                return [s, t]
            connect(s, t)

