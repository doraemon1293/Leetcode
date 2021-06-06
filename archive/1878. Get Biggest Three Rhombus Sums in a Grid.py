from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        ans = []
        for x in range(M):
            for y in range(N):
                summ = grid[x][y]
                ans.append(summ)
                length = 1
                while x - length >= 0 and x + length < M and y - length >= 0 and y + length < N:
                    summ = 0
                    for i in range(length + 1):
                        j = length - i
                        for dx, dy in set([(i, j), (i, -j), (-i, j), (-i, -j)]):
                            # print(x,y,length,x+dx,y+dy)
                            summ += grid[x + dx][y + dy]
                    ans.append(summ)
                    length += 1
        ans = sorted(set(ans), reverse=True)[:3]
        return ans