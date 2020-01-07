import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        M, N = len(grid), len(grid[0])
        visited = set()
        q = collections.deque([[0, 0, 1]])
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while q:
            x, y, length = q.popleft()
            for direction in directions:
                x1, y1 = x + direction[0], y + direction[1]
                if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 0 and (x1, y1) not in visited:
                    q.append([x1, y1, length + 1])
                    visited.add((x1, y1))
                    if (x1, y1) == (N - 1, N - 1):
                        return length + 1
        return -1
