from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        ans = []
        for y in range(N):
            for x in range(M):
                nbr_y = y + grid[x][y]
                if nbr_y < 0 or nbr_y >= N or grid[x][y] != grid[x][nbr_y]:
                    y = -1
                    break
                else:
                    y = nbr_y
            # print(x,y)
            ans.append(y)
        return ans




