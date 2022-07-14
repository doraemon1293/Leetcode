from typing import List
import collections
import functools


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        # print(M,N)
        fired = [[float("inf")] * N for i in range(M)]
        q = collections.deque()
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    fired[x][y] = 0
                    q.append((x, y, 0))
        while q:
            x, y, t = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 0:
                    if fired[x1][y1] == float("inf"):
                        fired[x1][y1] = t + 1
                        q.append((x1, y1, t + 1))
        # for row in fired:
        #     print(row)

        @functools.lru_cache(None)
        def go(wait_minutes):
            q = collections.deque([(0, 0, wait_minutes)])
            visited={(0,0)}
            while q:
                x, y, t = q.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 0:
                        if (x1, y1) == (M - 1, N - 1) and t + 1 <= fired[M - 1][N - 1]:
                            return True
                        if fired[x1][y1] > t + 1 and (x1,y1) not in visited:
                            visited.add((x1,y1))
                            q.append((x1, y1, t + 1))
            return False

        if go(0) == False:
            return -1
        if fired[0][0] == fired[M - 1][N - 1] == float("inf") and go(0):
            return 10 ** 9

        lo, hi = 0, min(fired[0][0], fired[M - 1][N - 1]) + 1
        ans = -float("inf")
        while lo <= hi:
            # print(lo,hi)
            mid = (lo + hi) // 2
            if go(mid):
                ans = max(ans, mid)
                lo = mid + 1
            else:
                hi = mid - 1

        return ans