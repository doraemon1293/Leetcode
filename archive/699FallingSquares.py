# coding=utf-8
'''
Created on 2017å¹?10æœ?17æ—?

@author: Administrator
'''


class Solution(object):

    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        squares = []
        ans = []
        max_height = -float("inf")
        for pos in positions:
            left, right, height = pos[0], pos[0] + pos[1], pos[1]
            temp = 0
            for i in range(len(squares) - 1, -1, -1):
                sq_left, sq_right, sq_height = squares[i]
                if not(left >= sq_right or right <= sq_left):
                    temp = max(temp, sq_height)
            height += temp
            max_height = max(max_height, height)
            squares.append((left, right, height))
            ans.append(max_height)
        return ans


positions = [[1, 2], [2, 3], [6, 1]]
# positions = [[100, 100], [200, 100]]
# positions = [[1, 5], [2, 2], [7, 5]]
positions = [[50, 47], [95, 48], [88, 77], [84, 3], [53, 87], [98, 79], [88, 28], [13, 22], [53, 73], [85, 55]]
print Solution().fallingSquares(positions)

