class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N=len(grid)
        maxRow=[max(row) for row in grid]
        maxCol=[max(col) for col in zip(*grid)]
        return sum([max(min(maxRow[i],maxCol[j])-grid[i][j],0) for i in range(N) for j in range(N)])

grid=[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

print(Solution().maxIncreaseKeepingSkyline(grid))

