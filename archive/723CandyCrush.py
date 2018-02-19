# coding=utf-8
'''
Created on 2017å¹?11æœ?6æ—?

@author: Administrator
'''


class Solution(object):

    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        elimateing = {1}
        while elimateing:
            elimateing = set()
            for x in xrange(m):
                for y in xrange(n):
                    if board[x][y] != 0:
                        if 0 < x < m - 1:
                            if board[x - 1][y] == board[x][y] == board[x + 1][y]:
                                elimateing.add((x - 1, y))
                                elimateing.add((x, y))
                                elimateing.add((x + 1, y))
                        if 0 < y < n - 1:
                            if board[x][y - 1] == board[x][y] == board[x][y + 1]:
                                elimateing.add((x, y - 1))
                                elimateing.add((x, y))
                                elimateing.add((x, y + 1))
            if elimateing:
                for x, y in elimateing:
                    board[x][y] = 0

                for y in xrange(n):
                    arr = [board[x][y] for x in xrange(m)if board[x][y] != 0]
                    arr = [0] * (m - len(arr)) + arr
                    for i in xrange(m):
                        board[i][y] = arr[i]
#             for x in board:
#                 print x
#             print elimateing
        return board


board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]
print Solution().candyCrush(board)
