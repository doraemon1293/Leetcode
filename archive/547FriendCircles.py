# coding=utf-8
'''
Created on 2017�?5�?9�?

@author: Administrator
'''


class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.root = {}

        def union(a, b):
            self.root[find(b)] = find(a)

        def find(a):
            if a not in self.root:
                self.root[a] = a
            x = a
            path = []
            while x != self.root[x]:
                path.append(x)
                x = self.root[x]
            for node in path:
                self.root[node] = x
            return x

        N = len(M)

        for x in range(N):
            for y in range(N):
                if M[x][y]:
                    union(x, y)

        return len(set([find(x) for x in range(N)]))


M = [[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]]
print(Solution().findCircleNum(M))
