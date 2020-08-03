from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0
        for row in range(N-1):
            if 1 in grid[row][row+1:]:
                flag = False
                for r in range(row + 1, N):
                    if 1 not in grid[r][row + 1:]:
                        ans += r - row
                        flag = True
                        grid[row:r + 1] = [grid[r]] + grid[row:r]
                        break
                if flag == False:
                    return -1
        return ans