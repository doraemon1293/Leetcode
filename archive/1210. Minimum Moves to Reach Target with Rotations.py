import collections


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def validate1(x1, y1, x2, y2):
            for x in (x1, y1, x2, y2):
                if x < 0 or x >= n:
                    return False
            return grid[x1][y1] == 0 and grid[x2][y2] == 0



        def validate(x1, y1, x2, y2):
            for x in (x1, y1, x2, y2):
                if x < 0 or x >= n:
                    return False
            return grid[x1][y1] == 0 and grid[x2][y2] == 0 and ((x1, y1, x2, y2) not in visited)

        n = len(grid)
        visited = set()
        visited.add((0, 0, 0, 1))
        q = collections.deque([(0, 0, 0, 1, 0)])
        while q:
            x1, y1, x2, y2, steps = q.popleft()
            if (x1, y1, x2, y2) == (n - 1, n - 2, n - 1, n - 1):
                return steps
            # right
            nx1, nx2, ny1, ny2 = x1, y1 + 1, x2, y2 + 1
            if validate(nx1, nx2, ny1, ny2):
                q.append((nx1, nx2, ny1, ny2, steps + 1))
                visited.add((nx1, nx2, ny1, ny2))
            # down
            nx1, nx2, ny1, ny2 = x1 + 1, y1, x2 + 1, y2
            if validate(nx1, nx2, ny1, ny2):
                q.append((nx1, nx2, ny1, ny2, steps + 1))
                visited.add((nx1, nx2, ny1, ny2))
            # clockwise
            if x1 == x2 and y1 + 1 == y2:
                nx1, nx2, ny1, ny2 = x1, y1, x1 + 1, y1
                if validate1(x1+1,y1,x2+1,y2) and validate(nx1, nx2, ny1, ny2):
                    q.append((nx1, nx2, ny1, ny2, steps + 1))
                    visited.add((nx1, nx2, ny1, ny2))
            # anti clock
            if x1 + 1 == x2 and y1 == y2:
                nx1, nx2, ny1, ny2 = x1, y1, x1, y1 + 1
                if validate1(x1,y1+1,x2,y2+1) and validate(nx1, nx2, ny1, ny2):
                    q.append((nx1, nx2, ny1, ny2, steps + 1))
                    visited.add((nx1, nx2, ny1, ny2))
            print(q)
        return -1
