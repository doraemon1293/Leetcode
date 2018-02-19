# coding=utf-8
'''
Created on 2017å¹?9æœ?22æ—?

@author: Administrator
'''


class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rowSet = [set(range(1, 10)) for _ in xrange(9)]
        colSet = [set(range(1, 10)) for _ in xrange(9)]
        groupSet = [set(range(1, 10)) for _ in xrange(9)]

        def get_group(i, j):
            return i / 3 * 3 + j / 3

        filling = []
        for x in xrange(9):
            for y in xrange(9):
                if board[x][y] != ".":
                    num = int(board[x][y])
                    rowSet[x].remove(num)
                    colSet[y].remove(num)
                    groupSet[get_group(x, y)].remove(num)
                else:
                    filling.append((x, y))

        def dfs(ind):
            if ind == len(filling):
                return True
            x, y = filling[ind]
            valid = rowSet[x] & colSet[y] & groupSet[(get_group(x, y))]
            for num in valid:
                # fill num in x,y
                board[x][y] = str(num)
                rowSet[x].remove(num)
                colSet[y].remove(num)
                groupSet[(get_group(x, y))].remove(num)
                if dfs(ind + 1):
                    return True
                # unfill num in x,y
                rowSet[x].add(num)
                colSet[y].add(num)
                groupSet[(get_group(x, y))].add(num)
                board[x][y] = "."

        dfs(0)

