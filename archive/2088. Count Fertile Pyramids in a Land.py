import bisect
from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        grid_range = []
        for x in range(M):
            row = []
            left = None
            for y in range(N):
                if grid[x][y]:
                    if left == None:
                        left = right = y
                    else:
                        right = y
                else:
                    if left is not None and right is not None:
                        row.append((left, right))
                        left = right = None
            if left is not None and right is not None:
                row.append((left, right))
                left = right = None
            grid_range.append(row)

        ans = 0

        def in_range(row, left, right):
            ind = bisect.bisect_right(row, (left, float("inf"))) - 1
            # print(row,left,right,ind)
            if ind >= 0:
                if row[ind][0] <= left <= right <= row[ind][1]:
                    return True
            return False

        for x in range(M):
            for y in range(N):
                if grid[x][y]:
                    # downwards
                    left, right = y - 1, y + 1
                    line = x + 1
                    while left >= 0 and right < N and line < M and in_range(grid_range[line], left, right):
                        ans += 1
                        line += 1
                        left -= 1
                        right += 1
                    # print(x, y, line)

                    # upwards
                    left, right = y - 1, y + 1
                    line = x - 1
                    while left >= 0 and right < N and line >= 0 and in_range(grid_range[line], left, right):
                        ans += 1
                        line -= 1
                        left -= 1
                        right += 1
                    # print(x,y,line)
        return ans
grid = [[0,1,1,0],[1,1,1,1]]

print(Solution().countPyramids(grid))