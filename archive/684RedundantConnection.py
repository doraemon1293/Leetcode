# coding=utf-8
'''
Created on 2017å¹?9æœ?26æ—?

@author: Administrator
'''


class Solution(object):

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        degrees = defaultdict(int)
        nbrs = defaultdict(set)
        for s, t in edges:
            nbrs[s].add(t)
            nbrs[t].add(s)
            degrees[s] += 1
            degrees[t] += 1
        oneDegrees = deque([k for k, v in degrees.items() if v == 1])
        while oneDegrees:
            s = oneDegrees.popleft()
            for t in nbrs[s]:
                degrees[t] -= 1
                nbrs[t].remove(s)
                if degrees[t] == 1:
                    oneDegrees.append(t)
        for s, t in edges[::-1]:
            if degrees[s] > 1 and degrees[t] > 1:
                return [s, t]


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print Solution().findRedundantConnection(edges)
