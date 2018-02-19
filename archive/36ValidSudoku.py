# coding=utf-8
'''
Created on 2016å¹?11æœ?11æ—?

@author: Administrator
'''


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import Counter

        for i in range(9):
            counter_row = Counter(board[i])
            if [[v] for k, v in counter_row.items() if k != '.' and v != 1]:
                return False

        for i in range(9):
            counter_row = Counter([board[j][i] for j in range(9)])
            if [[v] for k, v in counter_row.items() if k != '.' and v != 1]:
                return False
        for i in range(9):
            counter_row = Counter([board[x][y] for x in range(i / 3 * 3, i / 3 * 3 + 3) for y in range(i % 3 * 3, i % 3 * 3 + 3)])
            if [[v] for k, v in counter_row.items() if k != '.' and v != 1]:
                return False
        return True
