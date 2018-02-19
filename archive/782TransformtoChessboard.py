# coding=utf-8
'''
Created on 13 Feb 2018

@author: Administrator
'''


class Solution(object):

    def movesToChessboard(self, board):
        from collections import Counter
        N = len(board)
        ans = 0
        for counter in (Counter([tuple(x) for x in board]), Counter(zip(*board))):
            # print(counter)
            if len(counter) != 2:
                return -1
            # print(sorted(counter.values()))
            if sorted(counter.values()) != [N // 2, (N + 1) // 2]:
                return -1
            line1, line2 = counter
            # print(line1, line2)
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1
            if N % 2:
                if line1.count(1) > line1.count(0):
                    starts = [[(i + 1) % 2 for i in range(N)]]
                else:
                    starts = [[i % 2 for i in range(N)]]
            else:
                starts = [[i % 2 for i in range(N)], [(i + 1) % 2 for i in range(N)]]
            ans += min([sum([line1[i] != start[i] for i in range(N)]) for start in starts]) // 2

        return ans


board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
print(Solution().movesToChessboard(board))
