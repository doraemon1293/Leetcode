# coding=utf-8
'''
Created on 13 Feb 2018

@author: Administrator
'''


class Solution:

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        visited = {(0, 0)}
        q = [(grid[0][0], 0, 0)]
        ans = 0
        N = len(grid)
        while q:
            elevation, r, c = heapq.heappop(q)
            ans = max(ans, elevation)
            if (r, c) == (N - 1, N - 1):
                return ans
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r0, c0 = r + dx, c + dy
                if 0 <= r0 < N and 0 <= c0 < N and (r0, c0) not in visited:
                    heapq.heappush(q, (grid[r0][c0], r0, c0))
                    visited.add((r0, c0))


grid = [[0, 2], [1, 3]]
print(Solution().swimInWater(grid))
