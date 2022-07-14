import math
import itertools
import functools


class Solution(object):
    def maxTrailingZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        @functools.lru_cache(None)
        def foo(x):
            a = b = 0
            x_ = x
            while x_ % 2 == 0:
                x_ //= 2
                a += 1

            x_ = x
            while x_ % 5 == 0:
                x_ //= 5
                b += 1
            return a, b

        M, N = len(grid), len(grid[0])

        grid = [[foo(row[y]) for y in range(len(row))] for row in grid]

        top = [[0] * N for _ in range(M)]
        left = [[0] * N for _ in range(M)]
        for x in range(M):
            two = five = 0
            for y in range(N):
                two += grid[x][y][0]
                five += grid[x][y][1]
                left[x][y] = [two, five]

        for y in range(N):
            two = five = 0
            for x in range(M):
                two += grid[x][y][0]
                five += grid[x][y][1]
                top[x][y] = [two, five]

        if M == 1:
            return min(left[0][N - 1])
        if N == 1:
            return min(top[M - 1][0])

        ans = 0
        for x in range(M):
            for y in range(N):
                two_, five_ = grid[x][y]
                # # whole column
                # two, five = top[M - 1][y]
                # ans = max(ans, min(two, five))
                # # whole row
                # two, five = left[x][N - 1]
                # ans = max(ans, min(two, five))
                # ←↓
                two = top[x][y][0] + left[x][y][0] - two_
                five = top[x][y][1] + left[x][y][1] - five_
                ans = max(ans, min(two, five))

                # ↓→
                two = top[x][y][0] + left[x][N - 1][0] - left[x][y][0]
                five = top[x][y][1] + left[x][N - 1][1] - left[x][y][1]
                ans = max(ans, min(two, five))

                # ↑←
                two = (top[M - 1][y][0] - top[x][y][0]) + left[x][y][0]
                five = (top[M - 1][y][1] - top[x][y][1]) + left[x][y][1]
                ans = max(ans, min(two, five))

                # ↑→
                two = (top[M - 1][y][0] - top[x][y][0]) + (left[x][N - 1][0] - left[x][y][0]) + two_
                five = (top[M - 1][y][1] - top[x][y][1]) + (
                        left[x][N - 1][1] - left[x][y][1]) + five_
                ans = max(ans, min(two, five))
        return ans


