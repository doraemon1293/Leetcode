# coding=utf-8
'''
Created on 2017å¹?7æœ?3æ—?

@author: Administrator
'''


class UnionFInd(object):

    def __init__(self, m, n):
        self.m, self.n = m, n
        self.id = {}
        self.size = {}
        self.islands = 0

    def addPoint(self, point):
        if point not in self.id:
            self.id[point] = point
            self.size[point] = 1
            self.islands += 1
        points = [(point[0] + xt, point[1] + yt) for xt, yt in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)) if 0 <= point[0] + xt < self.m and 0 <= point[1] + yt < self.n and (point[0] + xt, point[1] + yt) in self.id]
        self.union(points)
        return self.islands

    def find(self, point):
        if point in self.id:
            arr = []
            while point != self.id[point]:
                arr.append(point)
                point = self.id[point]
            root = point
            for point in arr:
                self.id[point] = root
            return root

    def union(self, points):
        roots = set([self.find(point) for point in points])
        maxi = 0

        for root in roots:
            if self.size[root] > maxi:
                maxi = self.size[root]
                heaviest_root = root

        for root in roots:
            if self.id[root] != heaviest_root:
                self.size[heaviest_root] += self.size[root]
                self.id[root] = heaviest_root
                del self.size[root]
                self.islands -= 1


class Solution(object):

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        union = UnionFInd(m, n)
        for point in positions:
            ans.append(union.addPoint(tuple(point)))
        return ans


m = 2
n = 2
positions = [[0, 0], [1, 1], [0, 1]]
print Solution().numIslands2(m, n, positions)
