# coding=utf-8
'''
Created on 2017å¹?7æœ?3æ—?

@author: Administrator
'''


class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        from collections import deque
        if board == []: return []
        m, n = len(board), len(board[0])
        q = deque([(0, j) for j in xrange(n) if board[0][j] == "O"] + \
                [(m - 1, j) for j in xrange(n) if board[m - 1][j] == "O"] + \
                [(i, 0) for i in xrange(1, m - 1) if board[i][0] == "O"] + \
                [(i, n - 1) for i in xrange(1, m - 1) if board[i][n - 1] == "O"]
                )
        visited = [[False] * n for _ in xrange(m)]
        while q:
            i, j = q.popleft()
            visited[i][j] = True
            if i - 1 >= 0 and board[i - 1][j] == "O" and not visited[i - 1][j]:
                visited[i - 1][j] = True
                q.append((i - 1, j))
            if i + 1 < m and board[i + 1][j] == "O" and not visited[i + 1][j]:
                visited[i + 1][j] = True
                q.append((i + 1, j))
            if j - 1 >= 0 and board[i][j - 1] == "O" and not visited[i][j - 1]:
                visited[i][j - 1] = True
                q.append((i, j - 1))
            if j + 1 < n and board[i][j + 1] == "O" and not visited[i][j + 1]:
                visited[i][j + 1] = True
                q.append((i, j + 1))
        # print visited
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"


board = ["OO", "OO"]
for i in xrange(len(board)):
    board[i] = list(board[i])

Solution().solve(board)
print board
