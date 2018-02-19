# coding=utf-8
'''
Created on 2017å¹?9æœ?28æ—?

@author: Administrator
'''
from collections import deque


class Solution(object):

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        houses = []
        distance = {}
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 1:
                    houses.append((x, y))
                elif grid[x][y] == 0:
                    distance[(x, y)] = [0, 0]
        for house in houses:
            visited = set()
            q = deque()
            q.append((house, 0))
            while q:
                p, dis = q.popleft()
                x, y = p
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < m and 0 <= y1 < n and (x1, y1) not in visited and grid[x1][y1] == 0:
                        q.append(((x1, y1), dis + 1))
                        distance[(x1, y1)][0] += 1
                        distance[(x1, y1)][1] += dis + 1
                        visited.add((x1, y1))
        return min([v[1] for v in distance.values() if v[0] == len(houses)] or [-1])


grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
print Solution().shortestDistance(grid)

