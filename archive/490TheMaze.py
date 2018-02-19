# coding=utf-8
'''
Created on 2017å¹?5æœ?22æ—?

@author: Administrator
'''
from copy import copy


class Solution(object):

    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        from collections import deque
        x, y = start
        m, n = len(maze), len(maze[0])
        visited = set((x, y))
        q = deque([(x, y)])

        while q:
            x, y = q.popleft()
            # up
            x0, y0 = x, y
            while x0 - 1 >= 0 and maze[x0 - 1][y0] != 1:
                x0 -= 1
            if (x0, y0) not in visited:
                if [x0, y0] == destination: return True
                visited.add((x0, y0))
                q.append((x0, y0))
            # down
            x0, y0 = x, y
            while x0 + 1 < m and maze[x0 + 1][y0] != 1:
                x0 += 1
            if (x0, y0) not in visited:
                if [x0, y0] == destination: return True
                visited.add((x0, y0))
                q.append((x0, y0))
            # left
            x0, y0 = x, y
            while y0 - 1 >= 0 and maze[x0][y0 - 1] != 1:
                y0 -= 1
            if (x0, y0) not in visited:
                if [x0, y0] == destination: return True
                visited.add((x0, y0))
                q.append((x0, y0))
            # right
            x0, y0 = x, y
            while y0 + 1 < n and maze[x0][y0 + 1] != 1:
                y0 += 1
            if (x0, y0) not in visited:
                if [x0, y0] == destination: return True
                visited.add((x0, y0))
                q.append((x0, y0))
        return False

