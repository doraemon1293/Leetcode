# coding=utf-8
'''
Created on 2017�?9�?8�?

@author: Administrator
'''


class Solution(object):

    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        from collections import Counter
        import re
        self.memo = {}

        def removeContinuorsBall(board):
            pattern = "R{3,}|Y{3,}|B{3,}|G{3,}|W{3,}"
            while re.search(pattern, board):
                board = re.sub(pattern, "", board)
            return board

        def dfs(board, counter):
            if board == "": return 0
            if board in self.memo: return self.memo[board]
            res = float("inf")
            for i in xrange(len(board)):
                # 两个连续颜色的球 跳过第一�? 新球放在第二个的右面
                if i < len(board) - 1 and board[i] == board[i + 1]:
                    continue
                elif i > 0 and board[i] == board[i - 1] and counter[board[i]] > 0:
                    newBoard = board[:i + 1] + board[i] + board[i + 1:]
                    newBoard = removeContinuorsBall(newBoard)
                    counter[board[i]] -= 1
                    temp = dfs(newBoard, counter)
                    res = min(res, 1 + temp)
                    counter[board[i]] += 1
                # 单个�?
                elif counter[board[i]] > 1:
                    newBoard = board[:i + 1] + board[i] * 2 + board[i + 1:]
                    newBoard = removeContinuorsBall(newBoard)
                    counter[board[i]] -= 2
                    temp = dfs(newBoard, counter)
                    res = min(res, 2 + temp)
                    counter[board[i]] += 2
            self.memo[board] = res
            return res

        counter = Counter(hand)
        for k in "RYBGW":
            counter.setdefault(k, 0)
        ans = dfs(board, counter)
        return ans if ans != float("inf") else -1


board = "RBYYBBRRB"
hand = "YRBGB"
print Solution().findMinStep(board, hand)

