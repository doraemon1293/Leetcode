# coding=utf-8
'''
Created on 2016å¹?11æœ?15æ—?

@author: Administrator
'''


class Solution(object):

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == "X":
                    temp = ((i - 1) < 0 or board[i - 1][j] == ".") + ((i + 1) >= len(board) or board[i + 1][j] == ".") + \
                    ((j - 1) < 0 or board[i][j - 1] == ".") + ((j + 1) >= len(board[i]) or board[i][j + 1] == ".")
                    ans += (temp - 2) if temp > 2 else 0
        return ans / 2


board = ["X..X", "...X", "...X"]
print Solution().countBattleships(board)
