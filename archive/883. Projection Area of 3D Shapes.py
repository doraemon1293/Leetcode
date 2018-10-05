class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(grid[x][y]>0 for x in range(len(grid)) for y in range(len(grid)))+sum([max(x) for x in grid])+sum([max(y) for y in zip(*grid)])
