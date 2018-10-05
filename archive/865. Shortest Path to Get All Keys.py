class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        from collections import deque
        m, n = len(grid), len(grid[0])

        def find_start(grid):
            keys = 0
            for x in range(m):
                for y in range(n):
                    ch = grid[x][y]
                    if ch == "@":
                        start = (x, y)
                    if "a" <= ch <= "f":
                        keys = max(keys, ord(ch) - ord("a") + 1)
            return keys, start

        keys, start = find_start(grid)
        x, y = start
        target = (1 << keys) - 1
        visited = set([(x, y, 0)])
        q = deque([(x, y, 0, 0)])
        while q:
            x, y, cur_keys, step = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                    ch = grid[nx][ny]
                    if "a" <= ch <= "f":
                        nkeys = cur_keys | (1 << (ord(ch) - ord("a")))
                        if (nx, ny, nkeys) not in visited:
                            if nkeys == target:
                                return step + 1
                            visited.add((nx, ny, nkeys))
                            q.append((nx, ny, nkeys, step + 1))
                    elif "A" <= ch <= "F":
                        if (cur_keys >> ord(ch) - ord("A")) & 1:
                            if (nx, ny, cur_keys) not in visited:
                                visited.add((nx, ny, cur_keys))
                                q.append((nx, ny, cur_keys,step+1))
                    else:
                        if (nx, ny, cur_keys) not in visited:
                            visited.add((nx, ny, cur_keys))
                            q.append((nx, ny, cur_keys,step+1))
        return -1

grid=["@.a.#",
      "###.#",
      "b.A.B"]
print(Solution().shortestPathAllKeys(grid))