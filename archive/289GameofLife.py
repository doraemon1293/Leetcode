# coding=utf-8
'''
Created on 2017å¹?6æœ?7æ—?

@author: Administrator
'''


class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        m, n = len(board), len(board[0])
        for x in xrange(m):
            for y in xrange(n):
                live_nbr = 0
                for xt, yt in [(x + d[0], y + d[1]) for d in delta if 0 <= x + d[0] < m and 0 <= y + d[1] < n]:
                    if board[xt][yt] & 1 == 1:
                        live_nbr += 1
                if board[x][y] & 1 == 1:
                    if live_nbr < 2:
                        board[x][y] &= 1
                    elif 2 <= live_nbr <= 3:
                        board[x][y] |= 2
                    elif live_nbr > 3:
                        board[x][y] &= 1
                elif live_nbr == 3:
                    board[x][y] |= 2
        for x in xrange(m):
            for y in xrange(n):
                board[x][y] >>= 1


board = [[1, 0, 1],
         [0, 1, 0],
         [1, 0, 1]]
Solution().gameOfLife(board)
print board
