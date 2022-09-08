import collections
from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        arr = []
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                arr.append([grid[i][j], i, j])
        arr.sort()
        row_max = collections.defaultdict(int)
        col_max = collections.defaultdict(int)
        new_grid = [[0] * N for _ in range(M)]
        for num, i, j in arr:
            new_num = max(row_max[i], col_max[j]) + 1
            row_max[i] = col_max[j] = new_num
            new_grid[i][j] = new_num
        return new_grid



