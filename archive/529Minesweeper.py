# coding=utf-8
'''
Created on 2017å¹?4æœ?18æ—?

@author: Administrator
'''


class Solution(object):

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click
        m = len(board)
        n = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        def reveal(x, y):

            def get_count_of_adj_mines(x, y):
                ans = 0
                for direction in directions:
                    if 0 <= x + direction[0] < m and 0 <= y + direction[1] < n:
                        new_x, new_y = x + direction[0], y + direction[1]
                        if board[new_x][new_y] == "M":
                            ans += 1
                return  ans

            mines = get_count_of_adj_mines(x, y)
            if mines == 0:
                board[x][y] = "B"
                for direction in directions:
                    if 0 <= x + direction[0] < m and 0 <= y + direction[1] < n and board[x + direction[0]][ y + direction[1]] == "E":
                        reveal(x + direction[0], y + direction[1])
            else:
                board[x][y] = str(mines)

        reveal(x, y)
        return board


board = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
click = [3, 0]
print "\n".join(["".join(x) for x in Solution().updateBoard(board, click)])
