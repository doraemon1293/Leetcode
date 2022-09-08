import bisect


class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:

        def get_rank(x):
            rank = 0
            for row in grid:
                rank += bisect.bisect_right(row, x)
            return rank

        M, N = len(grid), len(grid[0])
        left = min([row[0] for row in grid])
        right = max(row[-1] for row in grid)
        while left < right:
            mid = (left + right) // 2
            rank = get_rank(mid)
            if rank < (M * N + 1) // 2:
                left = mid + 1
            else:
                right = mid
        return left
