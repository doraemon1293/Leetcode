import heapq


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        for x in range(M):
            for y in range(N):
                if grid[x][y] == "S":
                    x0, y0 = x, y
                if grid[x][y] == "B":
                    x1, y1 = x, y
                if grid[x][y] == "T":
                    x2, y2 = x, y

        heap = [(0, x0, y0, x1, y1)]
        visited = set()
        visited.add((x0, y0, x1, y1))
        target = (x2, y2)

        def val(x, y):
            return 0 <= x < M and 0 <= y < N and grid[x][y] != "#"

        while heap:
            steps, x0, y0, x1, y1 = heapq.heappop(heap)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xn, yn = x0 + dx, y0 + dy
                if val(xn, yn):
                    if (xn, yn) == (x1, y1):
                        xn1, yn1 = x1 + dx, y1 + dy
                        if (xn1, yn1) == target:
                            return steps + 1
                        if val(xn1, yn1) and (xn, yn, xn1, yn1) not in visited:
                            heapq.heappush(heap, (steps + 1, xn, yn, xn1, yn1,))
                            visited.add((xn, yn, xn1, yn1))
                    else:
                        if (xn, yn, x1, y1) not in visited:
                            heapq.heappush(heap, (steps, xn, yn, x1, y1))
                            visited.add((xn, yn, x1, y1))
        return -1
