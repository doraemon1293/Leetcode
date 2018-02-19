# coding=utf-8
'''
Created on 2017å¹?10æœ?8æ—?

@author: Administrator
'''


class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [] or grid[0] == []:
            return 0
        m, n = len(grid), len(grid[0])
        from collections import deque
        self.visited = set()

        def bfs(x, y):
            q = deque([(x, y)])
            res = 1
            self.visited.add((x, y))
            while q:
                x0, y0 = q.popleft()
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    x1, y1 = x0 + dx, y0 + dy
                    if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1 and (x1, y1) not in self.visited:
                        q.append((x1, y1))
                        self.visited.add((x1, y1))
                        res += 1
            return res

        ans = 0
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == 1 and (x, y) not in self.visited:
                    ans = max(ans, bfs(x, y))
        return ans


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
grid = [[1]]

print Solution().maxAreaOfIsland(grid)

