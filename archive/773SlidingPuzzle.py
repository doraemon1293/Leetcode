

class Solution:

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        from copy import deepcopy
        from collections import deque

        def toStr(board):
            return "".join([str(x) for x in (board[0] + board[1])])

        if toStr(board) == "123450": return 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    x0, y0 = i, j
                    break

        q = deque()
        q.append([board, 0, x0, y0])
        visited = set(toStr(board))
        while q:
            temp = q.popleft()
            step, x0, y0 = temp[1], temp[2], temp[3]
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                state = deepcopy(temp[0])
                x1, y1 = x0 + dx, y0 + dy
                if 0 <= x1 < 2 and 0 <= y1 < 3:
                    state[x0][y0], state[x1][y1] = state[x1][y1], state[x0][y0]
                    s = toStr(state)
                    if s == "123450": return step + 1
                    if s not in visited:
                        visited.add(s)
                        q.append([state, step + 1, x1, y1])
        return -1


board = [[3, 2, 4], [1, 5, 0]]
# board = [[1, 2, 3], [4, 0, 5]]
board = [[1, 2, 3], [5, 4, 0]]
print(Solution().slidingPuzzle(board))
