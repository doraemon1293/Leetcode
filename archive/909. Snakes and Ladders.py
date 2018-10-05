from collections import deque


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        x, y = m - 1, 0
        inc = 1
        edges = {}
        for i in range(1, m * n + 1):
            if board[x][y] != -1:
                edges[i] = board[x][y]
            y += inc
            if y < 0 or y >= n:
                x -= 1
                y -= inc
                inc *= -1
        print(edges)
        q = deque([(1, 0)])
        visited = {1}
        while q:
            x, steps = q.popleft()
            for i in range(1, 7):
                new_x = edges.get(x + i, x + i)
                if new_x not in visited:
                    q.append((new_x, steps + 1))
                    visited.add(new_x)
                    if new_x == m * n:
                        return steps + 1
        return -1


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]
print(Solution().snakesAndLadders(board))
