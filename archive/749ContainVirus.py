# coding=utf-8
'''
Created on 18 Dec 2017

@author: Administrator
'''


class Solution(object):

    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m = len(grid)
        n = len(grid[0])

        def solve(x, y):
            willAffect = set()
            affected = [(x, y)]
            grid[x][y] = circles + 1
            walls = 0
            q = deque([(x, y)])
            while q:
                x0, y0 = q.popleft()
                grid[x0][y0] = circles + 1
                for x1, y1 in ((x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1)):
                    if 0 <= x1 < m and 0 <= y1 < n:
                        if grid[x1][y1] == 0:
                            walls += 1
                            willAffect.add((x1, y1))
                        elif grid[x1][y1] == circles:
                            grid[x1][y1] = circles + 1
                            affected.append((x1, y1))
                            q.append((x1, y1))
#             print(circles)
#             for x in grid:
#                 print(x)
            return affected, willAffect, walls

        ans = 0
        circles = 0
        while True:
            circles += 1
            maxWillAffect = -float("inf")
            willAffectArr = []
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == circles:
                        affected, willAffect, walls = solve(x, y)
                        willAffectArr.append(willAffect)
                        if len(willAffect) > maxWillAffect:
                            willInsolated = affected
                            maxWillAffect = len(willAffect)
                            addingWalls = walls
                            ind = len(willAffectArr) - 1

            if willAffectArr == []:
                break
            else:
                ans += addingWalls
                for i in range(len(willAffectArr)):
                    if i != ind:
                        for x, y in willAffectArr[i]:
                            grid[x][y] = circles + 1
                for x, y in willInsolated:
                    grid[x][y] *= -1
#                 print()
#                 for x in grid:
#                     print(x)
        return ans


grid = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1, 1, 1, 1, 1],
 [1, 1, 1, 0, 0, 0, 0, 0, 0]]
print(Solution().containVirus(grid))
