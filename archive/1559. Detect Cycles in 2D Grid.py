from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        visited = set()
        circle = set()

        def dfs(x, y, x0, y0):
            visited.add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x1, y1 = x + dx, y + dy
                if (x1, y1) != (x0, y0) and 0 <= x1 < M and 0 <= y1 < N:
                    if (x1, y1) in circle and len(circle) >= 4:
                        return True
                    elif grid[x1][y1] == grid[x][y] and (x1, y1) not in circle:
                        circle.add((x1, y1))
                        if dfs(x1, y1, x, y):
                            return True
                        circle.remove((x1, y1))
            return False

        for x in range(M):
            for y in range(N):
                if (x, y) not in visited:
                    if dfs(x, y, None, None):
                        return True
        return False


grid = [["b", "a", "c"],
        ["c", "a", "c"],
        ["d", "d", "c"],
        ["b", "c", "c"]]
print(Solution().containsCycle(grid))
