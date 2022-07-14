from typing import List
import collections


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[
        List[int]]:

        q = collections.deque([(start[0], start[1], 0)])
        dist = {(start[0], start[1]): 0}
        M, N = len(grid), len(grid[0])
        ans = []
        if grid[start[0]][start[1]] > 1 and pricing[0] <= grid[start[0]][start[1]] <= pricing[1]:
            ans.append((0, grid[start[0]][start[1]], start[0], start[1]))

        while q:
            x, y, d = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] != 0 and (x1, y1) not in dist:
                    dist[x1, y1] = d + 1
                    q.append((x1, y1, d + 1))
                    if pricing[0] <= grid[x1][y1] <= pricing[1]:
                        ans.append((d + 1, grid[x1][y1], x1, y1))

        ans.sort()
        return [[x[2],x[3]] for x in ans[:k]]